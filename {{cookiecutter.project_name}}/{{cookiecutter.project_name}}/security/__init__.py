from pyramid.authorization import ACLAuthorizationPolicy
from .base import BaseAuthPolicy
from pyramid.events import NewResponse

# Change this if you use custom user authenticator
from .base import BaseUserRetriever as UserRetriever

# Adding CORS headers
from .cors_response import add_cors_headers


def includeme(config):
    auth_policy = BaseAuthPolicy(
        config.get_settings().get('auth.secret', 'seCrite')
    )
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_authentication_policy(auth_policy)
    config.add_request_method(UserRetriever, 'user_retriever', reify=True)
    config.add_subscriber(add_cors_headers, NewResponse)

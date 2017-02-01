from pyramid.authorization import ACLAuthorizationPolicy
from .base import BaseAuthPolicy

# Change this if you use custom user authenticator
from .base import BaseUserRetriever as UserRetriever


def includeme(config):
    auth_policy = BaseAuthPolicy(
        config.get_settings().get('auth.secret', 'seCrite')
    )
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_authentication_policy(auth_policy)
    config.add_request_method(UserRetriever, 'user_retriever', reify=True)

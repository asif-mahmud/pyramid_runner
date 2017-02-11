from pyramid.authorization import ACLAuthorizationPolicy
from datetime import timedelta
from pyramid.events import NewResponse

# Adding CORS headers
from .cors_response import add_cors_headers


def includeme(config):
    auth_secret = config.get_settings().get('auth.secret', 'seCrite')

    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_subscriber(add_cors_headers, NewResponse)

    # Include pyramid_jwt
    config.include('pyramid_jwt')
    config.set_jwt_authentication_policy(
        auth_secret,
        expiration=timedelta(hours=3)
    )

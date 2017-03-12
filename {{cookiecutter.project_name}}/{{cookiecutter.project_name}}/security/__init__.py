import datetime

import pyramid.authorization as authorization
import pyramid.events as events


# Adding CORS headers
from . import cors_response as cors


def includeme(config):
    auth_secret = config.get_settings().get('auth.secret', 'seCrite')
    config.set_authorization_policy(
        authorization.ACLAuthorizationPolicy()
    )
    config.set_jwt_authentication_policy(
        auth_secret,
        expiration=datetime.timedelta(hours=3)
    )
    config.add_subscriber(cors.add_cors_headers, events.NewResponse)
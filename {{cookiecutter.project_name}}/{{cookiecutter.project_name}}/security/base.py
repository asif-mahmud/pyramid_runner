from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.request import Request


class BaseUserRetriever(object):
    """Base class to retrieve user info.

    Instance of this class will be accessible through `pyramid.request.Request`.
    To customise user authentication and user info extracting from the
    `request` instance inherit this class and add it to `.includeme(config)`
    function. See the `.includeme(config)` function for way of doing that.

    Usage:
    ```
    class CustomUserRetriever(BaseUserRetriever):
        def get_user(self):
            return custom_method()

        def get_user_id(self):
            return custom_userid_method()
    ```

    See the code for a sample use case.

    Note: Make sure `get_user` method returns `None` or a valid or authenticated
    `user`.
    """

    def __init__(self, request):
        if isinstance(request, Request):
            self.request = request

    def get_user(self):
        username = self.request.params.get('name', [])
        userid = self.request.params.get('id', [])
        if username and userid:
            return dict(
                name=username,
                id=userid,
            )

    def get_user_id(self):
        if self.get_user():
            return self.get_user()['id']


class BaseAuthPolicy(AuthTktAuthenticationPolicy):
    """Base authentication policy to provide a stateless authentication.

    No need to subclass this class. But if you want to do so anyway
    implement both `authenticated_userid` and `unauthenticated_userid`
    """

    def authenticated_userid(self, request):
        return request.user_retriever.get_user_id()

    def unauthenticated_userid(self, request):
        return request.user_retriever.get_user_id()

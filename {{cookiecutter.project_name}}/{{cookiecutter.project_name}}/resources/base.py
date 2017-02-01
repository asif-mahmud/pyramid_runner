from pyramid.request import Request
from pyramid.security import (
    Allow,
    Everyone,
    ALL_PERMISSIONS
)


class BaseResource(object):
    """Define abstract __acl__ method for all Resources."""

    def __acl__(self):
        raise NotImplementedError('ACL(__acl__) not implemented in {}'.format(
            self.__class__
        ))


class BaseRoot(BaseResource):
    """Base class for Root Resource.

    This simplifies the resource tree from within Root resource. Child resource MUST accept the
    following parameters -

        1. parent - instance of the parent resource
        2. key - the key string for which the Child is being reached
        3. request - the current `pyramid.request.Request` object

    The root will be accessible by `request.root` object.

    Usage:
    ```
    class Root(BaseRoot):
        __tree__ = dict(
            child1 = child1_cls,
            ...
        )
    ```

    Attributes:
        request(pyramid.request.Request): the current request instance
    """

    __name__ = None
    __parent__ = None
    __tree__ = dict()

    def __init__(self, request):
        if isinstance(request, Request):
            self.request = request

    def __getitem__(self, item):
        child = self.__tree__.get(item, [])

        if child:
            return child(self, item, self.request)
        else:
            raise KeyError

    def __acl__(self):
        """Assuming the Root resource can be accessed by everyone."""
        return [
            (Allow, Everyone, ALL_PERMISSIONS),
        ]


class BaseChild(BaseResource):
    """Base class for any child resource.

    Subclass this class to provide a child node in the resource tree. Further to
    provide child of the inherent class implement `get_child_instance(key)` method.

    Every child must implement `__acl__` method to provide proper authorization
    policy fot it.

    Usage:
    ```
    class CatList(BaseChild):
        def get_child_instance(self, key):
            if key in database:
                return Cat(parent, key, self.request)

        def __acl__(self):
            return [DENY_ALL]
    ```

    Note: The returned child of `get_child_instance` must inherit `BaseChild`.
    """

    def __init__(self, parent, key, request):
        self.__parent__ = parent
        self.__name__ = key
        if isinstance(request, Request):
            self.request = request

    def get_child_instance(self, key):
        return []

    def __getitem__(self, item):
        child = self.get_child_instance(item)

        if child:
            if issubclass(child, BaseChild):
                return child
            else:
                raise ValueError('Child is not of type BaseChild')
        else:
            raise KeyError

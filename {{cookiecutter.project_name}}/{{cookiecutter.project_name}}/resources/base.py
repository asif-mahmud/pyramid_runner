import logging
import datetime

import pyramid.request as request
import pyramid.security as security


class BaseResource(object):
    """Define abstract __acl__ method for all Resources."""

    def __acl__(self):
        raise NotImplementedError('ACL(__acl__) not implemented in {}'.format(
            self.__class__
        ))

    def log_error(self, method, error):
        """Log error messages from the views."""
        logging.error(
            '[{}] From {}.{}: {}'.format(
                datetime.datetime.now().isoformat(),
                self.__class__.__name__,
                method.__name__,
                error
            )
        )


class BaseRoot(BaseResource):
    """Base class for Root Resource.

    This simplifies the resource tree from within Root resource. Child
    resource MUST accept the following parameters -

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

    def __init__(self, req):
        if isinstance(req, request.Request):
            self.request = req

    def __getitem__(self, item):
        child = self.__tree__.get(item, [])

        if child:
            return child(self, item, self.request)
        else:
            raise KeyError

    def __acl__(self):
        """Assuming the Root resource can be accessed by everyone."""
        return [
            (security.Allow, security.Everyone, security.ALL_PERMISSIONS),
        ]


class BaseChild(BaseResource):
    """Base class for any child resource.

    Subclass this class to provide a child node in the resource tree. Further
    to provide child of the inherent class implement `get_child_instance(key)`
    method.

    Every child must implement `__acl__` method to provide proper authorization
    policy fot it.

    Usage:
    ```
    class CatList(BaseChild):
        def child_class(self, key):
            if key in database:
                return Cat

        def child_instance(self, key):
            return Cat(self, key, self.request)

        def __acl__(self):
            return [DENY_ALL]
    ```

    Note: The returned child of `get_child_instance` must inherit `BaseChild`.
    """

    def __init__(self, parent, key, req):
        self.__parent__ = parent
        self.__name__ = key
        if isinstance(req, request.Request):
            self.request = req

    def child_class(self, key):
        """Override this method to construct the resource tree.

        Return the child class of type `BaseChild`. To return
        an instance use `child_instance` method.
        """
        return None

    def child_instance(self, key):
        """Provide an instance of the child resource."""
        return None

    def __acl__(self):
        return [
            (security.Allow, security.Everyone, security.ALL_PERMISSIONS),
        ]

    def __getitem__(self, item):
        # Try finding a child class first
        ChildCls = self.child_class(item)

        if ChildCls:
            if issubclass(ChildCls, BaseChild):
                return ChildCls(self, item, self.request)
            else:
                raise ValueError('Child is not of type BaseChild')

        # Try finding a child instance
        child_instance = self.child_instance(item)
        if child_instance:
            if isinstance(child_instance, BaseChild):
                return child_instance
            else:
                raise ValueError('Child is not of type BaseChild')

        # Could not find any child
        raise KeyError()

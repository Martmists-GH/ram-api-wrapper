# TODO: Custom url parameters

import sys

from . import v1, v2

__all__ = ["v1", "v2", "Route", "Result"]

# Add routes as attributes
for v in [v1, v2]:
    for n, r in v.routes.items():
        setattr(v, n, r)

# Import classes
if sys.version_info >= (3, 5, 0):
    # Add async functions
    from .async_ import Route, Result
else:
    from .sync_ import Route, Result

del v, n, r, sys

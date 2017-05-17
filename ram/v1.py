import sys

if sys.version_info >= (3, 5, 0):
    # Add async functions
    from .async_ import Route
else:
    from .sync_ import Route

imgtypes = [
    "cry", "cuddle", "hug", "kiss", "lewd",
    "lick", "nom", "nyan", "owo", "pat",
    "pout", "rem", "slap", "smug", "stare",
    "tickle", "triggered", "nsfw-gtn",
    "potato", "kermit"]

routes = {
    img: Route(base_url="https://rra.ram.moe/",
               path="i/r?type=" + img,
               cdn_url="https://wia.ram.moe/")
    for img in imgtypes}

__all__ = ["routes"] + list(routes.keys())
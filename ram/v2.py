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
    "types": Route(base_url="https://api.ram.moe/",
                   path="images/types"),
    "tags": Route(base_url="https://api.ram.moe/",
                  path="images/tags"),
    "random": Route(base_url="https://api.ram.moe/",
                    path="images/random",
                    cdn_url="https://cdn.ram.moe/")
}

for img in imgtypes:
    routes["random_"+img] = Route(
        base_url="https://api.ram.moe/",
        path="images/random&type=" + img,
        cdn_url="https://cdn.ram.moe/")

__all__ = ["routes"] + list(routes.keys())

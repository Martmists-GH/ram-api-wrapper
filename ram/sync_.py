import io

try:
    import requests
except ImportError:
    print("Requests module not installed, sync functions not available!")


class ResponseError(BaseException):
    pass


class Route:
    def __init__(self, base_url, path, cdn_url=None,
                 method="GET", headers=None):
        self.base_url = base_url
        self.path = path
        self.method = method
        self.headers = headers

    def sync_query(self, url_params=None):
        res = getattr(requests, self.method.lower())(
                self.base_url+self.path, headers=self.headers)
        if 200 <= res.status_code < 300:
            retval = res.json()

            # Some endpoints are not images
            if self.cdn_url is None:
                return retval
            return Result(**retval, base_url=self.base_url)

        else:
            raise ResponseError(
                    "Expected a response code in range 200-299, got {}"
                    .format(res.status_code))


class Result:
    def __init__(self, path, img_id, img_type, nsfw, cdn_url):
        self.path = path
        self.img_id = img_id
        self.img_type = img_type
        self.nsfw = nsfw
        self.cdn_url = cdn_url

    def sync_download(self):
        res = requests.get(self.cdn_url+self.path)
        if 200 <= res.status_code < 300:
            return io.BytesIO(res.content)
        else:
            raise ResponseError(
                    "Expected a response code in range 200-299, got {}"
                    .format(res.status_code))

import json
from urllib import parse, request


class ConnpassClient:
    def create_request(self, key: str, value: str) -> request.Request:
        url = parse.urlunparse(
            (
                "https",
                "connpass.com",
                "api/v1/event",
                None,
                parse.urlencode({key: value}),
                None,
            )
        )
        return request.Request(url)

    
    def get(self, key: str, value: str) -> request.Request:
        req = self.create_request(key, value)
        with request.urlopen(req) as res:
            data = json.load(res)
        return data
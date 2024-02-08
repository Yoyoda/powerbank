from requests import Session as BaseSession


class Session(BaseSession):
    def __init__(self, *args, base_url=None, token=None, token_prefix='bearer ', **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.base_url = base_url
        if token:
            self.headers.update(
                Accept="application/json",
                Authorization=token_prefix+token,
            )

    def request(self, method, url, *args, **kwargs):
        if self.base_url and url[:4] != 'http':
            url = self.base_url + url
        return super().request(method, url, *args, **kwargs)

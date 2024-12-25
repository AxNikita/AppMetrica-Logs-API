class AppmetricaClientError(Exception):
    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        self.request = kwargs.pop('request', None)


class AppmetricaApiError(Exception):
    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        self.request = kwargs.pop('request', None)


class AppmetricaConfigError(AppmetricaClientError):
    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        self.request = kwargs.pop('request', None)

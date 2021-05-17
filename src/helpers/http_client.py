import requests


class Client:
    """Class for implementing http requests logic"""
    def __init__(self):
        self.request = requests

    def get_request(self, *args, **kwargs):
        r"""Sends a GET request.

        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        return self.request.get(*args, **kwargs)

    def post_request(self, *args, **kwargs):
        r"""Sends a POST request.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        return self.request.post(*args, **kwargs)

    def put_request(self, *args, **kwargs):
        r"""Sends a PUT request.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        return self.request.put(*args, **kwargs)

    def delete_request(self, *args, **kwargs):
        r"""Sends a DELETE request.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        return self.request.delete(*args, **kwargs)

    def universal_request(self, *args, **kwargs):
        """Sends any request.
        :param method: HTTP method to use.
        :param url: URL to send.
        :param headers: dictionary of headers to send.
        :param files: dictionary of {filename: fileobject} files to multipart upload.
        :param data: the body to attach to the request. If a dictionary or
            list of tuples ``[(key, value)]`` is provided, form-encoding will
            take place.
        :param json: json for the body to attach to the request (if files or data is not specified).
        :param params: URL parameters to append to the URL. If a dictionary or
            list of tuples ``[(key, value)]`` is provided, form-encoding will
            take place.
        :param auth: Auth handler or (user, pass) tuple.
        :param cookies: dictionary or CookieJar of cookies to attach to this request.
        :param hooks: dictionary of callback hooks, for internal usage.
        """
        return self.request.Request(*args, **kwargs)

import requests
from src.helpers.counters import execution_time_delta


class SessionHttp(requests.Session):
    def __init__(self):
        super().__init__()

    def get_request(self, *args, **kwargs):
        r"""Sends a GET request.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        return self.get(*args, **kwargs)

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
        return self.post(*args, **kwargs)

    def put_request(self, *args, **kwargs):
        r"""Sends a PUT request.
        :param session: (Optional)  :default value False:
        Boolean type param if true request is sending in session, None or False sending 1 request 1 session.
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        return self.put(*args, **kwargs)

    def delete_request(self, *args, **kwargs):
        r"""Sends a DELETE request.
        :param session: (Optional)  :default value False:
        Boolean type param if true request is sending in session, None or False sending 1 request 1 session.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        return self.delete(*args, **kwargs)


class ClientHttp:
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
        :param session: (Optional)  :default value False:
        Boolean type param if true request is sending in session, None or False sending 1 request 1 session.
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
        :param session: (Optional)  :default value False:
        Boolean type param if true request is sending in session, None or False sending 1 request 1 session.
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        return self.request.delete(*args, **kwargs)


if __name__ == '__main__':
    @execution_time_delta
    def no_session():
        print("no session")
        for i in range(10):
            ClientHttp().get_request(url="https://google.com")

    session = SessionHttp()


    @execution_time_delta
    def with_session():
        print("session")
        for i in range(10):
            session.get_request(url="https://google.com")


"""Module for registration endpoint"""
from src.configuration.config import Config
from src.helpers.http_client import SessionHttp, ClientHttp


class ApiUser:
    """Class for User manipulations: register, login etc.."""
    def __init__(self, session):
        """

        :param session: Sets http session handler.
        """
        self.register_path = fr"/api/v{Config.VERSION_API}/register"
        self.signup_path = fr"/api/v{Config.VERSION_API}/signup"
        self.login_path = fr"/api/v{Config.VERSION_API}/login"
        self.profile_path = fr"/api/v{Config.VERSION_API}/profile"
        self.base_url = Config.APP_URI
        self.request = session

    def signup(self):
        """Method for User registration"""

        url = f"{self.base_url}{self.signup_path}"

        payload = "expiry=86400&login_from=login+page&password=123456&" \
                  "email=doroshenkoaldm%40gmail.com&organization=test1&job_title=test1&name=test1"
        headers = {
            'authority': 'app.cosmosid.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'dnt': '1',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://app.cosmosid.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://app.cosmosid.com/register',
            'accept-language': 'uk-UA,uk;q=0.9',
            'cookie': '_gcl_au=1.1.473645444.1621968503; G_ENABLED_IDPS=google; _ga=GA1.2.44310533.1621968507;'
                      ' _gid=GA1.2.1062023571.1621968507;'
                      ' __hstc=39762172.90882a227902a4bf619889fa695c31db.1621968507683.1621968507683.1621968507683.1;'
                      ' hubspotutk=90882a227902a4bf619889fa695c31db; __hssrc=1; __hssc=39762172.1.1621968507684;'
                      ' messagesUtk=36b4058eace349bba5ad353b57127151'
        }

        response = self.request.post(url, headers=headers, data=payload)

        print(response.text)

    def login(self):
        self.request.get_request(
            url=f"{self.base_url}{self.login_path}"

        )

    def get_profile(self, profile_id: str):

        url = f"{self.base_url}{self.profile_path}?"
        payload = f"_={profile_id}"
        headers = {
            'authority': 'app.cosmosid.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'dnt': '1',
            'x-token': '232e7e1e-30d5-4bf8-a5d2-377183c68721',
            'sec-ch-ua-mobile': '?0',
            'accept': 'application/json',
            'x-userdatetime': '2021-05-25T21:15:29+03:00',
            'x-requested-with': 'XMLHttpRequest',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://app.cosmosid.com/settings',
            'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'messagesUtk=a608d64183b8445db0bf9d68175d2071'
        }

        response = self.request.get(url, headers=headers, data=payload)

        print(response.text)

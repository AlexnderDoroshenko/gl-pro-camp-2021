"""Module for registration endpoint"""
from src.configuration.config import Config
from src.helpers.http_client import ClientHttp


class ApiUser:
    """Class for User manipulations: register, login etc.."""
    def __init__(self):
        self.register_path = r"/api/v1/register"
        self.signup_path = r"/api/v1/signup"
        self.login_path = r"/api/v1/login"
        self.base_url = Config.BASE_URL
        self.request = ClientHttp
        self.token = Config.TOKEN

    def login(self):
        self.request().get_request(
            url=f"{self.base_url}{self.login_path}",
            headers={"Accept": "application/json, text/javascript, */*; q=0.01",
                     "Authorization": self.token,
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
            params={"expiry": 86400,"login_from": "login+page"}
            )
        return self




    # {"contactFields": {"email": "doroshenkoaldm@gmail.com", "firstName": "Alexander"}, "formSelectorClasses": ".jss161",
    #  "formSelectorId": "",
    #  "formValues": {"Job Title": "QA Automation Engineer", "Organization": "Nayax", "I agree with the": "Checked"},
    #  "labelToNameMap": {"Job Title": "job_title", "Organization": "organization", "I agree with the": ""},
    #  "pageTitle": "CosmosID", "pageUrl": "https://app.cosmosid.com/register", "portalId": 4249792, "type": "SCRAPED",
    #  "utk": "cf252e02d2f9918a411b1b1c0ab54c34", "uuid": "97478be1-d3c5-4ceb-b4c7-9a47ab0f0ac9",
    #  "version": "collected-forms-embed-js-static-1.239"}

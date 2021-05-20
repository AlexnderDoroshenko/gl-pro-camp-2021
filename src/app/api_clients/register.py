"""Module for registration endpoint"""
from src.configuration.config import Config
from src.helpers.http_client import SessionHttp, ClientHttp


class ApiUser:
    def __init__(self):
        self.register_path = r"/api/v1/register"
        self.login_path = r"/api/v1/login"
        self.url = Config.APP_URI
        self.request = ClientHttp()


    def login(self):
        self.request.get_request(
            url=f"{self.url}{self.login_path}"
        )



    # {"contactFields": {"email": "doroshenkoaldm@gmail.com", "firstName": "Alexander"}, "formSelectorClasses": ".jss161",
    #  "formSelectorId": "",
    #  "formValues": {"Job Title": "QA Automation Engineer", "Organization": "Nayax", "I agree with the": "Checked"},
    #  "labelToNameMap": {"Job Title": "job_title", "Organization": "organization", "I agree with the": ""},
    #  "pageTitle": "CosmosID", "pageUrl": "https://app.cosmosid.com/register", "portalId": 4249792, "type": "SCRAPED",
    #  "utk": "cf252e02d2f9918a411b1b1c0ab54c34", "uuid": "97478be1-d3c5-4ceb-b4c7-9a47ab0f0ac9",
    #  "version": "collected-forms-embed-js-static-1.239"}

from http.client import responses
from endpoints.enpoints_handler import Endpoint
import requests

class GetLinkEndpoint(Endpoint):

    def get_long_using_short(self, code):
        base_url = 'https://gotiny.cc/api/'
        response = requests.get(f'{base_url}{code}')
        self.status = response.status_code
        self.text = response.text
        return response.text

    def chek_save_link_match_sent_link(self, sent_link):
        assert self.text == sent_link


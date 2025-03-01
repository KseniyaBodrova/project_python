import requests
from endpoints.enpoints_handler import Endpoint


class CreateLinkEndpoint(Endpoint):
    status = None
    long = None
    code = None
    sent_code = None

    def create_short_link_for_long_link(self, long_url, code=None):
        if code:
            response = requests.post(
                'https://gotiny.cc/api',
                headers={'Content-Type': 'application/json'},
                json={'long': long_url, 'custom': code}
            )
        else:
            response = requests.post(
                'https://gotiny.cc/api',
                headers={'Content-Type': 'application/json'},
                json={'input': long_url}
            )
        self.sent_code = code if code else None
        self.sent_link = long_url
        self.status = response.status_code
        self.long = response.json()[0]['long']
        self.code = response.json()[0]['code']
        return response


    def check_response_link_matches_long_link(self):
        assert self.sent_link == self.long

    def check_code_is_not_empty(self):
        assert len(self.code) > 0

    def check_response_code_is_code_sent(self):
        assert self.code == self.sent_code

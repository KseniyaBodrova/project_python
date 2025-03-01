import requests

from conftest import link_creator_endpoint, random_sent_code
from endpoints.create_link_endpoint import CreateLinkEndpoint

def test_create_short_link(link_creator_endpoint):
    long_link = 'https://sky.pro/media/privatnost-metodov-v-python/'
    link_creator_endpoint.create_short_link_for_long_link(long_url=long_link)
    link_creator_endpoint.check_response_status_is_ok()
    link_creator_endpoint.check_response_link_matches_long_link()
    link_creator_endpoint.check_code_is_not_empty()

def test_custom_short_link(link_creator_endpoint, random_sent_code):
    long_link = 'https://sky.pro/media/privatnost-metodov-v-python/'
    code = random_sent_code
    link_creator_endpoint().create_short_link_for_long_link(long_link, code)
    link_creator_endpoint.check_response_status_is_ok()
    link_creator_endpoint.check_response_link_matches_long_link()
    link_creator_endpoint.check_response_code_is_code_sent()

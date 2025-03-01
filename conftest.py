import string

import pytest
from endpoints.create_link_endpoint import CreateLinkEndpoint
from endpoints.get_short_endpoint import GetLinkEndpoint
import random

@pytest.fixture()
def link_creator_endpoint():
    return CreateLinkEndpoint()

@pytest.fixture()
def get_url_endpoint():
    return GetLinkEndpoint()

@pytest.fixture()
def random_sent_code():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

@pytest.fixture()
def create_random_link(link_creator_endpoint, random_sent_code):
    long_link = f'http://{random_sent_code}.com'
    link_creator_endpoint.create_short_link_for_long_link(long_link)
    return link_creator_endpoint.code, long_link


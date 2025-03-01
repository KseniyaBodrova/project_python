from conftest import link_creator_endpoint, random_sent_code

def resolve_tiny_link(create_random_link, get_url_endpoint):
    code, long_link = create_random_link
    get_url_endpoint.create_short_link_for_long_link(code)
    get_url_endpoint.check_response_status_is_ok()
    get_url_endpoint.chek_save_link_match_sent_link(long_link)
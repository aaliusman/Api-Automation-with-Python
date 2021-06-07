from utilities.configuration import get_config
import requests

from utilities.resources import api_resources


def after_scenario(context, scenario):
    if 'Library' in scenario.tags:
        url = f"{get_config()['API']['endpoint']}{api_resources.delete_book}"
        delete_book_response = requests.post(url,
                                             json={
                                                 "ID": context.book_id
                                             })
        json_resp = delete_book_response.json()
        print(json_resp)
        assert delete_book_response.json()['msg'] == "book is successfully deleted"

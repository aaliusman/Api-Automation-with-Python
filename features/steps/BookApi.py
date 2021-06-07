from behave import *
from utilities.resources import *
import requests
from payload import *


@given("User have details which needs to be added to Library")
def step_impl(context):
    context.url = f"{get_config()['API']['endpoint']}{api_resources.add_book}"
    context.header = {"Content-Type": "application/json"}
    context.payload = add_book_payload('us', 'mnb324')


@when("User execute the AddBook PostAPI method")
def step_impl(context):
    context.response = requests.post(context.url,
                                     json=context.payload,
                                     headers=context.header
                                     )


@then("User verify book is successfully added")
def step_impl(context):
    json_resp = context.response.json()
    print(json_resp)
    print(type(json_resp))

    context.book_id = json_resp['ID']
    print(context.book_id)
    assert json_resp['Msg'] == 'successfully added', f"Response didn't match:  {json_resp['Msg']}"


@given("User needs {isbn} and {aisle} to be added to Library")
def step_impl(context, isbn, aisle):
    context.url = f"{get_config()['API']['endpoint']}{api_resources.add_book}"
    context.header = {"Content-Type": "application/json"}
    context.payload = add_book_payload(isbn, aisle)


@given("User utilize github credentials")
def step_impl(context):
    context.session = requests.session()
    context.session.auth = auth = ('aali.usman83@gmail.com', get_password())


@when("User hit getRepo API of github")
def step_impl(context):
    context.response = context.session.get(api_resources.github_repo)
    context.github = context.response.json()
    context.avatar = context.github[0]['owner']['avatar_url']
    print(context.avatar)


@then(u'User Verify status code of {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

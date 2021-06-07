import requests
from payload import *
from utilities.configuration import *
from utilities.resources import *

url = f"{get_config()['API']['endpoint']}{api_resources.add_book}"
print(url)
# query = 'select * from Books'
add_book_response = requests.post(url,
                                  json=add_book_payload('abcd', '12987'),
                                  headers={"Content-Type": "application/json"}
                                  )

json_resp = add_book_response.json()
print(json_resp)
print(type(json_resp))

book_id = json_resp['ID']
print(book_id)
assert json_resp['Msg'] == 'successfully added', f"Response didn't match:  {json_resp['Msg']}"

url = f"{get_config()['API']['endpoint']}{api_resources.delete_book}"
delete_book_response = requests.post(url,
                                     json={
                                         "ID": book_id
                                     })
json_resp = delete_book_response.json()
print(json_resp)
# assert delete_book_response.json()['msg'] == "book is successfully deleted"

# Authentication
session = requests.session()
session.auth = auth = ('aali.usman83@gmail.com', get_password())
url = 'https://api.github.com/user'
print(get_password())
# github_resp = requests.get(url, verify=False, auth=('aali.usman83@gmail.com', get_password()))
github_resp = session.get(url)
print(github_resp.status_code)

url2 = "https://api.github.com/user/repos"
resp = requests.get(url2, auth=('aali.usman83@gmail.com', get_password()))
print(resp.status_code)
github = resp.json()

print(github[0]['owner']['avatar_url'])

url = 'https://rahulshettyacademy.com/maps/api/place/add/json'
res = requests.post(url, params={'key': 'qaclick123', },
                    json=add_place_payload())
json_res = res.json()
print(json_res)
print(type(json_resp))
place_id = json_res['place_id']

url = 'https://rahulshettyacademy.com/maps/api/place/get/json'
get_res = requests.get(url,
                       params={'key': 'qaclick123',
                               'place_id': place_id})

jso_res = get_res.json()
print(jso_res)
print(type(jso_res))
print(jso_res['location']['latitude'])
print(jso_res['phone_number'])
print(jso_res['types'])

url = 'https://rahulshettyacademy.com/maps/api/place/update/json'
update_res = requests.put(url,
                       json=update_place_payload(place_id),
                       params={'key': 'qaclick123',
                               'place_id': place_id})

j_res = update_res.json()
print(j_res)


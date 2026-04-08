import requests

URL = 'http://objapi.course.qa-practice.com/object'


def new_post():
    body = {
        "name": "Gleb",
        "data": {
            "year": 2026,
            "price": 100
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(URL, json=body, headers=headers)
    assert response.status_code == 200, 'POST status code is incorrect'
    return response.json()['id']


def put_post():
    post_id = new_post()

    body = {
        "name": "UPDATED_Gleb",
        "data": {
            "year": 2026,
            "price": 999
        }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(f'{URL}/{post_id}', json=body, headers=headers)

    assert response.status_code == 200, 'PUT status code is incorrect'
    assert response.json()['name'] == body['name']


def patch_a_post():
    post_id = new_post()

    body = {
        "name": "PATCHED_Full"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.patch(f'{URL}/{post_id}', json=body, headers=headers)
    assert response.status_code == 200, 'PATCH status code is incorrect'


def delete_a_post():
    post_id = new_post()

    response = requests.delete(f'{URL}/{post_id}')

    assert response.status_code == 200, 'DELETE status code is incorrect'


put_post()
patch_a_post()
delete_a_post()

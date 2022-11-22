import pytest
import requests
import json
from urllib.parse import urljoin
from api.builder import Builder


class ResponseStatusCodeException(Exception):
    ...


class ApiClient:
    def __init__(self, base_url: str, login: str, password: str):
        self.base_url = base_url
        self.login = login
        self.password = password
        self.session = requests.Session()
        self.builder = Builder


    def _request(self, method, location, files=None, headers=None, data=None, params=None, allow_redirects=False, expected_status=200,):
        url = urljoin(self.base_url, location)
        response = self.session.request(method=method, url=url, files=files, headers=headers, data=data, params=params,
                                        allow_redirects=allow_redirects)
        if allow_redirects == False:
            if response.status_code != expected_status:
                raise ResponseStatusCodeException(f'Excpected {expected_status}, but got {response.status_code}')
        return response

    def post_login(self):
        data = {
            'email': 'newlogan95@mail.ru',
            'password': '123456A',
            'continue': 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26i',
            'failure': 'https://account.my.com/login/'
        }
        headers = {
            'Referer': 'https://target-sandbox.my.com/'
        }
        from requests.cookies import RequestsCookieJar
        self.session.post('https://auth-ac.my.com/auth?lang=ru&nosavelogin', headers=headers, data=data, allow_redirects=True)
        self.session.get('https://target-sandbox.my.com/csrf/')
        csrf = self.session.cookies['csrftoken']
        requests.cookies.RequestsCookieJar.set(self.session.cookies, 'X-CSRFToken', csrf)
        return

    def upload_image(self, file_path):
        file = {'file': open(file_path, 'rb')}
        image = self._request('POST', '/api/v2/content/static.json', headers=self.session.cookies, files=file)
        return image.json()['id']


    def check_created_company(self, id_created_company):
        self._request('GET', f'api/v2/campaigns/{id_created_company}.json', params='?fields=id,name,status', headers=self.session.cookies)
        return True

    def create_company(self, id_content):
        company_data = self.builder.create_company(id_content)
        data = json.dumps(company_data.data)
        response = self._request('POST', 'api/v2/campaigns.json', headers=self.session.cookies, data=data)
        company_data.id_created_company = json.loads(response.content.decode())['id']
        return company_data.id_created_company

    def delete_company(self, id_company):
        data = {'status': 'deleted'}
        self._request('POST', f'api/v2/campaigns/{id_company}.json', headers=self.session.cookies, data=json.dumps(data), expected_status=204)
        return

    def check_created_segment(self, id_segment):
        self._request('GET', f'api/v2/remarketing/segments/{id_segment}/relations.json', headers=self.session.cookies)
        return True

    def create_segment(self, relations_object_type, source_id=None):
        segment_data = self.builder.create_segment(relations_object_type, source_id)
        data = json.dumps(segment_data.data)
        response = self._request('POST', 'api/v2/remarketing/segments.json', headers=self.session.cookies, data=data)
        segment_data.id_segment = json.loads(response.content.decode())['id']
        return segment_data.id_segment

    def delete_segment(self, id_segment):
        self._request('DELETE', f'api/v2/remarketing/segments/{id_segment}.json', headers=self.session.cookies,
                      expected_status=204)
        return

    def add_vk_group(self, group='VK Образование'):
        response = self._request('GET', 'api/v2/vk_groups.json', params={'_q':'VK Образование'})
        id_group_in_found_list = int([item['id'] for item in json.loads(response.content.decode())['items'] if item['name'] == group][0])
        data = {
            'items':[{'object_id':id_group_in_found_list}]
        }
        response = self._request('POST', 'api/v2/remarketing/vk_groups/bulk.json', headers=self.session.cookies, data=json.dumps(data), expected_status=201)
        id_segment_group_vk = json.loads(response.content.decode())['items'][0]['id']
        return id_group_in_found_list, id_segment_group_vk

    def delete_segment_group_vk(self, id_segment_group_vk):
        self._request('DELETE', f'api/v2/remarketing/vk_groups/{id_segment_group_vk}.json', headers=self.session.cookies, expected_status=204)
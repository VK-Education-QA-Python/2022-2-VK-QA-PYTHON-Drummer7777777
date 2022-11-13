import re


class MySqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_count_request_by_type(self):
        reqs = dict()
        pattern = re.compile('"(\w+)\s.+"')
        with open('access.log', 'r') as log_file:
            for line in log_file:
                try:
                    type_req = pattern.findall(line)[0]
                except IndexError:
                    pass
                if type_req not in reqs.keys():
                    reqs[type_req] = 1
                else:
                    reqs[type_req] += 1
        for req in reqs.keys():
            self.client.execute_query(
                f'insert into `count_request_by_type` (`type_request`, `count_request`) values ("{req}", "{reqs[req]}")')

    def create_top_10_popular_request(self, count_top=10):
        reqs = dict()
        pattern = re.compile('"\w+\s(.+)\s.+"\s\d{3}')
        with open('access.log', 'r') as log_file:
            for line in log_file:
                try:
                    url_req = pattern.findall(line)[0]
                except IndexError:
                    pass
                if url_req not in reqs.keys():
                    reqs[url_req] = 1
                else:
                    reqs[url_req] += 1
        sorted_reqs = dict(sorted(reqs.items(), key=lambda x: x[1], reverse=True))
        reqs = dict()
        for key in list(sorted_reqs)[:count_top]:
            reqs[key] = sorted_reqs[key]
        for req in reqs.keys():
            self.client.execute_query(
                f'insert into `top_10_popular_request` (`path_request`, `count_request`) values ("{req}", "{reqs[req]}")')


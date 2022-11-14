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

    def create_top_5_big_request(self, count_top=5):
        reqs = dict()
        num_str = 1
        pattern_url = re.compile('"\w+\s(.+)\s.+"\s\d{3}')
        pattern_status = re.compile('".+"\s(\d{3})')
        pattern_size = re.compile('".+"\s\d{3}\s(\d+)\s')
        pattern_ip = re.compile('(\d+\.\d+\.\d+\.\d+)')
        with open('access.log', 'r') as log_file:
            for line in log_file:
                status = int(pattern_status.findall(line)[0])
                if status >= 400 and status < 500:
                    url = pattern_url.findall(line)[0]
                    size = int(pattern_size.findall(line)[0])
                    ip = pattern_ip.findall(line)[0]
                    if len(reqs) < count_top:
                        reqs[num_str] = {'url': url, 'status': status, 'size': size, 'ip': ip}
                    else:
                        min_size = min([reqs[req]['size'] for req in reqs])
                        if size > min_size:
                            for req in reqs:
                                if reqs[req]['size'] == min_size:
                                    reqs.pop(req)
                                    break
                            reqs[num_str] = {'url': url, 'status': status, 'size': size, 'ip': ip}
                num_str += 1
        for req in reqs.keys():
            self.client.execute_query(
                """insert into `top_5_big_request` (`number_str_in_logs`, `status_request`, `size_request`, `ip_request`) \
                values ("{}", "{}", "{}", "{}")""".format(req, reqs[req]["status"], reqs[req]["size"], reqs[req]["ip"]))


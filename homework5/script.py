import re
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--json", action="store_true")
args = parser.parse_args()


def formating_output(output):
    if args.json:
        output = json.dumps(output, indent=4)
        format = '.json'
        return output, format
    else:
        format = '.txt'
        pretty_output = str()
        for name_info in list(output):
            reqs = str()
            for key in list(output[name_info]):
                reqs = reqs + '\t' + str(key) + ' : ' + str(output[name_info][key]) + '\n'
            pretty_output += f"{name_info}:\n {reqs}"
        return pretty_output, format


def recording_output(output, format):
    with open(f'analysis_logs_py{format}', 'w') as file:
        file.write(output)

def count_request_for_type():
    reqs = dict()
    pattern = re.compile('"(\w+)\s.+"')
    with open('access.log','r') as log_file:
        for line in log_file:
            try:
                type_req = pattern.findall(line)[0]
            except IndexError:
                pass
            if type_req not in reqs.keys():
                reqs[type_req] = 1
            else:
                 reqs[type_req] += 1
    return {"Count request for type": reqs}


def top_10_popular_request():
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
    for key in list(sorted_reqs)[:10]:
        reqs[key] = sorted_reqs[key]
    return {"Top 10 popular request": reqs}


def top_5_big_request():
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
                if len(reqs) < 5:
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
    return {"Top 5 big request": reqs}







reqs = count_request_for_type()
reqs =  {**reqs, **top_10_popular_request()}
reqs = {**reqs, **top_5_big_request()}
output, format = formating_output(reqs)
recording_output(output, format)

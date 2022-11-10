import re


# reqs = dict()
# pattern = re.compile('(\d+\.\d+\.\d+\.\d+)')
# with open('access.log','r') as log_file:
#     line = log_file.readline()
#     print (line)
#     print(pattern.findall(line))
reqs = {'asd': 123, 'fds': 32}
reqs.pop('asd')
print(reqs)
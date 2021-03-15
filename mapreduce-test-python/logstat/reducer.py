#!/usr/bin/python
from operator import itemgetter
import sys
from collections import defaultdict

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip,0) + num

    except ValueError:
        pass


sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))

freq_ips = defaultdict(list)

for ip, count in sorted_dict_ip_count:
    h,ip_ = ip.split(' ')

    try:
        h = int(h)
        count = int(count)
        freq_ips[h].append([ip,count])

    except ValueError:
        pass

beg = input ('Enter start time: ')
beg = int(beg)
en = input ('Enter end time: ')
en = inst(en)
for i in range(beg,en):
    t_3 = sorted(freq_ips[i], key=lambda v:v[1], reverse=True)[0:3]
    print '%s\t%s' % (i, t_3)

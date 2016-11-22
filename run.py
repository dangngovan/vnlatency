from rq import Queue
from worker import conn

q = Queue('latency', default_timeout=5400, connection=conn)
## Tao Dictionary
dict = {}
with open("ip_range_data") as f:
    for line in f:
        try:
            (key, val) = line.split(":")
            dict[str(key)] = val.strip()
        except ValueError:
            print('Ignoring: malformed line: "{}"'.format(line))
from latency import check_latency
for k,v in sorted(dict.items()):
    result = q.enqueue(check_latency,k,v)

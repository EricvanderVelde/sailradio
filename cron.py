import json
import os
import sys
from crontab import CronTab
from datetime import datetime
import time

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)

    return utc_datetime + offset

cron = CronTab(user = os.getlogin())
iter = cron.find_comment('NAVTEX') # matches foobar1
for job in iter:
    print(job)
    cron.remove(job)
    cron.write()

if len(sys.argv) > 1 and sys.argv[1] == 'add':
    with open('schedule.json') as f:
        d = json.load(f)

    for s in d.get('schedules', []):
        command_line = 'cd {} && sleep {} && ./run.sh {} >/dev/null 2>&1'.format(os.environ.get('PWD'), s['start'][6:8], s['id'])
        print(command_line)

        utc_start_time = datetime.strptime(s['start'],"%H:%M:%S")
        local_start_time = datetime_from_utc_to_local(utc_start_time)

        job = cron.new(command=command_line, comment='NAVTEX')
        job.hour.on(local_start_time.hour)
        job.minute.on(local_start_time.minute)
        
        cron.write()

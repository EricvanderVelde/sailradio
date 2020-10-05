import json
import os
from crontab import CronTab

cron = CronTab(user = os.getlogin())
iter = cron.find_comment('NAVTEX') # matches foobar1
for job in iter:
    print(job)
    cron.remove(job)
    cron.write()

with open('schedule.json') as f:
    d = json.load(f)

for s in d.get('schedules', []):
    command_line = 'cd /home/eric/Documents/navtex/sched && sleep {} && ./run.sh {} >/dev/null 2>&1'.format(s['start'][6:8],s['id'])
    print(command_line)

    job = cron.new(command=command_line, comment='NAVTEX')
    job.hour.on(s['start'][0:2])
    job.minute.on(s['start'][3:5])
    cron.write()

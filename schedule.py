import json
import sys
import os

trans_id = sys.argv[1]

def get_commands(name):
    for c in d.get('commands', []):
        if c['id'] == name:
            return c

def get_station(name):
    for s in d.get('stations', []):
        if s['id'] == name:
            return s

def get_radio(name):
    for r in d.get('radios', []):
        if r['id'] == name:
            return r

with open('schedule.json') as f:
    d = json.load(f)


for s in d.get('schedules', []):
    if s['id'] == trans_id:
        station = get_station(s['station'])
        radio = get_radio('radio1')
        commands = get_commands(station['mode'])

        tune_freq = (station['frequency']+station['offset'])/1000
        filename = 'files/'+s['filename']+'_'+trans_id

        command = commands['capture'].format(radio['hostname'], radio['port'], tune_freq, s['duration'], filename)
        print(command)
        os.system(command)

        command = commands['process'].format(filename, filename)
        print(command)
        os.system(command)

        #command = 'cat {}.txt'.format(filename)
        #print(command)
        #os.system(command)
   

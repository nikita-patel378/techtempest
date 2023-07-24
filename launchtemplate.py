import plistlib
from datetime import datetime
import json
#The class to create a plist file
class LaunchTemplate:
    def __init__(self, label):
        self.template = {
            'Label': label,
            'ProgramArguments': [],
            'StartCalendarInterval': []
        }

    def add_program_argument(self, argument):
        self.template['ProgramArguments'].append(argument)

    def add_start_calendar_interval(self, interval):
        self.template['StartCalendarInterval'].append(interval)

    def write_to_file(self, filename):
        with open(filename, 'wb') as file:
            plistlib.dump(self.template, file)



    
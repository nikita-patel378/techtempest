from launchtemplate import LaunchTemplate
import json
import subprocess
def main():
    # Create a LaunchTemplate
    lt = LaunchTemplate('remindertemplate')
    #Add path directory to python3
    lt.add_program_argument('python3')
    #Add directory to python script 
    lt.add_program_argument('taskmessage.py')
    # Add the time to execute to the 'StartCalendarInterval' parameter
    lt.add_start_calendar_interval({'Hour':18, 'Minute':20})
    #Name the file
    lt.write_to_file('remindertemplate.plist')

if __name__ == "__main__":
    main()
    
from datetime import datetime


def add_log(type, message, ip=None):

    # get the timestamp
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if type == "error":
        log_error(message, timestamp)
    
    elif type == "info":
        log_info(message, timestamp, ip)
    

def log_info(message, timestamp, ip):
    # Log the message to the myiptracker.log file
    with open('myiptracker.log', 'a') as log:
        log.write('{} - INFO - {} - {}\n'.format(timestamp, message, ip))

def log_error(message, timestamp):
    # Log the message to the myiptracker.log file
    with open('myiptracker.log', 'a') as log:
        log.write('{} - ERROR - {}\n'.format(timestamp, message))

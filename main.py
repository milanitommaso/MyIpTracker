import json
import public_ip as ip

import notify_user, log

def get_public_ip():
    public_ip = ip.get()
    return public_ip


def main():

    # Get the public IP
    try:
        new_ip = get_public_ip()
    except:
        print('Error getting public IP')
        log.add_log('error', 'Error getting public IP')
        return

    # Read the old IP from the data.json file
    try:
        with open('data.json') as data:
            public_ip_data = data.read()
        old_ip = json.loads(public_ip_data)['public_ip']
    except:
        print('Error reading the old IP')
        log.add_log('error', 'Error reading the old IP')
        return

    # Compare the old IP with the new IP
    if old_ip == new_ip:
        print('No change in IP')

        # Log that the IP has not changed
        log.add_log('info', 'No change in IP', new_ip)

    else:
        print('IP has changed')
        print('Old IP: {}'.format(old_ip))
        print('New IP: {}'.format(new_ip))

        # Write the new IP to the data.json file
        with open('data.json', 'w') as data:
            data.write(json.dumps({'public_ip': new_ip}))

        # Notify the user
        try:
            notify_user.telegram_message(new_ip)
        except:
            print('Error notifying user with Telegram')
            log.add_log('error', 'Error notifying user with Telegram')
            return

        # Log that the IP has changed
        log.add_log('info', 'IP has changed', new_ip)


if __name__ == '__main__':
    main()

import json
import public_ip as ip

def get_public_ip():
    public_ip = ip.get()
    return public_ip


def main():

    # Get the public IP
    new_ip = get_public_ip()

    # Read the old IP from the data.json file
    with open('data.json') as data:
        public_ip_data = data.read()
    old_ip = json.loads(public_ip_data)['public_ip']

    # Compare the old IP with the new IP
    if old_ip == new_ip:
        print('No change in IP')
    else:
        print('IP has changed')
        print('Old IP: {}'.format(old_ip))
        print('New IP: {}'.format(new_ip))

        # Write the new IP to the data.json file
        with open('data.json', 'w') as data:
            data.write(json.dumps({'public_ip': new_ip}))


if __name__ == '__main__':
    main()

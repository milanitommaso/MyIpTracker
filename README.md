# **MyIpTracker**

MyIpTracker is a Python script that notifies the user when their public IP address changes. It does this by checking the public IP address and comparing it to the previous one, and if it detects a change, it sends a message to the user via Telegram bot.

## **Requirements**

- Python 3.x
- **`public_ip`** module
- **`python_telegram_bot`** module
- **`requests`** module
- **`telegram`** module

You can install the required modules by running the following command:

```bash
pip install -r requirements.txt
```

## **Usage**

1. Clone the repository:

```bash
git clone https://github.com/milanitommaso/MyIpTracker.git
```

1. Open **`telegram_data.json`** and fill in the required fields:

```json
{
    "token": "YOUR_BOT_TOKEN",
    "chat_id": "YOUR_CHAT_ID"
}
```

You can get your Telegram bot by creating a new bot using BotFather.

1. Run the script:

```bash
python3 main.py
```

The script will check your public IP address and send a message to the specified Telegram chat whenever it detects a change.

1. To run the script periodically, you can set up a cron job:

### **Linux or macOS**

Open a terminal and run the following command:

```bash
crontab -e
```

Then add the following line to the file:

```
0 * * * * /usr/bin/python3 /path/to/main.py
```

Save the file and exit. This will run the script every hour on the hour. You can modify the **`0 * * * *`** part to change the schedule to your desired interval.

### **Windows**

Open the Task Scheduler app and click "Create Task". Give the task a name and choose "Run whether user is logged on or not" under the "Security options" section.

In the "Triggers" tab, click "New" and set the schedule to your desired interval.

In the "Actions" tab, click "New" and set the action to "Start a program". Set the path to your Python executable and the argument to the path of your **`main.py`** script.

Click "OK" to save the task.
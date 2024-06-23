# Telegram Echo Bot

This project is a simple Telegram Echo Bot built with Flask and deployed on Vercel. The bot echoes any message sent to it by the user.

## Prerequisites

- Python 3.x
- Telegram account
- Vercel account
- GitHub account

## Getting Started

### Step 1: Create a Telegram Bot

1. Open Telegram and search for the BotFather.
2. Use the command `/newbot` and follow the instructions to create your bot.
3. Note down the API token provided by BotFather.

### Step 2: Set Up Your Local Development Environment

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/TheBrainliestUser/echo_bot.git
    cd echo_bot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set your Telegram bot token in the environment:

    ```bash
    export TELEGRAM_BOT_TOKEN=your-telegram-bot-token
    ```

5. Run the Flask application:

    ```bash
    flask run
    ```

### Step 3: Deploy to Vercel

1. Commit your changes to your GitHub repository:

    ```bash
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    ```

2. Go to the [Vercel dashboard](https://vercel.com/), sign in, and click on "New Project".
3. Import your GitHub repository and deploy.
4. In the Vercel dashboard, go to the "Settings" tab of your project.
5. Add an environment variable:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: `your-telegram-bot-token`

### Step 4: Set the Webhook

After deploying, you will have a URL for your Vercel deployment (e.g., `https://your-vercel-project.vercel.app`). Use this URL to set your webhook.

Run the following script to set the webhook, replacing `YOUR_TELEGRAM_BOT_TOKEN_HERE` and `YOUR_VERCEL_URL` with your actual bot token and Vercel URL:

```python
import requests

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
WEBHOOK_URL = 'YOUR_VERCEL_URL/webhook'

TELEGRAM_API_URL = f'https://api.telegram.org/bot{TOKEN}/'
url = TELEGRAM_API_URL + 'setWebhook'
payload = {
    'url': WEBHOOK_URL
}
response = requests.post(url, json=payload)
print(response.json())
```

### Project Structure

```
echo_bot/
├── app.py
├── requirements.txt
├── vercel.json
├── static/
└── templates/
    └── index.html
```

- **app.py**: The main Flask application.
- **requirements.txt**: Lists the Python dependencies.
- **vercel.json**: Configuration file for Vercel.
- **static/**: Directory for static files.
- **templates/**: Directory for HTML templates.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Vercel](https://vercel.com/)
- [requests](https://requests.readthedocs.io/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

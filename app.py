from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)

@app.message("hello")
def say_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hi, <@{message['user']}>! This is HelpDesk Chatbot")

def main():
    try:
        SocketModeHandler(app=app, app_token=SLACK_APP_TOKEN).start()
    except:
        print("Failed to start Slack SocketModelHandler")
    finally:
        print("Disconnected Slack Bot")

if __name__ == "__main__":
    main()


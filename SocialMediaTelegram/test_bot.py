import asyncio
import os
import json
import requests
import schedule
import time
from datetime import datetime
import random

class Channel:
    def __init__(self, chat_id, name, active):
        self.chat_id = chat_id
        self.name = name
        self.active = active

class TelegramAIAgent:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        self.channels = self.load_channels()
        self.posts = self.load_posts()

    def load_channels(self):
        with open("config.json", "r") as f:
            config = json.load(f)
        return [Channel(ch["chat_id"], ch["name"], ch["active"]) for ch in config["channels"]]

    def load_posts(self):
        try:
            with open("posts.txt", "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("⚠️ posts.txt file not found.")
            return []

    def generate_post(self):
        if not self.posts:
            return "⚠️ No content available. Please update posts.txt"
        return random.choice(self.posts)

    def post_to_channel(self, channel, content):
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": channel.chat_id,
            "text": content,
            "parse_mode": "HTML"
        }
        response = requests.post(url, json=payload)
        return response.ok, response.json()

    async def process_scheduled_posts(self):
        for channel in self.channels:
            if not channel.active:
                continue
            content = self.generate_post()
            success, response = self.post_to_channel(channel, content)
            if success:
                print(f"✅ Posted to {channel.name} - {channel.chat_id}")
            else:
                print(f"❌ Failed to post to {channel.name}: {response}")

# --- SCHEDULE POSTING ---
def job(agent):
    print(f"\n[SCHEDULED POST] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    asyncio.run(agent.process_scheduled_posts())

def run_scheduled_jobs():
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN") or "7571164093:AAGPzZaOvpky34osCzP6mALMfb8v9soIgzU"
    agent = TelegramAIAgent(bot_token)

    # Post at 9 AM, 2 PM, and 7 PM
    schedule.every().day.at("09:00").do(job, agent)
    schedule.every().day.at("14:00").do(job, agent)
    schedule.every().day.at("18:20").do(job, agent)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduled_jobs()

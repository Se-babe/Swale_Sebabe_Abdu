#!/usr/bin/env python3
"""
Telegram Bot Setup and Configuration Script
This script helps you properly configure your Telegram bot with real channels.
"""

import json
import os
import asyncio
import aiohttp
from datetime import datetime, timedelta

class TelegramBotSetup:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
    
    async def test_bot_token(self):
        """Test if the bot token is valid"""
        url = f"{self.base_url}/getMe"
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    result = await response.json()
                    if result.get("ok"):
                        bot_info = result["result"]
                        print(f" Bot token is valid!")
                        print(f"   Bot name: {bot_info['first_name']}")
                        print(f"   Username: @{bot_info['username']}")
                        print(f"   Bot ID: {bot_info['id']}")
                        return True, bot_info
                    else:
                        print(f" Invalid bot token: {result}")
                        return False, None
            except Exception as e:
                print(f" Error testing bot token: {e}")
                return False, None
    
    async def get_chat_info(self, chat_id):
        """Get information about a chat/channel"""
        url = f"{self.base_url}/getChat"
        data = {"chat_id": chat_id}
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=data) as response:
                    result = await response.json()
                    if result.get("ok"):
                        return True, result["result"]
                    else:
                        return False, result
            except Exception as e:
                print(f"Error getting chat info: {e}")
                return False, {"error": str(e)}
    
    async def send_test_message(self, chat_id):
        """Send a test message to verify bot can post"""
        url = f"{self.base_url}/sendMessage"
        test_message = f" Test message from your Telegram AI Agent\n\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n your bot is working correctly! "
        
        data = {
            "chat_id": chat_id,
            "text": test_message,
            "parse_mode": "HTML"
        }
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=data) as response:
                    result = await response.json()
                    return result.get("ok"), result
            except Exception as e:
                return False, {"error": str(e)}

def get_bot_token():
    """Get bot token from environment or user input"""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not token:
        print(" Telegram Bot Token Required")
        print("You can either:")
        print("1. Set environment variable: TELEGRAM_BOT_TOKEN=your_token")
        print("2. Enter it now (it won't be saved)")
        print()
        token = input("Enter your bot token: ").strip()
    
    return token

def create_proper_config(channels_info):
    """Create a proper configuration file with real channels"""
    config = {
        "channels": channels_info,
        "posting_schedule": {
            "daily_posts": 3,
            "posting_hours": [9, 14, 19],
            "timezone": "UTC"
        },
        "content_settings": {
            "topics": [
                "Technology trends",
                "Daily motivation", 
                "Industry insights",
                "Tips and tricks",
                "News updates"
            ],
            "styles": ["informative", "casual", "motivational"]
        },
        "bot_settings": {
            "parse_mode": "HTML",
            "disable_notification": False,
            "error_retry_attempts": 3,
            "post_delay_seconds": 2
        }
    }
    
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print(" Created proper config.json file")

async def interactive_setup():
    """Interactive setup process"""
    print(" Telegram AI Agent Setup")
    print("=" * 40)
    
    # Get bot token
    bot_token = get_bot_token()
    if not bot_token:
        print(" Bot token is required!")
        return False
    
    # Test bot token
    setup = TelegramBotSetup(bot_token)
    is_valid, bot_info = await setup.test_bot_token()
    
    if not is_valid:
        print(" Please check your bot token and try again")
        return False
    
    print(f"\n Now let's set up your channels...")
    print("You need to:")
    print("1. Add your bot to the channel as an administrator")
    print("2. Give it permission to 'Post Messages'")
    print("3. Get the channel username (e.g., @mychannel) or ID")
    print()
    
    channels_info = []
    
    while True:
        print(f"\n Channel Setup (Currently have {len(channels_info)} channels)")
        
        if len(channels_info) == 0:
            print("You need at least one channel to continue.")
        
        channel_input = input("Enter channel username (@channel) or ID, or 'done' to finish: ").strip()
        
        if channel_input.lower() == 'done':
            if len(channels_info) > 0:
                break
            else:
                print(" You need at least one channel!")
                continue
        
        if not channel_input:
            continue
        
        # Test channel access
        print(f" Testing access to {channel_input}...")
        
        chat_valid, chat_info = await setup.get_chat_info(channel_input)
        
        if chat_valid:
            channel_name = chat_info.get('title', chat_info.get('username', 'Unknown'))
            print(f" Found channel: {channel_name}")
            
            # Test sending message
            test_ok, test_result = await setup.send_test_message(channel_input)
            
            if test_ok:
                print(f" Successfully sent test message!")
                
                channels_info.append({
                    "chat_id": channel_input,
                    "name": channel_name,
                    "active": True
                })
                
                print(f" Added channel: {channel_name}")
                
            else:
                print(f" Could not send message to {channel_input}")
                print(f"   Error: {test_result.get('description', 'Unknown error')}")
                print("   Make sure the bot is admin with 'Post Messages' permission")
                
                add_anyway = input("Add this channel anyway? (y/N): ").strip().lower()
                if add_anyway == 'y':
                    channels_info.append({
                        "chat_id": channel_input,
                        "name": channel_name,
                        "active": False  # Mark as inactive since we can't post
                    })
        else:
            print(f"Could not access {channel_input}")
            print(f"   Error: {chat_info.get('description', 'Unknown error')}")
            print("   Make sure:")
            print("   - Channel username is correct (starts with @)")
            print("   - Bot is added to the channel")
            print("   - Bot has admin privileges")
    
    # Create configuration
    if channels_info:
        create_proper_config(channels_info)
        
        print(f"\n Setup Complete!")
        print(f"Configured {len(channels_info)} channels")
        print(f" Created config.json")
        print(f"\nYour channels:")
        for channel in channels_info:
            status = " Active" if channel["active"] else " Inactive"
            print(f"   {status} {channel['name']} ({channel['chat_id']})")
        
        return True
    else:
        print(" No channels configured. Setup incomplete.")
        return False

def create_test_script():
    """Create a simple test script"""
    test_script = '''#!/usr/bin/env python3
"""
Simple test script for Telegram AI Agent
"""
import asyncio
import os
from telegram_ai_agent import TelegramAIAgent

async def test_agent():
    """Test the agent with a single post"""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        print(" TELEGRAM_BOT_TOKEN not set!")
        return
    
    # Create agent (it will load config.json automatically)
    agent = TelegramAIAgent(bot_token)
    
    print(f" Loaded {len(agent.channels)} channels")
    for channel in agent.channels:
        status = "🟢" if channel.active else "🔴"
        print(f"   {status} {channel.name} ({channel.chat_id})")
    
    # Create a test post
    print("\\n Creating test post...")
    post = await agent.create_and_schedule_post(
        topic="Test message",
        style="informative",
        schedule_time=None  # Send immediately
    )
    
    print(f" Test post created: {post.content[:50]}...")
    
    # Process the post immediately
    await agent.process_scheduled_posts()
    
    print(" Test complete!")

if __name__ == "__main__":
    asyncio.run(test_agent())
'''
    
    with open("test_bot.py", "w") as f:
        f.write(test_script)
    
    print(" Created test_bot.py - use this to test your setup")

async def main():
    """Main setup function"""
    print("Welcome to Telegram AI Agent Setup! ")
    print()
    
    # Check if config already exists
    if os.path.exists("config.json"):
        print(" Found existing config.json")
        overwrite = input("Do you want to reconfigure? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("Setup cancelled. Using existing configuration.")
            return
    
    # Run interactive setup
    success = await interactive_setup()
    
    if success:
        # Create test script
        create_test_script()
        
        print("\n Next Steps:")
        print("1. Set your bot token as environment variable:")
        print(f"   export TELEGRAM_BOT_TOKEN=your_token")
        print("2. Test your setup:")
        print("   python test_bot.py")
        print("3. Run the full agent:")
        print("   python telegram_ai_agent.py")
        print("\n Tip: Use 'python gitignore_setup.py' to secure your files!")
    else:
        print("\n Setup incomplete. Please try again.")

if __name__ == "__main__":
    asyncio.run(main())

import datetime
import json
import os
from models import MessageRequest, Reminder, CommandLog

def search_ecommerce(product_name: str, platform: str):
    return {
        "platform": platform,
        "search_url": f"https://www.{platform.lower()}.com/search?q={product_name}"
    }

def send_message(request: MessageRequest):
    log = f"Sent '{request.message}' to {request.recipient} via {request.platform}."
    return {"log": log}

def add_reminder(reminder: Reminder):
    reminders = get_reminders()
    reminders.append(reminder)
    with open("ai_personal_assistant/data/reminders.json", "w") as f:
        json.dump([r.dict() for r in reminders], f, indent=4)
    return reminder

def get_reminders():
    if not os.path.exists("ai_personal_assistant/data/reminders.json"):
        return []
    with open("ai_personal_assistant/data/reminders.json", "r") as f:
        data = json.load(f)
        return [Reminder(**r) for r in data]

def delete_reminder(reminder_id: str):
    reminders = get_reminders()
    reminders = [r for r in reminders if r.id != reminder_id]
    with open("ai_personal_assistant/data/reminders.json", "w") as f:
        json.dump([r.dict() for r in reminders], f, indent=4)
    return True

def generate_search_url(query: str, platform: str):
    platform_url = {
        "youtube": "https://www.youtube.com/results?search_query=",
        "google": "https://www.google.com/search?q=",
        "bing": "https://www.bing.com/search?q="
    }
    url_prefix = platform_url.get(platform.lower(), "https://www.google.com/search?q=")
    return f"{url_prefix}{query}"

def play_media(query: str, platform: str):
    return f"Simulating playing '{query}' on {platform}."

def log_command(command: str, history: list):
    history.append(CommandLog(
        timestamp=datetime.datetime.now().isoformat(),
        command=command
    ))

def get_conversation_history(history: list):
    return history

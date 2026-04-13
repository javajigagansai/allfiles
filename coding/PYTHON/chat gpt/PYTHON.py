# ai_personal_assistant.py

"""
AI Personal Assistant
----------------------
Instructions:
1. Install Python 3.8+.
2. Install dependencies:
   pip install -r requirements.txt
3. Run the script:
   python ai_personal_assistant.py
4. Use voice or type commands to interact.
5. Tkinter GUI for logs and manual commands.

Note: Some features (e.g., WhatsApp, Amazon) require API keys and setup.
Replace placeholders with your API credentials where indicated.
"""

import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext
import re
import datetime
import webbrowser
import requests
import json
from threading import Thread
import time


class PersonalAssistant:
    """
    Main AI Personal Assistant class.
    """

    def _init_(self):
        self.name = "Assistant"
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.conversation_history = []
        self.preferences = {"voice": "default", "volume": 1.0}
        self.gui = None
        self.running = False
        self._setup_gui()

    def _setup_gui(self):
        """
        Initialize the Tkinter GUI.
        """
        self.gui = tk.Tk()
        self.gui.title(f"{self.name} - AI Personal Assistant")
        self.gui.geometry("600x400")

        self.log_area = scrolledtext.ScrolledText(self.gui, wrap=tk.WORD, height=15)
        self.log_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.command_entry = tk.Entry(self.gui, width=50)
        self.command_entry.pack(padx=10, pady=5)

        self.submit_button = tk.Button(
            self.gui, text="Submit Command", command=self._process_manual_command
        )
        self.submit_button.pack(pady=5)

        self._log("Assistant initialized. Say or type a command to start.")

    def _log(self, message):
        """
        Log messages to GUI and console.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        self.log_area.insert(tk.END, log_message)
        self.log_area.see(tk.END)
        print(log_message.strip())

    def _speak(self, text):
        """
        Speak out the given text.
        """
        self._log(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def _listen(self):
        """
        Listen for voice commands.
        """
        try:
            with sr.Microphone() as source:
                self._log("Listening for command...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio).lower()
                self._log(f"Recognized command: {command}")
                return command
        except sr.WaitTimeoutError:
            self._log("No command heard within timeout.")
        except sr.UnknownValueError:
            self._log("Could not understand the command.")
        except sr.RequestError as e:
            self._log(f"Speech recognition error: {e}")
        return ""

    def _process_manual_command(self):
        """
        Handle commands entered in the GUI.
        """
        command = self.command_entry.get().lower().strip()
        if command:
            self._log(f"Manual command: {command}")
            self._process_command(command)
            self.command_entry.delete(0, tk.END)

    def _process_command(self, command):
        """
        Core logic: process commands.
        """
        self.conversation_history.append(command)
        self._log(f"Processing command: {command}")

        if "change your name to" in command:
            self._change_name(command)
        elif "set a reminder" in command:
            self._set_reminder(command)
        elif "send an email" in command:
            self._send_email(command)
        elif "search for" in command and any(site in command for site in ["amazon", "flipkart", "walmart"]):
            self._search_ecommerce(command)
        elif "send a message" in command:
            self._send_message(command)
        elif "play" in command and any(platform in command for platform in ["youtube", "spotify", "netflix"]):
            self._play_media(command)
        elif "open website" in command:
            self._open_website(command)
        else:
            response = "Sorry, I didn't understand that. Please rephrase."
            self._speak(response)
            self._log(response)

    def _change_name(self, command):
        match = re.search(r"change your name to (\w+)", command)
        if match:
            self.name = match.group(1).capitalize()
            self.gui.title(f"{self.name} - AI Personal Assistant")
            response = f"My name is now {self.name}."
            self._speak(response)
            self._log(response)

    def _set_reminder(self, command):
        time_match = re.search(r"at (\d{1,2}:\d{2})", command)
        task_match = re.search(r"reminder for (.+?)( at|$)", command)
        if time_match and task_match:
            reminder_time = time_match.group(1)
            task = task_match.group(1)
            response = f"Reminder set for '{task}' at {reminder_time}."
            self._speak(response)
            self._log(response)
            # TODO: Use threading/timers for actual reminders
        else:
            response = "Please provide the task and time."
            self._speak(response)
            self._log(response)

    def _send_email(self, command):
        self._log("Simulating email sending (API setup required).")
        response = "Please provide recipient, subject, and body."
        self._speak(response)
        self._log(response)

    def _search_ecommerce(self, command):
        product_match = re.search(r"search for (.+?) on", command)
        if product_match:
            product = product_match.group(1)
            platform = "Amazon" if "amazon" in command else "Flipkart" if "flipkart" in command else "Walmart"
            response = f"Simulating search for '{product}' on {platform}."
            self._speak(response)
            self._log(response)
            # TODO: API integration
        else:
            response = "Please specify what to search for."
            self._speak(response)
            self._log(response)

    def _send_message(self, command):
        platform = "WhatsApp" if "whatsapp" in command else "Telegram" if "telegram" in command else "Instagram" if "instagram" in command else "Unknown"
        recipient_match = re.search(r"to (\w+)", command)
        message_match = re.search(r"message (.+?)( on|$)", command)
        if recipient_match and message_match:
            recipient = recipient_match.group(1)
            message = message_match.group(1)
            response = f"Simulating sending '{message}' to {recipient} on {platform}."
            self._speak(response)
            self._log(response)
            # TODO: API integration
        else:
            response = "Please provide recipient and message."
            self._speak(response)
            self._log(response)

    def _play_media(self, command):
        platform = "YouTube" if "youtube" in command else "Spotify" if "spotify" in command else "Netflix"
        content_match = re.search(r"play (.+?) on", command)
        if content_match:
            content = content_match.group(1)
            url = f"https://www.{platform.lower()}.com/search?q={content}"
            webbrowser.open(url)
            response = f"Playing '{content}' on {platform}."
            self._speak(response)
            self._log(response)
        else:
            response = "Please specify what to play."
            self._speak(response)
            self._log(response)

    def _open_website(self, command):
        url_match = re.search(r"open website (.+)", command)
        if url_match:
            url = url_match.group(1).strip()
            if not url.startswith("http"):
                url = f"https://{url}"
            self._log(f"Opening: {url}")
            webbrowser.open(url)
            self._speak(f"Opening {url}.")
        else:
            response = "Please specify a website URL."
            self._speak(response)
            self._log(response)

    def run(self):
        self.running = True
        self._log(f"{self.name} is ready. Say or type a command.")
        self._speak(f"Hello, I'm {self.name}. How can I help you?")

        while self.running:
            self.gui.update()
            time.sleep(0.1)

    def stop(self):
        self.running = False
        self.gui.destroy()
        self.engine.stop()
        self._log("Assistant stopped.")


def main():
    assistant = PersonalAssistant()
    try:
        assistant.run()
    except KeyboardInterrupt:
        assistant.stop()


if __name__ == "_main_":
    main()
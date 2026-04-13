import sys
import sqlite3
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLabel, QSystemTrayIcon, QMenu
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from playwright.sync_api import sync_playwright
import pyttsx3
import uuid

# Set Qt environment variables to ensure proper platform plugin initialization
if not os.environ.get("DISPLAY"):
    os.environ["DISPLAY"] = ":0"  # Default to display :0 if not set
os.environ["QT_LOGGING_RULES"] = "qt5ct.debug=false"
os.environ["QT_QPA_PLATFORM"] = "xcb"  # Primary platform
# Fallback to offscreen if xcb fails
if "xcb" not in QApplication.platformName():
    os.environ["QT_QPA_PLATFORM"] = "offscreen"

# Simulated AI Engine (replace with GPT-4 API in production)
class AIEngine:
    def __init__(self):
        self.memory = []  # Store conversation history
        self.persona = "professional"  # Default persona

    def process_command(self, command):
        # Simulate natural language understanding
        response = f"Processing command: {command}"
        if "draft email" in command.lower():
            response = self.draft_email(command)
        elif "search web" in command.lower():
            response = self.web_search(command)
        elif "organize files" in command.lower():
            response = self.organize_files(command)
        self.memory.append({"command": command, "response": response})
        return response

    def draft_email(self, command):
        # Simulate email drafting
        return "Drafted email based on: " + command

    def web_search(self, command):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://www.google.com")
            page.fill("input[name='q']", command)
            page.press("input[name='q']", "Enter")
            results = page.query_selector_all(".g")
            summary = [result.inner_text()[:100] for result in results[:3]]
            browser.close()
            return f"Web search results: {summary}"

    def organize_files(self, command):
        # Simulate file organization
        directory = os.path.expanduser("~/Desktop")
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                os.rename(
                    os.path.join(directory, filename),
                    os.path.join(directory, "organized_" + filename)
                )
        return f"Organized files in {directory}"

# Database for user preferences and logs
class DataStore:
    def __init__(self):
        self.conn = sqlite3.connect("novadesk.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS preferences (
                id INTEGER PRIMARY KEY,
                key TEXT UNIQUE,
                value TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                command TEXT,
                response TEXT
            )
        ''')
        self.conn.commit()

    def save_preference(self, key, value):
        cursor = self.conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO preferences (key, value) VALUES (?, ?)", (key, value))
        self.conn.commit()

    def get_preference(self, key):
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM preferences WHERE key = ?", (key,))
        result = cursor.fetchone()
        return result[0] if result else None

    def log_action(self, command, response):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO logs (timestamp, command, response) VALUES (datetime('now'), ?, ?)",
                      (command, response))
        self.conn.commit()

# Main Application Window
class NovaDeskWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ai_engine = AIEngine()
        self.data_store = DataStore()
        self.tts_engine = pyttsx3.init()
        self.init_ui()
        self.init_tray()
        self.check_permissions()

    def init_ui(self):
        self.setWindowTitle("NovaDesk")
        self.setGeometry(100, 100, 800, 600)

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Command input
        self.command_input = QTextEdit()
        self.command_input.setPlaceholderText("Enter your command (e.g., 'Draft email', 'Search web')")
        layout.addWidget(QLabel("Command:"))
        layout.addWidget(self.command_input)

        # Response display
        self.response_display = QTextEdit()
        self.response_display.setReadOnly(True)
        layout.addWidget(QLabel("Response:"))
        layout.addWidget(self.response_display)

        # Buttons
        button_layout = QHBoxLayout()
        execute_button = QPushButton("Execute")
        execute_button.clicked.connect(self.execute_command)
        speak_button = QPushButton("Speak Response")
        speak_button.clicked.connect(self.speak_response)
        button_layout.addWidget(execute_button)
        button_layout.addWidget(speak_button)
        layout.addLayout(button_layout)

    def init_tray(self):
        tray = QSystemTrayIcon(QIcon("icon.png"))  # Assume icon.png exists
        tray_menu = QMenu()
        show_action = tray_menu.addAction("Show")
        show_action.triggered.connect(self.show)
        quit_action = tray_menu.addAction("Quit")
        quit_action.triggered.connect(QApplication.quit)
        tray.setContextMenu(tray_menu)
        tray.show()

    def check_permissions(self):
        # Simulate permission check (first run)
        if not self.data_store.get_preference("permissions_granted"):
            self.response_display.setText("Welcome to NovaDesk! Please grant permissions for microphone, filesystem, and browser control.")
            self.data_store.save_preference("permissions_granted", "true")

    def execute_command(self):
        command = self.command_input.toPlainText()
        if command:
            response = self.ai_engine.process_command(command)
            self.response_display.setText(response)
            self.data_store.log_action(command, response)

    def speak_response(self):
        response = self.response_display.toPlainText()
        if response:
            self.tts_engine.say(response)
            self.tts_engine.runAndWait()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:  # Hotkey to show window
            self.show()

# Application Entry Point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NovaDeskWindow()
    window.show()
    sys.exit(app.exec_())
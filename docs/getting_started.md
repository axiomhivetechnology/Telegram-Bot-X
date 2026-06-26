# Getting Started with Telegram Bots

This guide is for absolute beginners who have never created a Telegram Bot before.

## 1. Create Your Bot
All Telegram bots are created through **@BotFather**.

1.  **Open Telegram** and search for `@BotFather`.
2.  **Start a chat** by clicking the "Start" button.
3.  **Create a new bot**: Send `/newbot`.
4.  **Name your bot**: This is the display name (e.g., `My First Helper`).
5.  **Give it a username**: This must end in `bot` (e.g., `helper_123_bot`).
6.  **Get your Token**: BotFather will give you an **API Token**. Keep this secret!

## 2. Setting Up Your Environment

### Python (Recommended)
1.  **Install Python**: Download from [python.org](https://www.python.org/).
2.  **Check installation**: Open your terminal/command prompt and type:
    ```bash
    python --version
    ```
3.  **Install a library**:
    ```bash
    pip install python-telegram-bot
    ```

### Node.js
1.  **Install Node.js**: Download from [nodejs.org](https://nodejs.org/).
2.  **Check installation**:
    ```bash
    node -v
    ```
3.  **Install a library**:
    ```bash
    npm install telegraf
    ```

## 3. Running Your First Bot
Go to the `templates/python/beginner` or `templates/nodejs/beginner` folder in this repo for a simple script you can run immediately.

### Basic Concepts
-   **Long Polling**: Your bot constantly asks Telegram "Do you have any new messages for me?". This is great for development.
-   **Commands**: Messages starting with `/` (like `/start` or `/help`).
-   **Updates**: Every interaction (message, button click) is an "Update".

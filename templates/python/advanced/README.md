# Advanced Python Bot (aiogram + SQLite)

This template is built with **aiogram 3**, a modern, asynchronous framework for high-performance bots.

## Features
- **Asynchronous Execution**: Built on `asyncio` for speed and efficiency.
- **Database Integration**: Uses `sqlite3` to persist user data.
- **Modern Syntax**: Uses decorators and filters for clean code.

## How to Run

1.  **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Set your Token**: Create a `.env` file with `TELEGRAM_TOKEN`.
3.  **Run the bot**:
    ```bash
    python bot.py
    ```

## Architecture
-   `bot.py`: Main entry point.
-   `users.db`: SQLite database (created automatically on first run).

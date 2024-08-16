# Anti-Spam Bot

This repository contains a Telegram bot designed to automatically detect and delete spam messages in a Telegram group or channel. The bot checks for messages containing URLs and deletes them to prevent spam.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Features

- **Automatic Spam Detection**: Detects messages containing URLs and deletes them to prevent spam.
- **Customizable**: You can easily customize the bot to add more spam detection criteria.

## Installation

### Prerequisites

- Python 3.7+
- A Telegram bot token (you can obtain one by chatting with [BotFather](https://t.me/botfather) on Telegram).

### Steps

1. **Clone the repository:**

   ```bash
   git clone git@github.com:V-Obojo/antispam.git
   cd antispam
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

4. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure your bot token:**

   - Copy the `config.ini.example` file to `config.ini`:

     ```bash
     cp config.ini.example config.ini
     ```

   - Open `config.ini` and add your Telegram bot token:

     ```ini
     [TOKEN]
     TOKEN = your-telegram-bot-token
     ```

## Usage

To start the bot, run the following command:

```bash
python as_main.py
```

The bot will begin polling for messages in the Telegram group or channel it's added to. Any message containing a URL will be automatically deleted.

**Note:** The bot must be added as an admin in the Telegram group or channel for it to have the necessary permissions to delete messages.


## Configuration

The bot's configuration is managed via the `config.ini` file. You can adjust various settings to customize the bot's behavior:

- **TOKEN**: Your Telegram bot token.
  
Additional customization options can be added as needed.

## Project Structure

```
telegram-antispam-bot/
│
├── antiSpam.py            # Contains the anti-spam logic
├── as_main.py             # The main entry point for the bot
├── config.ini.example     # Example configuration file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Contributing

Contributions are welcome! If you have ideas for improvements or bug fixes, feel free to fork the repository and submit a pull request. Please ensure that your code adheres to the necessary coding standards.
# Discord Word Filter Bot

The Discord Word Filter Bot is a Python application that allows you to create a bot for your Discord server, which can automatically block or censor specific words or phrases.

## Prerequisites

- Python 3.6 or higher
- Discord.py library (`discord.py`)
- dotenv library (`python-dotenv`)

## Installation

1. Clone this repository to your local machine: https://github.com/DeidaTypes/discord-filter-bot

2. Navigate to the project directory:

3. Install the required dependencies:

4. Set up the bot token:
- Create a new Discord bot on the Discord Developer Portal (https://discord.com/developers/applications).
- Copy the bot token.
- Create a new file named `.env` in the project root directory.
- Inside the `.env` file, add the following line:
  ```
  BOT_TOKEN=your-bot-token
  ```
  Replace `your-bot-token` with the token you obtained from the Discord Developer Portal.

## Configuration

In the `bot.py` file, you can modify the list of blocked words by editing the `blocked_words` variable. Add or remove words as desired. The bot will automatically block any message containing these words.

## Usage

1. Run the bot using the following command:
  
2. Invite the bot to your Discord server:
- Go to the Discord Developer Portal (https://discord.com/developers/applications) and select your bot.
- Under the "OAuth2" section, select the appropriate scopes and permissions for your bot.
- Copy the generated invite link and open it in your web browser.
- Select your server and authorize the bot to join.

3. Once the bot is in your server, it will automatically monitor and block any messages that contain the specified blocked words.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).






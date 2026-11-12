# Video Bot

SuperSlavik is a Python Telegram bot that processes videos with MoviePy and sends them back as MP4 files. The `/run` command displays a welcome message in Armenian.

## How It Works

1. Send a video to the bot using Telegram's video attachment option.
2. The bot downloads the video and saves it temporarily as `myvideo.mp4`.
3. MoviePy re-encodes the video and writes it to `dst_videos/output_video.mp4`.
4. The bot sends the resulting MP4 to the chat and deletes the temporary files after a successful send.

The current version always outputs MP4. If the input is already MP4, the bot re-encodes it in the same format.

## Technologies

- **Python** for the bot logic
- **pyTelegramBotAPI (`telebot`)** for receiving and sending Telegram videos
- **MoviePy** and **FFmpeg** for video processing

## Run Locally

1. Install the dependencies. The current `moviepy.editor` import uses the MoviePy 1.x API.

   ```powershell
   python -m pip install pyTelegramBotAPI "moviepy<2"
   ```

2. Create the `dst_videos` directory next to the script and run the bot from that directory's parent.

3. Get a bot token from `@BotFather` and update the script to read it from an environment variable.

   ```python
   bot = TeleBot(token=os.environ["TELEGRAM_BOT_TOKEN"])
   ```

4. In Windows PowerShell, set the token and start the bot. Replace `bot.py` with the actual script filename if needed.

   ```powershell
   $env:TELEGRAM_BOT_TOKEN = "<YOUR_BOT_TOKEN>"
   python bot.py
   ```

5. Open the bot in Telegram, send `/run`, then send a video to test it.

## Current Limitations

- Send videos as Telegram video attachments. Files sent as documents are outside the current handler.
- The bot uses fixed filenames, so simultaneous requests can overwrite each other's files.

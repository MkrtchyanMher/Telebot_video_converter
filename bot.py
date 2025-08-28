from telebot import TeleBot, types
import os
from moviepy.editor import *


TOKEN = '7005274873:AAHo7_BxMuwJD8uFsFL14tFGO87fyaOx-wQ'

bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['run'])
def run_my_bot(message):
    bot.send_message(message.chat.id, f'Բարև, իմ անունը SuperSlavik է, ես կկատարեմ քո երազանքը փոխելու վիդեո ֆայլի տիպը 🐟🐟🐟')

@bot.message_handler(content_types=['video'])
def handle_video(message):
    try:
        # Download the video file
        video_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(video_info.file_path)
        file_name = 'myvideo.mp4'  # Save the video with a specific name
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Convert the video format
        output_file = 'dst_videos/output_video.mp4'  # Specify the output file name
        video_clip = VideoFileClip(file_name)
        video_clip.write_videofile(output_file)

        # Send the converted video back to the user
        with open(output_file, 'rb') as video:
            bot.send_video(message.chat.id, video)

        # Clean up the temporary files
        os.remove(file_name)
        os.remove(output_file)
        
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Start the bot
bot.polling()
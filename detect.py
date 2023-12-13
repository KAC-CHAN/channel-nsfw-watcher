#Telegram @izuya

import pyrogram
from nsfw_detector import detect

api_id = 26788480
api_hash = "858d65155253af8632221240c535c314"
bot_token = "6551178239:AAGWE_oTVdeyoYGxCCabwdiN1xOFpfj3FfE"

bot = pyrogram.Client("nsfw_channel_bot", 
                      api_id,  
                      api_hash,
                      bot_token=bot_token)

@bot.on_message()
async def check_nsfw(client, message):

    # Check only messages in channel
    if not message.forward_from_chat:
        return

    # Get media from message if any
    media = message.photo or message.animation or message.video or message.sticker 

    # Detect NSFW
    if media:
        is_nsfw = detect(media)
    else:
        is_nsfw = False

    # Delete message if detected as NSFW
    if is_nsfw:
        await message.delete()

bot.run()

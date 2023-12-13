#Telegram @izuya

import pyrogram
from deeppavlov import configs, build_model

classifier = build_model(configs.nsfw.nsfw_bert)

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

  # Get media from message  
  media = message.photo or message.animation or message.video or message.sticker

  if media:
    # Pass media to classifier
    prediction = classifier({'image': media})['prediction']  
    # Check prediction
    is_nsfw = prediction == 'nsfw'

  if is_nsfw:
    # Delete NSFW message
    print("Deleting NSFW message")
    await message.delete()

# Run bot
if __name__ == '__main__':
  bot.run()

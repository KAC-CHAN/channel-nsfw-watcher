#Telegram @izuya

import pyrogram
import deeppavlov

api_id = 26788480
api_hash = "858d65155253af8632221240c535c314"
bot_token = "6551178239:AAGWE_oTVdeyoYGxCCabwdiN1xOFpfj3FfE"

bot = pyrogram.Client("nsfw_channel_bot", 
                      api_id,  
                      api_hash,
                      bot_token=bot_token)

from deeppavlov.core.commands.train import ModelTrainer
from deeppavlov import build_model

trainer = ModelTrainer()
print(trainer.configs) 

# Get NSFW config 
nsfw_config = <config identified from print>

classifier = build_model(nsfw_config)

@bot.on_message()
async def check_nsfw(client, message):

  media = message.photo or message.animation or message.video  

  if media:
    prediction = classifier({'image': media})['prediction']
    is_nsfw = prediction == 'porn'

  if is_nsfw:  
    await message.delete()

bot.run()

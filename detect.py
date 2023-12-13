#Telegram @izuya

import pyrogram
import deeppavlov

classifier = build_model(configs.nsfw.nsfw_bert)

api_id = 26788480
api_hash = "858d65155253af8632221240c535c314"
bot_token = "6551178239:AAGWE_oTVdeyoYGxCCabwdiN1xOFpfj3FfE"

bot = pyrogram.Client("nsfw_channel_bot", 
                      api_id,  
                      api_hash,
                      bot_token=bot_token)

classifier = deeppavlov.build_model(deeppavlov.configs.bert_base_cased.classify_bert)

@bot.on_message()
async def check_nsfw(client, message):

  media = message.photo or message.animation or message.video  

  if media:
    prediction = classifier({'image': media})['prediction']
    is_nsfw = prediction == 'porn'

  if is_nsfw:  
    await message.delete()

bot.run()

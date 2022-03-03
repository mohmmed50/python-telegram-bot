from telegram import *
from telegram.ext import *
from connect_data import *
from number import *
import logging
import json
import requests
import pyqrcode
import pytube 




#TOKEN = '5150207800:AAFiyxvUY8FqzpcZKDlYnoQKqKXXxs31cJE'
TOKEN = '5250776776:AAHFLSO37mV4kdZ2Z2ckQAxVASlRc34mY3M'



data_log_join = open('data.txt','a')
log_in = open('log.txt','a')
ra = {}
def data_update ():
    global ra
    for i in range(1,len(res)):
        val = worksheet.row_values(i+1)
        ra[str(val[2])] = str(val[4]) 
data_update ()
#print(ra)
noadmin_re = 'المشرف فقط من يمكنه التعديل'

mian_ms_id = ''

chose_admin = ''

point_num = ''

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
def downloadVideo(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    print(video.title)
    video.download(r'.\vid')
    return video.title
  
logger = logging.getLogger(__name__)



def new_user(data):
    global data_log_join
    data_log_join.write(str(data)+'\n')
    data_log_join.close()
    '''inside = 'f'
    for i in range(len(res)):
        val = worksheet.row_values(i+1)
        if val[0] == str(data.id):
            print('done')
            inside = 't'
    if inside == 'f':
        user = [data.id, data.name, data.full_name]
        worksheet.append_row(user) '''   


role,points = '',''
def out_by_id(user_id):
    global id,role,points 
    for i in range(len(res)):
        val = worksheet.row_values(i+1)
        if val[0] == str(user_id.id):
            print('done')
            role = val[3]
            points = val[4]
            break
    for i in range(len(res)):
        val = worksheet.row_values(i+1)
        if val[1] == str(user_id.name):
            print('done')
            role = val[3]
            points = val[4]
            break


# This function replies with 'Hello <user.first_name>'
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text=f'اهلا  {update.effective_user.first_name} 👋🏻'+'\nكيف استطيع مساعدتك🤔'+'\nِ')
    print(update.message.text)
    print(update.message.text)
    print(update.message.text)
    print(update.message.text)
    print(update.message.text)
    
    
def poits(update: Update, context: CallbackContext):
    out_by_id(update.effective_user)
    update.message.reply_text(f'اهلا {update.effective_user.first_name}\n نقاطك هيه \n {numbers[points]}'+'\nِ')
def admin(update: Update, context: CallbackContext):
    global chose_admin 
    if update.effective_user.name == '@M07mMedH':
        keyboard = [
        [InlineKeyboardButton("اضافة نقاط للطلاب", callback_data='chose_point_num')]
        ]
        Reply_marku = InlineKeyboardMarkup(keyboard)
        chose_admin = update.message.reply_text('اختر', reply_markup=Reply_marku)
    else:
        update.message.reply_text(noadmin_re)   


    #print(f"likes => {likes} and dislikes => {dislikes}")
dat = {}
def button(update: Update, context: CallbackContext) -> None:
    global dat
    global point_num
    query = update.callback_query
    query.answer()
    if query.data == 'chose_point_num':
        keyboard = [
        [InlineKeyboardButton("➕1️⃣", callback_data='add_point1'),InlineKeyboardButton("➕2️⃣", callback_data='add_point2'),InlineKeyboardButton("➕3️⃣", callback_data='add_point3')],
        [InlineKeyboardButton("➕4️⃣", callback_data='add_point4')],
        [InlineKeyboardButton("➕5️⃣", callback_data='add_point5')],
        ]
        Reply_marku = InlineKeyboardMarkup(keyboard)
        context.bot.editMessageText(chat_id=update.effective_chat.id,message_id=chose_admin.message_id, text="اختر عدد النقاط",reply_markup=Reply_marku)

    #query.edit_message_text(text=f"Selected option: {query.data}")
    blol = ['add_point1','add_point2','add_point3','add_point4','add_point5']
    for lol in blol:
        if update.effective_user.name == '@M07mMedH':
            if query.data == lol :
                point_num = int(lol[-1])
                if update.effective_user.name == '@M07mMedH':
                    keyboard = []
                    keo = 0
                    for i in range(len(res)):
                        
                        val = worksheet.row_values(i+1)
                        li = [InlineKeyboardButton(val[2], callback_data=i)]
                        keyboard.append(li)

                        dat[i] = val[1]
                        
                    print(dat)   
                    Rep = InlineKeyboardMarkup(keyboard)
                    context.bot.editMessageText(chat_id=update.effective_chat.id,message_id=chose_admin.message_id, text="اختر الطالب \n"+'عدد النقاط المختار =' +str(numbers[str(point_num)]),reply_markup=Rep)
                else:
                    pass
        for i in range(len(dat)):
            if query.data == str(i):
                if update.effective_user.name == '@M07mMedH':
                    print(dat[i])
                    val = worksheet.row_values(i+1)
                    print('val in ;',val[2])
                    worksheet.update_cell(i+1,5, str(int(val[4])+int(point_num)))  
                    data_update ()
                    context.bot.editMessageText(chat_id=update.effective_chat.id,message_id=chose_admin.message_id, 
                                                text=f" تم اضافة {str(numbers[str(point_num)])}  نقاط \n للطالب {val[2]}")
                    point_num = ''
                else:
                    pass 
    data_update ()
    #context.bot.send_message(chat_id=update.effective_chat.id,text = 'k')
def range0(update: Update, context: CallbackContext) :
    global ra
    out = ''
    ra_range = sorted(ra.items(), key=lambda x: int(x[1]), reverse=True)
    for i in ra_range:
        out = out + str(i[0]+'\t'+numbers[str(i[1])]+'\n')
    update.message.reply_text(out)

def upd0(update: Update, context: CallbackContext) :
    ms = update.message.message_id
    data_update ()
    
    
    #update.message.reply_text(chat_id=update.effective_chat.id,text = f"{i[0]},{i[1]}")
def msinfo(update: Update, context: CallbackContext) :
    global mian_ms_id
    if update.effective_user.name == '@M07mMedH':
        print(update.message.reply_to_message.message_id)
        mian_ms_id = update.message.reply_to_message.message_id
        context.bot.send_message(chat_id=update.effective_chat.id,text=str('\n تم تعيين الرسالة الرئيسية'))
    



def reply(update, context):
    global TOKEN
    user_input = update.message.text
    print(update.effective_user.first_name +'\t\t'+ update.message.text)
    #log_in.write(update.effective_user.first_name +'\t\t'+ update.message.text)
    d = update.effective_user.first_name +'\t\t'+ update.message.text
    url = f'https://api.telegram.org/bot5250776776:AAHFLSO37mV4kdZ2Z2ckQAxVASlRc34mY3M/sendMessage?chat_id=-1001586184673&text={d}'
    requests.get(url)
    if user_input[0] == '.':
        update.message.reply_text('مغلق للصيانه 😅')
        #x = json.loads(requests.get(f'https://api.simsimi.net/v2/?text={user_input}&lc=ar').text)
        #y = json.loads(x.text)
        #update.message.reply_text(x["success"])
        #print(x["success"])
        #d = x["success"]
        #url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=-1001586184673&text={d}'
        #requests.get(url)
    if user_input[0] == 'm':
        clear_ = user_input.replace(user_input[0],'')
        clear_0= clear_.replace('x','*')
        update.message.reply_text(eval(clear_0))

    if user_input[0] == 'q' and user_input[1] == 'r':
        scale_qr = ''
        out_out = user_input.replace('qr','')
        bot = Bot(token=TOKEN)
        print('heeer')
        if int(out_out[-1]) >= 1 :
            scale_qr = int(out_out[-1])
        text = pyqrcode.create(out_out)
        text.png(r'code.png', scale=scale_qr)
        bot.send_photo(chat_id=update.effective_chat.id, photo=open(r'.\code.png', 'rb'))
    if user_input[0] == 'd' or user_input[0] == 'D' :
        pass
        #out_out0 = user_input.replace(user_input[0],'')
        #bot = Bot(token=TOKEN)
        #print('heeer')
        #bot.send_video(chat_id=update.effective_chat.id, video=open(fr'.\vid\{downloadVideo(out_out0)}.mp4', 'rb'))
  



# Insert your token here update.effective_user.first_name
updater = Updater(TOKEN)


# Make the hello command run the hello function
updater.dispatcher.add_handler(CommandHandler(['hello','start'], hello))
########################
updater.dispatcher.add_handler(CommandHandler(['mypoints','points','mp'], poits))
updater.dispatcher.add_handler(CommandHandler(['ra'], range0))
updater.dispatcher.add_handler(CommandHandler(['upd'], upd0))
updater.dispatcher.add_handler(CommandHandler(['msinfo'], msinfo))
updater.dispatcher.add_handler(CommandHandler('admin', admin))
#updater.dispatcher.add_handler(CommandHandler('st', st))
#updater.dispatcher.add_handler(MessageHandler(Filters.document.category("image"), photo_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
##############################
updater.dispatcher.add_handler(CallbackQueryHandler(button))

# Connect to.Telegram and wait for messages
updater.start_polling()

# Keep the program running until interrupted
updater.idle()
'''
### gold  ###
sorted(ra.items(), key=lambda x: x[1], reverse=True)
sorted(ra.items(), key=lambda x: x[1], reverse=True)
sorted(ra.items(), key=lambda x: x[1], reverse=True)
context.bot.editMessageText(chat_id=update.effective_chat.id,
                                            message_id=chose_admin.message_id, 
                                            text=noadmin_re)
context.bot.editMessageText(chat_id=update.effective_chat.id,
                                message_id=l.message_id, 
                                text="edited")
def edit(update: Update, context: CallbackContext) -> None:
    context.bot.editMessageText(chat_id=update.message.chat_id,
                                message_id=update.message.reply_to_message.message_id, 
                                text="edited")


'''














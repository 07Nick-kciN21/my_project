from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, LocationMessage, QuickReply, QuickReplyButton, MessageAction
import account
import tem
import re
line_bot_api = LineBotApi('')
handler = WebhookHandler('')

i_or_d = -1
respond = ''
sp = ''
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']    
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
    mtext = event.message.text
    body = request.get_data(as_text=True)
    # body2 = re.split('"', body)
    # i=0
    # # for b in body2:
    # #     print("{}. {}".format(i,b))
    # #     i += 1
    # userid = body2[15]
    global respond, sp, i_or_d
    if (respond == '輸入項目'):
        try:
            account.insert_object(mtext, sp)
            message = TextSendMessage(text='成功輸入')
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        i_or_d = -1
        respond = ''
        sp = ''
    if (respond == '移除項目'):
        try:
            account.delete_object(mtext, sp)
            message = TextSendMessage(text='成功移除')
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        i_or_d = -1
        respond = ''
        sp = ''
    if(mtext == '收入' or mtext == '支出'):
        try:
            if(i_or_d == 1):
                message = TextSendMessage(text='輸入項目+金額')
                respond = '輸入項目'
                sp=mtext
            if(i_or_d == 0):
                message = TextSendMessage(text='輸入移除項目的日期與名稱')
                respond = '移除項目'
                sp=mtext
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    if (mtext == '輸入'):
        try:
            message = TextSendMessage(
                text = '類別',
                quick_reply = QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label='收入', text='收入')
                    ),  
                    QuickReplyButton(
                        action=MessageAction(label='支出', text='支出')
                    ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
            i_or_d = 1
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    if (mtext == '刪除'):
        try:
            message = TextSendMessage(
                text = '類別',
                quick_reply = QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label='收入', text='收入')
                    ),  
                    QuickReplyButton(
                        action=MessageAction(label='支出', text='支出')
                    ),
                    ]
                )
            )
            i_or_d = 0
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    if (mtext == '查看'):
        try:
            message = TextSendMessage(text=account.show_object())
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    if (mtext == '溫度'):
        try:
            message = TextSendMessage(
                text = '請選擇區域',
                quick_reply = QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label='北部', text='北部')
                    ),  
                    QuickReplyButton(
                        action=MessageAction(label='中部', text='中部')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='南部', text='南部')
                    ),  
                    QuickReplyButton(
                        action=MessageAction(label='東部', text='東部')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='離島', text='離島')
                    ),  
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        respond = ''
        sp = ''

    if(mtext == '北部' or mtext == '中部' or mtext == '南部' or mtext == '東部' or mtext == '離島'):
        try:
            message = TextSendMessage(text=tem.get_tem(mtext))
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        respond = ''
        sp = ''


if __name__ == '__main__':
    app.run()
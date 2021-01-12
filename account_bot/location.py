import re

from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction

line_bot_api = LineBotApi('5Mlo5QuAeO2LNdZjAy4DGAjiz244Qgpa5Vxy69mPYsJjxxVxu+io8FFsp0GRqUKuqki20Hp2I9vmEnZ0x4ZObXo3+xF8Mi4ZyKcU/cedQ3YvGOHnliZVAtJKqg53iFcZmBcbtLBMjECbaZDHti7mjQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('36b3b4c9fc3fed8a0579717d2c24ea2e')

#line_bot_api = LineBotApi('Chanel token')
#handler = WebhookHandler('Channel secret') #記得要改 :)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    print("signature = ", signature)
    body = request.get_data(as_text=True)
    print("body = ", body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if isinstance(event.message, TextMessage):
        mtext = event.message.text
        print("show picture!")
        picurl = 'https://img.freepik.com/free-vector/cute-happy-penguin-cartoon-icon-illustration-animal-nature-icon-concept-isolated-flat-cartoon-style_138676-2095.jpg'
        
        #開始找 UserID
        try:
            print("===== 開始找 UserID =====")
            body = request.get_data(as_text=True)
            print("body (type:string) = ", body)
            print("")
            body2 = re.split('"', body) #split body by ( " ) character
            print("body2 (type:list) = ", body2) #this will print out a list
            print("")
            print("userID = ", body2[15]) #pay attention to body2, the 15th one contain data about userID
            print("=========================")
            lineMsg = "user ID = " + str(body2[15])
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=lineMsg))
        except:
            print("FAIL to get userID")
        
    
if __name__ == '__main__':
    app.run()
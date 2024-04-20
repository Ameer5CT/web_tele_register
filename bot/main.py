import json
import os
import sys
import datetime
import telebot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from requests.exceptions import ConnectionError, ReadTimeout


adminID = 555555555
TOKEN = "5555555555:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
bot = telebot.TeleBot(TOKEN)

cred = credentials.Certificate("AAAAA-firebase-adminsdk-AAAAA-AAAAAAAAAA.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://AAAAA.europe-west1.firebasedatabase.app/"
})


@bot.message_handler(commands=['start'])
def start_message(msg):
    if msg.chat.type != "private" or msg.chat.id != adminID:
        return
    bot.send_message(msg.chat.id, "Running...")


@bot.callback_query_handler(func=lambda message: True)
def callback(call):
    if call.message.chat.type != "private" or call.message.chat.id != adminID:
        return
    if call.data == "Reject":
        bot.edit_message_text("Signup rejected ❌\n\n" + call.message.text.split("\n", 2)[2],
                              call.message.chat.id, call.message.id)
    if call.data == "Confirm":
        members = db.reference("members/").get()
        id_num = 0
        if members:
            id_num = len(db.reference("members/").get())
        lines = call.message.text.splitlines()
        text = ""
        db.reference("members/" + str(id_num) + "/_id").set(str(id_num))
        for line in lines:
            if line.find(':') != -1:
                record_name = line.split(':')[0].strip().lower().replace(' ', '_')
                record_value = line.split(':')[1].strip()
                db.reference("members/" + str(id_num) + "/" + record_name).set(record_value)
                text += record_name + " = " + record_value + "\n"

        bot.edit_message_text("Saved to the database ✅\n\n" + text, call.message.chat.id, call.message.id)

        backup_file_name = ("DB-Backup_" +
                            str(str(datetime.datetime.now())[:-7].replace(' ', '_')).replace(':', '-') +
                            ".json")
        with open(backup_file_name, 'w') as f:
            json.dump(db.reference('/').get(), f)
        bot.send_document(adminID, document=open(backup_file_name, 'r'))
        os.remove(backup_file_name)


try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError, ReadTimeout) as e:
    bot.send_message(adminID, "❌ System will flush ❌")
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

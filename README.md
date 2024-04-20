# web_tele_register

A signup web page linked with a Telegram bot to approve or reject the signup.



## A preview video:

[![](https://img.youtube.com/vi/0m1k5XQCLeE/0.jpg)](https://www.youtube.com/watch?v=0m1k5XQCLeE)


### Setup:

**1.** Create a telegram bot and get the Token of the bot, You can use this official telegram bot to create your own bot: https://t.me/BotFather

**2.** Get the ID of the telegram account that you want to make it the admin, There are many ways but this bot is easy to use: https://t.me/myidbot

**3.** Create a Realtime Database from Firebase and get the JSON credentials file.
### Make your edits:

**1.** In the beginning of "bot/main.py"

- Change adminID value to your telegram ID that you got in the setup steps.

- Change TOKEN to your Telegram bot Token.

- Add the Database credentials JSON file next to the main.py file and in the main.py change the "cred" file name to your JSON file name.

- Change "databaseURL" value to your database link.

**2.** In the end of "web/home.js"

- add your bot Token instead of "55555:AAAAAAAA".

- Add your telegram admin account ID instead of "5555555" that was written after "chat_id=".


### How to use:

You can create your own register web page and use the JavaScript here to send the register information to telegram.

But keep in mind that if you use it on the client side you will risk your telegram Token being stolen because the user can see it in the source file of the web page but the benefit of this way is that you don't need a server that works all the time.

You will need to run the Python file only when you want to click on the confirm button, And you can run that file on almost any system including Android.




### 🔗 Links
You can contact me if you need help, My username is Ameer5CT everywhere.

https://t.me/Ameer5CT

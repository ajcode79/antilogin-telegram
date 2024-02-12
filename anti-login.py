#Do Not Manipulate
#It's Free Forever Please Do Not Sell
#Communication With Us Through Telegram Bot
#-------------------------------------------------------------------------------------------
# Telegram : @ajcodebot
# GitHub : ajcode79
#-------------------------------------------------------------------------------------------
from pyrogram import Client
from pyrogram.types import Message
import os, psutil, json, random, re
from glob import glob


class Helpers:
    @staticmethod
    def file_get_contents(file_path: str):
        with open(file_path, "r", encoding="utf8") as f:
            return f.read()

    @staticmethod
    def file_put_contents(file_path: str, content):
        with open(file_path, "w", encoding="utf8") as f:
            f.writelines(content)

    @staticmethod
    def random(length: int = 8) -> str:
        chars = "QWERTYUIOPLKJHGFDSAZCXVBNMqwertyuioplkjhgfdsazcxvbnm0123456789"
        chars_array = list(chars)
        key = ""
        for _ in range(length):
            key += random.choice(chars_array)
        return key

    @staticmethod
    def number(text: str):
        if text is not None:
            translation_table = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
            translation_table2 = str.maketrans("۰١٢٣٤٥٦٧٨٩", "0123456789")
            return text.translate(translation_table).translate(translation_table2)

    @staticmethod
    def delete_folder(dir_: str):
        file_names = glob(f"{dir_}/*")
        for file in file_names:
            if os.path.isdir(file):
                Helpers.delete_folder(file)
            else:
                os.remove(file)
        os.rmdir(dir_)

    @staticmethod
    def combine_data(values, keys=None):
        if values is not None:
            keys = keys or ("id", "coin", "inv", "step", "star", "warn", "time", "date", "self", "tabchi", "type", "ok", "phone",
            "listself", "listtabchi")
            return dict(zip(keys, values))

    @staticmethod
    def get_memory_usage():
        process = psutil.Process()
        used_memory_in_mb = process.memory_info().rss / 1024 ** 2
        return "{:.2f}".format(used_memory_in_mb)

    @staticmethod
    def getloadavg():
        avg = 0
        for i in psutil.getloadavg():
            avg += i
        return avg / len(psutil.getloadavg())


if not os.path.exists("session_string.txt"):
    with open("session_string.txt", "x"):
        pass

#Phone Number Account Telegram
phone_number = "REPLACE-YOUR-NUMBER"
app = Client(
    "bot",
    #Api ID Account Telegram
    api_id= REPLACE-API-ID,
    #Api Hash Account Telegram
    api_hash="REPLACE-API-HASH",
    phone_number=phone_number
)
if Helpers.file_get_contents("session_string.txt"):
    app.session_string = Helpers.file_get_contents("session_string.txt")

#ID Number Of Admin
admin = REPLACE-ID-NUMBER
#ID Number For Burn The Code To Be Sent
chattex = REPLACE-ID-NUMBER
with app:
    app.send_message(chat_id=admin, text="Bot is running bro /n dev : @ajcodebot")
    if session := app.export_session_string():
        Helpers.file_put_contents("session_string.txt", session)


@app.on_message()
def message_update(client, message: "Message"):
    from_id = message.from_user.id
    text = message.text
    chat_id = message.chat.id
    
    
    if chat_id == 777000:
        if match := re.search("(Login code:) ([0-9]{3,6})", text, flags=re.I).groups():
            number = match[1]
            app.send_message(chat_id=chattex, text=number)


app.run()

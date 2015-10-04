# -*- coding: utf-8 -*-
from line import LineClient
from os import environ
import re

try:
    LINE_USER_TOKEN    = environ.get("LINE_USER_TOKEN", "")
    LINE_COMPUTER_NAME = environ.get("LINE_COMPUTER_NAME", "LineBotWorker")
    client = LineClient(authToken=LINE_USER_TOKEN, com_name=LINE_USER_TOKEN)
except:
    print("Login Failed")
    exit()

while True:
    for group in list(set(client.groups) | set(client.contacts)):
        chat = client.getMessageBox(group.id)
        if not chat.unreadCount:
            continue
        messages = client.getRecentMessages(chat, chat.unreadCount)
        messages.reverse()
        for message in messages:
            if client.profile == message.sender:
                continue
            elif re.match(r'(เล้ง|เลิ้ง|เลี้ยง)', message.text):
                chat.sendMessage("ว่าไงครัซซ")


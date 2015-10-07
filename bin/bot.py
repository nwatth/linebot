# -*- coding: utf-8 -*-
import os; os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from line import LineClient
from os import environ
import re

try:
    LINE_USER_TOKEN    = environ.get("LINE_USER_TOKEN", "")
    LINE_COMPUTER_NAME = environ.get("LINE_COMPUTER_NAME", "LineBotWorker")
    client = LineClient(authToken=LINE_USER_TOKEN, com_name=LINE_COMPUTER_NAME)
except Exception as e:
    print "Login Failed\n", e.message
    exit()

while True:
    group = client.getGroupByName("LineBotWorker")
    chat = client.getMessageBox(group.id)
    messages = client.getRecentMessages(chat, chat.unreadCount)
    messages.reverse()
    for message in messages:
        if re.match(r'(เล้ง|เลิ้ง|เลี้ยง)', message.text):
            group.sendMessage("ว่าไงครัซซ")
            break


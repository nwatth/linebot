# -*- coding: utf-8 -*-
from line import LineClient
from os import environ
import re
import time

try:
    LINE_USERNAME      = environ.get("LINE_USERNAME", "")
    LINE_PASSWORD      = environ.get("LINE_PASSWORD", "")
    LINE_COMPUTER_NAME = environ.get("LINE_COMPUTER_NAME", "LineBotWorker")
    client = LineClient(id=LINE_USERNAME, password=LINE_PASSWORD, com_name=LINE_COMPUTER_NAME)
    print "Connected"
    if client.verifier:
        print client.verifier, client.pinCode
except Exception as e:
    print "Login Failed\n", e.message
    exit()

while True:
    group = client.getGroupByName("LineBotWorker")
    chat = client.getMessageBox(group.id)
    if not chat or not chat.unreadCount: continue
    messages = client.getRecentMessages(chat, chat.unreadCount)
    messages.reverse()
    for message in messages:
        if re.match(r'(เล้ง|เลิ้ง|เลี้ยง)', message.text):
            group.sendMessage("ว่าไงครัซซ")
            break
    time.sleep(5)


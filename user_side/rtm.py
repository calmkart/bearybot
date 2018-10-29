# -*- coding:utf-8 -*-
import time
import requests
from bearychat import RTMClient

from rtm_loop import RTMLoop
import handle as user_handle


def main():
    # init the rtm client
    client = RTMClient("4497da8bed21123490cfa9b06ddaf540",
                       "https://rtm.bearychat.com")

    resp = client.start()  # get rtm user and ws_host

    user = resp["user"]
    ws_host = resp["ws_host"]

    loop = RTMLoop(ws_host)  # init the loop
    loop.start()
    time.sleep(2)

    status = ""

    while True:
        error = loop.get_error()

        if error:
            print(error)
            continue

        message = loop.get_message(True, 5)

        if not message or not message.is_chat_message():
            continue
        try:
            print("rtm loop received {0} from {1}".format(message["text"],
                                                          message["uid"]))
        except Exception:
            continue

        if message.is_from(user):
            continue
        # 翻译模式
        if status == "":
            # 帮助提示
            if message["text"] == ":help:" or message["text"] == "?":
                loop.send(message.reply(user_handle.main_helper()))
                continue
            # 进入学习模式
            if message["text"] == ":learn:":
                loop.send(message.reply(user_handle.learn_helper()))
                status = "learn"
                continue

            # 普通翻译
            if message["text"]:
                r = requests.post("http://127.0.0.1:6789/translate/trans_api",
                                  json={"text": message["text"], "dest": "zh-cn"})
                if r.status_code == 200:
                    loop.send(message.reply(r.text))
                else:
                    loop.send(message.refer("出错了！请联系管理员！"))
        # 学习模式
        elif status == "learn":
            #帮助提示
            if message["text"] == "help":
                loop.send(message.reply(user_handle.learn_helper()))
                continue
            #获取词库名
            if message["text"] == "get_dict_list":
                loop.send(message.reply(user_handle.get_dict_list()))
                continue

            #获取指定词库所有用户学习情况
            if message["text"].startswith("info dict "):
                loop.send(message.reply(
                    user_handle.info("dict", message["text"])))
                continue
            #获取指定用户所有词库学习情况
            if message["text"].startswith("info user "):
                loop.send(message.reply(
                    user_handle.info("user", message["text"])))
                continue
            #退出学习模式,返回翻译模式
            if message["text"] == "exit":
                loop.send(message.reply(user_handle.main_helper()))
                status = ""
                continue
            #开始学习
            if message["text"].startswith("start "):
                continue


if __name__ == '__main__':
    main()

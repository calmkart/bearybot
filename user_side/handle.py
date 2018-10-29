# -*- coding:utf-8 -*-
import requests
import traceback
import logging



def main_helper():
    result = '''翻译模式:
1.输入 :helper: 获取帮助
2.输入 :learn: 进入学习模式
3.在讨论组中@本机器人并输入 :pk: 进入单词pk模式
4.直接输入任何语言，自动翻译成中文
'''
    return result


def learn_helper():
    result = '''学习模式:
1.输入 start <词库名> 开始学习(不需要输入<>号)
2.输入 get_dict_list 获取词库列表
3.输入 info dict <词库名> 获取指定词库所有用户学习情况(不需要输入<>号,不加词库名默认返回为全词库排行)
4.输入 info user <用户名> 获取指定用户所有词库学习情况(不需要输入<>号)
4.输入 exit 退出学习模式
5.输入 help 获取此帮助
'''
    return result


def get_dict_list():
    try:
        r = requests.get("http://127.0.0.1:6789/learn/get_dict_list")
        if r.status_code == 200:
            if len(r.json()["result"]) == 0:
                return "当前词库列表为空,请联系管理员添加词库。"
            result = "当前词库列表如下:\r\n"
            for n, i in enumerate(r.json()["result"]):
                result += str(n+1) + ".  词库名 {0},  词库详情: {1},  词库单词数: {2}\r\n".format(
                    i["dict_name"].encode("utf8"), i["dict_details"].encode("utf8"), i["numbers"])
            return result
        return "系统出错,请联系管理员"
    except Exception:
        return "系统出错,请联系管理员"
        logging.getLogger('app_log').error(traceback.format_exc())

def info(method, text):
    try:
        if method == "dict":
            dict_name = text.split('info dict ')[1]
            r = requests.get("http://127.0.0.1:6789/learn/get_score",
                         params={"dict_name": dict_name})
            if r.status_code == 200:
                if len(r.json()["result"]) == 0:
                    return "查询结果为空"
                result = dict_name.encode("utf8") +" 词库学习情况如下:\r\n"
                for n, i in enumerate(sorted(r.json()["result"], key=lambda x: len(x["learned_words"]), reverse=True)):
                    result += str(n+1) + \
                        ". 用户 {0},  已学单词数: {1} \r\n".format(
                            i["username"].encode("utf8"), len(i["learned_words"]))
                return result
        elif method == "user":
            username = text.split('info user ')[1]
            r = requests.get("http://127.0.0.1:6789/learn/get_score",
                             params={"username": username})
            if r.status_code == 200:
                if len(r.json()["result"]) == 0:
                    return "查询结果为空"
                result = username.encode("utf8") + " 用户学习情况如下:\r\n"
                for n, i in enumerate(sorted(r.json()["result"], key=lambda x: len(x["learned_words"]), reverse=True)):
                    result += str(n+1) + \
                        ". 词库 {0},  已学单词数: {1} \r\n".format(
                            i["dict_name"].encode("utf8"), len(i["learned_words"]))
                return result
    except Exception:
        return "系统出错,请联系管理员"
        logging.getLogger('app_log').error(traceback.format_exc())

if __name__ == '__main__':
    get_dict_list()

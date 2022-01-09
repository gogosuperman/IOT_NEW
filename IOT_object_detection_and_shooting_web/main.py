# -*-coding:utf-8-*-
# coding=utf-8 #Python 2預設的編碼格式是ASCII，Python 3預設的編碼格式是UTF-8. 因此，如果我們使用Python 2執行的Python程式中出現了中文，就需要指定編碼格式為UTF-8（如果使用的是Python 3則不需要指定）.
from flask import Flask, render_template, request  # 目前 python 2.7 環境
import redis
# from app import create_app
from flask_bootstrap import Bootstrap

app = Flask(__name__)  # name 表目前執行模組
# bootstrap = Bootstrap(app)

r = redis.Redis(host='localhost',port = 6379)
@app.route("/")  # 函式裝飾 decorator 以函式為基礎提供附加的功能
def index():
    return render_template("index.html")


# result checker html page
@app.route("/submit", methods=["POST", "GET"])
# 代表我們要處理的網站路徑
def submit():
    if request.method == "POST":
        speak = request.form["words"]
        r.set('voice',speak)
        return render_template("sucess.html", result=speak)
        res = ""
        # if len(speak) > 0:
        #     res = "success"
        #     return render_template("sucess.html", result=speak)
        # else:
        #     res = "fail"
        #     return render_template("index.html")


if __name__ == "__main__":  # 如果以主程式執行
    app.debug = True
    app.run()  # 立即啟動主程式 #網站程式需要 24 小時持續執行，程式中斷就會斷掉
    # heroku 1Qaz2wsx!!
# https://iot-app-zion27.herokuapp.com/

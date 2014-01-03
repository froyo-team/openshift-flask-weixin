from flask import Flask, render_template, send_from_directory
from config import *
from Model.models import db
from wx.weixin import robot

app = Flask(__name__)

app.config.from_object(Config)

robot.init_app(app, rule=WeiXinConfig.RULE)

db.init_app(app)

@app.route('/test')
def test():
    return 'test pape'

def main():
    app.run()

if __name__ == "__main__":
    main()
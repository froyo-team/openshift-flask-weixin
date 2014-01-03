# -*- coding: utf-8 -*-
from flask.ext.werobot import WeRoBot
from config import *

from werobot.reply import ArticlesReply, Article, TextReply

robot = WeRoBot(token=WeiXinConfig.TOKEN)

		

@robot.subscribe
def subscribe(message):
		#处理关注事件
		pass

@robot.text
def text_resp(message):
		#处理文字信息
		pass

@robot.image
def image_resp(message):
		#处理图片信息
		pass
		

@robot.location
def location_resp(message):
		#处理地理位置信息
		pass
@robot.voice
def voice_resp(message):
		#处理语音信息
		pass

@robot.link
def link_resp(message):
		#处理链接信息
		pass

def resp_text(message, content):
		#回复文本消息
		reply = TextReply(message=message, content=content)
		return reply

def resp_artical(message, artical_list):
		#回复图文信息,这里artical_list是包含多个字典的list
		reply = ArticlesReply(message=message)
		for item in artical_list:
				article = Article(
				    title= item['title'],
				    desription=item['desription'],
				    img=item['img'],
				    url=item['url']
				)
				reply.add_article(article)
		return reply

# encoding: utf-8
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request, tvno="0"):
	tv_list = [
		{"name": "陈小春与爱子吸睛同框-20170907", "tvcode": "XMzAxMDQ0MjI3Ng=="},
		{"name": "陈小春发飙训哭Jasper-20170914", "tvcode": "XMzAyMjI3Njk3Ng=="},
		{"name": "暖萌小小春实力宠嗯哼-20170921", "tvcode": "XMzAzNTk5NjE0NA=="},
		{"name": "温柔小春哥吓懵Jasper-20170928", "tvcode": "XMzA1MTgwNjg2MA=="},
		{"name": "Jasper变身4岁县太爷-20171005", "tvcode": "XMzA2NTMxNDgxMg=="},
		{"name": "春哥整蛊Jasper反被坑-20171012", "tvcode": "XMzA3OTU0MjI3Ng=="},
		{"name": "小小春爆笑撞脸欧阳锋-20171019", "tvcode": "XMzA5NDUxMjYxMg=="},
		{"name": "Jasper告白春哥哭红眼-20171026", "tvcode": "XMzExMDc4NTkzNg=="},
		{"name": "妈妈团探班萌娃超惊喜-20171102", "tvcode": "XMzEyNzYxODQ0OA=="},
	]
	template = get_template("index.html")
	now = datetime.now()
	tvno = tvno
	tv = tv_list[int(tvno)]
	hour = now.timetuple().tm_hour
	html = template.render(locals())
	return HttpResponse(html)


def engtv(request, tvno="0"):
	tv_list = [
		{"name": "战狼2", "tvcode": "XMzA4OTA4OTQyMA=="},
		{"name": "王牌保镖", "tvcode": "XMzExNDgyNzU0NA=="},
		{"name": "极盗车神", "tvcode": "XMzA5MDc5NDEyOA=="},
		{"name": "赛车总动员3", "tvcode": "XMzA4MTc3NzI2OA=="},
	]
	template = get_template("engtv.html")
	now = datetime.now()
	tvno = tvno
	tv = tv_list[int(tvno)]
	html = template.render(locals())
	return HttpResponse(html)


def carlist(request, maker="0"):
	car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan', 'Toyota']
	car_list = [[],
				['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
				['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
				['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
				['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
				['Camry', 'Altis', 'Yaris', '86', 'Prius', 'Vios', 'RAV4', 'Wish']
				]
	maker = int(maker)
	maker_name = car_maker[maker]
	cars = car_list[maker]
	template = get_template("carlist.html")
	html = template.render(locals())
	return HttpResponse(html)


def carprice(request, maker="0"):
	car_maker = ['Ford', 'Honda', 'Mazda']
	car_list = [
				[{'model': 'Fiesta', 'price': 203500},
				 {'model': 'Focus', 'price': 605000},
				 {'model': 'Mustang', 'price': 900000}],
				[{'model': 'Fit', 'price': 450000},
				 {'model': 'City', 'price': 150000},
				 {'model': 'NSX', 'price': 1200000}],
				[{'model': 'Mazda3', 'price': 329999},
				 {'model': 'Mazda5', 'price': 603000},
				 {'model': 'Mazda6', 'price': 850000}],
				]
	maker = int(maker)
	maker_name = car_maker[maker]
	cars = car_list[maker]
	template = get_template("carprice.html")
	html = template.render(locals())
	return HttpResponse(html)

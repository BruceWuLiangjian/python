from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader,Context
import datetime

class Person(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex
		
	def say(self):
		return  "my name is " + self.name
	
		

def index(request):
	t = loader.get_template("index.html")
	
	user = {"name":"tom","age":23,"sex":"male"}
	
	person = Person("jack",0,"female")
		
	book_list = ["python","ruby","java","c"]
	
	c = Context({"title":"django","user":user,"book_list":book_list,"today":datetime.datetime.now()})
	
	return HttpResponse(t.render(c))
	
def time(request):
	t = loader.get_template("time.html")
	c = Context({"today":datetime.datetime.now()})
	return HttpResponse(t.render(c))
	
	
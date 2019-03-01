from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
	return render(request,'about.html')
def homepage(request) :
	return render(request, 'home.html')
def admin(request):
	return HttpResponse('<h1>you are the admin </h1>')
def result(request) :
	full_text = request.GET['fulltext']
	words1 = full_text.split()
	words = len(words1)
	dic_words = {}

	for word in words1 :
		if word in dic_words :
			dic_words[word] +=1
		else :
			dic_words[word] = 1

	dic_words = dic_words.items()
	dic_words = sorted(dic_words,key=operator.itemgetter(1),reverse=True)

	return render(request , 'count.html',{'output':full_text,'words' : dic_words,'wordslen':words})

#!/usr/bin/python -tt
import urllib
from bs4 import BeautifulSoup
import requests
import nltk


def ReturnMoonPhase():
    string = ''
    counter= 0
    lines = []
    sor = requests.get('https://google.com/search?q=Todays moon phase').text
    soup = BeautifulSoup(sor,features="html.parser")
    art = soup.find('div' , class_="BNeawe s3v9rd AP7Wnd")
    summ = art.find('div' , class_="BNeawe s3v9rd AP7Wnd")

    t = nltk.word_tokenize(str(summ))
    for i in range(len(t)):
    	if counter == 3:
    		break
    	if t[i -1] == '>':
    		start = True
    		counter += 1
    	if start:
    		if t[i -1 ] == '<':
    			start = False
    		string += (t[i - 1] + ' ')
    newstring = ''
    for i in string:
    	if i != '>' and i != '<':
    		newstring += i
    return newstring

def googlesearch(search):
    string = ''
    counter= 0
    lines = []
    sor = requests.get('https://google.com/search?q=' + search).text
    soup = BeautifulSoup(sor,features="html.parser")
    art = soup.find('div' , class_="BNeawe s3v9rd AP7Wnd")
    summ = art.find('div' , class_="BNeawe s3v9rd AP7Wnd")
    start = False
    t = nltk.word_tokenize(str(summ))
    for i in range(len(t)):
    	if counter == 100:
    		break
    	if t[i -1] == '>':
    		start = True
    		counter += 1
    	if start:
    		if t[i -1 ] == '<':
    			start = False
    		string += (t[i - 1] + ' ')
    newstring = ''
    for i in string:
    	if i != '>' and i != '<':
    		newstring += i
    return newstring

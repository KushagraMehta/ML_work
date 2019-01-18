#/usr/bin/ python3

from tkinter import *
from bs4 import BeautifulSoup 
import requests
from googlesearch import search

root = Tk()

label1 = Label(root, text="Search")
E1 = Entry(root, bd =5)

def getE1():
    return E1.get()



def DataScraping():
	getE1()
	keyword = getE1()
	webdata=search(keyword,num=1,tld="co.in",stop=5)

	for url in webdata:
		source = requests.get(url).text
		html = BeautifulSoup(source,"lxml")
		file_store=open("data.txt","a")

		for article in html.find_all('p'):
			print(article.text)
		print("############################################\n")




submit = Button(root, text ="Submit", command = DataScraping)
label1.pack()
E1.pack()
submit.pack(side =BOTTOM)
root.mainloop()

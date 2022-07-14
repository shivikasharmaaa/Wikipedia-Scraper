'''

Author: Shivika Sharma
Date: Octoer 21, 2021
This script scrapes a wikipedia page and get the required elements using a menu-based system.

'''


# Importing required modules.
from bs4 import BeautifulSoup
import requests
import time

#Menu function.
def printmenu(soup):
	print("\nPlease choose one of the following options: ")
	print("\t 1. Print the entire HTML code")
	print("\t 2. Print H1 tags")
	print("\t 3. Print H2 tags")
	print("\t 4. Print H3 tags")
	print("\t 5. Paragraphs tags")
	print("\t 6. Print hyperlinks in the given HTML")
	print("\t 7. Scrape another Wikipedia page")
	print("\t 8. Exit")
	x = (input("Enter your option: "))
	if x=='1':
		partone(soup)
	elif x=='2':
		parttwo(soup)
	elif x=='3':
		part3(soup)
	elif x=='4':
		part4(soup)
	elif x=='5':
		part5(soup)
	elif x=='6':
		part6(soup)
	elif x=='7':
		scrapehtml()
	elif x=='8':
		print("Thank you!")
	else:
		print("Invalid Option")
		print("Please try again.")
		time.sleep(1)
		printmenu(soup)

#This function prints the body of the HTML code.
def partone(soup):
	print("****HTML Code****")
	print(soup.prettify())
	time.sleep(1)
	printmenu(soup)

#This function finds all the H1 tags and prints them.
def parttwo(soup):
	h1text = []
	for tag in soup.find_all('h1'):
		h1text.append(tag.text)

	print("The main heading is: ")
	for element in h1text:
		print(element)
	print()
	time.sleep(1)
	printmenu(soup)

#This function finds all the H2 tags and prints them.
def part3(soup):
	h2text = []
	for tag in soup.find_all('h2'):
		h2text.append(tag.text)

	print("The sub-articles are: ")
	for element in h2text:
		print(element)
	print()
	time.sleep(1)
	printmenu(soup)

#This function finds all the H3 tags and prints them.
def part4(soup):
	h3text = []
	for tag in soup.find_all('h3'):
		h3text.append(tag.text)

	for element in h3text:
		print(element)
	print()
	time.sleep(1)
	printmenu(soup)

#This function finds and prints text within all the paragraphs in the HTML code.
def part5(soup):
	paragraphs = []
	for para in soup.find_all('p'):
		paragraphs.append(para.text)
	print("The Paragraphs are: ")
	for element in paragraphs:
		print(element)
	print()
	time.sleep(1)
	printmenu(soup)

#This function inputs the required number of links and prints them.
def part6(soup):
	links = []
	numberoflinks = int(input("Enter the required number of links: "))
	for link in soup.find_all("a"):
		url = link.get("href")
		if url!=None:
			if 'https' and '/wiki' not in url:
				
				links.append("https://en.wikipedia.org/wiki/"+url)
			elif 'https' not in url:
				links.append("https://en.wikipedia.org"+url)
			else:
				links.append(url)
			numberoflinks -=1
		if(numberoflinks==0): break
	for element in links:
		print(element)
	print()
	time.sleep(1)
	printmenu(soup)

#This function is used to scrape the given HTML code.
def scrapehtml():
	htmlpage = input("Enter link to the Wikipedia page to be scraped: ")
	try:
		page = requests.get(htmlpage)
		#scraping using BeautifulSoup
		soup = BeautifulSoup(page.content, 'html.parser').body
		time.sleep(1)
		
	except:
		print("Invalid url.\nPlease try again.")
		time.sleep(1)
		scrapehtml()
		return
	printmenu(soup)
	
#Starting call.
scrapehtml()


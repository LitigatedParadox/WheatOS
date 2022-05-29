from base64 import encode
import random
from tkinter import N
from tokenize import String
from typing import Text
from bs4 import BeautifulSoup
import math
import requests
import googlesearch
from googlesearch import search
import google
import wikipedia
import webbrowser
import tkinter as tk
import Gwaphing_Calculator_Thank_You_Ninja as Graph

while True:
    #Welcome message
    Command1 = input("Welcome to the Python WheatOS Multi Purpose Tool. Type '/help' for a list of commands and information about WheatOS.\n")
    #Search Engine
    if Command1 == '/search':
            Search = input('Please enter your question:')
            query = Search
            for x in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(x)
    if Command1 == '/wiki':
        print("Wikipedia searching with WheatOS takes the topic you want to learn about and finds the closest matching Wikipedia article. Please be very careful with your grammar and make sure to use underscores to seperate new words.")
        WikiSearch = input('Please enter your question:')
        WikiResult = 'https://en.wikipedia.org/wiki/' + WikiSearch
        UserChoice = input("You are about to open:")
        print(WikiResult)
        UserChocie = input("Do you want to open this link? Y/N: ")
        if UserChocie == 'Y':
            URL = WikiResult
            webbrowser.open_new_tab(URL)

    #Calculator
    if Command1 == '/calculate':
        CalculatorType = input('Please select the Calculator type you would like. 1. Simple Calculator, 2. Constants list')
        if CalculatorType == '1':
            def add(x, y):
                return x + y
            def subtract(x, y):
                return x - y
            def multiply(x, y):
                return x * y
            def divide(x, y):
                return x / y
            def sqrt(x,y):
                math.sqrt(x, y)
            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")
            while True:
                OperationChoice = input("Enter choice(1/2/3/4): ")
                if OperationChoice in ('1', '2,', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second numbner: "))
                    if OperationChoice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))
                    elif OperationChoice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))
                    elif OperationChoice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))
                    elif OperationChoice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))
                    next_calculation = input("Would you like to do another calculation? (Y/N): ")
                    if next_calculation == "N":
                        break
                else:
                    print("Invalid Input")
        if CalculatorType == '2':
            print("e =", math.e)
            print("Pi =", math.pi)
            print("Tau =", math.tau)
#Web Scraper
    if Command1 == '/scrape':
        url = input('Please enter the URL of the website you would like to scrape here: ')
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        TextvsTag = input('Would you like to search for text within the page or for a specific tag within the source code? Tag/Text: ')
        if TextvsTag == "Tag":
            UserTag = input('Please enter the tag you would like to scrape for here: ')
            UserTag = str(UserTag)
            UserTagFind = doc.find(UserTag)
            StringYN = input("Would you like to print the string of the tag you are scraping for? Y/N: ")
            if StringYN == 'N':
                print(UserTagFind.prettify())
            if StringYN == 'Y':
                print(UserTagFind.string)
        if TextvsTag == "Text":
            UserText = input('Please enter the text you would like to search for:')


    #Help Message
    if Command1 == '/help':
        print("WheatOS is a machine learning algorithm that aims to make a multipurpose, ever learning, open source tool that anybody can use free of charge. WheatOS currently has three main functions:")
        print("A search engine")
        print("A web scraper")
        print("A calculator")    
        
    Command2 = input("To use the search engine '/search' to begin, to use our calculator type '/calculate' before your equation, to use our webscraper type /scrape to begin the scraping process.")

    #Search Engine
    if Command2 == '/search':
            Search = input('Please enter your question:')
            query = Search
            for x in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(x)
    if Command2 == '/wiki':
        print("Wikipedia searching with WheatOS takes the topic you want to learn about and finds the closest matching Wikipedia article. Please be very careful with your grammar and make sure to use underscores to seperate new words.")
        WikiSearch = input('Please enter your question:')
        WikiResult = 'https://en.wikipedia.org/wiki/' + WikiSearch
        UserChoice = input("You are about to open:")
        print(WikiResult)
        UserChocie = input("Do you want to open this link? Y/N: ")
        if UserChocie == 'Y':
            URL = WikiResult
            webbrowser.open_new_tab(URL)

#Calculator
#Basic Operations
    if Command2 == '/calculate':
        CalculatorType = input('Please select the Calculator type you would like. 1. Simple Calculator, 2. Constants list 3. Graphing Calculator: ')
        if CalculatorType == '1':
            def add(x, y):
                return x + y
            def subtract(x, y):
                return x - y
            def multiply(x, y):
                return x * y
            def divide(x, y):
                return x / y
            def sqrt(x,y):
                math.sqrt(x, y)
            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")
            while True:
                OperationChoice = input("Enter choice(1/2/3/4): ")
                if OperationChoice in ('1', '2,', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second numbner: "))
                    if OperationChoice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))
                    elif OperationChoice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))
                    elif OperationChoice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))
                    elif OperationChoice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))
                    next_calculation = input("Would you like to do another calculation? (Y/N): ")
                    if next_calculation == "N":
                        break
                else:
                    print("Invalid Input")
#Constants List        
        if CalculatorType == '2':
            print("e =", math.e)
            print("Pi =", math.pi)
            print("Tau =", math.tau)
            Next = input("Would you like to use another WheatOS function? Y/N")
            if Next == 'N':
                break
#Graphing Calculator
        if CalculatorType == '3':
            Graph1 = str(input('Input your equation here: '))
            Scale = int(input('Scale of 1: '))
            Quality = int(input('Points per scale unit: '))
            print('Loading...')
            Graph.Graph(Scale, Quality, Graph1)
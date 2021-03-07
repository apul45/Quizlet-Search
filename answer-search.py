from bs4 import BeautifulSoup
from googlesearch import search
from os import system
import requests
import random

def main():

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
        }

    print(" Answer Search ".center(50,'-'), end="\n\n")
    
    originalquestion = input("Enter the question: ")
    answerNum = int(input("The # of answers [More = better accuracy]: "))
    question = 'site:quizlet.com "%s"' % (originalquestion.strip(' \" '))

    quizlets = []
    answers = []

    for url in search(question, tld="com", lang="en", num=answerNum, start=0, stop=answerNum, pause=1):
        quizlets.append(url)

    # Juicy Stuff

    for i in range(len(quizlets)):
        r = requests.get(quizlets[i], headers=headers[random.randint(0,len(headers))])
        soup = BeautifulSoup(r.content, features="html.parser")
        cards = soup.find_all("span", {'class' : 'TermText'}, )
        for i in range(len(cards)):
            text = cards[i].get_text()
            if originalquestion in text:
                answers.append(cards[i+1].get_text())
                break
    
    
    print("\n")
    for ans in answers:
        print("Answer:        ", ans)
    print("\n\n")

main()
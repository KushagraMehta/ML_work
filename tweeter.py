import tweepy
from tkinter import *
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt


API_key = "bSh5wvnGDnoE0HShQjbLcDCj5"
API_secret_key = "mwyr7FEk1z54uqhqxRSnHCoEM9QgdNVfEPNofH6gU3VwIbgfcs"
Access_token = "2953318536-Pm32gN5okawo4lcZlzpIIxfzvRpAuPWIZcbP9lT"
Access_token_secret = "BYzfYILbGoVrCfPt2exw4JBLnDBP8eKWDETOftiO285Ff" 

auth = tweepy.OAuthHandler(API_key,API_secret_key)
auth.set_access_token(Access_token,Access_token_secret)

api = tweepy.API(auth)

# GUI PART
root = Tk()

label1 = Label(root, text="Search")
E1 = Entry(root, bd =5)

label2 = Label(root, text="Sample Size")
E2 = Entry(root, bd =5)

def getE1():
    return E1.get()
def getE2():
    return E2.get()



def DataProjector():

    getE1()
    keyword = getE1()

    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)

    Tweet_Data=""
    for tweet in tweepy.Cursor(api.search, q=keyword,result_type="recent", lang="en").items(numberOfTweets):
        Tweet_Data = Tweet_Data + tweet.text
    
    F = open("Tweet_Data_file.txt","a")
    F.write(Tweet_Data)
    F.close()
    sent_token = sent_tokenize(Tweet_Data)
    word_token = word_tokenize(Tweet_Data)

    """print(sent_token)
                print('___________________@@@@@@@@@@@@@@@@@@@@@@@@@@@@_________________')
                print(word_token)
            """
    text = nltk.Text(word_token)
    
    frequency_distribution = nltk.FreqDist(text)
    Plot = frequency_distribution.most_common(10)
    
    names = []
    values = []
    
    for i in Plot:
        names.append(i[0])
        values.append(i[1])
    print(names)
    print(values)
    fig, axs = plt.subplots()
    axs.plot(names, values)
    fig.suptitle('Top 10')
    plt.show()
    print (frequency_distribution.plot())

submit = Button(root, text ="Submit", command = DataProjector)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
submit.pack(side =BOTTOM)

root.mainloop()
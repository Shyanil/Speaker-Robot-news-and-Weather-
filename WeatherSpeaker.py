import json
import requests
import pyttsx3

print("Welcome to weather speaker Robot")
try:
 while(True):
  name = input("Enter the Location You Want data: ")
  news = input("Which news you want to Listen: ")
  if(name == "q"):
      break
  url = f"https://api.weatherapi.com/v1/current.json?key=77a3ccb019014c718e944706240907&q={name}"
  urlNews = f"https://newsapi.org/v2/everything?q={news}&from=2024-06-09&sortBy=publishedAt&apiKey=52927c3833b541d3850aa9ffa1bf9397"
  s=requests.get(urlNews)
#   print(s.text) 
  d = requests.get(url)
#   print(d.text) 
  dic = json.loads(d.text)
 
  dic1 = dic["current"]["temp_c"]
  dic2 = dic["current"]["humidity"]
  dic3 = dic["current"]["wind_mph"]
  dic4 = dic["location"]["localtime"]
  fullData = f"The Wether of the {name} is {dic1} , {name}  humidity is  {dic2} and wind miles per hour is  {dic3}. Today Date and Time is {dic4}"
  nic = json.loads(s.text)
  
  article = nic["articles"]
  anticly = article[0]
  nic1 = anticly["source"]["name"]
  nic2 = anticly ["title"]
  nic3 = anticly["description"]
  fullDataNews = f"The {news} is News Source Name is {nic1} . The Hot News is Today {nic2} and and listen More about it {nic3}"
  command =pyttsx3.init()
  command.setProperty("rate", 150)
  command.say(fullData)
  command.say(fullDataNews)
  command.runAndWait()
except Exception as e:
    print("The robot has stopped because something went wrong." , e)
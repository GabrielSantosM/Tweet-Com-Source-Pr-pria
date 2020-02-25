# -*- coding: utf-8 -*-
import random, os, sys
import tweepy

consumer_secret = "catTtKEz5pFrsPH8FeYDV6bmxf11hUlgrGOhk2W7ygT0sSTwPN"
consumer_key = "XXLdwcdEdcQWYtLs7g2QGT60W"           #Credencias do twitter dev
access_token = "1124355942693445633-6PxXq9IupO7Fmgc0oxW0gUiO1gfp15"
access_token_secret = "BIc9VCwzVV4T2YiZC7KE3Zh6TJZAm2r2gn3UbwYCski3v"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)          #Logando 


texto = "siga meu adm"  #Inserir o texto desejado aqui


   
api.update_status(status=texto) #Então postamos no twitter o texto gerado

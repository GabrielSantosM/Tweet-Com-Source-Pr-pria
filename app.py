

consumer_secret = ""
consumer_key = ""           #Credencias do twitter dev
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)          #Logando 


texto = ""  #Inserir o texto desejado aqui entre ""


   
api.update_status(status=texto) #Então postamos no twitter o texto gerado

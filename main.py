import requests
import schedule
import time
import random
from datetime import datetime


def job():
    list=[
        "Wonderful project, Be aware of scammer", 
        "this project is very good and this projector has a lot of attractions",
        " so hopefully the project will be good",
        ".experienced team , sir help me",
        ". Without doubt woooo asu", 
        "this is one of the best project.",
        "This project looks very interesting.",
        " I am interested, dont spam guys you lol", 
        "and I will support this project until it is successful",
        "according to the plan that has been setI have participated in following the guidelines",
        "and rules of this airdrop", 
        "I hope that many people will be lucky to get a prize from this airdrop.",
        "with the opportunity to take part in this airdrop",
        " I am very enthusiastic because this is an excellent project", 
        "let's take it to the This project looks very interesting.",
        " I am interested , i love all",
        " and I will support this project until it is successful according to the plan that has been setI have participated in following the guidelines and rules of this airdrop",
        " I hope that many people will be lucky to get a prize from this airdrop.with the opportunity to take part in this airdrop", 
        "I am very enthusiastic because this is an excellent project", 
        "let's take it to the moonA very smart project brings us excitement to always follow.",
        "I believe This project will work and succeed.",
        "because this project is with a great team that always provide creative"
        "We can do it , go to the moon", "Please do not spam guys", " let us support this project as their Buff for make a strongest Pengu in crypto ! ",
        "Lets gooo guys", "hallo guys , be active sir akakakwkwkwk", "be active guys keep pushing pussying , hahaha", "how to be man sir :(", "tolol beut dah asu","p kontl guys :v",
        "Lets be active and dont spam", "nice guys, good afternoon", "be active and stay humble", "hello bro, nice good moring","helloo broooo, i love you all",
        "Someone could tell me about this project? tell me in private pliss",
        "Lets discuss more about this project sir , how",
        "I think this project will be mooooreeeee and expensive",
        "Lets go to the moooooonnnn , i can see u guys",
        "Be Active Guys :) and dont spam",
        "Good project i thinks , good job bro",
        "when market rilis sir hehe" ,
        "This poject To the Moon , lets active dont spam",
        "I am the Greatest one , but lie :(",
        "Hai have nice a day bro","Hello  dont spam guys","is mint afddress already sir?","Heho, i know you bro wkwk","Haiiiiiii kontolodon asu","Haii gift me some gift bro","Haiii bro , wanna see my cute poto :*","wkwkwkwk bodong cok gateli","wkw asu","AOK AOK AOK AOK", " AOK AOK, kontol babi asu hello guys"
    ]

    general = {
    'content' : random.choice(list)
    
    }
    general1 = {
    'content' : random.choice(list)
    
    }
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time,general)
    
    header ={
        #auth = punyamu dewe
        'authorization': 'NDczMzQ0NDg5NjIxMDI4ODg1.YYo_IQ.-lKTfPeX0i4V7f32SA_tILhHfXg'}

    
    general = requests.post("https://discord.com/api/v9/channels/909740442806026302/messages" , data=general,headers=header)
    no_topik = requests.post("https://discord.com/api/v9/channels/909203262496964625/messages" , data=general1,headers=header)
    

# def check_rank():
#     rank = {
#         'content' : "!rank"
#     }


#     header ={
#         #auth = punyamu dewe
#         'authorization': 'NDczMzQ0NDg5NjIxMDI4ODg1.YYo_IQ.-lKTfPeX0i4V7f32SA_tILhHfXg'}

#     rank_check = requests.post("https://discordapp.com/api/v9/channels/904759692214038530/messages" , data=rank ,headers=header)


def on_setting():
    general={
        'status': "online"
    }
    
    header ={
        #auth = punyamu dewe
        
        'authorization': 'NDczMzQ0NDg5NjIxMDI4ODg1.YYo_IQ.-lKTfPeX0i4V7f32SA_tILhHfXg'
        }

    
    akun_setting= requests.post("https://discord.com/api/v9/users/@me/settings" , data= general,headers=header)
    


schedule.every(0.56).minutes.do(job)

# schedule.every(5.5).minutes.do(check_rank)
on_setting()
print( on_setting())

# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
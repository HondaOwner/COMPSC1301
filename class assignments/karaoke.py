text = ''' Drivin' solo, I'm just swervin' through my ends
When I'm sober I just don't like who I am
Pour me up a four and I'll feel like myself again
Roll me up some dope and I'll feel like myself again
I'ma break every box they try to put me in
I got a lot of enemies who used to be my friends
Pour me up a four and I'll feel like myself again
Roll me up some dope and I'll feel like myself again
I was sober for an hour but I'm rollin' off a bean now
The drugs, they give me confidence, I'm sayin' what I mean now
The Xannies help me slow up, the lean it help me speed down
Ballin', yeah I'm ballin', I won't hit it if she beat now
Callin', yeah she callin', your bitch got me on the speed dial
Driving through the Rex, I look at faces don't see no smiles
It's grimy in the 6ix, who can I trust? I'll never know now
Sprite is extra dark now, my doggie in the dog pound
They say I'm on the come up, but I've been on the come down
See me doin' good, they start to hate, that's how it goes now
I don't know why they mad at me, I always stay ten toes down
Drivin' through my city by myself, that's how I roll now
Drivin' solo, I'm just swervin' through my ends
When I'm sober I just don't like who I am
Pour me up a four and I'll feel like myself again
Roll me up some dope and I'll feel like myself again
I'ma break every box they try to put me in
I got a lot of enemies who used to be my friends
Pour me up a four and I'll feel like myself again
Roll me up some dope and I'll feel like myself again
I remember bein' a kid my teachers told me I wouldn't be shit
Diamonds in my pinky, look like water, make me seasick
Never had no help so don't approach me on some free shit
Did this by myself so why the fuck would I do a remix?
His bitch gave me top, don't want the pussy, he can keep it
Money and the power, fuck respect 'cause I don't need it
Drivin' to the west, I popped a bean and now I'm speedin'
Know some people in the 6ix that dissed me for no reason
Sending shots, they sendin' shots, on road I never see them
Takin' Ls, they takin' Ls, I never wanna be them
Got your bitch beside me, she just asked me what a bean is
Put her number in my phone, and you know I delete it
Drivin' solo, I'm just swervin' through my ends
When I'm sober I just don't like who I am
Pour me up a four and I'll feel like myself again
Roll me up some dope and I'll feel like myself again
I'ma break every box they try to put me in
I got a lot of enemies who used to be my friends
Pour me up a four and I'll feel like myself again
Roll me up some dope and I'll feel like myself again
Drivin' solo, I'm just swervin' through my ends
Pour me up a four and I'll feel like myself again
I'ma break every box they try to put me in
Pour me up a four and I'll feel like myself again
Roll me up some dope and I'll feel like myself again
Drivin' solo, I'm just swervin' through my ends
'''

words = text.split("\n") # \n makes it print by line entered into the text
maxlen = 0
for word in words:
    if len(word) > maxlen:
        maxlen = len(word)
maxlen += 2 # biggest word is 16 characters

import time
for word in words:
    print(f'{word:^{maxlen}}') # ^ shifts 6, or centers
    time.sleep(2)

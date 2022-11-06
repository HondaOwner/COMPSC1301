# lettercount incremental programming

song = '''You think I'm pretty without any makeup on
You think I'm funny when I tell the punch line wrong
I know you get me, so I let my walls come down, down
Before you met me
I was alright, but things were kinda heavy
You brought me to life, now every February
You'll be my Valentine, Valentine
Let's go all the way tonight
No regrets, just love
We can dance, until we die
You and I, will be young forever
You make me
Feel like I'm livin' a teenage dream
The way you turn me on, I can't sleep
Let's run away and don't ever look back, don't ever look back
My heart stops
When you look at me, just one touch
Now, baby, I believe this is real
So take a chance and don't ever look back, don't ever look back
We drove to Cali and got drunk on the beach
Got a motel and built a fort out of sheets
I finally found you, my missing puzzle piece
I'm complete
Let's go all the way tonight
No regrets, just love
We can dance until we die
You and I, will be young forever
You make me
Feel like I'm livin' a teenage dream
The way you turn me on, I can't sleep
Let's run away and don't ever look back, don't ever look back
My heart stops
When you look at me, just one touch
Now baby I believe this is real
So take a chance and don't ever look back, don't ever look back
I'ma get your heart racing in my skin-tight jeans
Be your teenage dream tonight
Let you put your hands on me in my skin-tight jeans
Be your teenage dream tonight
(Tonight, tonight, tonight, tonight, tonight, tonight)
You make me
Feel like I'm livin' a teenage dream
The way you turn me on, I can't sleep
Let's run away and don't ever look back, don't ever look back (no)
My heart stops
When you look at me, just one touch
Now, baby, I believe this is real (oh)
So take a chance and don't ever look back, don't ever look back
I'ma get your heart racing in my skin-tight jeans
Be your teenage dream tonight
Let you put your hands on me in my skin-tight jeans
Be your teenage dream tonight
(Tonight, tonight, tonight, tonight, tonight, tonight)
'''

song = song.lower() # makes lowercase
# print(song)

letters = [i for i in song if i.islower() ]
letters.sort()
# print(letters)
al = [chr(i) for i in list(range(ord('a'), ord('z') + 1))] # character for every i in range of a to z, and then + 1 to include the z
# print(al)
frq = [song.count(i) for i in al]
# print(frq)
most_frq = max(frq)
# print(most_frq)
# print(frq.index(most_frq))

for x in range(len(frq)):
    print("There are:", frq[x], "instances of the letter", al[x])

popular = frq.index(most_frq)
print("The most popular letter was", al[popular])
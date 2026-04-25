import random
x=(random. randrange(0,1000))
y= int(input( "guess a number between 0 and 1000:"))
g_count=0
while x!=y:
    g_count=g_count + 1
    print('guess count:', g_count)
    if x>y>x-100:
        print("guess a little higher")
    elif x+100>y>x:
        print("guess a little lower")
    elif x-100>=y:
        print('guess higher')
    elif y>=x+100:
        print("guess lower")
    y= int(input( "guess a number between 0 and 1000:"))

if x==y:
    print('You Win')

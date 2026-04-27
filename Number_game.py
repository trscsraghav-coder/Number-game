import random
x=(random. randrange(0,1000))
y= int(input( "guess a number between 0 and 1000:"))
g_count=0
def update_score(g_count):
    with open('num_game_hs.txt', 'r') as f:
        content = f.read() 
        if g_count < int(content):
            with open('num_game_hs.txt', 'w') as f:
                f.write(str(g_count))
                print('new highscore!', g_count)
        else:
            print('Current highscore is: ', content)
           

while x!=y:
    g_count+=1
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
    print('Your score is: ', g_count)
    update_score(g_count)

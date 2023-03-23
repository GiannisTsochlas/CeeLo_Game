#Ioannis Tsoxlas, A.M. 4993

#inputs section

players=input('Number of players (between 2 and 6): ')

if not players.isdigit():
    print("Something wrong happened: invalid literal for int() with base 10:",players)
    players=3
    print("I'm setting the number of players to 3")
elif not 2<=int(players)<=6 :
    print("I expected between 2 and 6 players\nI'm setting the number of players to 3")
    players=3
else:
    players = int(players)#to input pernei kati->str alla epidh 8elo thn anisotita prepei na to kanw int 

coins=input('Number of coins per player (between 5 and 100):')

if not coins.isdigit():
    print('Something wrong happened: invalid literal for int() with base 10:',coins)
    coins=10
    print("I'm setting the number of coins to 10")
elif not 5<=int(coins)<=100 :
    print('Something wrong happened: invalid literal for int() with base 10:',coins)
    coins=10
    print("I'm setting the number of coins to 10")
else:
    coins=int(coins)

#1 Game Section

import random

playerslist=[]
playersscore=[0]
betlist=[0]#<-

for i in range(1,players+1):
    playerslist.append(i)
    playershowhasbet=playerslist[-1]
for s in range(1,players+1):
    playersscore.append(coins)

# Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
##print('\nplayerslist is ',playerslist)##bgale
#print('\nplayersscore is ',playersscore)##bgale

print('\nGame begins with', players, 'players.')
print('Each player has', coins, 'coins.')
banker=random.randint(1,players)
print('Player', banker, 'is randomly chosen as banker')

#loopsection

MAINFLAG=True

while   MAINFLAG :

    print('\nCurrent balance:')

    
    for player in range(1,players+1):
        print('Player', player, 'has', playersscore[player], 'coins')
    bank=input('\nPlayer'+str(banker)+': You are the banker! Please enter a valid bank amount: ')#tip to input mporei na parei mono str mesa kai ana balo , to pairnei san parametro


    flag1=True
    while flag1:
        if not bank.isdigit():
            bank=input('Player'+str(banker)+': You are the banker! Please enter a valid bank amount: ')
        elif not 1<=int(bank)<=playersscore[banker]:
            bank=input('Player'+str(banker)+': You are the banker! Please enter a valid bank amount: ')
        else :
            bank=int(bank)
            flag1=False

            
    for i in playerslist:
        if i==banker:
            betlist.append(0)
            continue##gia na mhn paei kateythian katw (sto epoimeno if)
        if bank-sum(betlist)==0 and i!=1:##betlist[i-1]
            print('player',i,'and others you can not bet an additional amount')
            playershowhasbet = i
            for i in range(i,players+1):
                betlist.append(0)
            break


        else:
            bet=input('Player: '+str(i)+' Please enter a valid bet: ')
            flag2=True
            
            while flag2:
                #print(betlist)
                if not bet.isdigit():
                    bet=input('Player: '+str(i)+' Please enter a valid bet: ')
                elif int(bet)>playersscore[i]:
                    bet=input('Player: '+str(i)+' Please enter a valid bet: ')
                elif not 1<=int(bet)<=(bank-sum(betlist)):
                    bet=input('Player: '+str(i)+' Please enter a valid bet: ')
                else :
                    bet=int(bet)
                    flag2=False
                    betlist.append(bet)#<-

    # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
    #print('\nbetlist is ',betlist)
    
#2 Game Section 'I deyteri fasi tou gyrou ksekinaei otan exoun pontarei.'
    print('\nRound starts:')
    for i in playerslist:
        if i==banker:
            print('Player ',i,': Banker with bank amount=',sum(betlist),':')
        else:
            try:
                print('Player ',i,': has bet',betlist[i],':')
            except:
                break
#zaria toy banker
    input('\nBanker: press ENTER to roll dice')##tip mporw na bazw ayto gia na trexw oses fores thelw to programa kai na mhn xanome !!!!
    roll=[]
    
    while True:
        for x in range(3):
            zari=random.randint(1,6)
            roll.append(zari)
        print(roll)
        
        #Automatic win if's

        flag3=False#to xrisimopoiow gia thn periptosh poy prepei na riksoyn zaria kai oi players
        if 4 in roll and 5 in roll and 6 in roll:
            print('Automatic Win! Banker wins all bets! Round ends!')
            for i in playerslist:
                if i==banker:
                    playersscore[banker]=playersscore[banker]+sum(betlist)
                else:
                    try:#try giati stin periptwsi pou den mporoyn na paiksoun oloi oi paixtes tha vgalei index error
                        playersscore[i]=playersscore[i]-betlist[i]
                    except:
                        break
            print(playersscore)
            betlist=[0]
            break
        elif (roll[0]==roll[1] and roll[2]==6) or (roll[0]==roll[2] and roll[1]==6) or (roll[1]==roll[2] and roll[0]==6):
            print('Automatic Win! Banker wins all bets! Round ends!')
            for i in playerslist:
                if i==banker:
                    playersscore[banker]=playersscore[banker]+sum(betlist)
                else:   
                    try:
                        playersscore[i]=playersscore[i]-betlist[i]
                    except:
                        break
            print(playersscore)
            betlist=[0]
            break
        elif roll[0]==roll[1]==roll[2]:
            print('Automatic Win! Banker wins all bets! Round ends!')
            for i in playerslist:
                if i==banker:
                    playersscore[banker]=playersscore[banker]+sum(betlist)
                else:   
                    try:
                        playersscore[i]=playersscore[i]-betlist[i]
                    except:
                        break
            print(playersscore)
            betlist=[0]
            break
            
        #Automatic Loss if's

        elif 1 in roll and 2 in roll and 3 in roll:
            print('Automatic Loss! Banker loses all bets! Round ends!')

            for i in playerslist:
                 if i==banker:
                     playersscore[i]=playersscore[i]-sum(betlist)
                 else:
                     try:
                        playersscore[i]=playersscore[i]+betlist[i]
                     except:
                        break

            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
            #print('playersscore is',playersscore)

            if banker + 1 > players:
                banker = banker - (players - 1)
            else:
                banker = banker + 1
            betlist=[0]
            print('New Banker is ', banker)
            break
        elif (roll[0]==roll[1] and roll[2]==1) or (roll[0]==roll[2] and roll[1]==1) or (roll[1]==roll[2] and roll[0]==1):
            print('Automatic Loss! Banker loses all bets! Round ends!')
            for i in playerslist:
                if i==banker:
                    playersscore[i]=playersscore[i]-sum(betlist)
                else:
                    try:
                        playersscore[i]=playersscore[i]+betlist[i]
                    except:
                        break
            print(playersscore)

            if banker + 1 > players:
                banker = banker - (players - 1)
            else:
                banker = banker + 1
            print('New Banker is ',banker)
            betlist=[0]
            break

        #Score Definition if

        elif (roll[0]==roll[1]):
            score=roll[2]
            print('Banker scored ',score,' points')
            flag3=True
            break
        elif(roll[1]==roll[2]):
            score=roll[0]
            print('Banker scored ',score,' points')
            flag3=True
            break
        elif (roll[0]==roll[2]):
            score=roll[1]
            print('Banker scored ',score,' points')
            flag3=True
            break

        #Roll Again if

        else:
            print('Banker rolls again')
            roll=[]


#Players rollings

    while flag3:
        flag_NewBankerIs = False
        for i in range(1, players + 1):

            if i == playershowhasbet :

                flag3 = False
                #break

            if i==banker:#locate the banker in order to not have the ability to play again
                 #print('\n')
                 continue
            if betlist[i]==0 and i<banker:
                print('\n player',i,'you can not bet ')
                continue
            if betlist[i]==0 and i>banker:
                print('\n player',i,'and others you can not bet')
                break

            else:

                input('\nPlayer'+str(i)+': press ENTER to roll dice')
                roll=[]

                while True:
                    for x in range(3):
                        zari=random.randint(1,6)
                        roll.append(zari)
                    print(roll)

                    #PLayers Automatic win if's

                    if 4 in roll and 5 in roll and 6 in roll:
                        print('Player Wins!')

                        for z in playerslist:
                            if z==i:
                                playersscore[z]=playersscore[z]+sum(betlist)
                            elif z==banker:
                                playersscore[z]=playersscore[z]-betlist[i]
                            else:
                                try:
                                    playersscore[z]=playersscore[z]-betlist[z]
                                except:
                                    break
                        flag_NewBankerIs=True
                        print('\nNew banker is player')

                        break

                    elif roll[0]==roll[1]==roll[2]:
                        print('Player Wins')

                        for z in playerslist:
                            if z==i:
                                playersscore[z]=playersscore[z]+sum(betlist)
                            elif z==banker:
                                playersscore[z]=playersscore[z]-betlist[i]
                            else:
                                try:
                                    playersscore[z]=playersscore[z]-betlist[z]
                                except:
                                    break
                        flag_NewBankerIs=True
                        print('\nNew banker is player')

                        break

                    #Players Score Definition if##xriazete na prosarmosw ta scores
                    elif (roll[0]==roll[1]):
                        iscore=roll[2]
                        print('Player scored ',iscore,' points')

                        if iscore > score :
                            print('Player Wins')
                            playersscore[i] = playersscore[i] + betlist[i]
                            playersscore[banker] = playersscore[banker] - betlist[i]

                            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
                            #print('playersscore is =', playersscore)

                        elif iscore < score:
                            print('Banker wins')
                            playersscore[i]=playersscore[i]-betlist[i]
                            playersscore[banker]=playersscore[banker]+betlist[i]

                            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
                            #print('playersscore is =',playersscore)

                        elif iscore==score:
                            print("It's a tie between the banker and the player!")
                            # den exei dokimastei akoma (ayto mallon prepei na to balw se ola ta iscore = score)

                            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
                            #print('playersscore is =', playersscore)

                        break
                    elif(roll[1]==roll[2]):
                        iscore=roll[0]
                        print('Player scored ',iscore,' points')
                        if iscore > score :
                            print('Player Wins')
                            # den exei dokimastei akoma (ayto mallon prepei na to balw se ola ta iscore > score)
                            playersscore[i] = playersscore[i] + betlist[i]
                            playersscore[banker] = playersscore[banker] - betlist[i]

                            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
                            #print('playersscore is =', playersscore)

                        elif iscore < score:
                            print('Banker wins')
                            # den exei dokimastei akoma (ayto mallon prepei na to balw se ola ta iscore < score)
                            playersscore[i] = playersscore[i] - betlist[i]
                            playersscore[banker] = playersscore[banker] + betlist[i]

                            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
                            #print('playersscore is =', playersscore)

                        elif iscore==score:
                            print("It's a tie between the banker and the player!")
                            # den exei dokimastei akoma (ayto mallon prepei na to balw se ola ta iscore = score)

                            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
                            #print('playersscore is =', playersscore)

                        break

                    elif (roll[0]==roll[2]):
                        iscore=roll[1]
                        print('Player scored ',iscore,' points')
                        if iscore > score :
                            print('Player Wins')
                            
                            playersscore[i] = playersscore[i] + betlist[i]
                            playersscore[banker] = playersscore[banker] - betlist[i]

                            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
                            #print('playersscore is =', playersscore)

                        elif iscore < score:
                            print('Banker wins')
                            
                            playersscore[i] = playersscore[i] - betlist[i]
                            playersscore[banker] = playersscore[banker] + betlist[i]

                            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
                            #print('playersscore is =', playersscore)

                        elif iscore==score:
                            print("It's a tie between the banker and the player!")
                            

                            # Gia diefkolynsi metatropis kai katanoisis tou kwdika mporeis; na valeis afta ta print se isxy
                            #print('playersscore is =', playersscore)

                        break
                    #Roll Again if
                    else:
                        print('Player rolls again')
                        roll=[]

                #synthkh gia allagh banker thn exw balei sto telos wste na mhn yparksoyn mperdemata me to score

                if flag_NewBankerIs:
                    banker=i
                    flag_NewBankerIs=False


    # check for bankrupt again in order not to be able to replay the main loop

    P = 0
    for i in range(len(playersscore)):# poios pexths einai
        if playersscore[i] <= 0:
            P = P + 1
        else:
            continue
    if P >= 2:  # επειδή το playersscore έχει παντα το πρωτο στοιχειο 0 (playersscore[0]=0)
        playersscore[0]=1#oste na mhn exw 2 midenika mesa sto playerscore
        print('\nPlayer',playersscore.index(0),'is bankrupt. Game ends.')
        print('Winner is player',playersscore.index(max(playersscore)),'with score : ',max(playersscore))
        MAINFLAG = False

    betlist = [0]


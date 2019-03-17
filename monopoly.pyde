# By: Michael Sheinman, Jake Graef
# Finished in June 20, 2018
# monopoly
# This is the final version of our monopoly game


# Libraries
import random
add_library("minim")

# Variables
actualTurn = 1
baserentcost = 50
bank_balance = 9999999
c = 1
countDeaths = 0
talking = 0
indexer = 0
infoShow = 0
parkingMoney = 0
sellMouse = 0
sellKey = 0
sellShow = 0
count = 0
counter = 0
big_x = 0
counter_of_equal = 0
delane=0
playerTurn = 1
dice = 0
numberChar = 0
countdown = 0
one = 0
two = 0
variableNum = 1
# Initial x & y position of the user
x = 750
y = 555



# Booleans
house_in_progress = False
dying_in_progress = False
stopIt=False
equal = False
inter=True
should_print_sucess = False
should_print_failure = False
die = False
jailedKey = False
roll = False
purchase_in_progress = False
fees_in_progress = False
attempt_one = False
wait = False
sold = False
toShow = False
intructions = False
cool_bonus = False
podiums = False
show_passed_go = False
instruct = False
rent_in_progress = False
in_parking = False
jail_in_progress = False
startGame = False
show_other_text = False
three_in_row = False
kick_in_progress = False
is_cards = False
gameOver = False
force_to_sell = False
delaney_forces = False
did_game_start_two = False

# Lists
listOfImages=[]
prop=[1,4,20,21,30,38]
podiumPlayers=[]
listOfNum2=[]
HouseAngleList={}
placesNoHouses=['DETENTION', 'GO', 'GO TO', 'BUS STOP 1', 'BUS STOP 2', 'BUS STOP 3', 'BUS STOP 4',
                'GRAD FEES','ANNOUNCEMENTS','BONUS MARKS','STUDENT PARKING','NCDSB','DSBN']
placesToNotDoAnything = ['DETENTION', 'GO', 'GO TO']
places = ['GO','BDSS','BONUS MARKS','WESTLANE','GRAD FEES','BUS STOP 1','ST. MICHAELS',
        'ANNOUNCEMENTS','ST. PAULS','LAURA SECORD','DETENTION','A-N MYER','NCDSB',
        'SIR W. CHURCHIL','ST. FRANCIS','BUS STOP 2','HOLY CROSS','BONUS MARKS','EDEN',
        'DENNIS MORRIS','STUDENT PARKING','THOROLD','ANNOUNCEMENTS','WELLAND',
        'NIAGARA CATHOLIC','BUS STOP 3','ST. CALLEGIATE','E.L. CROSSLY','DSBN'
        ,'PORT COLBORNE','GO TO','ORCHARD PARK','DSBN ACADEMY','BONUS MARKS','LAKESHORE',
        'BUS STOP 4','ANNOUNCEMENTS','BLESSED TRINITY','GRAD FEES','GSS']
bank_places = ['GO', 'BDSS', 'BONUS MARKS','WESTLANE','GRAD FEES','BUS STOP 1','ST. MICHAELS',
        'ANNOUNCEMENTS','ST. PAULS','LAURA SECORD','DETENTION','A-N MYER','NCDSB',
        'SIR W. CHURCHIL','ST. FRANCIS','BUS STOP 2','HOLY CROSS','BONUS MARKS','EDEN',
        'DENNIS MORRIS','STUDENT PARKING','THOROLD','ANNOUNCEMENTS','WELLAND',
        'NIAGARA CATHOLIC','BUS STOP 3','ST. CALLEGIATE','E.L. CROSSLY','DSBN'
        ,'PORT COLBORNE','GO TO','ORCHARD PARK','DSBN ACADEMY','BONUS MARKS','LAKESHORE',
        'BUS STOP 4','ANNOUNCEMENTS','BLESSED TRINITY','GRAD FEES','GSS']
# words for instructions
words = [       "","","                          INSTRUCTIONS","","1. OBJECTIVE - The object of the game is to become the wealthiest player","    through buying, renting and selling of property.",
              "","2. Each player will start with the amount of $1500.",
              "","3. All players will start at the 'GO' position and move in a clockwise direction around the board.",
              "","4. After each player lands on or goes past 'GO' they will recieve $200.",
              "","5. THE MOVE","    The amount of tiles you move is dependant on the role of both of the dice rolled.","        ~If the roll of both di are equal then the user will have the chance to roll again","            ~If the user gets 3 doubles in a row then they will be sent directlty to jail.","    User will have the chance to sell before their turn has begun and buy if they","    land on a property that has not been purchased ",
              "","6. For all regular coloured properities is as the following.","   a) If player is the first to land on property or has not been bought,","      player will have option to purchase for amount displayed.","   b) If player does not want to purchase property then it will reain for sale.","   c) If you own a property you can purchase a house to up the rent expense times 1.5","   d) If player lands on a property that has already been purchased they will","      have to pay the rent amount for that property.",
              "","7. SPECIAL PROPERTIES","   BONUS MARKS - This will display a message of a reward or a","   command to move to another location on the board.","   GRAD FEES - If a player lands on location marked 'grad fees'","   user will have to pay the fee of $150 to the bank.","   BUS STOP - These prperties act as other coloured properties","   with the exception that they cannot recieve houses. However","   if they have more than one bus stop rent prices will rise by $50.","   ANNOUNCEMENT - An announcement acts as either a reward or deduction,","   it appears as a card and will alert the player the information.","   NCDSB(Niagara Catholic District School Board) - This property is like","   any other property however rent price is dependant on the dice value.","   DSBN(District School Board of Niagara) - This property is like","   any other property however rent price is dependant on the dice value.",
              "","8. STUDENT PARKING: - If a user lands on this space during the game","    they will collect all of the money that has been accumulated from tax fees",            "","9. JAIL  ","    ~JUST VISITING - Players that have not been sent to jail will be in the 'Just Visiting'","     position of the jail.","    ~Players That have been sent to jail will be required to stay there until 1 of the following","    conditions have been met","        ~Double roll - user rolls the same number on both di","        ~It is the player's third turn spent in jail, that roll will be counted as their roll out of jail.",
              "","10. BANKRUPTCY","    ~If user has insufficient funds in their bank account and have to pay rent or another expense","     the following will occur","        ~If the user has properties they will be asked which property they will sell.","        ~If the user does not have any properties then the player will be declared bankrupt and will be","     removed from the game. ",
              "","11. BUTTONS","    ~There are buttons located on the side of the playing screen where you can buy, sell, pass, houses","    and info","    ~You will be instructed on what buttons to press when Mr. Delaney instructs you.","~    To roll the dice you must click on the dice in the center of the screen then two dice will roll","    and the roll will be broadcasted in the top right corner of the playing board",
              "",""
              "",
              "          PRESS SHIFT TO START - ENJOY YOUR GAME"]
new_words = []
coordinateXList=[655,590,525,460,395,330,265,200,140,65,65,65,65,65,65
                 ,65,65,65,65,65,140,200,265,330,395,460,525,590,655,750,750,750,750
                 ,750,750,750,750,750,750,750,750]
coordinateYList=[555,555,555,555,555,555,555,555,555,555
                 ,492,443,395,345,295,245,200,150,100,20,20,20
                 ,20,20,20,20,20,20,20,20,100,150,200,245,295
                 ,345,395,443,492,555]

# Instructions Var
chase_y=30
stop=0

# Dictionaires
is_in_jail = {}
players={}
players2={}
playersAndProperty = {}
plyersCoord={}
user_houses = {}
playersAndMoney = {}
playersAndBuses = {}

bonus = {'go': 'Advance to go!',
         '200 money': 'You earn a scholarship\n in value of $200',
         'keep going' : 'What are you looking at?!\nKeep working!\nYou get another turn'
          }
announcements = {'detention': 'You have been given 2 \ndays detention',
                 'grad fee': 'School grad fee! Pay $150',
                 'dance': 'Dance fee! Pay $100\nYou have to come!'
                }
positionsAndCosts = {'GO':0,'BDSS':80,'BONUS MARKS':0,'WESTLANE':80,'GRAD FEES':60,'BUS STOP 1': 200,'ST. MICHAELS' : 100,
        'ANNOUNCEMENTS': 0,'ST. PAULS': 100,'LAURA SECORD': 110,'DETENTION':0,'A-N MYER':170,'NCDSB': 150,'SIR W. CHURCHIL':170,
        'ST. FRANCIS': 180,'BUS STOP 2': 200 ,'HOLY CROSS': 190,'BONUS MARKS':0,'EDEN':190,'DENNIS MORRIS': 200,'STUDENT PARKING': 0,'THOROLD': 260,
        'ANNOUNCEMENTS': 0,'WELLAND': 260,'NIAGARA CATHOLIC':270,'BUS STOP 3': 200,'ST. CALLEGIATE': 260,'E.L. CROSSLY': 260,'DSBN': 150,'PORT COLBORNE':260,'GO TO':0,
        'ORCHARD PARK': 350,'DSBN ACADEMY': 350, 'BONUS MARKS': 0,'LAKESHORE':360,'BUS STOP 4': 200,'ANNOUNCEMENTS': 0,'BLESSED TRINITY':375,'GRAD FEES':0,
        'GSS':400}
basicRentValue = {'GO':0,'BDSS':30,'BONUS MARKS':0,'WESTLANE':30,'GRAD FEES':0,'BUS STOP 1': 50,'ST. MICHAELS': 30,
        'ANNOUNCEMENTS':0,'ST. PAULS':30,'LAURA SECORD':30,'DETENTION':60,'A-N MYER':40,'NCDSB':50,'SIR W. CHURCHIL':40,
        'ST. FRANCIS': 40,'BUS STOP 2': 50,'HOLY CROSS':60,'BONUS MARKS':60,'EDEN':60,'DENNIS MORRIS':60,'STUDENT PARKING':60,'THOROLD':65,
        'ANNOUNCEMENTS':0,'WELLAND':65,'NIAGARA CATHOLIC':65,'BUS STOP 3': 50,'ST. CALLEGIATE': 70,'E.L. CROSSLY':70,'DSBN': 50,'PORT COLBORNE':70,'GO TO':60,
        'ORCHARD PARK': 75,'DSBN ACADEMY':75,'BONUS MARKS':0,'LAKESHORE':75,'BUS STOP 4': 50,'ANNOUNCEMENTS':0,'BLESSED TRINITY':85,'GRAD FEES':0,
        'GSS':85}
# basicRentValue will never change, but positionsAndRentValue does change. 
positionsAndRentValue = {'GO':0,'BDSS':30,'BONUS MARKS':0,'WESTLANE':30,'GRAD FEES':0,'BUS STOP 1': 50,'ST. MICHAELS': 30,
        'ANNOUNCEMENTS':0,'ST. PAULS':30,'LAURA SECORD':30,'DETENTION':60,'A-N MYER':40,'NCDSB':50,'SIR W. CHURCHIL':40,
        'ST. FRANCIS': 40,'BUS STOP 2': 50,'HOLY CROSS':60,'BONUS MARKS':60,'EDEN':60,'DENNIS MORRIS':60,'STUDENT PARKING':60,'THOROLD':65,
        'ANNOUNCEMENTS':0,'WELLAND':65,'NIAGARA CATHOLIC':65,'BUS STOP 3': 50,'ST. CALLEGIATE': 70,'E.L. CROSSLY':70,'DSBN': 50,'PORT COLBORNE':70,'GO TO':60,
        'ORCHARD PARK': 75,'DSBN ACADEMY':75,'BONUS MARKS':0,'LAKESHORE':75,'BUS STOP 4': 50,'ANNOUNCEMENTS':0,'BLESSED TRINITY':85,'GRAD FEES':0,
        'GSS':85}

# TESTING LOOP - This is not part of the code, but if you want to check the end of the game uncomment the next lines
# for mykey in positionsAndRentValue.keys():
#     positionsAndRentValue[mykey] *= 100

# String Variables
char='?'

# Game going, functions, classes, etc
class money_transformations:        
    # For transformations between players
    def normal_transformation(self, amount, paying, paid):
        global playersAndMoney
        playersAndMoney[paying] -= amount


# This is the function which uses the above class and defines when to make the money transformation 
# and when the user may not have enough money
def use_money_class(amount = 0, paying = bank_balance, paid = bank_balance):
    global playersAndMoney, playerTurn, playersAndProperty, force_to_sell, dying_in_progress
    try:
        if amount > playersAndMoney['Player' + str(playerTurn)] and len(playersAndProperty['Player' + str(playerTurn)]) == 0:
            kicked_out()
        elif amount > playersAndMoney['Player' + str(playerTurn)] and len(playersAndProperty['Player' + str(playerTurn)]) > 0:
            if not dying_in_progress:
                myClass = money_transformations()
                myClass.normal_transformation(amount, paying, paid)
            if dying_in_progress:
                if playersAndMoney['Player' + str(playerTurn)] > 0:
                    force_to_sell = False
                else:
                    force_to_sell = True
            else:
                force_to_sell = True
            dying_in_progress = True
        else:
            myClass = money_transformations()
            myClass.normal_transformation(amount, paying, paid)
    except KeyError:
        pass

# General class for building, houses and hotles will be child classes of this class
class Building(object):
    def __init__(self, x, y, heights, lengths):
        # The information here is the coordinates, height, and length as those always stay the same
        self.x = x
        self.y = y
        self.heights = heights
        self.lengths = lengths

# Child class of the class defined above - building
class Houses(Building):
    def __init__(self, x, y, heights, lengths, colour, price, turn):
        super(Houses, self).__init__(x, y, heights, lengths)
        # Variables that change: the turn, the house colours, and the price
        self.colour = colour
        self.price = price
        self.turn=turn
    # This function builds the houses
    def BuildIt(self):
        school=loadImage('school'+str(self.turn)+'.png')
        image(school,self.x,self.y,self.heights,self.lengths)

# A function that only takes place if the user got kicked out
def kicked_out():
    global playerTurn, podiumPlayers,playersAndMoney, is_in_jail, players, playersAndProperty, plyersCoord, numberChar, kickedGuy, kick_in_progress
    kickedGuy = playerTurn
    toKick = 'Player' + str(playerTurn)
    podiumPlayers.append(players[toKick])
    del playersAndMoney[toKick]
    del is_in_jail[toKick]
    listOfImages.remove(players[toKick])
    del players[toKick]
    del playersAndProperty[toKick]
    del plyersCoord[toKick]
    numberChar -= 1
    kick_in_progress = True
    equal = False
    change_actual_turn()

# Setting up images and the starting screen
def setup():
    global sf, first, secon, img3, img4, img5, img6
    textSize(24)
    size(1000,600)
    background(255)
    img2=loadImage('mono.png')
    imageMode(CENTER)
    image(img2,400,300,800,600)
    # This images are for a gif we implemented
    first = loadImage("frame_0_delay-0.1s.gif")
    secon = loadImage("frame_1_delay-0.1s.gif")
    img3 = loadImage("frame_2_delay-0.1s.gif")
    img4 = loadImage("frame_3_delay-0.1s.gif")
    img5 = loadImage("frame_4_delay-0.1s.gif")
    img6 = loadImage("frame_5_delay-0.1s.gif")
    minim=Minim(this)
    sf=minim.loadFile("MonopolyBackgroundMusic.mp3")

# buy/sell/pass/house/info buttons and deciding when are they showed
def background_buttons(buy, pas, to_info, to_sell, houses):
    # Loading images which will usually be used
    imageMode(CENTER)
    buttonP=loadImage('buy.png')
    buttonPass=loadImage('pass.png')
    sell=loadImage('sell.png')
    house=loadImage('houses.png')
    info=loadImage('info.png')
    
    # Makes the button glow if the mouse is there
    if 805 <= mouseX <= 990 and 20 <= mouseY <= 100 and buy==True:
        buy2=loadImage('buy2.png')
        image(buy2,900,60,190,80)
    else:
        if buy:
            noTint()
            image(buttonP,900,60,190,80)
    # Makes the pass button glow if the mouse is there
    if 805 <= mouseX <= 990 and 115 <= mouseY <= 205 and pas == True:
        noTint()
        pass2=loadImage('pass2.png')
        image(pass2,900,160,190,80)
    else:
        if pas:
            noTint()
            image(buttonPass,900,160,190,80)
    
    # Makes the info button glow if the mouse is there
    if 805 < mouseX < 995 and 420 < mouseY < 500 and to_info == True:
        noTint()
        info2=loadImage('info2.png')
        image(info2,900,460,190,80)
    else:
        if to_info:
            noTint()
            image(info,900,460,190,80)
    
    # Makes the sell button glow if the mouse is there
    if 805 < mouseX < 995 and 220 < mouseY < 300 and to_sell == True:
        sell2=loadImage('sell2.png')
        image(sell2,900,260,190,80)
    else:
        if to_sell:
            noTint()
            image(sell,900,260,190,80)
    
    # Make the house button glow if the mouse is there
    if 805 <= mouseX <= 995 and 320 < mouseY < 400 and houses==True:
        house2=loadImage('house2.png')
        image(house2,900,360,190,80)
    else:
        if houses:
            noTint()
            image(house,900,360,190,80)

# This function will take care of delaney's text (in-game instructor)
def delaney_talking(enter, pay = 0, mySize = 12):
    global positionsAndRentValue, playersAndMoney, playerTurn
    delan=loadImage('delaney.png')
    image(delan,250,350,300,300)
    textSize(mySize)
    fill(0)
    try:
        if pay <= playersAndMoney["Player" + str(playerTurn)]:
            text(enter, 235, 250)
        else:
            text("You must pay $" + str(pay) +  " rent \nYou are missing " + 
            str(pay - playersAndMoney["Player" + str(playerTurn)]) + 
            ", \nYou must sell a property.\nOnce finished, click RIGHT" , 235, 250)
    except KeyError:
        text(enter, 235, 250)

# Whenever a mouse is pressed, this function takes place
def mousePressed():
    global roll, equal, talking, infoShow,sellShow, purchase_in_progress, show_other_text, playersAndMoney, char, should_print_failure, should_print_sucess, \
    counter_of_equal, playerTurn, plyersCoord, is_in_jail, die, playersAndProperty, toShow, is_cards, myPlace, myann, jail_in_progress, wait, sold, cool_bonus,\
    house_in_progress, countdown, three_in_row, HouseAngleList, infoShow
    if sellMouse==1:
        talking=1
    
    # Assuming the user is attempting to create a house
    if house_in_progress == True:
        # When the user presses on the button
        if 805 <= mouseX <= 995 and 320 < mouseY < 400:
            # If they have enough money....
            if playersAndMoney['Player'+str(playerTurn)] >= 100:
                playersAndMoney['Player'+str(playerTurn)] -= 100
                xer=(plyersCoord['Player'+str(playerTurn)][0])
                yer=(plyersCoord['Player'+str(playerTurn)][0])
                turned=1
                # This is an algorithm to detmine where the house will be placed
                if plyersCoord['Player'+str(playerTurn)][1] < 80:
                    xer=(plyersCoord['Player'+str(playerTurn)][0])
                    turned=1
                    yer=(plyersCoord['Player'+str(playerTurn)][1]) + 40
                elif plyersCoord['Player'+str(playerTurn)][1]>525:
                    xer=(plyersCoord['Player'+str(playerTurn)][0])
                    turned=2
                    yer=(plyersCoord['Player'+str(playerTurn)][1]) - 40
                elif plyersCoord['Player'+str(playerTurn)][0]<105:
                    xer=(plyersCoord['Player'+str(playerTurn)][0]) + 40
                    yer=(plyersCoord['Player'+str(playerTurn)][1])
                    turned=3
                elif plyersCoord['Player'+str(playerTurn)][0]>695:
                    xer=(plyersCoord['Player'+str(playerTurn)][0]) - 40
                    yer=(plyersCoord['Player'+str(playerTurn)][1])
                    turned=4
                objects=Houses(xer,yer,
                                50,50,'green',100,turned)
                # Using the class function to actually show the house
                objects.BuildIt()
                user_houses[places[plyersCoord['Player'+str(playerTurn)][2]]] = [xer, yer]
                new = int(positionsAndRentValue[places[plyersCoord['Player'+str(playerTurn)][2]]] * 0.5)
                positionsAndRentValue[places[plyersCoord['Player'+str(playerTurn)][2]]] += new
                HouseAngleList[places[plyersCoord['Player'+str(playerTurn)][2]]] = turned
                
            else:
                # A case scenrio when the user lacks money
                delaney_talking("No enough Money!")
            change_actual_turn()
            house_in_progress = False
        # When the user presses on pass, nothing happen
        elif 805 <= mouseX <= 995 and 120 <= mouseY < =200:
            house_in_progress = False
            change_actual_turn()
    if (infoShow==2 or infoShow==1) and sellShow != 1:
        # When the user pressed on the mouse button
        if 805 < mouseX and mouseX < 995 and 420 < mouseY and mouseY < 500:
            infoShow = 1
        if 465<mouseX<535 and 365<mouseY<425:
            infoShow=2
    if (sellShow == 2 or sellShow == 1) and infoShow != 1:
        if 805 < mouseX < 995 and 220 < mouseY < 300:
            talking = 0
            selling()
        if 465<mouseX<535 and 390 < mouseY < 450:
            sellShow = 2
    if roll == True:
        wait = False
        cool_bonus = False
        toShow = False
        purchase_in_progress = False
        is_cards = False
        if 360 <= mouseX <= 435 and 260 <= mouseY <= 335:
            # Rolling the die once the user presses on the board die 
            global die, one, two, dice
            # the countdown is what creates the gif for dies
            countdown = 6
            die = True
            roll = False
            one = int(random.randint(1,6))
            two = int(random.randint(1,6))
            dice = one + two
            if is_in_jail['Player'+str(playerTurn)] == False:
                if one == two:
                    equal = True
                    counter_of_equal += 1
                    if counter_of_equal == 3:
                        three_in_row = True
                else:
                    equal = False
                    counter_of_equal = 0
            else:
                if one == two:
                    is_in_jail['Player'+str(playerTurn)] = False
                else:
                    equal = False
                    die = False
                    is_in_jail['Player'+str(playerTurn)] -= 1
                    if is_in_jail['Player'+str(playerTurn)] == 0:
                        is_in_jail['Player'+str(playerTurn)] = False
                    change_actual_turn()
    # This lines occurs if the user has the chance to purchase a property
    elif purchase_in_progress == True:
        if 805 <= mouseX <= 990 and 20 <=mouseY<= 100 and not jail_in_progress and not in_parking and not rent_in_progress:
            # Assuming the user presses on buy and they have enough money, the purchase will be successful.
            if mousePressed and playersAndMoney['Player'+str(playerTurn)] >= positionsAndCosts[places[plyersCoord['Player'+str(playerTurn)][2]]] and \
                purchase_in_progress and not is_cards and not toShow:
                delaney_talking("Purchase Successful!")
                should_print_sucess = True
                show_other_text = False
                purchase_in_progress = False
                use_money_class(positionsAndCosts[places[plyersCoord['Player'+str(playerTurn)][2]]], "Player" + str(playerTurn))
                playersAndProperty['Player'+str(playerTurn)].append(places[plyersCoord['Player'+str(playerTurn)][2]])
                bank_places.remove(places[plyersCoord['Player'+str(playerTurn)][2]])
                
                # This lines check whether the property is a bus, in which case the rent changes accordingly
                current_property = places[plyersCoord['Player'+str(playerTurn)][2]]
                if 'BUS STOP' in current_property:
                    playersAndBuses['Player'+str(playerTurn)] += 1
                    totalBuses = playersAndBuses['Player'+str(playerTurn)]
                    value = 50 * totalBuses
                    if 'BUS STOP 1' in playersAndProperty['Player'+str(playerTurn)]:
                        positionsAndRentValue['BUS STOP 1'] = value
                    if 'BUS STOP 2' in playersAndProperty['Player'+str(playerTurn)]:
                        positionsAndRentValue['BUS STOP 2'] = value
                    if 'BUS STOP 3' in playersAndProperty['Player'+str(playerTurn)]:
                        positionsAndRentValue['BUS STOP 3'] = value
                    if 'BUS STOP 4' in playersAndProperty['Player'+str(playerTurn)]:
                        positionsAndRentValue['BUS STOP 4'] = value
                # Property is purchased, turn is over
                change_actual_turn()                             
            elif mousePressed and playersAndMoney['Player'+str(playerTurn)] < positionsAndCosts[places[plyersCoord['Player'+str(playerTurn)][2]]]:
                delaney_talking("Not enough money!")
                should_print_failure = True
                show_other_text = False
                purchase_in_progress = False
                change_actual_turn()   
        # If the user presses on pass
        elif 805 <= mouseX <= 990 and 115 <= mouseY <= 205 and not jail_in_progress and not is_cards and not toShow and not in_parking:
            purchase_in_progress = False
            show_other_text = False
            delaney_talking("Did not purchase!")
            change_actual_turn()
        elif 325 <= mouseX <= 525 and 325 <= mouseY <= 525 and is_cards:
            if not toShow:
                toShow = True
                if myPlace == 'BONUS MARKS':
                    if myBonus == 'keep going':
                        cool_bonus = True
                        is_cards = False
                        delaney_talking(bonus[myBonus])
                    else:
                        rectMode(CENTER)
                        fill(244, 244, 244)
                        rect(425, 425, 200, 100)
                        fill(0)
                        textSize(24)
                        text('Bonus Marks', 350, 400)
                        textSize(12)
                        text(bonus[myBonus], 355, 420)
                        text('Click on the card to continue!', 330, 470)
                # Showing the announcement card
                else:
                    rectMode(CENTER)
                    fill(244, 244, 244)
                    rect(425, 425, 200, 100)
                    fill(0)
                    textSize(20)
                    text('Announcements', 340, 400)
                    textSize(12)
                    text(announcements[myann], 355, 420)
                    text('Click on the card to continue!', 330, 470)
                
            else:
                # Showing the bonus mark card
                if myPlace == 'BONUS MARKS':
                    if myBonus == 'go':
                        plyersCoord['Player'+str(playerTurn)][2] = 0
                        plyersCoord['Player'+str(playerTurn)][0] = 750
                        plyersCoord['Player'+str(playerTurn)][1] = 555
                        use_money_class(-200,'Player' + str(playerTurn))
                    elif myBonus == '200 money':
                        use_money_class(-200,'Player' + str(playerTurn))
                    elif myBonus == 'keep going':
                        delaney_talking(bonus[myBonus])
                        wait = True
                        
                else:
                    if myann == 'detention':
                        jail_in_progress = False
                        is_in_jail['Player' + str(playerTurn)] = 2
                        plyersCoord['Player'+str(playerTurn)][2] = 10
                        plyersCoord['Player'+str(playerTurn)][0] = 65
                        plyersCoord['Player'+str(playerTurn)][1] = 555
                        equal = False
                    elif myann == 'grad fee':
                        use_money_class(150,'Player' + str(playerTurn))
                    elif myann == 'dance':
                        use_money_class(100,'Player' + str(playerTurn))
                is_cards = False
                toShow = False
                purchase_in_progress = False
                if not wait:
                    if not force_to_sell:
                        change_actual_turn()
                else:
                    wait = False
# This function occurs whenever the user releases a key
def keyReleased():
    global startGame, sellKey, playersAndProperty, indexer, sellShow, talking, jailedKey, inter, intructions, purchase_in_progress, show_other_text, \
    jail_in_progress, places, plyersCoord, playerTurn, fees_in_progress, rent_in_progress, die, attempt_one, toFind, positionsAndRentValue, playedPaid, \
    in_parking,instruct, parkingMoney, countDeaths,podiums,kick_in_progress, force_to_sell, delaney_forces, bank_places, three_in_row, equal, die, user_houses, gameOVer
    # if sell is going on
    if sellKey == 1:
        if key == 'y':
            # The user agreed to sel
            myPlace = playersAndProperty['Player'+str(playerTurn)].index(places[indexer+1])
            property = places[indexer+1]
            # Buses have special conditions under rent
            if 'BUS STOP' in property:
                if 'BUS STOP 1' in property:
                    positionsAndRentValue['BUS STOP 1'] -= 50
                if 'BUS STOP 2' in property:
                    positionsAndRentValue['BUS STOP 2'] -= 50
                if 'BUS STOP 3' in property:
                    positionsAndRentValue['BUS STOP 3'] -= 50
                if 'BUS STOP 4' in property:
                    positionsAndRentValue['BUS STOP 4'] -= 50
                positionsAndRentValue[property] = 50
            elif property in user_houses.keys():
                del user_houses[property]
                del HouseAngleList[property]
            playersAndProperty['Player'+str(playerTurn)].pop(myPlace)
            sellingCost = positionsAndCosts[places[indexer+1]]
            sold = True
            bank_places.append(places[indexer+1])
            playersAndMoney['Player'+str(playerTurn)] += (sellingCost/2)
            board=loadImage('mon.png')
            image(board,400,300,800,600)
            delaney_talking("Ok")
            sellKey = 0
            sellMouse = 0
            sellShow = 2
            talking = 0
            delaney_forces = False
            force_to_sell = False
            positionsAndRentValue[property] = basicRentValue[property]
        elif key=='n':
            sellMouse = 0
            sellKey = 0
            talking = 0
    if keyCode == SHIFT and startGame == False:
        instruct = False
        startGame = True
        inter = False
    elif key == 'r':
        intructions = True
    if keyCode == RIGHT:
        # GRAD FEES
        if fees_in_progress:
            if not force_to_sell:
                fees_in_progress = False
                change_actual_turn()
                purchase_in_progress = False
        # Paying rent
        elif rent_in_progress:
            # Special rent case, rent has to be calculated according to die roll
            if toFind == 'DSBN' or toFind == 'NCDSB':
                amount = 10 * dice 
                use_money_class(amount, "Player" + str(playerTurn), playerPaid)
                use_money_class(-amount, playerPaid, "Player" + str(playerTurn)) 
            else:
                use_money_class(-positionsAndRentValue[toFind], playerPaid, "Player" + str(playerTurn))  
                use_money_class(positionsAndRentValue[toFind], "Player" + str(playerTurn), playerPaid)
            rent_in_progress = False                   
            if not force_to_sell:
                purchase_in_progress = False
                attempt_one = False
        # Actually sending to jail if they rolled three in a row
        elif three_in_row:
            is_in_jail['Player'+str(playerTurn)] = 2
            counter_of_equal = 0
            plyersCoord['Player'+str(playerTurn)][2] = 10
            plyersCoord['Player'+str(playerTurn)][0] = 65
            plyersCoord['Player'+str(playerTurn)][1] = 555
            die = False
            equal = False
            three_in_row = False
            # user is sent to jail, therefore the turn is over
            change_actual_turn()
        # This is if the user is sent to jail
        elif jailedKey == True:
            jail_in_progress = False
            # Dictionaries and coordinates are changed appropiartely.
            is_in_jail['Player' + str(playerTurn)] = 2
            plyersCoord['Player'+str(playerTurn)][2] = 10
            plyersCoord['Player'+str(playerTurn)][0] = 65
            plyersCoord['Player'+str(playerTurn)][1] = 555
            purchase_in_progress = False
            die = False
            change_actual_turn()
            jailedKey=False
        # Providing money if the user landed on "student parking" spot
        elif in_parking:
            use_money_class(-parkingMoney,'Player' + str(playerTurn))
            parkingMoney = 0
            in_parking = False
            die = False
            purchase_in_progress = False
            change_actual_turn()
        elif gameOver:
            # Showing the podium
            podiums=True
            podium()
        elif kick_in_progress and countDeaths != (numberChar):
            stopIt = False
            kick_in_progress = False
    
        
# This appears exactly once the game starts
def game_start():
    global x,y, count,img,delane,img1, die, counter, dice, numberChar, playerTurn, char, equal, intructions
    faded=loadImage('mono.png')
    imageMode(CENTER)
    image(faded,400,300,800,600)

    if delane==0:
        delaney_talking("Hello,\nI am Mr.Delaney!\nTo continue press space...")
        if key==' ':
            delane=1
    else:
        delaney_talking('WELCOME TO MONOPOLY\nSCHOOL EDITION\nTo start, press Shift\nFor rules, press "r"')

# This function takes user input for how many characters are in the game
def character_number():
    listOfNum=[]
    global x,y, podiumNumberChar, count,img,img1, die, counter, dice, numberChar, playerTurn, char, equal,listOfNum2
    img1=loadImage(str(char))
    faded=loadImage('mono.png')
    background(255)
    imageMode(CENTER)
    image(faded,400,300,800,600)
    fill(255)
    rectMode(CENTER)
    rect(315,400,100,50)
    delaney_talking("CHoOSE NUMBER OF CHAR!\n\nType into box from 2-4!")
    textSize(20)
    if keyPressed and len(listOfNum)==0:
        if key=='2' or key=='3' or key=='4':
            listOfNum.append(key)
            listOfNum2.append(key)
            text(''.join(listOfNum),310,405)
        elif key==ENTER and len(listOfNum2)>0:
            numberChar=int(listOfNum2[-1])
            podiumNumberChar=numberChar
    else:
        if len(listOfNum2)>0:
            text(listOfNum2[-1],310,405)

# This is a function that draws the board
def initial_image():
    global x,y, count,img,img1, die, counter, dice, numberChar, playerTurn, char, equal
    img1=loadImage(str(char))
    faded=loadImage('mono.png')
    background(255)
    imageMode(CENTER)
    image(faded,400,300,800,600)
    chooseChar()
    
# This is the function that draws the character
def set_coordinates():
    for i in range(len(players.keys())):
        current_player = players.keys()[i]
        saved_image = players[current_player]
        img1 = loadImage(str(saved_image))
        x = plyersCoord[current_player][0]
        y = plyersCoord[current_player][1]
        image(img1,x,y,75,75)
        
# This is the function to draw the board
def set_character():
    global x,y, count,img,img1, die, HouseAngleList,counter, dice, numberChar, playerTurn, char, equal, purchase_in_progress, playerTurn, user_houses, is_cards, \
    toShow, jailedKey
    if purchase_in_progress == False:
        char=players['Player'+str(playerTurn)]        
    img1=loadImage(str(char))
    board=loadImage('mon.png')
    background(255)
    imageMode(CENTER)
    image(board,400,300,800,600)
    x=plyersCoord['Player'+str(playerTurn)][0]
    y=plyersCoord['Player'+str(playerTurn)][1]
    set_coordinates()
    # Checking what buttons should be showed
    if house_in_progress:
        b = True
        e = True
    else:
        b = False
        e = False
    if purchase_in_progress and not is_cards and not toShow and not jailedKey and not rent_in_progress:
        a = True
    else:
        a = False
    # Sending this variables into a function
    background_buttons(a, b, True, True, e)
    draw_button(playerTurn)
    if len(user_houses.values()) > 0:
        for i in range(0,len(user_houses.values())):
            school=loadImage('school'+str(HouseAngleList.values()[i])+'.png')
            image(school,int(user_houses.values()[i][0]),int(user_houses.values()[i][1]),50,50)

# shows all dies
def show_dices():
    textSize(24)
    text("Die:", 600, 125)
    text("Total:", 590, 220)
    textSize(20)
    fill(255)
    # Rectangles - will contain the dies
    rect(600, 150, 40, 40)
    rect(640, 150, 40, 40)
    rect(620, 255, 50, 50)   
    fill(0)
    # This is where you add dies and total - placed inside the boxes above
    text(one, 595, 160)
    text(two, 635, 160)
    text(dice, 615, 265)
    strokeWeight(4)
    stroke(0)

# The code behind the button which indicates the user's turn
def draw_button(playerTurn):
    textSize(20)
    bar=loadImage('IBar.png')
    image(bar,900,550,200,100)
    fill(0)
    text('Player '+str(playerTurn),895,550)
    logo=loadImage(str(players['Player'+str(playerTurn)]))
    image(logo,850,550,40,40)

# This function is constantly being called while the game function runs to indicate a turn is over and a new one is about to start
def change_actual_turn():
    global playerTurn, numberChar
    if equal:
        pass
    else:
        while True:
            if playerTurn > 4:
                playerTurn = 1
                if "Player" + str(playerTurn) in players.keys():
                    break
            else:
                playerTurn += 1
                if "Player" + str(playerTurn) in players.keys():
                    break

# Picking a random bonus card + showing it
def bonus_cards():
    global bonus, announcements, myBonus
    myBonus = random.choice(bonus.keys())
    rectMode(CENTER)
    fill(244, 244, 244)
    rect(425, 425, 200, 100)
    textSize(32)
    fill(0)
    bonusImage=loadImage('bonus.png')
    image(bonusImage,425,425,150,150)

# Picking a random announcement card + showing
def my_ann():
    global bonus, announcements, myBonus, myann
    myann = random.choice(announcements.keys())
    rectMode(CENTER)
    fill(244, 244, 244)
    rect(425, 425, 200, 100)
    textSize(20)
    fill(0)
    annImage=loadImage('ann.png')
    image(annImage,425,425,150,150)

# Game function
def game():
    # Global variables
    global x,y,jailedKey, infoShow, count,img,img1, die, counter, dice, numberChar, variableNum, playerTurn, char, equal, purchase_in_progress, \
    should_print_sucess, should_print_failure, did_game_start_two, rent_in_progress, playerPaid, placesToNotDoAnything, attempt_one, show_other_text, show_passed_go\
    , is_cards, bonus, myBonus, HouseAngleList, toShow, myPlace, jail_in_progress, fees_in_progress, toFind, parkingMoney, in_parking, house_in_progress, user_houses
    if numberChar == 0:
        character_number()
    else:
        if len(players)<numberChar and not purchase_in_progress:
            initial_image()
        else:
            set_character()

            should_print_sucess = False
            should_print_failure = False
            if die == True or purchase_in_progress:
                show_passed_go = True
                if not purchase_in_progress:
                    show_dices()
                    plyersCoord['Player'+str(playerTurn)][0]=coordinateXList[plyersCoord['Player'+str(playerTurn)][2]]
                    plyersCoord['Player'+str(playerTurn)][1]=coordinateYList[plyersCoord['Player'+str(playerTurn)][2]]
                    if plyersCoord['Player'+str(playerTurn)][2]==39:
                        plyersCoord['Player'+str(playerTurn)][2]=0
                    else:
                        plyersCoord['Player'+str(playerTurn)][2]+=1
                    # Providing the user with 200 dollars once they pass GO
                    if places[plyersCoord['Player'+str(playerTurn)][2]] == 'GO':
                        use_money_class(-200,'Player' + str(playerTurn))
                # This is what determines whether the user should actually move or not
                if dice-1==counter or purchase_in_progress or rent_in_progress:
                    myPlace = places[plyersCoord['Player'+str(playerTurn)][2]]
                    # another condition if the user landed on announcements or bonus cards
                    if places[plyersCoord['Player'+str(playerTurn)][2]] == 'BONUS MARKS' or places[plyersCoord['Player'+str(playerTurn)][2]] == 'ANNOUNCEMENTS':
                        is_cards = True
                    # if the user landed on Grad Fees
                    elif places[plyersCoord['Player'+str(playerTurn)][2]] == 'GRAD FEES' and not fees_in_progress:
                        use_money_class(150, "Player" + str(playerTurn))
                        parkingMoney += 150
                        fees_in_progress = True
                    # condition if the user landed on student parking
                    elif places[plyersCoord['Player'+str(playerTurn)][2]] == 'STUDENT PARKING':
                        in_parking = True
                    show_passed_go = False
                    if not rent_in_progress:
                        purchase_in_progress = True
                        show_other_text = True
                        die=False
                        counter=0
                    if places[plyersCoord['Player'+str(playerTurn)][2]] in placesToNotDoAnything and not rent_in_progress:
                        if places[plyersCoord['Player'+str(playerTurn)][2]] == 'GO TO':
                            jailedKey=True
                        else:
                            purchase_in_progress = False
                            die = False
                            change_actual_turn()
                    # if the user landed on property owned by another player
                    elif not is_cards and places[plyersCoord['Player'+str(playerTurn)][2]] not in bank_places or rent_in_progress:
                        if not rent_in_progress:
                            toFind = places[plyersCoord['Player'+str(playerTurn)][2]]
                            copyOfDic = playersAndProperty
                            keyToAdd = 'Player'+str(playerTurn)
                            valueToAdd = playersAndProperty['Player'+str(playerTurn)]
                            del copyOfDic['Player'+str(playerTurn)]
                            for x in copyOfDic:
                                if toFind in copyOfDic[x]:
                                    playerPaid = x
                                    rent_in_progress = True
                            playersAndProperty[keyToAdd] = valueToAdd
                            if rent_in_progress == False:
                                if places[plyersCoord['Player'+str(playerTurn)][2]] not in placesNoHouses and \
                                    places[plyersCoord['Player'+str(playerTurn)][2]] not in user_houses:
                                    house_in_progress = True
                                else:
                                    change_actual_turn()
                                purchase_in_progress = False
                        else:
                            # Special properties
                            if toFind == 'DSBN' or toFind == 'NCDSB':
                                amount = dice * 10
                                delaney_talking("Private property!\nPay 10 * %s = $%s rent to \n%s! Press RIGHT \nARROW to advance!" % (str(dice), str(amount), playerPaid), amount)
                            else:
                                delaney_talking("Private property!\nPay $%s rent to %s!\nPress RIGHT ARROW to \nadvance!" % (str(positionsAndRentValue[toFind]), 
                                playerPaid), positionsAndRentValue[toFind])
                            draw_button(playerTurn)

                else:
                    # The variables increases, until it will reach the die roll and the movement will stop
                    counter+=1
                if len(players)>=numberChar and not rent_in_progress:
                    board = loadImage('mon.png')
                    background(255)
                    image(board,400,300,800,600)
                    fill(0)
                    draw_button(playerTurn)
                    if purchase_in_progress and not jail_in_progress and not toShow and not is_cards and not fees_in_progress and not in_parking:
                        a = True
                        b = True
                    else:
                        a = False
                        b = False
                    if house_in_progress:
                        b = True
                        e = True
                        a = False
                    else:
                        e = False
                    background_buttons(a, b, True, True, e)
                    if len(user_houses.values())>0:
                        for i in range(0,len(user_houses.values())):
                            school=loadImage('school'+str(HouseAngleList.values()[i])+'.png')
                            image(school,int(user_houses.values()[i][0]),int(user_houses.values()[i][1]),50,50)
                    if places[plyersCoord['Player'+str(playerTurn)][2]] == 'GO TO' and purchase_in_progress:
                        delaney_talking('You have landed in\nDetention!\nPress "RIGHT ARROW"\nto advance!')
                        equal = False
                        jail_in_progress = True
                    if toShow or is_cards or purchase_in_progress:
                        if toShow or is_cards or show_other_text == True and places[plyersCoord['Player'+str(playerTurn)][2]] in bank_places and \
                            places[plyersCoord['Player'+str(playerTurn)][2]] not in placesToNotDoAnything:
                            if is_cards and not toShow:
                                delaney_talking("You landed on \n%s!\nClick on the card \nto see what you got! ")
                                if myPlace == 'BONUS MARKS':
                                    bonus_cards()
                                else:
                                    my_ann()
                            elif toShow:
                                if myPlace == 'BONUS MARKS':
                                    if myBonus == 'keep going':
                                        cool_bonus = True
                                        is_cards = False
                                        delaney_talking(bonus[myBonus])
                                        spinDie()
                                        roll = True
                                    else:
                                        rectMode(CENTER)
                                        fill(244, 244, 244)
                                        rect(425, 425, 200, 100)
                                        # Bonus mark
                                        fill(0)
                                        textSize(24)
                                        text('Bonus Marks', 350, 400)
                                        textSize(12)
                                        text(bonus[myBonus], 355, 420)
                                        text('Click on the card to continue!', 330, 470)
                                else:
                                    rectMode(CENTER)
                                    fill(244, 244, 244)
                                    rect(425, 425, 200, 100)
                                    # Bonus mark
                                    fill(0)
                                    textSize(20)
                                    text('Announcements', 340, 400)
                                    textSize(12)
                                    text(announcements[myann], 355, 420)
                                    text('Click on the card to continue!', 330, 470)
                            elif fees_in_progress:
                                draw_button(playerTurn)
                                delaney_talking("You have to pay $150 GRAD\n FEES press RIGHT \nARROW to advance")
                            elif in_parking:
                                delaney_talking('You recieve $%s from\nStudent Parking! Click \nRIGHT ARROW to advance!' % parkingMoney)
                            elif purchase_in_progress == True:
                                delan = loadImage('delaney.png')
                                image(delan,250,350,300,300)
                                ph = places[plyersCoord['Player'+str(playerTurn)][2]]
                                if str(ph) == 'NIAGARA CATHOLIC':
                                    textSize(10)
                                else:
                                    textSize(12)
                                text('If you would like to\npurchase %s \nfor $%s click "buy"! \nOr click "pass"!' % (ph, str(positionsAndCosts[ph])), 235, 250)
                    set_coordinates()
                    show_dices()
            else:
                spinDie()

def Instructions():
    global chase_y, instruct
    instruct = True
    background(0)
    fill(255)
    for i in range(len(words)):
        textSize(20)
        if re.search(r'INSTRUCTIONS', words[i]):
            textSize(40)
        if re.search(r'PRESS SHIFT TO START - ENJOY YOUR GAME', words[i]):
            textSize(35)
        text(words[i],10,chase_y)
        chase_y+=30
    chase_y=30
def keyPressed():
    if instruct==True:
        if keyCode==DOWN:
            global stop, chase_y
            if len(words)!=0:
                new_words.append(words[0])
                words.remove(words[0])
            else:
                words.extend(new_words)
                del new_words[:]
            background(0)
            global stop
            if stop==0:
                global chase_y
                for i in range(len(words)):
                    textSize(20)
                    if re.search(r'INSTRUCTIONS', words[i]):
                        textSize(40)
                    if re.search(r'PRESS SHIFT TO START - ENJOY YOUR GAME', words[i]):
                        textSize(35)
                    text(words[i],10,chase_y)
                    chase_y+=30
                stop=1
            chase_y=30
            stop=0
def mouseWheel(event):
    global stop, chase_y
    if instruct==True:
        if len(words)!=0:
            new_words.append(words[0])
            words.remove(words[0])
        else:
            words.extend(new_words)
            del new_words[:]
        background(0)
        global stop
        if stop==0:
            global chase_y
            for i in range(len(words)):
                textSize(20)
                if re.search(r'INSTRUCTIONS', words[i]):
                    textSize(40)
                if re.search(r'PRESS SHIFT TO START - ENJOY YOUR GAME', words[i]):
                    textSize(35)
                text(words[i],10,chase_y)
                chase_y+=30
            stop=1
        chase_y=30
        stop=0
def podium():
    countingPosition=numberChar+1
    background(255)
    podiumImage=loadImage('Podium.png')
    img2=loadImage('mono.png')
    image(img2,400,300,800,600)
    image(podiumImage,400,300,400,400)
    if podiumNumberChar==2:
        dude=loadImage(str(podiumPlayers[1]))
        image(dude,400,150,150,150)
        dude1=loadImage(str(podiumPlayers[0]))
        image(dude1,300,250,150,150)
    elif podiumNumberChar==3:
        dude=loadImage(str(podiumPlayers[2]))
        image(dude,400,150,150,150)
        dude1=loadImage(str(podiumPlayers[1]))
        image(dude1,300,250,150,150)
        dude2=loadImage(str(podiumPlayers[0]))
        image(dude2,500,250,150,150)
    elif podiumNumberChar==4:
        dude=loadImage(str(podiumPlayers[3]))
        image(dude,400,150,150,150)
        dude1=loadImage(str(podiumPlayers[2]))
        image(dude1,300,250,150,150)
        dude2=loadImage(str(podiumPlayers[1]))
        image(dude2,500,250,150,150)
        dude3=loadImage(str(podiumPlayers[0]))
        image(dude3,600,350,150,150)
   
def draw():
    global x,y, sf, count,img,img1, die,inter, counter, dice, numberChar, playerTurn, char, equal, intructions, purchase_in_progress, kickedGuy, kick_in_progress, \
    delaney_forces, first,stopIt, secon,countDeaths, purchase_in_progress, instruct, img3, img4, img5, img6, countdown, big_x, three_in_row, sellShow, gameOver
    if podiums==True:
        podium()
    else:
        if startGame==False:
            if intructions and inter==True:
                background(0)
                Instructions()
            else:
                game_start()
        else:
            # infoshow is 2
            if sellShow == 1:
                selling()
            elif infoShow == 1:
                # but it is not getting here
                infoFunction()
            elif kick_in_progress:
                if countDeaths == (podiumNumberChar) or stopIt==True:
                    pass
                else:
                    countDeaths += 1
                if countDeaths==(numberChar) or gameOver:
                    gameOver = True
                    delaney_talking('The game is over!\nClick RIGHT ARROW \nto view podium!')
                    if len(podiumPlayers)==podiumNumberChar:
                        pass
                    else:
                        podiumPlayers.append(listOfImages[0])
                else:
                    text('Player %s is bankrupt, to \ncontinue with %s players \nclick RIGHT ARROW\nOtherwise, click Esc' % (str(kickedGuy), str(numberChar)), 235, 250)
                    stopIt=True
            elif countdown > 0:
                set_character()
                if big_x == 1:
                    image(first, 200, 200)
                elif big_x == 2:
                    image(secon, 200, 200)
                elif big_x == 3:
                    image(img3, 200, 200)
                elif big_x == 4:
                    image(img4, 200, 200)
                elif big_x == 5:
                    image(img5, 200, 200)
                elif big_x == 6:
                    image(img6, 200, 200)
                if big_x == 6:
                    big_x = 0
                else:
                    big_x += 1
                countdown -= 1
            elif three_in_row:
                delaney_talking("Third Double roll!\nGo to detention!\nPress RIGHT ARROW")
            elif house_in_progress == True:
                HousingFunction()
            elif force_to_sell:
                delan=loadImage('delaney.png')
                image(delan,250,350,300,300)
                textSize(12)
                text('You run out of money to\npay your debt!\nYou must sell a property!\nClick on Sell!', 235, 250)
                background_buttons(False, False, False, True, False)
            elif delaney_forces:
                sellShow = 1
            else:
                game()
    # sf.play()

def HousingFunction():
    set_character()
    delan=loadImage('delaney.png')
    image(delan,250,350,300,300)
    textSize(12)
    text('You own this property!\nClick houses to put a house \non it for $100! Or pass!', 235, 250)
    background_buttons(False, True, True, True, True)

def infoFunction():
    textSize(16)
    global infoShow, playerTurn
    exits=loadImage('exit.png')
    infoBox=loadImage('infoBox.png')
    image(infoBox,400,300,400,400)
    image(exits,500,400,100,100)
    fill(255)
    text('$'+str(playersAndMoney['Player'+str(playerTurn)]), 490,260)
    counted=280
    for i in range(0,len(playersAndProperty['Player'+str(playerTurn)])):
        text('- '+str(playersAndProperty['Player'+str(playerTurn)][i]),250,counted)
        counted+=20
    fill(0)

# This function is called anytime the user presses the selling button
def selling():
    global sellShow, playerTurn, talking, sellMouse, sellKey, indexer, playersAndProperty
    sellShow = 1
    mousyY = 520
    board=loadImage('mon.png')
    image(board,400,300,800,600)
    if talking == 1:
        fill(0)
        delan=loadImage('delaney.png')
        image(delan,250,350,300,300)
        textSize(12)
        cost = int(positionsAndCosts[places[indexer+1]] / 2)
        text("Are you sure you want\nto sell "+places[indexer+1]+'\n for $%s? Press y/n!' % cost, 235, 250)
        sellKey=1
    else:
        exits=loadImage('exit2.png')
        sellBox=loadImage('sellBox.png')
        image(sellBox,400,300,400,400)
        image(exits,500,425,100,100)
        for i in range(0,len(coordinateXList)):
            try:
                if (-10<mouseY<80 and 0<mouseX<115) or (520<mouseY<600 and -10<mouseX<115) or (-10<mouseY<80 and 685<mouseX<1000) or (520<mouseY<600 and 685<mouseX<1000):
                    pass
                elif (coordinateXList[i]-25) < mouseX < (coordinateXList[i]+25) and (coordinateYList[i]-55) < mouseY < (coordinateYList[i]+55) and 700>mouseX>115:
                    if -10<mouseY<500:
                        mousyY=40
                        indexer=(9-coordinateXList.index(coordinateXList[i]))+19
                    else:
                        mousyY=560
                        indexer=coordinateXList.index(coordinateXList[i])
                    if places[indexer+1] in playersAndProperty['Player'+str(playerTurn)]:
                        fill(0,127)
                        rect(coordinateXList[i]+5,mousyY,65,80)
                        sellMouse=1
                    else:
                        fill(255,0,0,127)
                        rect(coordinateXList[i]+5,mousyY,65,80)
                        sellMouse=0
    
                elif (coordinateXList[i]-55) < mouseX < (coordinateXList[i]+55) and (coordinateYList[i]-25) < mouseY < (coordinateYList[i]+25) and (mouseX<115 or mouseX>700):
                    if 0<mouseX<300:
                        mousyY=55
                        indexer=coordinateYList.index(coordinateYList[i])
                    else:
                        mousyY=745
                        indexer=(29-coordinateYList.index(coordinateYList[i]))+19
                    if places[indexer+1] in playersAndProperty['Player'+str(playerTurn)]:
                        fill(0,127)
                        rect(mousyY,coordinateYList[i]+5,110,50)
                        sellMouse=1
                    else:
                        fill(255,0,0,127)
                        rect(mousyY,coordinateYList[i]+5,110,50)
                        sellMouse=0
            except IndexError:
                break

# This function occurs after the turn is changed and shows the die image
def spinDie():
    global roll, actualTurn,infoShow, sellShow, dying_in_progress
    dying_in_progress = False
    draw_button(playerTurn)
    if infoShow != 1 and sellShow != 1:
        infoShow=2
        sellShow=2
        diceImage=loadImage('dice.png')
        imageMode(CENTER)
        image(diceImage,400,300,100,100)
        if is_in_jail['Player' + str(playerTurn)] != False:
            delaney_talking("You're locked in detention!\nGet double to go free!")
    elif infoShow == 1:
        infoFunction()
    elif sellShow == 1:
        selling()
    img1=loadImage(str(char))
    roll=True

# Chossing character
def chooseChar():
    global char, numberChar, c,listOfImages
    textSize(50)
    text('CHOSE CHARACTER',150,150)
    strokeWeight(4)
    stroke(255)
    fill(0)
    rectMode(CENTER)
    rect(150,300,125,125)
    character=loadImage('bulldog.png')
    image(character,150,300,125,125)
    rect(315,300,125,125)
    character2=loadImage('bucanners.png')
    image(character2,315,300,115,115)
    rect(480,300,125,125)
    character3=loadImage('bolt.png')
    image(character3,480,300,125,125)
    rect(645,300,125,125)
    character4=loadImage('eagle.png')
    image(character4,645,300,115,115)
    strokeWeight(4)
    # If the user picks bulldog
    if 'bulldog.png' in players.values():
        tint(167)
        stroke(0)
        rect(150,300,125,125)
        image(character,150,300,125,125)
    else:
        if 85<=mouseX<=215 and 255<=mouseY<=365:
            textSize(15)
            text('SIR. W.CHURCHILL',90,385)
            textSize(50)
            tint(167)
            noTint()
            stroke(204, 102, 0)
            rect(150,300,125,125)
            image(character,150,300,125,125)
            if mouseButton==LEFT:
                if 'bulldog.png' in players.values():
                    pass
                else:
                    char='bulldog.png'
                    players['Player'+str(c)]=char
                    players2['Player'+str(c)]=char
                    plyersCoord['Player'+str(c)]=[x,y,0]
                    is_in_jail['Player' + str(c)] = False
                    playersAndMoney['Player'+str(c)] = 1500
                    playersAndProperty['Player'+str(c)] = []
                    playersAndBuses['Player'+str(c)] = 0
                    c+=1
                    listOfImages.append(char)
                    strokeWeight(0)
    # Otherwise if the user picks bucanners
    if 'bucanners.png' in players.values():
            tint(167)
            stroke(0)
            rect(315,300,125,125)
            image(character2,315,300,115,115)
    else:
        if 250<=mouseX<=380 and 255<=mouseY<=365:
            textSize(15)
            text('BEAMSVILLE',270,385)
            textSize(50)
            noTint()
            stroke(204, 102, 0)
            rect(315,300,125,125)
            image(character2,315,300,115,115)
            if mouseButton==LEFT:
                if 'bucanners.png' in players.values():
                    pass
                else:
                    char='bucanners.png'
                    players['Player'+str(c)] = char
                    players2['Player'+str(c)]=char
                    plyersCoord['Player'+str(c)] = [x,y,0]
                    is_in_jail['Player'+str(c)] = False
                    playersAndProperty['Player'+str(c)] = []
                    playersAndMoney['Player'+str(c)] = 1500
                    playersAndBuses['Player'+str(c)] = 0
                    c += 1
                    listOfImages.append(char)
                    strokeWeight(0)
    # Otherwise if the user picks bolt
    if 'bolt.png' in players.values():
            tint(167)
            stroke(0)
            rect(480,300,125,125)
            image(character3,480,300,125,125)
    else:
        if 415<=mouseX<=545 and 255<=mouseY<=365:
            textSize(15)
            text('BLESSED TRINITY',420,385)
            textSize(50)
            noTint()
            stroke(204, 102, 0)
            rect(480,300,125,125)
            image(character3,480,300,125,125)
            if mouseButton==LEFT:
                if 'bolt.png' in players.values():
                    pass
                else:
                    char='bolt.png'
                    players['Player'+str(c)]='bolt.png'
                    players2['Player'+str(c)]='bolt.png'
                    is_in_jail['Player'+str(c)] = False
                    playersAndProperty['Player'+str(c)] = []
                    plyersCoord['Player'+str(c)]=[x,y,0]
                    playersAndMoney['Player'+str(c)] = 1500
                    playersAndBuses['Player'+str(c)] = 0
                    c+=1
                    listOfImages.append(char)
                    strokeWeight(0)
    # Otherwise if the user picks eagle
    if 'eagle.png' in players.values():
            tint(167)
            stroke(0)
            rect(645,300,125,125)
            image(character4,645,300,115,115)
    else:
        if 580<=mouseX<=710 and 255<=mouseY<=365:
            textSize(15)
            text('GRIMSBY SECONDARY',565,385)
            textSize(50)
            noTint()
            stroke(204, 102, 0)
            rect(645,300,125,125)
            image(character4,645,300,115,115)
            if mouseButton==LEFT:
                if 'eagle.png' in players.values():
                    pass
                # Entering the eagle as part of the players
                else:
                    char='eagle.png'
                    players['Player'+str(c)]='eagle.png'
                    players2['Player'+str(c)]='eagle.png'
                    plyersCoord['Player'+str(c)]=[x,y,0]
                    playersAndMoney['Player'+str(c)] = 1500
                    playersAndProperty['Player'+str(c)] = []
                    is_in_jail['Player'+str(c)] = False
                    playersAndBuses['Player'+str(c)] = 0
                    c += 1
                    listOfImages.append(char)
                    strokeWeight(0)
    noTint()
    
def startIt():
    global startGame
    startGame = False
    
# Code finished so far!


import time
import random
import math

# game function
success = 0
wins = 0
myHealth = 50
experience = 0
endgame = 0
myMaxAttack = 8
myMinAttack = 4
minstage = 1
maxstage = 50

myMaxHealth = 30
myWeapVal = 0
myArmorVal = 0

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Welcome to the cavern of secrets!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(1)

print(r'''
                         __________
                      .~#########%%;~.
                     /############%%;`\
                    /######/~\/~\%%;,;,\
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
 X# \.X        @#%,.@                  @#%,.@        X./  #
  ##  X          @#%,.@              @#%,.@          X   #
, "# #X            @#%,.@          @#%,.@            X ##
   `###X             @#%,.@      @#%,.@             ####'
  . ' ###              @#%.,@  @#%,.@              ###`"
    . ";"                @#%.@#%,.@                ;"` ' .
      '                    @#%,.@                   ,.
      ` ,                @#%,.@  @@                `
                          @@@  @@@  
''')

class weapon(object):
    def __init__(self, name, description, minAttack, maxAttack, value):
        self.name = name
        self.description = description
        self.minAttack = minAttack
        self.maxAttack = maxAttack
        self.value = value
    def __str__(self):
        return "You wield the {}, {}, with Max Attack of {}\n".format(self.name, self.description, self.maxAttack)
       
    def obtainWeapon(self):
        print(" ")
        print("!!! NEW WEAPON acquired. You have obtained the {}, {},  Max Attack increased by {}!!!".format(self.name, self.description, self.maxAttack))
        global myWeapVal
        global myMaxAttack
        global myMinAttack
        myMaxAttack = myMaxAttack + self.maxAttack
        myMinAttack = myMaxAttack/2.5
        myWeapVal = self.value

class armor(object):
    def __init__(self, name, description, health, value):
        self.name = name
        self.description = description
        self.health = health
        self.value = value
        
    def __str__(self):
        return "You are wearing the {}, {}, with health buff of {}\n".format(self.name, self.description, self.health)
       
    def obtainArmor(self):
        print(" ")
        print("!!! NEW ARMOR acquired. You have obtained the {}, {}.  Health increased by {}!!!".format(self.name, self.description, self.health))
        global myArmorVal
        global myMaxHealth
        myMaxHealth = myMaxHealth + self.health
        myArmorVal = self.value
        


        
#BattleAx = weapon("BattleAx", "forged from the strongest steel", 27, 82, 4)
#WarHammer = weapon("War Hammer", "instrument of doom", 35, 241, 3)
#CrossBow = weapon("CrossBow", "", 12, 24, 2)
#SlingShot = weapon("Sling Shot", "precise if not powerful", 6, 13, 1)

time.sleep(2)
print(". . . . ")

print("You enter the Cavern of Secrets in search of the mighty Red Dragon, armed with only your fists and courage. Your quest begins now!")
time.sleep(1)


print(". . . . ")


class enemy(object):
    def __init__(self, name, health, minAttack, maxAttack, approach, exp, exppercent, image,endgame):
        self.name = name
        self.health = health
        self.minAttack = minAttack
        self.maxAttack = maxAttack
        self.approach = approach
        self.exp = exp
        self.exppercent = exppercent
        self.image = image
        self.endgame = endgame

    def describeEnemy(self):
        print(self.image)
        print("{} has {} health and {} max Attack".format(self.name, self.health, self.maxAttack))


    def startFight(self):
        global myMaxAttack
        global myMaxHealth
        print(" ")
        time.sleep(2)
        print(self.approach)
        time.sleep(1)
        print(" ")
        self.describeEnemy()
        time.sleep(1)
        print("    You have",myMaxHealth,"health and",myMaxAttack,"max Attack")
        print()

# list of enemies
Blob = enemy("Red Blob", 10, 1, 3, "An amorphous blob sneaks up on you!",5,1.05,'',1)
Blob.image = r'''

   __///\\\__
   |  0  0  \
   \   ____  \
    \ (____)  \
    /         /
 __/_______ _/

 '''

GiantBlob = enemy("Giant Blob", 8000, 100, 200, "The monstrous Giant Blob attacks!",100,1.10,'',16)
GiantBlob.image = r'''

    ______///\\\_____
    |      0  0      \
    \      ____       \
     \    (____)       \
     /                 /
 ___/_________________/

 '''

Spider = enemy("Spider", 30, 8, 10, "You walk into a spider web!",10,1.05,'',11)
Spider.image =r'''

              (
               )
              (
        /\  .-"""-.  /\
       //\\/  ,,,  \//\\
       |/\| ,;;;;;, |/\|
       //\\\;-"""-;///\\
      //  \/   .   \/  \\
     (| ,-_| \ | / |_-, |)
       //`__\.-.-./__`\\
      // /.-(() ())-.\ \\
     (\ |)   '---'   (| /)
      ` (|           |) `
        \)           (/

'''
Turtle = enemy("Iron Turtle", 120, 4, 5, "This turtle is slow but has a deceptively hard shell.",10,1.05,'',12)
Turtle.image = r'''
                          ___-------___
                         _-~~             ~~-_
                      _-~                    /~-_
   /^\__/^\         /~  \                   /    \
 /|  O|| O|        /      \_______________/        \
| |___||__|      /       /                \          \
|          \    /      /                    \          \
|   (_______) /______/                        \_________ \
|         / /         \                      /            \
 \         \^\\         \                  /               \     /
   \         ||           \______________/      _-_       //\__//
     \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
       ~-----||====/~     |==================|       |/~~~~~
        (_(__/  ./     /                    \_\      \.
               (_(___/                         \_____)_)

'''

Elephant = enemy("Elephant", 100, 9, 15, "A giant elephant charges at you!", 50,1.1, '',2)
Elephant.image = r'''

                      
                          .. ..oooo.....ooo...
                    .odSS4PYYYSSOOXXXXXXXXXOodbgooo.
                   /SSYod$$$$SSOIIPXXXXXXXXXYYP.oo.*b.
                  ($$Yd$$$$SSSOII:XXXXXXXX:IIoSSS$$b.Y,
                   \Yd$$$$SSSOII:XXXXXXXXXX:IIOOSSS$$$b\
                    d$$$$SSSOOI:XP"YXXXXXXXX:IIOOSSSS$$$\
                    Y$$$SSSOOII:XbdXXXXXP"YX:IIOOOSS$$$$)
                    'Y$$$SSSOI:XXXXXXXXXbodX:IIOOSS$$$$$/
                     "Y$$$SSSOI(PoTXXXXXTo)XXIIOOOSS$$$*'
                       ""*Y$S(((PXXXXXXXY))dIIOSSS$$dP'
                          "*'()P;XXXXXXXXY)IIOSSS$P".oS,
                          (S'(P;XXXXXXXP;Y)XXYOP".oSSSSb
                         (S'(P;'XXXXXXX';Y).ooooSSSSSSSS)
                         (S'(P;'XXXXXXP';Y).oSSSSSSSSSSSP
                         (SS'Y);YXXXXX';(Y.oSSSSSSSSSSSSP
                          YSS'Y)'YXXX".(Y.oSSP.SSSSSSSSY
                           YSS'"" XXX""oooSSP.SSSSSSSSY
                           SSSSSS YXXX:SSSSP.SSSSSSSSY
                           SSSSSP  YXb:SSSP.S"SSSSSSP
                           S(OO)S   YXb:SY    )SSSSS
                           SSSSO    )YXb.I    ISSSSP
                           YSSSY    I."YXXb   Y(SS)I
                           )SSS(    dSSo.""*b  YSSSY
                           OooSb   dSSSSP      )SSS(
                                   dSSSY       OooSS
                                   OooSP                 
                                

'''

Ogre = enemy("Blood Ogre", 400, 10, 25, "A bloodthirsty ogre blocks your path! He wields a mighty War Hammer...",100,1.20,'',3)
Ogre.image = r'''
                           __,='`````'=/__
                          '//  (o) \(o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \
                   /      ,               \,-`\`_,-`\_,..--'\
                  ,`    ,/,              ,>,   )     \--`````\
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo

'''

Serpent = enemy("Serpent", 300, 8, 80, "What is that hissing sound??",70,1.1,'',0)
Serpent.image = r'''
      _    _
   ,-(|)--(|)-.
   \_   ..   _/
     \______/
       V  V                                  ____
       `.^^`.                               /^,--`
         \^^^\                             (^^\
         |^^^|                  _,-._       \^^\
        (^^^^\      __      _,-'^^^^^`.    _,'^^)
         \^^^^`._,-'^^`-._.'^^^^__^^^^ `--'^^^_/
          \^^^^^ ^^^_^^^^^^^_,-'  `.^^^^^^^^_/ 
           `.____,-' `-.__.'        `-.___.'   

'''

Rhyno = enemy("Angry Rhino", 1000, 12, 50, "You accidentally awaken a sleeping ryhno...",60,1.2,'',14)
Rhyno.image = r'''


                              ,-.             __
                             ,'   `---.___.---'  `.
                           ,'   ,-                 `-._
                         ,'    /                       \
                      ,\/     /                        \\
                  )`._)>)     |                         \\
                  `>,'    _   \                  /       |\
                    )      \   |   |            |        |\\
           .   ,   /        \  |    `.          |        | ))
           \`. \`-'          )-|      `.        |        /((
            \ `-`   a`     _/ ;\ _     )`-.___.--\      /  `'
             `._         ,'    \`j`.__/        \  `.    \
               / ,    ,'       _)\   /`        _) ( \   /
               \__   /        /nn_) (         /nn__\_) (
                 `--'           /nn__\             /nn__\

'''
Snail = enemy("Poison Snail", 500, 400, 500, "A snail inches forward. Is it stronger than it appears?",250,1.2,'',0)
Snail.image = r'''
           eed*"""""""""**be,
        .d"                  "b.
      .d                        b.
    ."         ..eeeeee..         ".
   P        z$*"        "*e.        9.
  A       d"                "b       A
 J       J    .e*""""""%c     A       L
A       A    d"          $     L      A
#       %   d      d**y  'L    %      #
#       %   $     $ ,, Y  .$   %      #       _ _ 
#       %   $     *  """   F   %      #      (@)@)
#       V    4.    $.   .e"    Y      #        % %
#        $    *.    """"     .Y      V         $ $
#        'b     "b.      ..e*       Y         .eeee
V         '$      ""eeee""        eP         A     %
 Y         eb                ..d*"         _#    O %
 I    _e%*""""*$ee......ee$*"eeeeeeeezee$**"       $
  V ,"                                            B
  J'                                        _,e=""
.'#######################################DWB''
'''


BlueDragon = enemy("Blue Dragon", 10000, 25, 300, "Suddenly, the Blue Dragon appears...",500,1.2,'',0)
BlueDragon.image = r'''

                                        $,  $,     ,            
                                        "ss.$ss. .s'     
                                ,     .ss$$$$$$$$$$s,              
                                $. s$$$$$$$$$$$$$$`$$Ss       
                                "$$$$$$$$$$$$$$$$$$o$$$       ,       
                               s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s  
                              s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,     
                              s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"   
                             s$$$$$$$$$$'         `"""ss"$"$s""      
                             s$$$$$$$$$$,              `"""""$  .s$$s
                             s$$$$$$$$$$$$s,...               `s$$'  `
                         `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-
                           `""""$$$$$$$$$$$$$$$$$$$$#####$$$$$$"     $.$'
                                 "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|
                                  "$$$$$$$$$$$$$$$$$$$$$$$$##s    .$$" $ 
                                   $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `
                                  $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""' 
                             ,   ,"     '  $$$$$$$$$$$$$$$$####s  
                             $.          .s$$$$$$$$$$$$$$$$$####"
                 ,           "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"
                 $           .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"
                 Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""
                  "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"
           ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'
           $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,
           $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$
            "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$
              $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.
   )          $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.
  ((          $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$ 
  ) \         $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
 (   )        $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$'
 )  ( (       $$"$$$$$$$$$$$#####.$$$$$###'                .###$$$$$$$$$$"
 (  )  )   _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$
 ) (  ( \.         "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"
(   )$ )  )        ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"        
(   ($$  ( \     _sS"  `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,       
 )  )$$$s ) )  .      .   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'  `$$   
  (   $$$Ss/  .$,    .$,,s$$$$$$##S$$$$$$$$$$$$$$$$$$$$$$$$S""        ' 
    \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$        `$$.        `$$.
        `"S$$$$$$$$$$$$$$$$$#"      $          `$          `$
            `"""""""""""""'         '           '           '
 
'''


RedDragon = enemy("Red Dragon", 25000, 200, 1000, "Here comes the mighty Red Dragon!",1000,10,'',99)
RedDragon.image = r'''

                                                 /===-_---~~~~~~~~~------____
                                                |===-~___                _,-'
                 -==\\                         `//~\\   ~~~~`---.___.-~~
             ______-==|                         | |  \\           _-~`
       __--~~~  ,-/-==\\                        | |   `\        ,'
    _-~       /'    |  \\                      / /      \      /
  .'        /       |   \\                   /' /        \   /'
 /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _)   ;  ),   __--~~
                    '~~--_/      _-~/-  / \   '-~ \
                   {\__--_/}    / \\_>- )<__\      \
                   /'   (_/  _-~  | |__>--<__|      |
                  |0  0 _/) )-~     | |__>--<__|     |
                  / /~ ,_/       / /__>---<__/      |
                 o o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `

'''
#end list of enemies



def fight(enemy):
    global maxstage
    global minstage
    global myHealth
    global myMaxHealth
    myHealth = myMaxHealth
    global myMaxAttack
    global myMinAttack
    global experience
    enemyHealth = enemy.health
    global endgame
    global myWeapVal

    ch1 = str(input("Do you fight? [y/n]: "))

    if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes',""]:

        while myHealth > 0 and enemyHealth > 0:

        
            myAttack = random.randint(int(myMinAttack),int(myMaxAttack))
            enemyAttack = random.randint(enemy.minAttack, enemy.maxAttack)
            myHealth = myHealth - enemyAttack
            if myHealth< 0:
                myHealth = 0
        
            enemyHealth = enemyHealth - myAttack

            if enemyHealth< 0:
                enemyHealth = 0
            print("FIGHT!--------->")
            time.sleep(1)
            print("you took",enemyAttack,"damage and your opponent took",myAttack,"damage.")
            print("*****your health is",myHealth,"and your enemy's health is",enemyHealth)
            time.sleep(1)
       


        if myHealth <1:
            print("---You lose, try again---")
            
        else:    
            experience = experience + enemy.exp
            print("|---You win. Experience increased by {} to {}. Health restored.---|".format(enemy.exp, experience))
            myMaxAttack = math.ceil(myMaxAttack* enemy.exppercent)
            myMaxHealth = int(myMaxHealth*enemy.exppercent)
            global wins
            wins = wins + 1
            print("{} enemies have been defeated".format(wins))       
            endgame = enemy.endgame
            drop(endgame)
               
    else:
        print("You ran away!")



def drop(dropvalue):
    global myWeapVal
    global myArmorVal
    global myHealth
    setstage(dropvalue)
    if dropvalue == 3 and myWeapVal <3:
        myWeapon = weapon("War Hammer", "instrument of doom", 50, 72, 3)
        myWeapon.obtainWeapon()
        time.sleep(2)
        print(". . . . ")
    if dropvalue == 2 and myWeapVal<2:
        myWeapon = weapon("Dagger", "a blade forged from the purest steel", 12, 24, 2)
        myWeapon.obtainWeapon()
        time.sleep(2)
        print(". . . . ")
    if dropvalue == 1 and myWeapVal<1:
        myWeapon = weapon("Sling Shot", "precise if not powerful", 4, 6, 1)
        myWeapon.obtainWeapon()
        time.sleep(2)
        print(". . . . ")


    if dropvalue == 16 and myArmorVal <16:
        myArmor = armor("Golden Helmet", "completing the ultimate suit of armor", 500, 14)
        myArmor.obtainArmor()
        time.sleep(2)
    
    if dropvalue == 15 and myArmorVal <15:
        myArmor = armor("Golden Shield", "that can block even the Dragon's fiery breath", 300, 14)
        myArmor.obtainArmor()
        time.sleep(2)
        print(". . . . ")    
    if dropvalue == 14 and myArmorVal <14:
        myArmor = armor("Golden Chain Mail", "virtually impenetrable", 200, 14)
        myArmor.obtainArmor()
        time.sleep(2)
        print(". . . . ")
    if dropvalue == 12 and myArmorVal <12:
        myArmor = armor("Bronze Helmet", "heavy and durable", 28, 12)
        myArmor.obtainArmor()
        time.sleep(2)
        print(". . . . ")
    if dropvalue == 11 and myArmorVal<11:
        myArmor = armor("Old Wooden Shield", "which has seen better days, but is better than nothing", 5, 11)
        myArmor.obtainArmor()
        time.sleep(2)
        print(". . . . ")
    if endgame == 99:
        print("You have slayed the mighty dragon! Your quest is over!")
        print("{} enemies have been defeated".format(wins +1))
        print("Experience earned was {}".format(experience))
        print("Thanks for playing!")
        myHealth = 0 #end game


def setstage(dropvalue):
    global minstage
    global maxstage
    if dropvalue == 3 and myWeapVal <3:
        minstage = 50
        maxstage = 120
       
    if dropvalue == 2 and myWeapVal <2:
        minstage = 20
        maxstage = 80

Blob.startFight()
fight(Blob)

while myHealth > 0:
    randomFight = random.randint(minstage,maxstage)
    if randomFight >=1 and randomFight<= 15:
        Blob.startFight()
        fight(Blob)
    if randomFight >=16 and randomFight<= 30:
        Spider.startFight()
        fight(Spider)
    if randomFight >=36 and randomFight<= 42:
        Turtle.startFight()
        fight(Turtle)
    if randomFight >=46 and randomFight<= 54:
        Elephant.startFight()
        fight(Elephant)
    if randomFight >=55 and randomFight<= 65:
        Ogre.startFight()
        fight(Ogre)
    if randomFight >=66 and randomFight <= 74:
        Serpent.startFight()
        fight(Serpent)
    if randomFight >=75 and randomFight <= 85:
        Rhyno.startFight()
        fight(Rhyno)
    if randomFight >=86 and randomFight <= 92:
        Snail.startFight()
        fight(Snail)
    if randomFight >=93 and randomFight <= 100:
        GiantBlob.startFight()
        fight(GiantBlob)
    if randomFight >=100 and randomFight <= 110:
        BlueDragon.startFight()
        fight(BlueDragon)
    if randomFight >=111 and randomFight <= 118:
        RedDragon.startFight()
        fight(RedDragon)
            

    time.sleep(2)
    print(". . . . ")
    


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Norah", color = "#DC143C")
define a = Character("Andrew", color = "#00FFFF")
define b = Character("Broker", color = "#FF8C00")
define d = Character("Dr Lee", color = "#0096FF")
#define p = Character("Prediction", color = "#273746")

image picture_1 = "bg thedoor.png"
image picture_2 = "andrewroom.png"
image picture_3 = "bg withdialogue"
image picture_4 = "outside.png"
image picture_5 = "kitchenroom.png"
image picture_6 = "blackbg.png"
image picture_7 = "phoneCallAndrew.png"
image picture_8 = "phoneCallFather.png"
image picture_9 = "doorknob1.png"
image picture_10 = "doorknob2.png"
image picture_11 = "doorknob3.png"
image picture_12 = "door-perspective.png"
image picture_13 = "door_chair.png"
image picture_14 = "bluebg.png"
image picture_15 = "phone1.png"
image picture_16 = "door_bg-woknob.png"
image picture_17 = "titlebck.png"






#image picture_2 = im.Scale("roomtest", 2402*1280/2402, 1345*720/1345)
#image picture_3 = im.Scale("withdialogue", 2400*1280/2400, 1341*720/1341)

image andrew normal = "andrew_bw.png"
image broker normal = "broker_bw.png"
image norah normal = "norah_bw.png"
image dad normal = "dad.png"

image andreww normal = "andrew720.png"
image norahh normal = "nora720.png"
image andrewF normal = "andrew_flipped.png"
image norahF normal = "noraflipped.png"
image norahB normal = "noraback.png"

image norahH normal = "handdoor.png"

image knob normal = "doorknob.png"

default norahAnxious = 0
default andrewSupport = 0
default norahAnxiousTimes = 0
default andrewSupportTimes = 0

transform left:
    xpos  0.05 
    ypos 0.333
    
transform left2:
    xpos  0.05 
    ypos 0.356
    
transform leftA:
    xpos  0.05 
    ypos 0.218
   
transform right:
    xpos  0.7 
    ypos 0.218
    
transform rightB:
    xpos  0.7 
    ypos 0.230    
    
transform right2:
    xpos  0.7 
    ypos 0.333

transform center2:
    xpos  0.3 
    ypos 0.333
    
transform holds:
    xpos  0.21 
    ypos 0.371
    
transform theHandle0:
    xpos  0.379 
    ypos 0.499
    rotate 1
    



transform theHandle:
    xpos  0.379 
    ypos 0.499
    rotate 1
    easeout 1.0 
    rotate 1
    easeout 1.0 
    rotate 1
    easeout 1.0 
    rotate 1
    easeout 1.0 
    rotate 6
    easeout 0.7 
    rotate 10
    easeout 0.6 
    rotate 12
    easeout 0.5 
    rotate 18
    easeout 0.5 
    rotate 21
    easeout 0.8 
    rotate 26
    easeout 0.1 
    rotate 21
    easeout 0.1 
    rotate 17
    easeout 0.1 
    rotate 13
    easeout 0.2 
    rotate 9
    easeout 0.1 
    rotate 3

  

    repeat


#image norah normal = im.Scale("norah720.png", 377/2, 1280/2)



#"audio/TheDoor_Sample1.mp3"
#"audio/GoodNight.mp3"



# The game starts here.

label start:
    
    stop music
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    
    
    jump Ep1_S1_Apartment1

    # This ends the game.
    return

label Ep1_S1_Apartment1:
    
    scene picture_6
    
    $norahAnxious = 0
    $andrewSupport = 0
   

    play music "audio/ChapterTheme.mp3" loop 
    
    
    "{cps=25}Chapter 1: The Apartment{/cps}"
    "{cps=25}August 16, 2023. Tallinn, Estonia{/cps}"
    "{cps=25}3:52 PM{/cps}"
    

    play music "audio/SuspenseMusic.mp3" loop fadein 0.5
    
    
    
    
    #"hey"
    scene picture_2
    show broker normal at center
    b "Hello guys, so... Andrew and Norah, right?" 
        
    hide broker normal at center

    show andrew normal at right
    a "Yes, hi."
    hide andrew normal at right

    show norah normal at left
    n "Hello."
    hide norah normal at left

    show broker normal at center
    b "Nice to meet you!"
    hide broker normal at center

    show andrew normal at right
    a "Nice to meet you, too. Thanks!"
    hide andrew normal at right

    show broker normal at center
    b "So feel free to take a look at the apartment. I know you came here straight from the airport, you must be tired. You can drink some water; I even made coffee if you want."
    hide broker normal at center

    show andrew normal at right
    a "Thank you a lot. That is very appreciated. At the airport, though, we had already had a cup of coffee. But I'm sure I'll drink it later. I am really a coffeeholic."
    hide andrew normal at right

    show broker normal at center
    b "Okay, so let me quickly show you an apartment. I showed it to you via video call, but I believe this is new to Norah."
    hide broker normal at center

    show norah normal at left
    n "Yes. But Andrew showed me the pictures."
    hide norah normal at left

    show broker normal at center
    b "Everything is just as it is in the listing and as I showed through the video call. It's a really comfortable apartment. As you can see, the bedroom is here, and the next room is designed to function as both a bedroom and a kitchen."
    hide broker normal at center

    show andrew normal at right
    a "Yes, I see. It's very convenient and comfortable. Norah?" 
    hide andrew normal at right

    jump choicesLabel1

label choicesLabel1:
    scene picture_2
    play music "audio/SuspenseMusic - mini.mp3" loop
    show norah normal at left

    menu choices1:
        "Yes, looks really comfy. Thanks.": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump broker0
        "Is there a washer in the bathroom?":#2
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            jump broker2
        "Is there an air conditioner?":#3
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            jump broker3
   
label choicesLabel2:
    scene picture_2
    play music "audio/SuspenseMusic - mini.mp3" loop fadein 0.5
    show norah normal at left
    menu choices2:
        "What about the refrigerator?":#4
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            $norahAnxious += 10
            jump broker4
        "Do you have a TV?":#5
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            $norahAnxious += 10
            jump broker5
        "Thanks, I don't have any other questions.": #6
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump broker0


label choicesLabel4:
    scene picture_2
    show norah normal at left

    menu choices3:
        "What is the average amount of utilities?":#7
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            $norahAnxious += 10
            jump broker6
        "We walked about 10 minutes from the bus stop to get here. Is it the closest bustop?":#8
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            $norahAnxious += 10
            jump broker7
        "Thanks, I don't have any other questions.": #6
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump broker0

label choicesLabel5:
    scene picture_2
    show norah normal at left

    menu choices4:    
        
        "What is the closest grocery?":#9
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            jump broker8
        "What about the neighbours?":#10
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            jump broker9
        "Thanks, I don't have any other questions.": #6
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump broker0

label broker0:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "So, if there is no more question and you are ready to sign. I can give the lease right now."
    hide broker normal at center

    show andrew normal at right
    a "Yes, we are ready, aren't we?!"
    hide andrew normal at right

    jump choicesLabel3

label broker2:
    scene picture_4
    play music "audio/SuspenseMusic.mp3" loop 
    #show broker normal at center
    b "Unfortunately, there is no washing machine. However, the laundry is directly above the building, and it is significantly cheaper if you purchase a 6-month laundry card. I told Andrey he could share the prices with you."
    b "Any other question?"
    hide broker normal at center

    jump choicesLabel2

label broker3:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "No, there is not. But to be honest, you don't even need it. Because the temperature is usually around 23 degrees Celsius at most, but if you really need air conditioning, simply open a window."
    b "Any other question?"
    hide broker normal at center

    jump choicesLabel2

label broker4:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "Yes, there is a refrigerator in the kitchen. But it's not too big. Fortunately, not too small too."
    b "Any other question?"
    hide broker normal at center

    jump choicesLabel4
    

label broker5:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "No, we don't have a TV here. But if you really need a TV, you can rent it or buy second-hand TVs. Facebook's Marketplace is popular here."
    b "Any other question?"
    hide broker normal at center

    jump choicesLabel4

label broker6:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "So, you must pay for electricity, water, gas, internet, trash, and building maintenance. There is also a small charge for elevator and cleaning services. "
    b "So, it should be around 150 euros in the winter and 80 euros in the summer. I mailed Andrew the previous utility bills."
    b "Any other question?"
    hide broker normal at center

    jump choicesLabel5

label broker7:
    scene picture_4
    play music "audio/SuspenseMusic.mp3" loop 
   # show broker normal at center
    b "And that is because you came from the airport! However, if you want to get to the city centre or the university, you can take the tram or trolley bus from the stop behind this building. It takes approximately 3-4 minutes to get to the bus stop. So it's not that far."
    b "Any other question?"
    hide broker normal at center

    jump choicesLabel5

label broker8:
    scene picture_4
    play music "audio/SuspenseMusic.mp3" loop 
   # show broker normal at center
    b "It is located in the same building as a laundry. So all you have to do is cross the street."
    b "Any other question?"
    hide broker normal at center

    jump choicesLabel1

label broker9:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "There are quiet and friendly people."
    b "Any other question?"
    hide broker normal at center

    jump choicesLabel1

label choicesLabel3:
    show norah normal at left

    play music "audio/SuspenseMusic - mini.mp3" loop 
    menu choicesLease:
        "Give me a second. I will quickly read it.":
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            jump broker10 #"Sure""
        "Yes! Let's sign!":
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump Ep1_S1_Apartment2

label choicesLabelHouseRules:
    play music "audio/SuspenseMusic - mini.mp3" loop 
    show norah normal at left

    menu choicesHouseRules:
        "So, the only thing that is prohibited is smoking. Can I assume that pets are allowed?":#11
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            jump broker11
        "Three months deposit?":#12
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            $norahAnxious += 10
            jump broker12
        "When should we send the money?":#13
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            jump broker13
        "Hmm... Okay, Let's sign!":
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump Ep1_S1_Apartment2

label broker10:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "Sure" #10
    hide broker normal at center

    jump choicesLabelHouseRules

label broker11:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "Yes, technically. Pets are allowed. But Andrew mentioned that you don't have any pets. Anyway... if you intend to have a pet, notify the owner before bringing it into the apartment."
    hide broker normal at center

    jump choicesLabelHouseRules

label broker12:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "Yes, we had a previous incident with the tenants. There were students, and they threw a party and trashed the place. After that, the owner decided to increase the amount of the deposit. I can't do anything with this."
    hide broker normal at center

    jump choicesLabelHouseRules

label broker13:
    play music "audio/SuspenseMusic.mp3" loop 
    show broker normal at center
    b "As you can see, you need to send the rent for the next month on the 25th at the latest."
    hide broker normal at center

    jump choicesLabelHouseRules

label Ep1_S1_Apartment2:

    scene picture_2
    play music "audio/SuspenseMusic.mp3" loop 

    show broker normal at center
    b "Then, congrats on your new apartment! By the way, there is a study desk, which we can remove if it bothers you."
    hide broker normal at center
    
    show andrew normal at right
    a "Oh, no. The-other-way-round! That is what I need! I am doing my PhD in Applied Physics. So the desk for me is even more important than the bed."
    hide andrew normal at right

    show broker normal at center
    b "Huh, okay. Then that's all."
    hide broker normal at center

    play music "audio/ChapterTheme.mp3" loop 
    scene picture_1
    show norahB normal at center
    n "The peephole is too high."
    hide norahB normal at center

    show broker normal at right
    b "Sorry?"
    hide broker normal at right

    show norah normal at center
    n "Oops, I was thinking loudly. Sorry. I was saying that the peephole is very high. I can't reach it."
    hide norah normal at center

    show broker normal at right
    b "Yes, people in our country are tall, which is probably why the peephole was raised."
    hide broker normal at right

    show andrewF normal at leftA
    a "Hmm, interesting."
    hide andrewF normal at leftA

    play music "audio/SuspenseMusic.mp3" loop 
    scene picture_2
    show broker normal at center
    b "Okay, then I will leave. From this moment on, you keep the touch with the owner. I will send his number by email. And the rest is according to the lease contract. Take care, bye."
    hide broker normal at center

    show andrewF normal at leftA
    a "Thanks."
    hide andrewF normal at leftA

    show norahF normal at right2
    n "Thanks, bye!"
    hide norahF normal at right2
    
    jump Ep1_S2_Kitchen
    

label Ep1_S2_Kitchen:
    
    scene picture_6 

    play music "audio/ChapterTheme.mp3" loop 
    
    
    "{cps=25}A few hours later{/cps}"
    
   
    jump Ep1_S2_CofeeMachine

label Ep1_S2_CofeeMachine:
    
    scene picture_5
    
    play music "audio/KitchenTalk.mp3" loop 
   
    show norah normal at left
    n "Ohh, wow! Andrew, did you notice our coffee machine?"
    hide norah normal at left
    #scene picture_2
    show andrew normal at right
    a "Yes, looks expensive! That's really cool. Do you want to know a secret?"
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    n "Ok."
    hide norah normal at left
    #scene picture_2
    show andrew normal at right
    a "I rented this apartment just for this coffee machine. Haha."
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    n "Yes, and I'm sure you're not joking."
    hide norah normal at left
    #scene picture_2
    show andrew normal at right
    a "Maybe you can try to test it?"
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    n "C'mon, you've just finished your coffee!"
    hide norah normal at left
    #scene picture_2
    show andrew normal at right
    a "If the testing goes well, I'll be able to drink my coffee later tonight."
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    n "Huh..."
    play music "audio/KitchenTalk - mini.mp3" loop  loop fadein 0.5
    jump choicesCoffeeMachine
   
   
    
    show norah normal at left
    scene picture_5
    menu choicesCoffeeMachine:
        "Go to sleep": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump sleep12
        "Read a book":#2
            hide norah normal at left
            play sound "audio/ClickSound.mp3"
            play music "audio/KitchenTalk - mini.mp3" loop 
            jump book12
        "Watch a movie":#3
            hide norah normal at left
            play sound "audio/ClickSound.mp3"
            play music "audio/KitchenTalk - mini.mp3" loop 
            jump movie12
        "Test the coffee machine":#4
            play sound "audio/ClickSound.mp3"
            play music "audio/KitchenTalk - mini.mp3" loop 
            jump coffeemachine12
            
label sleep12:
    
    scene picture_5
    
   
    show norah normal at left
    n "All right, Andrew. I'm going to bed."
    hide norah normal at left
    #scene picture_2
    show andrew normal at right
    a "Okay, Good night!"
    hide andrew normal at right
    play music "audio/Predict.mp3" loop 
    scene picture_5
    show norah normal at left
    jump checkTheDoor
    
label read12:
    
    scene picture_5
    play music "audio/KitchenTalk.mp3" loop 
    
   
    show norah normal at left
    n "Okay, Andrew. Then I read the book."
    hide norah normal at left
    scene picture_2
    show andrew normal at right
    a "Okay, Good night!"
    hide andrew normal at right
    show norah normal at left
    play music "audio/Predict.mp3" loop 
    jump checkTheDoor
    
label movieEnd12:
    
    scene picture_2
    play music "audio/KitchenTalk.mp3" loop 
    
   
    show norah normal at left
    n "Okay. I'll watch a movie before going to bed."
    hide norah normal at left
    scene picture_5
    show andrew normal at right
    a "Okay, Good night!"
    hide andrew normal at right
    show norah normal at left
    jump checkTheDoor
    
menu book12:
    
        "The Picture of Dorian Gray": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump read12
        "Grief Is Love: Living with Loss":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump read12
        "Time Is a Mother":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump read12
            
menu movie12:
 
        "The Power of the Dog": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump movieEnd12
        "Nomadland":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump movieEnd12
        "Parallel Mothers":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump movieEnd12
            
menu coffeemachine12:
 
        "Search the price on Google": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump coffeemachineprice
        "Make coffee":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump makeACoffee
            
label makeACoffee:
    
    scene picture_2
    show andrew normal at right
    a "Wow! I can hear the coffee machine grinding."
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    n "Yes, yes, soon it will be ready."
    hide norah normal at left
    scene picture_2
    show andrew normal at right
    a "Thanks; please leave it; I'll drink it soon."
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    n "Okay."
    hide norah normal at left
    scene picture_2
    show andrew normal at right
    a "If you're going to sleep, then good night."
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    play music "audio/Predict.mp3" loop 
    jump checkTheDoor
    
    
            
label coffeemachineprice:
    
    play music "audio/KitchenTalk.mp3" loop 
   
    show norah normal at left
    n "Wow! Andrew, can you guess the price?"
    hide norah normal at left
    play music "audio/KitchenTalk - mini.mp3" loop 
    scene picture_5
    show andrew normal at right
    jump choicesCoffeeMachinePriceGuess
    
menu choicesCoffeeMachinePriceGuess:
    
        "150 €?": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump coffeemachinewrong
        "350 €?":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump coffeemachineright
        "750 €?":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump coffeemachinewrong
        "No idea, tell me...":#4
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump coffeemachineunknown
    
 
   
label coffeemachinewrong:
    
    play music "audio/KitchenTalk.mp3" loop 
   
    hide andrew normal at right
    show norah normal at left
    n "No! It's 349€!"
    hide norah normal at left
    
    jump Ep1_S2_CofeeMachineFinalTalk
    
label coffeemachineright:
    
    play music "audio/KitchenTalk.mp3" loop 
   
    hide andrew normal at right
    show norah normal at left
    n "Exactly! It's 349€! Crazy, right?"
    hide norah normal at left
    
    jump Ep1_S2_CofeeMachineFinalTalk

label coffeemachineunknown:
    
    play music "audio/KitchenTalk.mp3" loop 
   
    hide andrew normal at right
    show norah normal at left
    n "It's 349€!"
    hide norah normal at left
    
    jump Ep1_S2_CofeeMachineFinalTalk
    
label Ep1_S2_CofeeMachineFinalTalk:
    
    
    #scene picture_2
    show andrew normal at right
    a "I'm quite sure they've used it before!"
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    n "But it looks like new, I don't know"
    hide norah normal at left
    #scene picture_2
    show andrew normal at right
    a "So I suppose it deserves to be put to the test!"
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    n "Yes, it does! I'll try"
    
    jump sleep12
    

menu checkTheDoor:
    
        "Good night!": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump Ep1_S3
        "Could you please check if the door is locked?":#2
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            jump labelCheckingTheDoor
    

    
label labelCheckingTheDoor:
    
    scene picture_2
    show andrew normal at right
    a "I'm studying now; I'll check it later before going to bed."
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    jump insistCheckTheDoor
    
    
menu insistCheckTheDoor:
    
    
        "Please, check it now.": #1
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            scene picture_2
            show andrew normal at right
            jump andrewCheckingTheDoor
        "Okay, I'll do it myself.":#2
            play sound "audio/ClickSound.mp3"
            $norahAnxious += 10
            hide norah normal at left
            jump norahChecksTheDoor21
        "Okay, please, just don't forget.":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump andrewYesSure
                
menu andrewCheckingTheDoor:
    
    
        "Okay, wait!": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            $andrewSupport += 10
            jump andrewChecksTheDoor
        "Can't you just do it yourself?":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump norahChecksTheDoor12
        "Don't you see that I'm busy now?":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump norahChecksTheDoor2
            
                
label andrewChecksTheDoor:
    
    scene picture_1
    show andrewF normal at leftA
    a "Yep, it's locked."
    hide andrewF normal at leftA
    scene picture_5
    show norah normal at left
    n "Oh, thanks. I have locked it up."
    hide norah normal at left
    scene picture_1
    show andrew normal at leftA
    a "You did?"
    hide andrew normal at leftA
    scene picture_5
    show norah normal at left
    n "I just wanted you to double-check."
    hide norah normal at left
    scene picture_1
    show andrew normal at right
    a "Okay, then... So it's locked. Don't worry."
    hide andrew normal at right
    scene picture_5
    show norah normal at left
    n "Thanks."
    hide norah normal at left
    
    jump Ep1_S3
            
            
label norahChecksTheDoor12:
    
    scene picture_5
    show norah normal at left
    n "Ok, I'll do."
    hide norah normal at left
    jump norahChecksTheDoor21
    
label norahChecksTheDoor21:
    
    scene picture_1
    show norahB normal at center
    n "Yes, it is locked."
    hide norahB normal at center
    scene picture_2
    show andrew normal at right
    a "But I didn't lock it."
    hide andrew normal at right
    scene picture_1
    show norah normal at right2
    n "I locked it; I just wanted to check it before going to sleep."
    hide norah normal at left2
    scene picture_2
    show andrew normal at right
    a "So, now you can be sure that it is locked."
    hide andrew normal at right
    scene picture_1
    show norah normal at right2
    n "Yes, Good night!"
    hide norah normal at left
    scene picture_2
    show andrew normal at right
    a "Good night!"
    hide andrew normal at right
    
    jump Ep1_S3
        
label norahChecksTheDoor2:
    
    scene picture_5
    show norah normal at left
    n "Okay!"
    hide norah normal at left
    scene picture_1
    show norah normal at center
    n "Yes, it is."
    hide norah normal at center
    scene picture_2
    show andrew normal at right
    a "You have already locked it before, right?"
    hide andrew normal at right
    scene picture_1
    show norah normal at right
    n "Yes, an hour ago."
    hide norah normal at left
    scene picture_2
    show andrew normal at right
    a "So what's the point of bothering me about something you've already done?"
    hide andrew normal at right
    scene picture_1
    show norah normal at right
    n "I simply wanted to double-check."
    hide norah normal at left
    scene picture_2
    show andrew normal at right
    a "So, did you double-check it?"
    hide andrew normal at right
    scene picture_1
    show norah normal at right
    n "Yes."
    hide norah normal at left
    scene picture_2
    show andrew normal at right
    a "Great, that good night."
    hide andrew normal at right
    scene picture_1
    show norah normal at right
    n "Good night."
    hide norah normal at left
    
    
    jump Ep1_S3
            

label andrewYesSure:

    scene picture_2
    show andrew normal at right
    a "Yes, sure."
    hide andrew normal at right
    jump Ep1_S3

label Ep1_S3:
    
    scene picture_6

    play music "audio/ChapterTheme.mp3" loop 
    
    
    "{cps=25}3 Months before {/cps}"
                     
    play music "audio/PhoneCall.mp3" loop 

    scene picture_7
    a "Hey dad! Guess what?"
    scene picture_8
    d "What is it? You sound happy!"
    scene picture_7
    a "Remember that PhD I applied for? I got in!"
    scene picture_8
    d "That’s great news! I’m proud of you son."
    d "That means you’ll have to move to Tallinn, right?"
    d "Why don't you take your sister with you?"
    scene picture_7
    a "…What? Why would I take Norah all the way here?"
    a "I’m the one who got accepted for a PhD in Applied Physics, not her."
    scene picture_8
    d "You know that’s not what I mean."
    d "It’s just that… I think a change of surroundings could really benefit her at the moment."
    scene picture_7
    a "Okay, that’s true..."
                     
    play music "audio/PhoneCall - mini.mp3" loop 
    jump phoneCallChoice
                     
                     

menu phoneCallChoice:
    
    
        "...but that means I’ll have to get a bigger place.": #1
            play sound "audio/ClickSound.mp3"
            $andrewSupport += 10
            hide norah normal at left
            jump phoneCallOption1
        "...but that means I’ll have to babysit her all the time.":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump phoneCallOption2
                     
label phoneCallOption1:
    
    play music "audio/PhoneCall.mp3" loop
    scene picture_8
    d "Hey, your pops is a well paid surgeon."
    d "Just look for a nice apartment and I’ll pay for her half of the rent."
    d "It’s important that she starts to feel better. And this might really help her."
    
                     
    
    jump phoneCallNext
                     
label phoneCallOption2:
    
    play music "audio/PhoneCall.mp3" loop
    scene picture_8
    d "Hey, Norah might not feel well right now, but that doesn't mean she cannot be independent."
    d "Do I have to remind you of all the times she cooked for you because she was afraid you’d only eat pizza and burgers?"
    d "Why don’t you look for an apartment with a nice kitchen? She used to love cooking for you."
    d "I’ll pay her half of the rent. It’s important that she starts to feel better. And this might really help her."
    
    jump phoneCallNext
                     
                                          
label phoneCallNext:
    
    scene picture_7
    a "Okay, okay. I get your point."
    a "But I’m only taking her because you promised to pay her rent."
    a "So you’re not taking that back okay?"
    scene picture_8
    d "You know I always keep my word."
    d "It’s just that I haven’t really been able to be there for Norah since the incident because of my work."
    d "So this is the best I can do for her right now. So thank you for helping me Andrew."
    
    jump endOfChapter1
    
    
label endOfChapter1:
    
    play music "audio/TheHandle.mp3" loop 
    
    scene picture_6
    $norahAnxiousTimes = norahAnxious/10
    $andrewSupportTimes = andrewSupport/10
    
    "{cps=25}End of Chapter 1{/cps}"
    "{cps=25}The {b}[norahAnxiousTimes]{/b} choices you made increased Norah's anxiety.{/cps}"
    "{cps=25}Also, {b}[andrewSupportTimes]{/b} of your choices strengthened Andrew's support for Norah.{/cps}"
    "{cps=25}The next 19 chapters are currently in development. {/cps}"
    "{cps=25}However, if you'd like to learn more about The Parallax Door, here are a few options:{/cps}"
    
    jump optionalPart


menu optionalPart:
    
    
        "About the Narrative": #1
            play sound "audio/ClickSound.mp3"
            jump aboutNarrative
        "About the Player's Actions":#2
            play sound "audio/ClickSound.mp3"
            jump aboutPlayer
        "Play another scene":#3
            play sound "audio/ClickSound.mp3"
            jump Ep2_S1_CoffeeMachine
        "Restart the game":#3
            play sound "audio/ClickSound.mp3"
            jump Ep1_S1_Apartment1
            
            
label aboutNarrativeIntro:
    
    scene picture_14
    
    "{cps=25}You now have the chance to get some more information on the background of the characters in the novel.{/cps}"
    "{cps=25}NB! The following may contain SPOILERS.{/cps}"
    
    menu aboutNarrative:
    
        "Backstory of Andrew": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump aboutAndrew
        "Backstory of Norah":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump aboutNorah
        "Backstory of Dr Lee":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump aboutLee
        "Title Explanation":#4
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump aboutTheTitle
        "The Narrative Format":#5
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump aboutFormat
        "Return":#6
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump optionalPart
    
    
label aboutAndrew:
    
    scene picture_14
    show andreww normal at left
    
    "{cps=25}The player learns in the first chapter that Andrew has been accepted into a PhD program in Applied Physics.{/cps}"
    "{cps=25}He just moved to new country with his sister. However, a flashback reveals that he was hesitant to bring her along, but agreed at his father's insistence.{/cps}"
    "{cps=25}He is uncomfortable that his sister is living with him, because from his perspective, she causes him more trouble, making it difficult for him to focus on his studies.{/cps}"
    "{cps=25}While he looks for a job for his sister, she rejects all offers, claiming she is not ready.{/cps}"
    "{cps=25}The primary conflict between Andrew and Norah arises when she breaks an expensive coffeemachine in their apartment.{/cps}"
    "{cps=25}In addition, after a few weeks, she claims that she believes someone is following her because one night she noticed the door handle slowly move down, as if someone from the other side was attempting to open the door.{/cps}"
    "{cps=25}Andrew calls his father often with concerns about Norah's behavior. Even leaving her alone in the apartment worries him.{/cps}"
    "{cps=25}After the late-night doorknob incident (which Andrew does not believe occurred), Norah requests that they move to a new apartment immediately.{/cps}"
    "{cps=25}One week later though, everything drastically changes: Andrew decides to host a little home party with his new colleagues. As they leave the party, one of his colleagues accidentally breaks the doorknob so that it cannot be locked until it is fixed.{/cps}"
    "{cps=25}Andrew realizes they must sleep tonight with the door unlocked.{/cps}"
    
    hide andreww normal at left2
    scene picture_6 
    jump aboutNarrative
    
label aboutNorah:
    
    scene picture_14
    show norahh normal at left2
    
    "{cps=25}Although the player (as Norah) has the option to skip the questions, it is clear that Norah may ask several questions and also be concerned about whether the door is locked. {/cps}"
    "{cps=25}A few months ago, she lost her best friend Lara, who died in a car accident. {/cps}"
    "{cps=25}There were substantial changes in her behavior as a result of this incident, including symptoms that matched those of obsessive-compulsive and post-traumatic stress disorders.{/cps}"
    "{cps=25}While Andrew believes it to be a simple grief, their father is more worried about the health of his daughter.{/cps}"
    "{cps=25}Norah accepts her father's advise on the potential advantages of environmental change and decides to move with her brother Andrew to another country.{/cps}"
    "{cps=25}However, the situation gets much more stressful: constantly haunted by memories of Lara.{/cps}"
    "{cps=25}Is this the last straw? On a particular night she saw the doorknob slowly descending.{/cps}"
    "{cps=25}Since she cannot reach the peephole, she considers holding the doorknob or grabbing a chair in order to see through the peephole.{/cps}"
    "{cps=25}No matter which option the player chose for Norah, neither will reveal who was on the other side of the door.{/cps}"
    "{cps=25}Norah cannot explain what she saw, and she does not rule out the possibility that it was Lara's ghost.{/cps}"
    "{cps=25}From that moment on, she lives in perpetual fear. And although her father and brother are unable to understand Norah's behavioral change, the player will realize that Lara was more than just a friend to Norah...{/cps}"
    
    
    hide norahh normal at left
    scene picture_6 
    jump aboutNarrative


    label aboutLee:
    
    scene picture_14
    show dad normal at left
    
    "{cps=25}The father of Andrew and Norah will appear in a flashback during the first few chapters. However, at the conclusion of the story, the player discovers he is more than a simple supporting character.{/cps}"
    "{cps=25}He is a loving father who truly cares about his daughter's health, but at some point, when he realizes that Norah is not doing well in another country.{/cps}"
    "{cps=25}He begins to blame himself, believing that his decision to send Norah there was perhaps self-serving, since his brother must now handle all of her whims.{/cps}"
    "{cps=25}After learning about the incident with the doorknob, he offers to cover the whole cost of a new apartment and suggests that Andrew and Norah move.{/cps}"
    "{cps=25}He also begins to call Norah on a regular basis. To help her deal with the loss, he tells her a story of a 12-year-old child he accidentally killed during a surgery and how difficult it was for him to cope with that.{/cps}"
    
    hide dad normal at left
    scene picture_6 
    jump aboutNarrative
    
    
    
    
    label aboutFormat:
    
    scene picture_17
    
    "{cps=25}Every chapter has three episodes. Each episode has several scenes. In each episode, the player is always given with a choices. Always, the last episode of a chapter is a flashback.{/cps}"
    scene picture_6 
    
    jump aboutNarrative
    
    label aboutTheTitle:
    
    scene picture_17
   
    
    "{cps=25}In the narrative, the door serves as a metaphor. On the one hand, the door presents Andrew with a potential career opportunity. On the other side, Norah has yet another chance to change her surroundings and gain control over her mental health.{/cps}"
    "{cps=25}And ultimately, the door to their rented dwelling is the symbol of fear, an unexplained obstacle in their lives.{/cps}"
    "{cps=25}And each of these doors is parallel to the next.{/cps}"
    "{cps=25}The choice of the term Parallax is a reference to Andrew's doctoral dissertation on the parallax effect.{/cps}"
    scene picture_6 
    
    jump aboutNarrative
        

    
 
    
    
menu aboutPlayer:
    
        "Why so many questions to the broker?": #1
            play sound "audio/ClickSound.mp3"
            jump aboutQuestion
        "Why ask about the coffee maker?":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump aboutCoffeeMachine
        "A movie or a book?":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump aboutLeisure
        "Andrew's responses":#4
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump aboutTheAndrewResponse
        "Return":#4
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump optionalPart
            
label aboutQuestion:
    
    scene picture_2
    show norah normal at left2
    show broker normal at rightB
    
    "{cps=25}The player has the option of skipping these questions or completing as many as possible.{/cps}"
    "{cps=25}The thing is, by asking too many questions, the player might unknowingly boost Norah's anxiety level.{/cps}"
    "{cps=25}Norah's anxiety level is a hidden variable that will eventually become crucial and influence the storyline.{/cps}"
   
    
    "{cps=25}For instance, Norah's current anxiety level is {b}[norahAnxious] points{/b}, which indicates that the player {b}[norahAnxiousTimes] times{/b} selected to ask her questions that raised her anxiety level.{/cps}"
    
    hide norah normal at left2
    hide broker normal at rightB
    scene picture_6 
    jump aboutPlayer
    
label aboutCoffeeMachine:
    
    scene picture_5
    show norah normal at left2
    show andrew normal at right
    
    "{cps=25}The purpose of this piece is to draw the player's attention to the price of the coffeemachine.{/cps}"
    "{cps=25}If Norah's anxiety level exceeds 100 in Chapter 3, she will break the coffee machine by mistake.{/cps}"
    
    
    hide norah normal at left2
    hide andrew normal at right
    scene picture_6 
    jump aboutPlayer
    
        
label aboutLeisure:
    
    scene picture_5
    
    "{cps=25}The purpose is to show what books and films she would like to read or watch. The result of this decision has no impact on the plot, however the player may learn more about Norah's preferences.{/cps}"
    
    
    
    scene picture_6 
    jump aboutPlayer
    
            
label aboutTheAndrewResponse:
    
    scene picture_15
    
    "{cps=25}There is an additional hidden variable for Andrew. The variable represents Andrew's support to his sister.{/cps}"
    
    
    "{cps=25}For instance, Andrew's current support level is {b}[andrewSupport] points{/b}, which indicates that the player {b}[andrewSupportTimes] times{/b} selected to support Norah.{/cps}"
    
    scene picture_6 
    jump aboutPlayer
    

    
label Ep2_S1_CoffeeMachine:
    
    scene picture_6
     

    play music "audio/ChapterTheme.mp3" loop 
    
    
    "{cps=25}Chapter 4: The Handle{/cps}"
    "{cps=25}October 23, 2023. Tallinn, Estonia{/cps}"
    "{cps=25}1:43 AM{/cps}"
    
    play music "audio/VitalG.mp3" loop 
    scene picture_5
    show norah normal at left
    n "I recently heard that car accidents kill over 3500 people throughout the world."
    n "Isn't it pretty funny? Your case is nothing more than a statistic in the grand scheme of things."
    n "How am I feeling right now?"
    n "It's almost as if I'm living in a parallel universe where you no longer exist. And it's unbearable."
    n "How did I feel during your funeral, do you want to know?"
    n "I was bored! That's what I felt."
    n "I was waiting for the funeral to end so I could call you and get away from all my feelings and to hang out with you somewhere."
    n "But damn! Not! You were inside a tomb."
    n "You remained still and emotionless during..."
    n "I couldn't call you - you were dead!"
    play music "audio/VitalG - mini.mp3" loop 
    
    menu lateNightChoices:
        "Keep remembering...": #1
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump lateNightThoughts
        "Go to check the door":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump theHandle
        "Go to sleep":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump sleepEp2
            
label lateNightThoughts:
    
    scene picture_5
    show norah normal at left
    n "The advice of my father is that a change of environment could be beneficial to my mental health."
    n "And now I find myself in this new place, but with all of the memories of you still in my head."
    n "Where are you now, Lara?"
    n "Where are you now..."
    n "Lara..."
    play music "audio/VitalG - mini.mp3" loop 
    
    menu lateNightChoices2:
        "Go to check the door":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump theHandle
        "Go to sleep":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump sleepEp2

label theHandle:
    
    
    play music "audio/beforeTheHandle.mp3" loop 
    
    scene picture_16
    show knob normal at theHandle0
    with Dissolve(1.0)
    scene picture_16
    show knob normal at theHandle
    with Dissolve(15.0)
    scene picture_16
    #show norahB normal at center2
    #with Dissolve(10.0)
    #scene picture_9
    #show norahB normal at center2


   
    
    jump theHandlePsycho
    
label theHandlePsycho:
    
    play music "audio/TheHandle.mp3" loop 
    scene picture_12
    
    n "Was it real?"
    n "Was it rl?"
    n "Ws it rl?"
    n "Waaas iiiiit reeeal?"
    n "Wasssss it real?"
    n "Wwwww?"
    n "What the hell just happened?"
    n "I saw the door handle move down."
    n "I saw!"
    n "Did I?"
    n "Am I being followed by someone?"
    n "Someone standing on the other side."
    n "Who?"
    n "This is real?"
    n "ts s rlll"
    n "rlllll"
    n "Lara?"
    n "Is this..."
    n "rllll"
    n "no"
    n "not real"
    n "nt rl"
    n "rll"
    n "nt"
    
    menu theHandleChoices2:
        "Look through the peephole":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump watchFromPeephole
        "Hold the handle":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump holdTheHandle
    
    jump theHandlePsycho
    
    
label watchFromPeephole:
    
    scene picture_12
    
    n "The peephole is too high!"
    
    menu theHandleChoices3:
        "Bring the chair":#2
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump bringTheChair
        "Hold the handle":#3
            play sound "audio/ClickSound.mp3"
            hide norah normal at left
            jump holdTheHandle
    
   
    
    
    
label sleepEp2:
    
    scene picture_5
    show norah normal at left
    n "Good Night, Norah!"
    n "Good Night, Lara!"
    
    scene picture_6
    
    jump optionalPart

label bringTheChair:
    
    scene picture_13
    n "I'm not seeing anybody. It's so dark."
    scene picture_6
    jump optionalPart
    
    

label holdTheHandle:
    
    scene picture_1
    show norahH normal at holds
    n "No one is there."
    n "It wasn't real."
    n "You're the only one who holds the handle."
    n "There is no one behind the door."
    n "And the door is locked."
    n "No one can enter..."
    n "It wasn't real..."
    n "Isn't it?"
    hide norahH normal at holds
    scene picture_6
    
    jump optionalPart
  


   
    
    
            


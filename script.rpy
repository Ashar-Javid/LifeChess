# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
label start:
    # starting background
    #press_white =False
    #press_black =False
    scene castle
    #play music "" 
    "In a place far away, there was a kingdom so vast and mighty that none rose to its magnificence!"
    "King was a wild old man who ruled over vast lands with briliance but his age was declining towards an end."
    "To preserve the kingdom, he decided to name his heir from one of his prince."
    "He announced the great \"Life Chess\" to select his heir."
    "He sent letters to both of his prince!!"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene letter
    "Prince are young,brave and strong man. However, their capabilities must be shown to prove them worthy of the throne.They were on a journey to northern border of the kingdom."
    pause 3.0
    #Change the location of narration lines to centre
    #scene letter
    "It is stated in your honor that "
    #Here we have to adjust the name input area
    python:
        Prince = renpy.input("Enter your name: ")

    "is demanded by the king to be present in the court, tomorrow."   
    pause 1.0
    #Change of scene 
    scene throne_room 
    show Old_advisor at Right
    show General at Left with dissolve
    show King at Center with dissolve

    General"Welcome majesty! The court awaits your presence."
    King"Maybe the prince is busy in more important matters than the kingdom itself."
    King"Or do you have an explanation for yourself?"
    jump character_selection
    #Selection of the charcter

    label character_selection:

    hide Old_advisor
    hide King
    hide General
    hide prince_black
    scene throne_room1
    
    #image button auto= "prince_white_%s" 
    #hovered setvariable(prince_white_hover,jump Prince_white)
    #if prince_white selected: 
    #    hovered=True
    #action (if hovered== True):
    #focus_mask True
    #hovered set variable("Prince","True")
    #unhovered set variable("Prince","")
    "Select a charcter to proceed:"
    menu: 
        "Prince Black": 
                "Your character is selected"
                $flag=2
                jump Prince_black
        "Prince White":
                "Your character is selected"
                $flag=1
                jump Prince_white    
    pause 2.0
    #add "prince_black" #at left
    #image button auto= "prince_black_%s"
    
    #imagebutton:   
    #idle "prince_white_idle.png"
    #hover "prince_white_hover.png"
    #focus_mask True
    #xpos 0.33 ypos 0.5
    #action Jump("Prince_white")
    
    
    #imagebutton:   
    #idle "prince_black_idle.png"
    #hover "prince_black_hover.png"
    #focus_mask True
    #xpos 0.66 ypos 0.5
    #action Jump("Prince_black")
        
    
    
   

        
    #menu:
    #    #If prince white selected
    #    "You have made your choice." if press_white==True:
    #        "Best of luck"
    #        jump Prince_white
    #    "You have made your choice." if press_black==True: 
    #        "Best of luck"
    #        jump Prince_black   
    
    #For prince_white
    label Prince_white :
        scene throne_room
        show Old_advisor at Right
        show General at Left with dissolve
        show King at Center with dissolve
        hide prince_black
        show prince_white_idle at Lowcenter
        Prince"Surely father, there is nothing more important to me than the service of the kingdom."
        Prince"I am well aware of my duties, but I was busy helping people who are living on the northern border after they were flooded."  
        pause 1.0   
        King"I don't doubt your abilities but make sure that your priorities don't hamper your naming as the heir."
        Old_advisor"You are right my majesty! The prince must prove his competence to succeed the throne after you."
        King "Upon this the king rose from his throne"
        King "It is  WE The King Who decide who IS Worthy and who is not!!. I need some time to think about my final decision. The Court is dimissed."
        "After a while you visit your father while he was in his chambers"
        Prince "Father I hope I am not disturbing you"
        King "ofcourse not my son, in fact i was also wanting to talk to you."
        pause 1.0
        King "You see , ruling a kingdom is a task no single man can manage on his own. Our advisors , Soldiers and MOST IMPORTANTLY, Your Mother 'The Kingmaker' are there side by side"
        pause 0.4
        King "I have to keep them all happy and i cannot afford to make you the new king while they are not convinced. You have to convince them if you want to be at your rightful place."
        Prince "Dont worry my father i will do everything in my command to make you proud"
        King "I expect no less from you"
        "Life Chess starts now!!!"
        hide Prince 
        hide King
        hide General
        hide Old_advisor
        jump Life_Chess

    #For prince_black
    label Prince_black : 
        scene throne_room
        show Old_advisor at Right
        show General at Left with dissolve
        show King at Center with dissolve
        hide prince_white
        show prince_black_idle at Lowcenter 
        Prince "My Duties are of no concern to you. I know what i have to do,and if you would give me the power i want i can show you what i am capable of"
        King "you demand from me the Throne! all your life you have done nothing but knock about and even now when there is a disaster in the northern border, You were there partying with your friends."
        pause 1.0
        King "if i want I can banish you from this kingdom forever. Court is dismissed"
        #Workingg...
        "Prince leaves in a state of anger and rage thinking of how you could get to that throne you dreamt of since you were a child.At last it occured to you , You have to gain the favour of those who are near your father. As the Kingdom is ruled by the king but run by the bureaucracy"
        pause 0.5
        "Prince now must convince his Mother as she is the queen and have a signifanct influence among the people and on your Father."
        pause 0.5
        "Prince must also convince the other two most important people: The General and The Wise Advisior"
        "Life Chess starts now!!!"
        hide Prince 
        hide King
        hide General
        hide Old_advisor
        jump Life_Chess
            


    label Life_Chess :
        scene garden
        show Queen at Left with dissolve 
        if (flag==2):
            show prince_black_idle at Right with dissolve
        if (flag==1):
            show prince_white_idle at Right with dissolve   
        
        Queen "Hi my dear, How are you?. I see that you are uneasy. Is there anything in your mind?"
        Prince "You are definitly true my Queen. I do have sonthing in my mind"
        Queen "Dont tell me you want to become the king!"
        Prince "Why not mother? I can surely bear the burden of the throne!! I am certainly capable of it"
        Queen "The throne is not a joke! whatever you and your father have between you is far from my concern. I only see you as a child who is ambitious and capable but not yet have the skill to command"
        Prince "Oh I surely can prove you wrong"
        Queen "Well, If you want to prove me wrong,Win this game of chess from me. If you succeed you will have my full support"
        hide Queen 
        hide Prince
        "Do you want to play chess?"
        menu:
            "Yes":
                    jump chess
            "No":
                    jump part_2
        #Scene general.i.e tictactoe
    label part_2:
        scene castle_general
        "In order to have a strong claim to the throne it is necessary that you have the support of General."
        "So win his affection to strengthen your claim to the throne." 
        if (flag==2):
            show prince_black_idle at Right with dissolve
        if (flag==1):
            show prince_white_idle at Right with dissolve 
        show  General at Left
        #show Prince at left 
          
        General "Oh so you have finally decided to come to me."
        Prince "So you know what H have come to say?"
        General "Of course I know ! "
        General "After what happend today ,I was sure you will show up sooner or later"
        Prince " SO if you know then what is your take on the matter?"
        General "You see I am a worrior,I only weigh a man by his capability to win. And you i think lack the tactic."
        Prince "Is that so, then i am here to accept any of your challenges!"
        General "Then come and outsmart me in this game of tick tac toe"
        hide General
        hide Prince
        "Do you want to play tic tack toe!"
        menu:
                "Yes":
                        jump tictactoe
                "No":
                        jump part_3
        #Scene Advisor .i.e the wisdom test
    label part_3:
         
        scene library
        "The advisor is one of the closest ones to the King,if anyone could convince him to anything was him."
        "He was a loyal servant to the old king as well. Make him your ally by showing your wisdom."
        #show Prince at left with dissolve
        if (flag==2):
            show prince_black_idle at Right with dissolve
        if (flag==1):
            show prince_white_idle at Right with dissolve  
        show Old_advisor at Left with dissolve
        Prince " Can I have the honor to be in your presence?"
        Old_advisor "Of course dear majesty. What brings you to this old servant of yours?"
        Prince "You are a wise man and I will talk to you very straight forward,
        I want to have a claim on the throne and I am ready to bear the reponsibilties of being a King
        If you show me your support, I will never forget your favour."
        Old_advisor"Being a King comes with great responsibilities. Are you wise enough to decide for the fate of thousands of people?"
        Prince"I have already proven myself earlier and I am ready to prove it again as well."
        Old_advisor "If that is what you think than answer these questions" 
        Old_advisor"If you can answer them than you are ready"
        #Questions of wisdom
        Old_advisor"Are you ready?" 
        Prince"The throne awaits me,Lets not keep it waiting."
        Old_advisor"What is power?"
        $Respect=0
        menu:
            "Power is just an illusion as all the true power belongs to the almighty.":
                Old_advisor"Perhaps,You are right"
                $Respect=Respect +1
            "Power is all for the king":
                Old_advisor"That is not the best answer"
            "Power is all for the people":
                Old_advisor"You were close"
   
        Old_advisor""
                
        #To be continued
        $game = win
        scene war
        if (game==win):
            "The journey of [Prince] has come to end. Congratulations fro the throne"
        if (game==lose):
            "The journey of [Prince] has come to end. Better luck next time."






    return

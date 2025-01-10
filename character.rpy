define Prince = Character("[Prince]",color = "#FFFF00")
define King= Character("King",color="#0000FF")
define Queen=Character("Queen",color="#FF0000")
define General=Character("General",color="#00008B")
define Old_advisor=Character("Advisor",color="0000FF")

image prince_white_idle= "prince_white_idle.png"
image prince_black_idle= "prince_black_idle.png"
image prince_white_hover= "prince_white_hover"
image prince_black_hover= "prince_black_hover"

#python:
#    if (flag==1):
#        image prince = "prince_black_idle.png"
#    if (flag==2):
#        image prince = "prince_white_idle.png"

screen throne_room1:
    imagebutton:   
        idle "prince_black_idle.png"
        hover "prince_black_hover.png"
        focus_mask True
        xpos 0.85 ypos 0.5
        action [Jump("Prince_black"),Hide ("courtroom")]

    imagebutton:   
        idle "prince_white_idle.png"
        hover "prince_white_hover.png"
        focus_mask True
        xpos 0.1 ypos 0.27
        action [Jump("Prince_white"),Hide("courtroom")]   
     

image King= "king.png"
image Queen= "queen.jpg"
image General= "general.png"
image Old_advisor= "advisor.png"
image castle ="castle.jpg"
image corridor="corridor.jpg"
image courtroom ="throne_room.jpg"
image garden = "garden.jpg"
image letter= "scroll.png"
image library= "library.jpg"
image castle_general="castle_general.jpg"
image war ="war.jpg"
import turtle  
from math import *
wn = turtle.Screen()
wn.setup(700, 600) #setting the screen size
sas = turtle.Turtle() #naming my turtle

print ('Hello, my name is Ichiraku, and I shall create any regular polygon your heart desires') #greeting the user

    

aa = wn.textinput("Type", "Are you trying to draw a star[S] or polygon[P] (P = Polygon, S = Star)") #using wn.textinput to have the screen pop up in the turtle screen 
while aa!= 'p' and aa!= 's' and aa!= 'P' and aa!= 'S':  #if it’s not p or s then it wont continue it’ll keep asking the user until they under the right command
    continue

p = "p"	#defining all the letters
s = "s"
d = "d"
c = "c"
e = "e"
inradius = "inradius"
circ = 'circ'
area = 'area'
per = 'per'
y= 'y'
n='n'

    
if aa.lower()==s:   #if “s” or ‘S’ is typed in this entire thing will be called (the .lower part means both lower case and capital s could be typed
    
    
    ww = wn.numinput("Points?", "How many vertices does your star have? (The minimum is 5, and only odd numbers can be picked, if an odd number is not picked, a star will not be drawn)", minval=5)  #how many points 
    x = wn.numinput("star", "What's the size of your star? (150 - 300", minval = 120, maxval = 200) #asking for size

    #asking for colour of boarder
    colouur = wn.textinput("Border", "What is the colour of the border of your shape ")
    colours = ("aquamarine","black","blue","brown","chocolate","coral","cyan","orchid","violet","gainsboro","gold","gray","green","grey","ivory","khaki","lavender","magenta","navy","orange","purple","pink","salmon","sienna","turquoise","violet","white","red","yellow", "AQUAMARINE","BLACK","BLUE","BROWN","CHOCOLATE","CORAL","CYAN","ORCHID","VIOLET","GAINSBORO","GOLD","GRAY","GREEN","GREY","IVORY","KHAKI","LAVENDER","MAGENTA","NAVY","ORANGE","PURPLE","PINK","SALMON","SIENNA","TURQUOISE","VIOLET","WHITE","RED","YELLOW") #listing all the possible colours, im doing this so if the user does not type any of these words, an error would not happen but rather a message telling them to type the correct input. I retyped the colours in al cap as well just in case if the user decides to type the input in all caps, I tried using the “.lower” command but it doesnt work (or i just dont know how to use it properly)
    while colouur not in colours or colouur ==  colours:
        colouur = wn.textinput("Color", "Invalid input. What's the color of your shape?") #what happens if they dont write a colour 

        
    colourfiill = wn.textinput("Inside", "What is the colour of the inside of your star") #doing the same thing as before but for the inside of the star
    colours = ("aquamarine","black","blue","brown","chocolate","coral","cyan","orchid","violet","gainsboro","gold","gray","green","grey","ivory","khaki","lavender","magenta","navy","orange","purple","pink","salmon","sienna","turquoise","violet","white","red","yellow", "AQUAMARINE","BLACK","BLUE","BROWN","CHOCOLATE","CORAL","CYAN","ORCHID","VIOLET","GAINSBORO","GOLD","GRAY","GREEN","GREY","IVORY","KHAKI","LAVENDER","MAGENTA","NAVY","ORANGE","PURPLE","PINK","SALMON","SIENNA","TURQUOISE","VIOLET","WHITE","RED","YELLOW") #same as before
    while colourfiill not in colours or colourfiill ==  colours:
        colourfiill = wn.textinput("Color", "Invalid input. What's the color of your shape?") #same as before
#formula’s for calculating the following for a star
    area = ((0.25 * ww * x**2)/(tan(pi/ww)))         # area
    per = ww * x                                        # perimeter
    irradius = ((0.5 * x )/(tan(pi/ww)))           # inner radius
    circ = ((0.5* x)/(sin(pi/(ww))))          # circumradius
    exter = (360/ww)                         # exterior angle
    inter = (((ww-2)/ww)*180)    #interior angle  



        
        
    sas.color(colouur)#applying the colour chosen from the user to the shape
    sas.fillcolor(colourfiill)
    sas.begin_fill()

    sas.penup()              #this is for centering the star
    sas.setpos(-0.5*(circ),0.25*(circ))
    sas.pendown()
    
    for i in range(int(ww)):
        sas.forward(x)
        sas.penup()
        sas.forward(10)
        sas.write(x,font=('Arial', 8, 'normal'))
        sas.backward(20)
       
        sas.pendown()                            #drawing the shape 
        sas.left(720/ww)
    sas.end_fill()
    sas.hideturtle()
    sas.right(90)
    sas.penup()
    sas.forward(150)      #where to write the label
    sas.write("The side length is " + str (x) + ' units', font=('Arial', 12, 'normal')) # what to write
    sas.forward(27)
    sas.write("The inradius is " + str (inradius) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The circumradius is " + str (circ) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The area is " + str (area) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The permimeter is " + str (per )+ ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The interior angle is " + str (inter) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The exterior angle is "+ str (exter) + ' units', font=('Arial', 12, 'normal'))
       


            
if aa.lower()==p:  #if p or P is typed in
    
    n = wn.numinput("SIDE?", "How many sides does your polygon have? (3-14)", minval=3, maxval=14)
    l = wn.numinput("SIDE?", "what’s the length of your polygon (60-165)", minval=60, maxval=120)
    

    colour = wn.textinput("Fill", "What is the colour of the boarder of your polygon")
    colours = ("aquamarine","black","blue","brown","chocolate","coral","cyan","orchid","violet","gainsboro","gold","gray","green","grey","ivory","khaki","lavender","magenta","navy","orange","purple","pink","salmon","sienna","turquoise","violet","white","red","yellow","AQUAMARINE","BLACK","BLUE","BROWN","CHOCOLATE","CORAL","CYAN","ORCHID","VIOLET","GAINSBORO","GOLD","GRAY","GREEN","GREY","IVORY","KHAKI","LAVENDER","MAGENTA","NAVY","ORANGE","PURPLE","PINK","SALMON","SIENNA","TURQUOISE","VIOLET","WHITE","RED","YELLOW")
    while colour not in colours or colour ==  colours:
        colour = wn.textinput("Colour", "OOPS! That’s not a colour! What's the color of your shape?")

        
    colorfill = wn.textinput("Boarder", "What is the colour of the inside of your polygon")
    while colorfill not in colours or colorfill ==  colours:
        colorfill = wn.textinput("Colour", "Hey! That’s not colour, please enter a colour! Please enter a colour") 


    inradius = (0.5 * l * (1/tan(pi / n)))
    circ = (0.5 * l * (1/sin(pi / n)))
    per = (n * l)
    area = ((0.5) * (n*l)) * (0.5 * l * (n * l))
    inter = (((n - 2) * 180)/n)
    exter = (360 / n)

       

    angle = 180-((n - 2)*180/n)
    a = l/(2*tan(pi/n))
    l = int(l)
    n = int(n)
    
    sas.begin_fill() 
    colorfill = str(colorfill)
    sas.color(colour)
    sas.up()
    sas.goto(-l/2, -a)
    sas.begin_fill()
    sas.down()
    sas.begin_fill()
    sas.fillcolor(colorfill)

    sas.penup()                                   # centers the polygon
    sas.setpos(-0.5*(circ),-0.5*(circ))
    sas.pendown()
    

    for i in range(n):
        sas.forward(l)
        sas.penup()
        sas.forward(10)
        sas.write(l,font=('Arial', 8, 'normal'))
        sas.backward(20)
        sas.pendown()
        sas.left(angle)
    sas.end_fill()
    sas.hideturtle()
    sas.end_fill()
        
    sas.right(90)
    sas.penup()
    sas.forward(40)
    sas.write("The side length is " + str (l) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The inradius is " + str (inradius) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The circumradius is " + str (circ) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The area is " + str (area) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The permimeter is " + str (per) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The interior angle is " + str (inter) + ' units', font=('Arial', 12, 'normal'))
    sas.forward(27)
    sas.write("The exterior angle is "+ str (exter) + ' units', font=('Arial', 12, 'normal'))


                           
  
                    
                           
                           


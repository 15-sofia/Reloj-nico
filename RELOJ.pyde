
def setup():
 size(600, 600)
 strokeWeight (4)
 stroke(227, 94, 11)
 fill(123, 223, 240)
 
s= 0 #time variable
m= 0 #time variable
h= 0 #time variabl
def draw ():
   
    ellipse(width /2, height/2, 200, 200)
    global h
    translate(width/2, height/2)
    rotate(radians(h))
    line(width /4, height/4, 10, 10)
    stroke(215, 11, 227)
    h += 0.02
    
    ellipse(width /4, height/4, 100, 100)
    global m
    translate(width/4, height/4)
    rotate(radians(m))
    line(width /4, height/4, 10, 10)
    stroke(27, 101, 245)
    m += 0.01
   

 

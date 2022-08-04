from turtle import *

def pentagon():
    color("blue","red")
    begin_fill()
    while True:
    
        forward(100)
        left(45)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

print(6//4)
import turtle

screen = turtle.Screen()
image = "Map-of-India-Worksheet.gif"
screen.addshape(image)
turtle.shape(image)

def click_on_dick(x, y):
    print(x, y)

turtle.onscreenclick(click_on_dick)
turtle.mainloop()
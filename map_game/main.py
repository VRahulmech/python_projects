import turtle
import map_data

India_map = turtle.Screen()
image = "India_map.gif"
India_map.addshape(image)
turtle.shape(image)

# def get_loc(x,y):
#     print(x,y)
#
# India_map.onscreenclick(get_loc)
# print(len(map_data.map_location))
score = 0
for i in range(len(map_data.map_location)):
    state = India_map.textinput(f"Question-{i+1}", "Enter the State name: ")
    print(state in map_data.map_location.keys())
    if state in map_data.map_location.keys():
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        print(map_data.map_location[state][0], type(map_data.map_location[state][0]))
        t.goto(map_data.map_location[state][0], map_data.map_location[state][1])
        t.write(state)
        score += 1

print(f"your score is {score}")
India_map.mainloop()

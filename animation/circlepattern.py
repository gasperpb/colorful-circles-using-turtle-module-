import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
color = ["#F061E6", "#85E65A", "#5AE6D5"]
for i in range(140):
    t.color(color[i % 3])
    t.circle(i)
    t.left(60)
turtle.mainloop()

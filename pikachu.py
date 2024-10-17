# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 02:02:01 2024

@author: ADMIN
"""

import turtle

# screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pikachu Drawing")

# Create turtle object 
pikachu = turtle.Turtle()
pikachu.speed(10)

# Function to draw filled shapes
def draw_filled_shape(color, points):
    pikachu.penup()
    pikachu.goto(points[0])
    pikachu.pendown()
    pikachu.begin_fill()
    pikachu.fillcolor(color)
    for point in points[1:]:
        pikachu.goto(point)
    pikachu.goto(points[0])
    pikachu.end_fill()

# ears
def draw_ears():
    # Left ear
    draw_filled_shape("black", [(0, 100), (-70, 200), (-80, 160), (-10, 110)])
    # Right ear
    draw_filled_shape("black", [(0, 100), (70, 200), (80, 160), (10, 110)])

# face
def draw_face():
    # Head
    pikachu.penup()
    pikachu.goto(0, 0)
    pikachu.pendown()
    pikachu.begin_fill()
    pikachu.circle(100)
    pikachu.fillcolor("yellow")
    pikachu.end_fill()

# eyes
def draw_eyes():
    # Left eye
    pikachu.penup()
    pikachu.goto(-40, 30)
    pikachu.pendown()
    pikachu.begin_fill()
    pikachu.circle(15)
    pikachu.fillcolor("black")
    pikachu.end_fill()

    # Right eye
    pikachu.penup()
    pikachu.goto(40, 30)
    pikachu.pendown()
    pikachu.begin_fill()
    pikachu.circle(15)
    pikachu.fillcolor("black")
    pikachu.end_fill()

# cheeks
def draw_cheeks():
    # Left cheek
    pikachu.penup()
    pikachu.goto(-60, -30)
    pikachu.pendown()
    pikachu.begin_fill()
    pikachu.circle(20)
    pikachu.fillcolor("red")
    pikachu.end_fill()

    # Right cheek
    pikachu.penup()
    pikachu.goto(60, -30)
    pikachu.pendown()
    pikachu.begin_fill()
    pikachu.circle(20)
    pikachu.fillcolor("red")
    pikachu.end_fill()

# Drawing mouth
def draw_mouth():
    # Lower part of mouth
    pikachu.penup()
    pikachu.goto(-40, -60)
    pikachu.pendown()
    pikachu.right(90)
    pikachu.circle(40, 180)
    pikachu.right(90)

# Main function to draw Pikachu
def draw_pikachu():
    draw_ears()
    draw_face()
    draw_eyes()
    draw_cheeks()
    draw_mouth()

# Run function 
draw_pikachu()



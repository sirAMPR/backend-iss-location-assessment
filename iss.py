#!/usr/bin/env python

__author__ = 'aradcliff'

import requests
import turtle
import time


def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()


def get_coordinates():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    return r.json()


def get_next_pass():
    r = requests.get('http://api.open-notify.org/iss-pass.json',
                     params={'lat': '39.7684', 'lon': '-86.1581', 'n': '1'})
    return r.json()


def init_turtle():
    iss = turtle.Turtle()
    next_pass = get_next_pass()
    rise_time = time.ctime(next_pass["response"][0]["risetime"])

    screen = turtle.Screen()
    screen.setup(width=720, height=360, startx=0, starty=0)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')

    iss.shape("iss.gif")
    iss.penup()
    iss.goto(-86.1581, 39.7684)
    iss.dot(5, "yellow")
    iss.color('yellow')
    iss.write(rise_time, align='right', font=("Arial", 14))

    return iss


def main():
    data = get_astronauts()
    print(
        f"Number of astronauts on the {data['people'][0]['craft']}: {data['number']}")
    for astro in data["people"]:
        print(f"- {astro['name']}")

    iss = init_turtle()
    while True:
        coords = get_coordinates()
        lat = float(coords["iss_position"]["latitude"])
        lon = float(coords["iss_position"]["longitude"])
        heading = iss.towards(lon, lat)
        if heading > 0.0:
            iss.setheading(heading)
        iss.goto(lon, lat)
        time.sleep(10)


if __name__ == '__main__':
    main()

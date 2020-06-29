#!/usr/bin/env python

__author__ = 'aradcliff'

import requests
import turtle


def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()


def get_coordinates():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    return r.json()


def init_turtle():
    iss = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width=720, height=360, startx=0, starty=0)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')
    iss.shape("iss.gif")
    iss.penup()
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
        print(iss.heading())
        iss.goto(lon, lat)
        # print(coords)


if __name__ == '__main__':
    main()

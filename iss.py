#!/usr/bin/env python

__author__ = 'aradcliff'

import requests


def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()


def main():
    data = get_astronauts()
    print(
        f"Number of astronauts on the {data['people'][0]['craft']}: {data['number']}")
    for astro in data["people"]:
        print(f"- {astro['name']}")


if __name__ == '__main__':
    main()

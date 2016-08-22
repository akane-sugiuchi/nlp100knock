# -*- coding: utf-8 -*-
def show_weather(x,y,z):
    return  "{}時の".format(x) + y + "は{}".format(z)

if __name__ == "__main__":
    x = 12
    y = "気温"
    z = 22.4
    print (show_weather(x,y,z))

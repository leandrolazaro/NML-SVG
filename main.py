import svg
import random
import json

def main():

    """
    Try out the SVG class by calling function to
    create and save a few drawings.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| SVG Library   |")
    print("-----------------")

    draw_all_shapes()

    i_want_to_believe()

    mondrian()


def draw_all_shapes():

    """
    Quick demo of creating SVG object, using all methods,
    and saving the finished file.
    """

    s = svg.SVG()

    s.create(256, 192)

    s.fill("#A0A0FF")
    s.circle("#000080", 4, "#0000FF", 32, 64, 96)
    s.line("#000000", 2, 8, 8, 248, 184)
    s.rectangle(64, 64, 112, 32, "#00FF00", "#008000", 4, 4, 4)
    s.text(32, 16, "sans-serif", 16, "#000000", "#000000", "codedrome.com")
    s.ellipse(64, 160, 32, 16, "#FF0000", "#800000", 4)

    s.finalize()

    try:
        s.save("allshapes.svg")
    except IOError as ioe:
        print(ioe)

    print(s)

def i_want_to_believe():

    """
    A more complex drawing for X Files fans.
    """

    s = svg.SVG()

    s.create(512, 768)

    s.fill("#000010");

    for star in range(0, 512):

        x = random.randrange(0, 512)
        y = random.randrange(0, 768)

        s.rectangle(1, 1, x, y, "white", "white", 0, 0, 0)

    s.text(96, 712, "sans-serif", 32, "#FFFFFF", "#FFFFFF", "I WANT TO BELIEVE")

    s.circle("silver", 1, "rgba(0,0,0,0)", 28, 256, 384)

    s.ellipse(256, 374, 8, 14, "#808080", "#808080", 0)
    s.ellipse(252, 372, 3, 2, "#000000", "#000000", 0)
    s.ellipse(260, 372, 3, 2, "#000000", "#000000", 0)
    s.rectangle(1, 1, 251, 371, "white", "white", 0, 0, 0)
    s.rectangle(1, 1, 259, 371, "white", "white", 0, 0, 0)
    s.line("black", 2, 254, 378, 258, 378)

    s.line("silver", 2, 234, 416, 226, 432)
    s.line("silver", 2, 278, 416, 286, 432)
    s.ellipse(256, 400, 64, 16, "silver", "silver", 4)

    s.finalize()

    try:
        s.save("iwanttobelieve.svg")
    except IOError as ioe:
        print(ioe)


def mondrian():

    bancs=[[0,1,2],[0,2,1],[2,0,1],[2,1,0],[1,2,0],[1,0,2]]

    inicio_zona_clock_x=-8*0.3333333333
    inicio_zona_clock_y=-6*0.333333

    posicaoinicialx_circuito=1
    posicaoinicialy_circuito=2

    cores_zona_clock=["white", "#bebebe", "#565656"]

    cores_clock=["#0cf60c", "#0405f2", "#f408f4"]

    escala=100

    a=0

    s = svg.SVG()

    with open('c17withoutcells') as json_file:
        data = json.load(json_file)
    for p in data:
        if a==0:
            s.create(int(p['numberX'])*escala*3, int(p['numberY'])*escala*6)
            s.fill("white")
            s.rectangle(int(p['numberX'])*escala, int(p['numberY'])*escala, 0, 0, "white", "black", 1, 0, 0)
            for i in range(10):
                for j in range(10):
                    for k in range(6):
                        for l in range(3):
                            s.rectangle(escala*3, (escala*2)*3, (inicio_zona_clock_x*3+j+l)*(escala*3)+(escala*6*j), (inicio_zona_clock_y*6+i+k)*((escala*2)*3)+(escala*6*5*i), cores_zona_clock[bancs[k][l]], "black", 0, 0, 0)        

            a=1
        else:
            if(str(p['logic'])=="cross"):
                s.rectangle(escala, (escala), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+escala/2, cores_clock[int(p['clock_zone'])], cores_clock[int(p['clock_zone'])], 0, 0, 0)
                s.line("black", (escala/8), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+escala/2, (int(p['x'])*escala)+(escala*posicaoinicialx_circuito)+escala, (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+escala/2)
                s.line("black", (escala/8), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+escala/2, (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+escala/2+(escala))
                s.line("black", (escala/8), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+escala/2+(escala), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito)+escala, (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+escala/2+(escala))
                s.line("black", (escala/8), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito)+escala, (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+escala/2+(escala), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito)+escala, (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+escala/2)
            else:
                s.rectangle(escala, (escala*2), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2), cores_clock[int(p['clock_zone'])], cores_clock[int(p['clock_zone'])], 0, 0, 0)

                s.line("black", (escala/8), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito)+escala, (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2))
                s.line("black", (escala/8), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+(escala*2))
                s.line("black", (escala/8), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito), (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+(escala*2), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito)+escala, (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+(escala*2))
                s.line("black", (escala/8), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito)+escala, (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2)+(escala*2), (int(p['x'])*escala)+(escala*posicaoinicialx_circuito)+escala, (int(p['y'])*(escala*2))+(escala*posicaoinicialy_circuito*2))

                if(p['type']!="regular"):
                    s.text((int(p['x'])*escala)+(escala*posicaoinicialx_circuito)+(escala/7), (int(p['y'])*(escala*2)+(escala*posicaoinicialy_circuito*2)+escala), "sans-serif", escala/1.5, "#FFFFFF", "#000000", str(p['id']))
                print('fixed_magnetization: ' + str(p['fixed_magnetization']))

    s.finalize()

    try:
        s.save("c17withoutcells.svg")
    except IOError as ioe:
        print(ioe)


main()


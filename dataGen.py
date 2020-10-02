from sense_hat import SenseHat
import math
import time
import csv
import atexit


red = [100, 0, 0]
green = [0, 100, 0]
blank = [0, 0, 0]

acts = ["start", "exit"]  # Expected activities

sense = SenseHat()
atexit.register(sense.clear)

while True:
    run = False
    c = 0
    sense.show_letter(acts[c][0], green)

    while not run:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                d = event.direction
                if d == "middle":
                    run = True if acts[c] != "e" else exit()
                    continue
                c = (
                    c + 1) % len(acts) if d in ["right", "up"] else (c-1) % len(acts)
                sense.show_letter(acts[c][0], green)

    # Creating csv file for logging of data
    file = "./" + time.strftime("%d-%m-%Y-%H:%M:%S") + ".csv"
    f = open(file, "w", newline="")
    dataCSV = csv.writer(f)

    labels = ["x", "y", "z"] #Change this part here according to what your team needs to collect.
    dataCSV.writerow(labels)

    sense.set_pixels([red for x in range(64)])
    while run:
        xc = (xc + 1) % len(crosses)
        data = <ENTER YOUR FUNCTION HERE> #Change this part here according to what your team needs to collect.
        x = <GET THE VALUE HERE> #Change this part here according to what your team needs to collect.
        y = <GET THE VALUE HERE> #Change this part here according to what your team needs to collect.
        z = <GET THE VALUE HERE> #Change this part here according to what your team needs to collect.

        dataCSV.writerow([x, y, z])

        for event in sense.stick.get_events():
            run = False if event.action == "pressed" and event.direction == "middle" else True

    sense.clear()
    f.close()

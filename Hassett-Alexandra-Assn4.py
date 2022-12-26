oil = 0  # oil starts empty
fuel = 0  # fuel starts empty
fuelCutoff = True  # fuel cutoff valve starts closed
choke = False  # choke starts off and not engaged
throttle = False  # throttle started retarded
engine = False  # engine starts off
generator = False  # generator engage starts off
breaker = False  # breaker engage starts off
lights = False  # lights start off
done = False  # whether we have successfully turned on the lights or not


def panel():  # print current state of operating features
    print(format("Oil Level:", ">30s"), end="   ")
    if oil == 0:
        print(">>EMPTY<<")
    else:
        print(str(oil) + " quarts")

    print(format("Fuel Level:", ">30s"), end="   ")
    if fuel == 0:
        print(">>EMPTY<<")
    else:
        print(str(fuel) + " gallons")

    print(format("Throttle:", ">30s"), end="   ")
    if throttle:
        print("advanced")
    else:
        print("not advanced")

    print(format("Choke:", ">30s"), end="   ")
    if choke:
        print("engaged")
    else:
        print("not engaged")

    print(format("Fuel Cutoff:", ">30s"), end="   ")
    if fuelCutoff:
        print("fuel off")
    else:
        print("fuel on")

    print(format("Generator:", ">30s"), end="   ")
    if generator:
        print("engaged")
    else:
        print("not engaged")

    print(format("Breakers:", ">30s"), end="   ")
    if breaker:
        print("engaged")
    else:
        print("not engaged")

    print(format("The engine is:", ">30s"), end="   ")
    if engine:
        if throttle:
            print(">>Running<<")
        else:
            print(">>Idle<<")
    else:
        print(">>Not Running<<")

    print(format("The generator is:", ">30s"), end="   ")
    if generator:
        print(">>Spinning<<")
    else:
        print(">>Not Spinning<<")

    print(format("The lights are:", ">30s"), end="   ")
    if lights:
        print(">>On<<\n")
    else:
        print(">>Off<<\n")
    print()


def menu():
    print(format("s - starter button", "<45s"), "b - breaker engage on/off")
    print(format("t - advance/retard throttle", "<45s"), "f - add diesel fuel")
    print(format("c - choke on/off", "<45s"), "o - add oil")
    print(format("v - fuel cutoff value open/closed", "<45s"), "w - wait")
    print(format("g - generator engage on/off", "<45s"), "q - quit\n")
    print(format("p - panel", "<45s"), "m - menu")
    print()


# welcome message
print("You have washed up on an abandoned island in the Caribbean. Your mission is to use the broken down", end=" ")
print("generator to turn on the lights and find your way home.")

panel()
menu()

while not done:
    r = input("How would you like to proceed? ")
    r = r.lower()

    # add fuel and alert user when fuel tank is full
    if r == "f" and fuel < 5:
        fuel += 1
        print("Fuel was added successfully")
    elif r == "f":
        print("Fuel is at max capacity")

    # add oil and alert user when oil tank is full
    if r == "o" and oil < 3:
        oil += 1
        print("Oil was added successfully")
    elif r == "o":
        print("Oil is at max capacity")

    # open and close the fuel valve
    if r == "v":
        if fuelCutoff:
            fuelCutoff = False
            print("Fuel valve is open")
        else:
            fuelCutoff = True
            print("Fuel valve is closed")

    # turn choke on and off
    if r == "c":
        if choke:
            choke = False
            print("Choke is no longer engaged")
        else:
            choke = True
            print("Choke is now engaged")
            # if engine and throttle are both on when we turn on choke, kill the engine
            if engine and throttle:
                engine = False
                print("Engine has died")

    # turn throttle on and off
    if r == "t":
        if throttle:
            throttle = False
            print("Throttle is no longer advanced")
            # if engine is on when throttle turns off, send the engine to an idle state
            if engine:
                print("Engine slows down to idle")
        else:
            throttle = True
            # if engine is on and choke is not, speed up the engine when throttle is engaged
            if engine and not choke:
                print("Throttle is now engaged and engine is up to speed")
            # if engine and choke are on when throttle is turn on, kill the engine
            elif engine and choke:
                engine = False
                print("Engine has died")
            else:
                print("Throttle is now engaged")

    # when starter button is pressed, turn on engine if we have oil and fuel, fuel valve open, choke on, throttle on
    if r == "s":
        if oil > 0 and fuel > 0 and not fuelCutoff and choke and not throttle and not engine:
            engine = True
            print("The engine is on!")
        # if starter button is pressed when engine already started
        elif engine:
            print("The already running engine is making scratching noises")
        # if incorrect conditions, let user know
        if oil == 0:
            print("You can hear the pistons scraping in their cylinders")
        if fuel == 0 or fuelCutoff or not choke or throttle:
            print("The engine refuses to start")

    if r == "g":
        # if generator is on and we turn it off, turn off the breakers and lights with it
        if generator:
            generator = False
            breaker = False
            lights = False
            print("Generator has been disengaged")
        # if engine is at operating speed, we turn on the generator
        elif engine and throttle and not generator:
            generator = True
            print("Generator is up and running. We have electricity!")
        # if engine is idle, kill the engine completely when we try to turn on generator
        elif not generator and engine and not throttle:
            engine = False
            print("Engine has died")
        else:
            print("Generator cannot turn on until engine is running at operating speed")

    # turn breakers on and off
    if r == "b":
        if breaker:
            breaker = False
            print("The breakers are no longer engaged")
            print("Lights turn off")
        # successfully turn on breakers and lights if generator is already on
        elif generator and not breaker:
            breaker = True
            lights = True
            print("The breakers are engaged and the lights are ON!")
            print("Enter quit [q] to exit game")
        else:
            print("Breakers cannot be engaged until generator is on")

    # wait for a theoretical hour and use up some fuel and oil
    if r == "w":
        if oil == 0:
            print("Waiting for an hour cost you oil. Refill to continue")
        else:
            oil -= 1
        if fuel == 0:
            print("Waiting for an hour cost you fuel. Refill to continue")
        else:
            fuel -= 1

    # print panel of current states
    if r == "p":
        panel()

    # print menu of command letters
    if r == "m":
        menu()

    # exit the game
    if r == "q":
        done = True

    # if user inputs anything other than predetermined commands, suggest they look at menu
    if r != "s" and r != "t" and r != "f" and r != "c" and r != "o" and r != "v" and r != "w" and r != "q" and r != "p" and r != "m" and r != "b" and r != "g":
        print("?")
        print("Print menu [m] to see commands")

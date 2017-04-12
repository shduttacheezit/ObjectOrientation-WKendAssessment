# This game is called the Primary Color Adventure!

color = int(raw_input("Hi there! Pick a primary color. 1 - Red, 2 - Blue and 3 - Yellow "))


if color == 1:
    print "Red it is. Now pick another primary color."
    print "\n"
    print '1. Red'
    print '2. Blue'
    print '3. Yellow'

    Rcolor = int(raw_input("> "))

    if Rcolor == 1:
        print "Red again. In a fiery mood, eh?"
        print "Birds of a feather flock together does not work here. Game over! You lose!"

    elif Rcolor == 2:
        print "You picked blue! Cool. Red and blue make purple. One purple star for you!"

    else:
        print "Woohoo! Red and yellow get you an orange star. Orange you glad you picked yellow?"

elif color == 2: 
    print "Blue it is. Now pick another primary color."
    print "\n"
    print '1. Red'
    print '2. Blue'
    print '3. Yellow'

    Bcolor = int(raw_input(">"))

    if Bcolor == 1:
        print "Red! Red and blue give you a purple star! Great job!"

    elif Bcolor == 2:
        print "Feeling blue? Well sorry to make you bluer, but you lose! Game over!"

    else:
        print "Alright! blue and yellow will give you green. One green star for you!"

else:
    print "Yeeeelllow, you picked yellow! Okay, now pick another primary color."
    print "\n"
    print '1. Red'
    print '2. Blue'
    print '3. Yellow'

    Ycolor = int(raw_input(">"))

    if Ycolor == 1: 
        print "Red and yellow, red and yellow, red and yellow: gets you an orange star!"

    elif Ycolor == 2: 
        print "Blue on top of yellow. Say hello to your green star!"

    else:
        print "Too much yellow makes Jack a dull boy. You lose! Game over."



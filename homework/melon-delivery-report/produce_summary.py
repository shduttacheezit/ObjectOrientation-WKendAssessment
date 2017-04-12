def melonsummary(date, the_file):
    print "Day", date

    date = 
    the_file = open(the_file)

    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered %s %ss for total of ${}" % (count, melon, amount)

    the_file.close()


melonsummary(19, "um-deliveries-20140519.txt")
melonsummary(20, "um-deliveries-20140520.txt")
melonsummary(21, "um-deliveries-20140521.txt")

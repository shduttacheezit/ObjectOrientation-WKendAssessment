
def melon_tallies(type_order_file):
    """Return tallies of each melon"""

    type_order= open(type_order_file)

    tallies = {"Musk": 0,
               "Hybrid": 0,
               "Watermelon": 0,
               "Winter": 0}

    for line in type_order:
        data = line.split("|")
        mtype = data[1]
        count = int(data[2])
        tallies[mtype] = tallies[mtype] + count

    type_order.close()

    return tallies


def revenue(tallies):
    """Return total revenue for each melon type"""
    total_revenue = 0
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue = total_revenue + revenue
        # print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
        print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)

    return total_revenue

def salesvsinternet(sales_file):
    """Return comparisons of salestaff and online"""

    sales = open(sales_file)

    online_revenue = 0 
    sales_revenue = 0
    
    for line in sales:
        data = line.split("|")
        if data[2] == "ONLINE":
            online_revenue += float(data[3])
        else: 
            sales_revenue += float(data[3])

    print "Salespeople generated ${:.2f} in revenue.".format(sales[1])
    print "Internet sales generated ${:.2f} in revenue.".format(sales[0])

    if sales_revenue > online_revenue:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

    sales_file.close

melon_tallies = melon_tallies("orders-by-type.txt")

revenue(melon_tallies)

print

salesvsinternet("orders-with-sales.txt")




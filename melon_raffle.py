"""Randomly pick customer and print customer info"""

# Add code starting here
# Hint: remember to import any functions you need from
    # other files or libraries
from random import choice
from customer_info import organize_customer_data

def winner(customers):
    chosen_one = choice(customers)
    print "The winner is %s, they can be reached at %s" % (chosen_one.name, chosen_one.email)


customers = organize_customer_data('customers.txt')

winner(customers)
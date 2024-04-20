"""Module providing a function."""
import random as r

def get_numbers_ticket(min, max, quantity):
    """Function generationg set of unique numbers."""
    # check parameters
    if min < 1 or max > 1000 or (quantity < min or quantity > max):
        return[]

    # generation of the set
    numbers = set()
    while len(numbers) < quantity:
        number = r.randint(min, max)
        # check existence the number in the set
        if number not in numbers:
            numbers.add(number)
    
    return sorted(numbers)
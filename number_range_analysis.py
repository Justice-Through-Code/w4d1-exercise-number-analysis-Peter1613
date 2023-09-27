#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION


def calculate_sum(start, end):
            num_add = 0
            for num in range(start, end + 1):
                num_add = num_add + num
            return(num_add)

    # if our arguments are 1 and 4, num will iterate through the range of numbers from 1 - 4 and add one 
    # number to the next as it goes through for a total of 10. As it stores the newest total in num_add, 
    # num will be 0 and add 1 to itself, num will be 1 and add 2 to itself, num will be 3 and add 3 to
    # itself, and then num will be 6 and add 4 to itself, giving us 10
    # My code adds 1 to end so that, for my example, 5 is calculated as the end range number 
    # typed by user, otherwise range would stop at 4.
     
# calculate_sum()

    # calculate_sum() Type in your arguments here - start number, and then type in your end number. 
    # For example, if you want to add the range of numbers 1 through 4, type in (1,4)
    # in the parenthesis next to calculate_sum so that it is calculate_sum(1,4). 1 and 4
    # are your arguments. 
    
"""Sorry, I had to de-indent the triple quotes because of red underline message.
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.

def find_smallest_number(start, end):
    num_small = start
    for num in range(start, end):
        if num < num_small:
            num_small = num  # Update num_small if a smaller number is found
    
    return(num_small)

# The specified range is start through end and I used start as my first element to initialize accumulator. I tested 
# the function with the arguments 100 and 200 and printed out 100. num checks the start element against every number 
# in the range up until the end element. num stores the smaller number of each comparison in num_small. In this example, 100 
# always ended up as the stored value when compared to 101, 102, etc. because it's smaller. 

# find_smallest_number()
    
"""Sorry, I had to de-indent the triple quotes because of red underline message.
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.

def find_largest_number(start, end):
        num_larg = end
        for num in range(start, end):
            if num > num_larg:
                num_larg = num  # Update num_larg if a larger number is found
    
        return(num_larg)

# The specified range is start through end and I used end as my first element to initialize accumulator. I tested 
# the function with the arguments 100 and 200 and printed out 200. num checks the start element against every number 
# in the range up until the end element. num stores the larger number of each comparison in num_larg. In this example, 200 
# always ended up as the stored value when compared to 101, 199, etc. because it's larger. 

# find_largest_number()

""" # Sorry, I had to de-indent the triple quotes because of red underline message.
#     """
#     # Find the largest number within the specified range.

#     # Args:
#         # start (int): The starting number of the range ( inclusive).
#         # end (int): The ending number of the range (inclusive).

#     Return:
#         int: The largest number within the range.
#     """
#     # TODO: Implement the logic to find the largest number within the range.
#     # TODO: Return the found largest number.

def count_even_numbers(start, end):
    accum_even = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            accum_even = accum_even + 1
    
    return(accum_even)

# I started with the accumulator accum_even which I initialized with 0 because it is my counter.
# Each time num iterates through my range and finds an even number, it adds one to itself. Since
# it started at 0, accum_even gives us a count of the number of even numbers. num checks each number
# by dividing it by 2 to see if it has a remainder. Only numbers with 0 as remainder are counted because
# even numbers are even because they are evenly divisible by 2. I tested the count_even_numbers function
# using 1 and 11 and received output 5.

# count_even_numbers()

#     Count the number of even numbers within the specified range.

    # Args:
    #     start (int): The starting number of the range (inclusive).
    #     end (int): The ending number of the range (inclusive).

    # Return:
    #     int: The count of even numbers within the range.
    
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.


def count_odd_numbers(start, end):
    accum_odd = 0
    for num in range(start, end + 1):
        if num % 2 >= 1:
            accum_odd = accum_odd + 1
    
    return(accum_odd)

# I started with the accumulator accum_odd which I initialized with 0 because it is my counter.
# Each time num iterates through my range and finds an odd number, it adds one to itself. Since
# it started at 0, accum_odd gives us a count of the number of odd numbers. num checks each number
# by dividing it by 2 to see if it has a remainder. Only numbers with 1 or more as remainder are counted because
# only odd numbers have remainders. Even numbers do not. I tested the count_even_numbers function
# using 1 and 11 and received output 5, which is wrong. I then realized that the end parameter in my for loop
# had to be end + 1. I ran it again and received correct answer 6.
    
# count_odd_numbers()

    # Count the number of odd numbers within the specified range.

    # Args:
    #     start (int): The starting number of the range (inclusive).
    #     end (int): The ending number of the range (inclusive).

    # Return:
    #     int: The count of odd numbers within the range.
    # """
    # # TODO: Implement the logic to count odd numbers within the range.
    # # TODO: Return the count of odd numbers.
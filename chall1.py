#Create a function that takes two numbers as arguments and returns their sum.

def addition(a, b):
	return a + b

#Write a function that takes an integer minutes and converts it to seconds.

def convert(minutes):
    return minutes * 60

#Create a function that takes a number as an argument, increments the number by +1 and returns the result.
def addition(num):
    return num + 1

#Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).
def sum_polygon(n):
    if n < 3:
        return 0
    return (n - 2) * 180

#Create a function that takes the age in years and returns the age in days.
def calc_age(age):
	return age * 365

#Write a function that converts hours into seconds.
def how_many_seconds(hours):
    return hours * 3600

#Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.
#squared(5) ➞ 25
def squared(a):
	return a * a

#Create a function that takes voltage and current and returns the calculated power.
def circuit_power(voltage, current):
    return voltage * current

#There is a single operator in Python, capable of providing the remainder of a division operation. Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.
def remainder(x, y):
    return x % y

#Create a function that takes a base number and an exponent number and returns the calculation.
def calculate_exponent(num, exp):
    return num ** exp
#this is num to power of num

#Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
def football_points(wins, draws, losses):
    return (wins * 3) + (draws * 1) + (losses * 0)

#Create a function that takes a boolean variable flag and returns it as a string.
def bool_to_string(flag):
    if flag:
        return "True"
    else:
        return "False"
#right ans
def bool_to_string(flag):
  return str(flag)

g
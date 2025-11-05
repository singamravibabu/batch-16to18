'''This file contains two functions.
One for converting Celsius to Fahrenheit
and another for converting Fahrenheit to Celsius.
However, we will add more measures in the future.'''

def to_fahrenheit(celsius):
    'This function converts Celsius to Fahrenheit'
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def to_celsius(fahrenheit):
    'This function converts Fahrenheit to Celsius'
    celsius = (fahrenheit - 32) * 5/9
    return celsius

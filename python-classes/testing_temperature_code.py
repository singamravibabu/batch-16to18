import temperature as t

for i in range(-40, 101, 20):
    result = t.to_celsius(i)
    print(f"{i} Fahrenheit is {result} Celsius")
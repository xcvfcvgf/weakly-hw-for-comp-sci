import math

print("Estimating π with François Viète's Infinite Product")

n = int(input("How many times do you want to repeat. POI the more time the code repeats, the more accurate the result will be"))

product = 1
value = math.sqrt(2)



for i in range(n):
    product = product * (value /2)
    value = math.sqrt(2 + value)

    
est_value_pi = 2/product


print(est_value_pi)

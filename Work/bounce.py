# bounce.py
#
# Exercise 1.5

initial_height = 100
boucing_factor = 0.6


for i in range(10):
    initial_height = initial_height * boucing_factor
    print(round(initial_height,4))


import pandas as pd
import math
import random
import time
import numpy as np


# population = pd.read_csv('data/population.csv')
# global_pop = population[population["Entity"] == "World"]
# global_pop = global_pop.rename(columns={"Population (historical estimates)":"pop"})
# # print(global_pop)
# global_pop_per_year = global_pop.pivot_table(index = "Year", values = "pop")
# pd.set_option('display.max_rows', 260)
# print(global_pop_per_year.tail())
# print(global_population["Year"], global_population["Population)"])


# quick sketch, based on the theory of a bottleneck around 700-800 thousand years ago:

# initial_population = 1280
# target_population = 7e9
# average_generation_time_years = 22.5
# r = math.log(3) / average_generation_time_years   # growth rate per generation (r)
# num_generations = math.log(target_population / initial_population) / math.log(1 + r)
# print("Number of generations:", num_generations)
# maths seems too generous, on reflection - pairs have kids, not people, and not all kids survive 
# model also gives 325 generations (or 7322.4 years) to reach 7bn, and that is clearly way too fast
# i was expecting the time required to reach pop to be less than the time actually
# taken, as the numebrs involved when calcualating ancestors (via 2^n) make shared 
# ancestry mathematically inevitable - those 1280 will have had kids, yeah, and those kids will have had kids, 
# but they will have had them with each other, and therefore the number  wont go up 'math.log(3)'


# ----------------------------------------------------------------

# t0 = time.perf_counter()

population = 1280
generations = 0

while population < 7000000000: 
    new_births = (5 * (population // 2))
    population += new_births * random.uniform(0,1)
    generations += 1
    
# t1 = time.perf_counter()
# print(t0, t1)

print(f"Population reached 7 billion in approximately {generations} generations.")



# when running it, this seems to be a bit unwieldy. the iteration count is pretty high to get to 7Bn, given 
# the mortality reduction, but i'm not sure how to reduce the iteration weight, or why it should need to be 
# adjusted - yes, 7bn is a big number, but it seems quite basic maths, wonder what i am missig 
# fixed; issue was the maths was wrong, a fairly basic/late night error: i was reducing the popluation too much, and so making it very slow to get to 7bn


# ----------------------------------------------------------------













# import math
# import time

# def calculate_population(t, P0, r):
#     K = 10e9  # Carrying capacity set to a large number
#     return K / (1 + ((K - P0) / P0) * math.exp(-r * t))

# t0 = time.perf_counter()

# P0 = 690
# average_generation_time_years = 25
# r = math.log(3) / average_generation_time_years

# t = 0
# while P0 < 7e9:  # Continue until the population reaches 7 billion
#     P0 = calculate_population(t, P0, r)
#     t += 1

# t1 = time.perf_counter()

# print(t0, t1)
# print(f"Population reached 7 billion in approximately {t} generations.")


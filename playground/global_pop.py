import pandas as pd
import math
import time

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




t0 = time.perf_counter()

pairs = 690
children_per_pair = 5
infant_mortality_rate = 0.4999
generations = 0
population = pairs * children_per_pair

while population < 7000000000:
    t1 = time.perf_counter()
    
    new_births = pairs * children_per_pair
    population += new_births
    deaths_due_to_mortality = population * infant_mortality_rate
    population -= deaths_due_to_mortality
    pairs = population // children_per_pair
    generations += 1
    t2 = time.perf_counter()
print(t0, t1, t2, t2-t0)
print(f"Population reached 7 billion in approximately {generations} generations.")

# this seems to be a bit unwieldy, the iteration count is pretty high to get to 7Bn, given 
# the mortality reduction, but i'm not sure how to reduce the iteration weight
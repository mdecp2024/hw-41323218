import math
 
# Given data
initial_population = 100  # initial population (P0)
target_population = 50000  # target population (P)
doubling_time = 3  # doubling time in hours (T)
 
# Solving for time (t) using the formula
time_required = doubling_time * (math.log(target_population / initial_population) / math.log(2))
 
print(f"The population will first reach 50,000 in approximately {time_required:.2f} hours.")


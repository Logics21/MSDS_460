import pandas as pd
import numpy as np
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize


# Creating a pandas DataFrame
Daily_req_db = pd.DataFrame({
    'Component': ['Sodium', 'Energy', 'Protein', 'Vitamin D', 'Calcium', 'Iron', 'Potassium', 'Cost per serving'],
    'Max/Min': ['Maximum', 'Minimum', 'Minimum', 'Minimum', 'Minimum', 'Minimum', 'Minimum','n/a'],
    'Daily Amount and measure': ['5000 milligrams (mg)', '2000 Calories (kilocalories, kcal)', '50 grams (g)',
                                 '20 micrograms (mcg)', '1,300 milligrams (mg)', '18 milligrams (mg)',
                                 '4700 milligrams (mg)',"dollars ($)"],
    'Cerial': ['2.7 %', '6.5 %', '4 %', '10 %', '0 %', '60 %', '1.38 %','.25'],
    'Chicken': ['.8 %', '7 %', '50 %', '0 %', '0 %', '0 %', '0 %','.89'],
    'Eggs': ['1.4 %', '3.5 %', '12 %', '5 %', '0 %', '5 %', '0 %','.22'],
    'Beef': ['1.5 %', '8.5 %', '46 %', '0 %', '0 %', '15 %', '0 %','1.49'],
    'Milk': ['3.2 %', '6.5 %', '16 %', '10 %', '25 %', '0 %', '8 %','.17'],
    'Veggies': ['.3 %', '1.75 %', '4 %', '2 %', '0 %', '3.9 %', '4.6 %','.36'],
    'Pancakes': ['9.8 %', '8 %', '10 %', '0 %', '4.6 %', '8.8 %', '1 %','.16'],
    'Pasta': ['0 %', '10 %', '14 %', '0 %', '0 %', '11 %', '2.5 %','.22'],
    'Protein Bar': ['11 %', '12 %', '32 %', '0 %', '4.6 %', '8.8 %', '4.6 %','1.8'],
    'Rice': ['0 %', '8 %', '6 %', '0 %', '0 %', '5.6 %', '1.1 %','.1']
})

# Remove the percentage sign from all columns except 'Component', 'Max/Min', and 'Daily Amount and measure'
Daily_req_db.iloc[:, 3:] = Daily_req_db.iloc[:, 3:].apply(lambda x: pd.to_numeric(x.str.rstrip(' %')))

# Create meals
Daily_req_db['Meal a'] = Daily_req_db['Chicken'] + Daily_req_db['Rice'] + Daily_req_db['Veggies']
Daily_req_db['Meal b'] = Daily_req_db['Beef'] + Daily_req_db['Pasta']
Daily_req_db['Meal c'] = Daily_req_db['Cerial'] + Daily_req_db['Milk']
Daily_req_db['Meal d'] = Daily_req_db['Protein Bar']
Daily_req_db['Meal e'] = Daily_req_db['Eggs'] + Daily_req_db['Pancakes']


Meal_table = Daily_req_db[['Component', 'Meal a', 'Meal b', 'Meal c', 'Meal d', 'Meal e']].copy()

# define variables
meal_a = LpVariable("Meal a", 0, None)  # Meal a >= 0
meal_b = LpVariable("Meal b", 0, None)  # Meal b >= 0
meal_c = LpVariable("Meal c", 0, None)  # Meal c >= 0
meal_d = LpVariable("Meal d", 0, None)  # Meal d >= 0
meal_e = LpVariable("Meal e", 0, None)  # Meal e >= 0

# defines the problem
prob = LpProblem("problem", LpMinimize)

# define constraints
prob += 1.1 * meal_a + 1.5 * meal_b + 5.9 * meal_c + 11.0 * meal_d + 11.2 * meal_e <= 100  # sodium
prob += 16.75 * meal_a + 18.5 * meal_b + 13.0 * meal_c + 12.0 * meal_d + 11.5 * meal_e >= 100  # Energy
prob += 60.0 * meal_a + 60.0 * meal_b + 20.0 * meal_c + 32.0 * meal_d + 22.0 * meal_e >= 100  # Protein
prob += 2.0 * meal_a + 0 * meal_b + 20 * meal_c + 0 * meal_c + 5 * meal_e >= 100  # Vitamin D
prob += 0 * meal_a + 0 * meal_b + 25 * meal_c + 4.6 * meal_c + 4.6 * meal_e >= 100  # Calcium
prob += 9.5 * meal_a + 26.0 * meal_b + 60.0 * meal_c + 8.8 * meal_c + 13.8 * meal_e >= 100  # Iron
prob += 5.7 * meal_a + 2.5 * meal_b + 9.38 * meal_c + 4.6 * meal_c + 1.0 * meal_e >= 100  # Potassium



# define objective function
prob += 1.35 * meal_a + 1.71 * meal_b + 0.42 * meal_c + 1.8 * meal_d + 0.38 * meal_e

# solve the problem
status = prob.solve()
print(f"Problem 1")
print(f"status={LpStatus[status]}")

# print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Objective = {value(prob.objective)}")
print(f"")


#Meal_list = ["meal_a","meal_a","meal_a","meal_a","meal_a","meal_a","meal_a"]



for i in range(1,8): #iterate throught number of days

# define variables
    meal_a = LpVariable("Meal a", 0, None)  # Meal a >= 0
    meal_b = LpVariable("Meal b", 0, None)  # Meal b >= 0
    meal_c = LpVariable("Meal c", 0, None)  # Meal c >= 0
    meal_d = LpVariable("Meal d", 0, None)  # Meal d >= 0
    meal_e = LpVariable("Meal e", 0, None)  # Meal e >= 0

# defines the problem
    prob = LpProblem("problem", LpMinimize)

# define constraints
    
    
    prob += 1.1 * meal_a + 1.5 * meal_b + 5.9 * meal_c + 11.0 * meal_d + 11.2 * meal_e <= 100  # sodium
    prob += 16.75 * meal_a + 18.5 * meal_b + 13.0 * meal_c + 12.0 * meal_d + 11.5 * meal_e >= 100  # Energy
    prob += 60.0 * meal_a + 60.0 * meal_b + 20.0 * meal_c + 32.0 * meal_d + 22.0 * meal_e >= 100  # Protein
    prob += 2.0 * meal_a + 0 * meal_b + 20 * meal_c + 0 * meal_c + 5 * meal_e >= 100  # Vitamin D
    prob += 0 * meal_a + 0 * meal_b + 25 * meal_c + 4.6 * meal_c + 4.6 * meal_e >= 100  # Calcium
    prob += 9.5 * meal_a + 26.0 * meal_b + 60.0 * meal_c + 8.8 * meal_c + 13.8 * meal_e >= 100  # Iron
    prob += 5.7 * meal_a + 2.5 * meal_b + 9.38 * meal_c + 4.6 * meal_c + 1.0 * meal_e >= 100  # Potassium
    
    Meal_list = [meal_a,meal_b,meal_c,meal_d,meal_e]
    
    if i <= len(Meal_list):
        prob += Meal_list[i-1] >= 1  # Minimum item


# define objective function
    prob += 1.35 * meal_a + 1.71 * meal_b + 0.42 * meal_c + 1.8 * meal_d + 0.38 * meal_e

# solve the problem
    status = prob.solve()
    print(f"status={LpStatus[status]}")

# print the results
    for variable in prob.variables():
        print(f"{variable.name} = {variable.varValue}")
            

    print(f"Day {i} Cost = ${value(prob.objective)}")
    print(f"")
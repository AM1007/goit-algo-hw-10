import pulp

# Create the maximization problem
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Decision variables
lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0, cat='Continuous')

# Objective function: maximize the total amount of products
prob += lemonade + fruit_juice, "Total Products Produced"

# Resource constraints
prob += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
prob += 1 * lemonade <= 50, "Sugar Constraint"
prob += 1 * lemonade <= 30, "Lemon Juice Constraint"
prob += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Solve the problem
prob.solve()

# Output the results
print("Status:", pulp.LpStatus[prob.status])
print("Lemonade produced:", pulp.value(lemonade))
print("Fruit juice produced:", pulp.value(fruit_juice))
print("Total products produced:", pulp.value(lemonade + fruit_juice))

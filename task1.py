import pulp

model = pulp.LpProblem("Lemonade", pulp.LpMaximize)  # Максимізація
Limo = pulp.LpVariable('limo', lowBound=0, cat='Integer')
Juice = pulp.LpVariable('juice', lowBound=0, cat='Integer')


model += Limo + Juice, "Profit"

# Додавання обмежень
model += 2 * Limo + 1 * Juice <= 100  # Обмеження для Water №1
model += 1 * Limo <= 50  # Обмеження для Sugar №2
model += 1 * Limo <= 30  # Обмеження для limo_juice №2
model += 2 * Juice <= 40  # Обмеження для puree №2

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Limo:", Limo.varValue)
print("Juice:", Juice.varValue)


# limo = {'water': 2, 'sugar':1, 'juice': 1}
# fruct_saft = {'puree': 1, 'water': 1}
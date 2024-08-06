import random
import matplotlib.pyplot as plt
import pandas as pd

def monte_carlo_simulation(num_simulations):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1

    probabilities = {sum_val: count / num_simulations * 100 for sum_val, count in sum_counts.items()}
    return probabilities

# Виконуємо симуляцію
num_simulations = 100000
simulated_probabilities = monte_carlo_simulation(num_simulations)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Порівняння результатів
sums = list(analytical_probabilities.keys())
analytical_values = list(analytical_probabilities.values())
simulated_values = [simulated_probabilities[sum_val] for sum_val in sums]

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(sums, analytical_values, marker='o', linestyle='-', label='Аналітичні ймовірності')
plt.plot(sums, simulated_values, marker='x', linestyle='--', label='Ймовірності методом Монте-Карло')
plt.xlabel('Сума')
plt.ylabel('Ймовірність (%)')
plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.show()

# Створення таблиці
table_data = {
    'Сума': sums,
    'Аналітична ймовірність (%)': analytical_values,
    'Ймовірність методом Монте-Карло (%)': simulated_values
}
df = pd.DataFrame(table_data)
print(df)

# Запис висновків у файл readme.md
with open("readme.md", "w") as file:
    file.write("# Висновки щодо правильності розрахунків\n\n")
    file.write("## Аналітичні ймовірності та ймовірності, отримані методом Монте-Карло\n\n")
    file.write(df.to_markdown(index=False))
    file.write("\n\n")
    file.write("## Висновки\n")
    file.write("Порівнюючи аналітичні ймовірності та ймовірності, отримані методом Монте-Карло, можна помітити, що результати досить близькі, що підтверджує правильність обчислень. Невеликі відхилення є результатом випадковості симуляції, але з більшим числом симуляцій ці відхилення стають ще меншими.\n")

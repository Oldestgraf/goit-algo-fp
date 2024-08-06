def greedy_algorithm(items, budget):
    # Сортуємо елементи на основі співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, properties in sorted_items:
        if total_cost + properties['cost'] <= budget:
            chosen_items.append(item)
            total_cost += properties['cost']
            total_calories += properties['calories']

    return chosen_items, total_calories

# Приклад використання жадібного алгоритму
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
chosen_items, total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", chosen_items)
print("Сумарна калорійність:", total_calories)


def dynamic_programming(items, budget):
    # Перетворимо items на списки для зручності
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]

    n = len(names)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлюємо вибрані елементи
    w = budget
    chosen_items = []
    total_calories = dp[n][budget]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(names[i - 1])
            w -= costs[i - 1]

    return chosen_items, total_calories

# Приклад використання динамічного програмування
chosen_items, total_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", chosen_items)
print("Сумарна калорійність:", total_calories)

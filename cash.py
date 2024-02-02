from cs50 import get_float


def calculate_quarters(amount):
    return amount // 0.25


def calculate_dimes(amount):
    return amount // 0.10


def calculate_nickles(amount):
    return amount // 0.05


while True:
    change = get_float("Change owed: ")
    if change > 0:
        break

quarters = calculate_quarters(change)
change = round(change - (quarters * 0.25), 2)

dimes = calculate_dimes(change)
change = round(change - (dimes * 0.10), 2)

nickles = calculate_nickles(change)
change = round(change - (nickles * 0.05), 2)

coins = int(quarters + dimes + nickles + (change * 100))

print(f"Change owed: {coins}")

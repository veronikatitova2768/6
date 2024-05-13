import random

# Списки предметов разных качеств
common_items = ["Меч", "Щит", "Посох", "Лук", "Броня"]
rare_items = ["Магический артефакт", "Эликсир здоровья", "Мантия скорости", "Амулет силы"]
epic_items = ["Драконий клинок", "Книга заклинаний", "Артефакт древних", "Кольцо великана"]
legendary_items = ["Меч героя", "Доспехи бессмертных", "Крылья ангела"]

# Шансы выпадения предметов
chance_common = 0.7
chance_rare = 0.2
chance_epic = 0.1
chance_legendary = 0.05

def open_lootbox():
    """Функция открывает лутбокс и возвращает выпавший предмет."""
    rand = random.random()
    if rand < chance_common:
        return random.choice(common_items)
    elif rand < chance_common + chance_rare:
        return random.choice(rare_items)
    elif rand < chance_common + chance_rare + chance_epic:
        return random.choice(epic_items)
    else:
        return random.choice(legendary_items)

def main():
    loot_results = {"Обычные": 0, "Редкие": 0, "Эпические": 0, "Легендарные": 0}
    loot_list = []

    for _ in range(20):
        item = open_lootbox()
        loot_list.append(item)
        if item in common_items:
            loot_results["Обычные"] += 1
        elif item in rare_items:
            loot_results["Редкие"] += 1
        elif item in epic_items:
            loot_results["Эпические"] += 1
        else:
            loot_results["Легендарные"] += 1

    print("Результаты открытия 20 лутбоксов:")
    for rarity, count in loot_results.items():
        print(f"{rarity}: {count}")

    if loot_results["Эпические"] > 3:
        print("(Удача!)")
    if loot_results["Легендарные"] > 1:
        print("(Большая удача!)")

    print("\nПолученные предметы:")
    for item in loot_list:
        if item in common_items:
            print("\033[0m" + item)  # Белый цвет
        elif item in rare_items:
            print("\033[34m" + item)  # Синий цвет
        elif item in epic_items:
            print("\033[35m" + item)  # Фиолетовый цвет
        else:
            print("\033[33m" + item)  # Оранжевый цвет

if __name__ == "__main__":
    main()

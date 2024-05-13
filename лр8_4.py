import random

def generate_doors(num_doors, num_prizes):
    doors = ["пусто"] * num_doors
    prize_indices = random.sample(range(num_doors), num_prizes)
    for idx in prize_indices:
        doors[idx] = "приз"
    return doors

def simulate_game(num_doors, num_prizes):
    doors = generate_doors(num_doors, num_prizes)
    
    # Игроки выбирают двери
    player1_choice = int(input("Игрок 1, выберите номер двери (от 1 до {}): ".format(num_doors))) - 1
    player2_choice = int(input("Игрок 2, выберите номер двери (от 1 до {}): ".format(num_doors))) - 1
    
    # Открывается одна из дверей без приза
    opened_door = random.choice([idx for idx in range(num_doors) if doors[idx] != "приз" and idx != player1_choice])
    
    # Если игрок решает изменить свой выбор, меняем его выбор
    change_choice = input("Игрок 1, хотите ли вы поменять свой выбор? (да/нет): ")
    if change_choice.lower() == "да":
        new_player1_choice = random.choice([idx for idx in range(num_doors) if idx != player1_choice and idx != opened_door])
        player1_choice = new_player1_choice
    
    # Проверяем результаты
    player1_wins = doors[player1_choice] == "приз"
    player2_wins = doors[player2_choice] == "приз"
    
    print("За дверью", opened_door + 1, "нет приза")
    
    if player1_wins:
        if change_choice.lower() == "да":
            print("Игрок 1 решил поменять свой выбор")
        else:
            print("Игрок 1 решил остаться при своем первоначальном выборе")
        print("Игрок 1 выигрывает!")
    else:
        print("Игрок 1 проигрывает.")
        
    if player2_wins:
        print("Игрок 2 выигрывает!")
    else:
        print("Игрок 2 проигрывает.")
    
    print()
    
    return player1_wins, player2_wins

def calculate_win_probabilities(num_doors, num_prizes, num_simulations):
    player1_wins_change = 0
    player2_wins_stay = 0
    
    for _ in range(num_simulations):
        player1_wins, player2_wins = simulate_game(num_doors, num_prizes)
        if player1_wins:
            player1_wins_change += 1
        if player2_wins:
            player2_wins_stay += 1
            
    prob_player1_change = player1_wins_change / num_simulations
    prob_player2_stay = num_prizes / num_doors  # Вероятность выбрать дверь с призом изначально
    
    return prob_player1_change, prob_player2_stay

num_doors = int(input("Введите количество дверей: "))
num_prizes = int(input("Введите количество призов: "))
num_simulations = 3

prob_player1_change, prob_player2_stay = calculate_win_probabilities(num_doors, num_prizes, num_simulations)

print(f"Вероятность выигрыша для игрока, меняющего свой выбор: {prob_player1_change:.4f}")
print(f"Вероятность выигрыша для игрока, оставшегося при своем первоначальном выборе: {prob_player2_stay:.4f}")
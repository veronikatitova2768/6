import random

def throw_ball():
    # Бросок мяча, вероятность поймать - 70%
    if random.random() <= 0.7:
        return True  # Мяч пойман
    else:
        return False  # Мяч не пойман

def computer_response():
    # Выбираем случайный ответ компьютера
    responses = [
        "Я забыл свой пароль, а какой ваш?",
        "Кажется, я перепутал свои биты. А вы?",
        "Интересное имя, но как насчет Вас?",
        "Я могу долго говорить о погоде, но давайте лучше заниматься наукой. Как вас зовут?",
        "Жаль, но мне придется назвать вас компьютером номер 2."
    ]
    return random.choice(responses)

def main():
    print("Игра начинается!")

    history = []  # Список для записи истории

    for turn in range(1, 11):  # Должно быть не меньше 10 ходов
        print("\nХод", turn)

        print("Компьютер бросает мяч:")
        if throw_ball():
            print("    Бросок, вы поймали мяч.")
            answer = input("    Вопрос: Ваше имя?\n    Ответ: ")
            history.append(f"Ход {turn}: Компьютер: Вопрос: Ваше имя? Ответ: {answer}")
        else:
            print("    Бросок, вы не поймали мяч.")
            answer = computer_response()
            print(f"    Вопрос: {answer}")
            computer_answer = input("    Ответ: ")
            history.append(f"Ход {turn}: Компьютер: Вопрос: {answer} Ответ: {computer_answer}")

        print("\nВы бросаете мяч:")
        if throw_ball():
            print("    Бросок, компьютер поймал мяч.")
            answer = input("    Вопрос: Где вы живете?\n    Ответ: ")
            history.append(f"Ход {turn}: Вы: Вопрос: Где вы живете? Ответ: {answer}")
        else:
            print("    Бросок, компьютер не поймал мяч.")
            answer = random.choice(["В каком городе вы родились?", "Какой ваш любимый цвет?"])
            print(f"    Вопрос: {answer}")
            computer_answer = input("    Ответ: ")
            history.append(f"Ход {turn}: Компьютер: Вопрос: {answer} Ответ: {computer_answer}")

    print("\nИгра окончена!")
    print("\nИстория:")
    for item in history:
        print(item)

if __name__ == "__main__":
    main()




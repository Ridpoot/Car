import random
import os
import time


def clear_screen():
    """Очистка экрана."""
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux, macOS
        os.system("clear")


class FootballPlayer:
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills  # Список навыков: [скорость, выносливость, техника]
        self.experience = 0
        self.club = None
        self.salary = 0
        self.injury = False  # У футболиста может быть травма
        self.goals = 0  # Количество голов за карьеру

    def train(self):
        """Тренировка для улучшения навыков."""
        if self.injury:
            print(f"\n{self.name} отдыхает из-за травмы.\n")
            return

        print(f"\n{self.name}, выберите тренировку:")
        print("1. Тренировка на скорость")
        print("2. Тренировка на выносливость")
        print("3. Тренировка на технику")

        try:
            choice = int(input("Введите номер тренировки: "))
            if choice in [1, 2, 3]:
                attribute = ["скорость", "выносливость", "техника"][choice - 1]
                increase = random.randint(1, 2)
                self.skills[choice - 1] = min(10, self.skills[choice - 1] + increase)
                print(f"{attribute.capitalize()} улучшена до {self.skills[choice - 1]}.\n")
                self.experience += random.randint(1, 3)
            else:
                print("Некорректный выбор. Тренировка пропущена.\n")
        except ValueError:
            print("Введите корректный номер тренировки.\n")

    def play_match(self):
        """Играть матч."""
        if self.injury:
            print(f"\n{self.name} не может сыграть из-за травмы.\n")
            return

        opponent_level = random.randint(5, 10)
        performance = (
            sum(self.skills) + self.experience // 10 + random.randint(-2, 2)
        ) // 3

        print(f"\n{self.name} играет матч против соперника уровня {opponent_level}.")
        print(f"Производительность: {performance}")

        if performance > opponent_level + 2:
            print(f"{self.name} забивает гол!\n")
            self.goals += 1
        elif performance < opponent_level - 2:
            print(f"{self.name} проигрывает матч.\n")
        else:
            print(f"{self.name} играет вничью.\n")

        # Шанс на травму
        if random.random() < 0.1:
            self.injury = True
            print(f"{self.name} получил травму!\n")

        self.experience += random.randint(1, 5)

    def recover_from_injury(self):
        """Восстановление после травмы."""
        if self.injury:
            print(f"\n{self.name} восстанавливается от травмы...")
            if random.random() < 0.7:
                self.injury = False
                print("Полное восстановление!\n")
            else:
                print("Восстановление продолжается.\n")

    def __str__(self):
        return (
            f"\nИмя: {self.name}\n"
            f"Возраст: {self.age}\n"
            f"Навыки: Скорость {self.skills[0]}, Выносливость {self.skills[1]}, Техника {self.skills[2]}\n"
            f"Опыт: {self.experience}, Голов: {self.goals}\n"
            f"Клуб: {self.club if self.club else 'Свободный агент'}, Зарплата: {self.salary}\n"
            f"Травма: {'Да' if self.injury else 'Нет'}\n"
        )


class FootballClub:
    def __init__(self, name, level, budget):
        self.name = name
        self.level = level
        self.budget = budget
        self.players = []

    def sign_player(self, player):
        """Подписать игрока."""
        salary_offer = random.randint(5000, 20000)
        if self.budget >= salary_offer:
            self.players.append(player)
            player.club = self.name
            player.salary = salary_offer
            self.budget -= salary_offer
            print(f"\n{self.name} подписал контракт с {player.name} на зарплату {salary_offer}!\n")
        else:
            print(f"\n{self.name} не хватает бюджета на {player.name}.\n")


def career_simulation():
    """Основной цикл симуляции карьеры."""
    clear_screen()
    player_name = input("Введите имя вашего футболиста: ")
    player = FootballPlayer(player_name, 20, [6, 7, 5])
    clubs = [
        FootballClub("Спартак", 4, 200000),
        FootballClub("ЦСКА", 5, 300000),
    ]

    print(f"\nДобро пожаловать, {player.name}! Начнем вашу карьеру.\n")
    time.sleep(2)

    actions = {
        "1": player.train,
        "2": player.play_match,
        "3": lambda: print(player),
        "4": lambda: sign_to_club(player, clubs),
        "5": exit_game,
    }

    while True:
        clear_screen()
        print(player)
        print("Доступные действия:")
        print("1. Тренироваться")
        print("2. Играть матч")
        print("3. Посмотреть статистику")
        print("4. Присоединиться к клубу")
        print("5. Завершить карьеру")

        choice = input("\nВведите номер действия: ")
        action = actions.get(choice, invalid_choice)
        action()


def sign_to_club(player, clubs):
    """Присоединение к клубу."""
    print("\nДоступные клубы:")
    for idx, club in enumerate(clubs, 1):
        print(f"{idx}. {club.name} (Бюджет: {club.budget})")

    try:
        choice = int(input("\nВыберите клуб: "))
        if 1 <= choice <= len(clubs):
            clubs[choice - 1].sign_player(player)
        else:
            print("\nНекорректный выбор.\n")
    except ValueError:
        print("\nВведите корректный номер клуба.\n")


def exit_game():
    """Завершить карьеру."""
    print("\nСпасибо за игру! Удачи в карьере!\n")
    exit()


def invalid_choice():
    """Обработка неверного ввода."""
    print("\nНекорректный выбор. Попробуйте снова.\n")
    time.sleep(1)


# Запуск симуляции
career_simulation()
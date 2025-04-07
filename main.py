import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} единиц урона.")
        print(f"У {other.name} осталось {other.health if other.health > 0 else 0} единиц здоровья.\n")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        # Инициализация героев: игрок вводит имя, компьютер получает имя по умолчанию
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("\nИгра начинается! Битва героев началась.\n")
        round_number = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"--- Раунд {round_number} ---")
            # Ход игрока:
            input("Нажмите Enter для атаки...")
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} пал в бою! Победа за {self.player.name}!")
                break

            # Ход компьютера:
            print("Ход компьютера:")
            # Добавим случайность: иногда компьютер пропускает ход
            if random.choice([True, False]):
                self.computer.attack(self.player)
            else:
                print(f"{self.computer.name} промахивается!\n")
            if not self.player.is_alive():
                print(f"{self.player.name} пал в бою! Победа за {self.computer.name}!")
                break

            round_number += 1

if __name__ == "__main__":
    game = Game()
    game.start()

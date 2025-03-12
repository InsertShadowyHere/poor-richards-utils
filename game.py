# This file contains all the logic required to run a basic game.
# It needs some work.

class Entity:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_entity(self, other):
        other.take_damage(self.attack)


class Player(Entity):
    def __init__(self, name, health, attack, inventory=None):
        super().__init__(name, health, attack)
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add_to_inventory(self, item):
        self.inventory.append(item)


class Enemy(Entity):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)


class Game:
    def __init__(self):
        self.player = None
        self.enemies = []

    def create_player(self, name, health, attack):
        self.player = Player(name, health, attack)

    def add_enemy(self, name, health, attack):
        enemy = Enemy(name, health, attack)
        self.enemies.append(enemy)

    def start_battle(self):
        if not self.player or not self.enemies:
            print("No player or enemies to start the battle.")
            return

        print(f"Battle started between {self.player.name} and enemies!")
        for enemy in self.enemies:
            while self.player.is_alive() and enemy.is_alive():
                self.player.attack_entity(enemy)
                if enemy.is_alive():
                    enemy.attack_entity(self.player)

            if not self.player.is_alive():
                print(f"{self.player.name} has been defeated!")
                break
            else:
                print(f"{enemy.name} has been defeated!")

        if self.player.is_alive():
            print(f"{self.player.name} has won the battle!")
        else:
            print("Enemies have won the battle.")
g = Game()
g.create_player("Player", 100, 10)
g.add_enemy("Enemy1", 50, 5)
g.start_battle()
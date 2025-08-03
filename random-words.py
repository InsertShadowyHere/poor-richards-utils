import random
x = list("I am a very laid-back person who gets along well with most everyone. I am interested in film and television. In my free time I like to spend time with friends, watch movies, play video games, listen to music, and just chill.")
y = []
for _ in range(len(x)):
    a = random.randint(0, len(x) - 1)
    y.append(x[a])
    x.pop(a)
print(''.join(y))
"""
combat (attHack, health, damage)
save/load

Menus we'll need:
player
options
dialogue
HUD


Player (Instance of `Player.tscn`)
├── Enemies (Container for enemy instances)
│   ├── Enemy1 (Instance of `Enemy.tscn`)
│   ├── Enemy2 (Instance of `Enemy.tscn`)
HUD (Instance of `HUD.tscn`)
├── Menus (Instance of `Menus.tscn`)
│   ├── MainMenu (Instance of `MainMenu.tscn`)
│   ├── OptionsMenu (Instance of `OptionsMenu.tscn`)
Level (Instance of `Level1.tscn`)
├── Dialogue (Instance of `Dialogue.tscn`)
├── SaveLoad (Instance of `SaveLoad.tscn`)
"""
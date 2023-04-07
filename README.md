# Sequel "Hero and Monsters 2: Magic Totem" (text game)

The player is a knight in a fantasy world. Your task is to defeat 10 monsters to save the kingdom from attack and thereby win the game.

# Game description:

The game has two types of monsters, each with its own type of attack.

The hero also has a choice of class: he can be a warrior, archer or mage. The class must be selected at the start of the game.

Encountered items can also be different:

```
sword 

bow 

arrows 

book of spells 

apple 

totem 
```

- If the player's class is a warrior, the maximum limit of the random attack index from an encountered sword should be increased. A warrior can randomly defend against close-range attacks.

- If the player's class is an archer, the maximum limit of the random attack index from an encountered bow should be increased. The archer can randomly defend against archer attacks.

- If the player's class is a mage, the maximum limit of the random attack index from an encountered book of spells should be increased. The mage can randomly defend against magical attacks.

- In battle, the hero is offered a choice of attack type. It is not possible to choose an attack for which the weapon is unavailable.

- Regardless of class, the hero starts his journey with a sword.

Attacks are now made step-by-step. After each blow, you can choose another attack if the protagonist and the enemy are still alive. While fighting, there is an option to escape from the enemy.

The totem saves the current game state and reloads it. The totem can be picked up or circumvented. If the hero has a totem - it is possible to reload the game from the moment the previous magical totem was raised upon failure. Reloading is single-use - when using the totem, the save location is lost. You can think of the totem as a one-time save.

# Chosen projection template:

Abstract factory.

# Justification for choosing the design template:

When writing the game, objects will be created (monsters, heroes, weapons). The basic patterns of behavior of each object are the same, their behavior will differ only depending on the choice of object type (for example, hero-mage, monster-archer).

Our abstract factory will create families of objects, and concrete factories for each of their types will be created from it.

Thus, one can implement the open-closed principle, simplify adding new object types, simplify code support.
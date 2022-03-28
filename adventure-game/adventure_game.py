import time
import random

cave_enemies = ["Fairy", "Goblin", "Giant Spider", "Bear", "Dragon"]
house_enemies = ["Witch", "Giant", "Orc", "Robot", "Zombie"]
opponent = ""
enemy_defeated = 0
player_loc = "field"


def validate_input(x):
    validInput = True
    while validInput:
        if x == "1":
            return int(x)
        elif x == "2":
            return int(x)
        else:
            x = input("(Please enter 1 or 2).\n")


def play_again():
    user_input = input("Would you like to play again?\n"
                       "Press 1 to Play Again or 2 to Exit the game.\n")
    user_input = validate_input(user_input)
    if user_input == 2:
        print("You have exited the game.")
        return False
    else:
        return True


def print_pause(text, text1=""):
    print(text, text1)
    time.sleep(1)


def field():
    print_pause("You find yourself standing in an open field, filled with",
                " grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked activities are "
                "happening somewhere around here, and has",
                "been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty steel sword.")


def field1(num_enemy_defeated, new_loc):
    print_pause("You are back to the field where you started your journey.")
    print_pause("You decide visit the nearby village"
                " and tell them of your victory.")
    print_pause("The villagers are happy but they still fear that"
                f" monsters from the {new_loc} might come and "
                "attack them.")
    print_pause("You tell the villagers that tomorrow he will take of "
                f"the monster in the {new_loc}. You rest for the "
                "night.")
    print_pause("The next day you wake up in the morning and prepare"
                f"yourself to fight the monster in the {new_loc}.")
    print_pause("The villagers gather to bid you farewell and the "
                "village head also gives you a shield and a health "
                "potion to aid you in your battles")
    if new_loc == "house":
        cave(num_enemy_defeated, "field")
    elif new_loc == "cave":
        house(num_enemy_defeated, "field")


def house(num_enemy_defeated, loc):
    rand_enemy = random.randint(0, 4)
    opponent = house_enemies[rand_enemy]
    print_pause("You knock on the door and "
                "encounter a", opponent)
    if num_enemy_defeated == 1 and loc == "field":
        fight2(opponent, loc="house")
    else:
        fight(opponent, loc="house", enemy_defeated=0)


def cave(num_enemy_defeated, loc):
    rand_enemy = random.randint(0, 4)
    opponent = cave_enemies[rand_enemy]
    print_pause("You peer into the cave and "
                "encounter a ", opponent)
    if num_enemy_defeated == 1 and loc == "field":
        fight2(opponent, loc="cave")
    else:
        fight(opponent, loc="cave", enemy_defeated=0)


def decisions(loc):
    if loc == "field":
        x = input("Enter 1 to knock on the door of the house.\n"
                  "Enter 2 to peer into the cave.\n"
                  "What would you like to do?\n"
                  "(Please enter 1 or 2).\n")
        return validate_input(x)
    elif loc == "house":
        x = input("Enter 1 to go back to the field.\n"
                  "Enter 2 to go to the cave.\n"
                  "What would you like to do?\n"
                  "(Please enter 1 or 2).\n")
        return validate_input(x)
    elif loc == "cave":
        x = input("Enter 1 to go to the house.\n"
                  "Enter 2 to go back to the field.\n"
                  "What would you like to do?\n"
                  "(Please enter 1 or 2).\n")
        return validate_input(x)


def goToLoc(goto, loc, enemy_defeated):
    if goto == 1 and loc == "field":
        house(enemy_defeated, "house")
    elif goto == 2 and loc == "field":
        cave(enemy_defeated, "cave")
    elif goto == 1 and loc == "house":
        field1(enemy_defeated, loc)
    elif goto == 2 and loc == "house":
        cave(enemy_defeated, "house")
    elif goto == 1 and loc == "cave":
        house(enemy_defeated, "cave")
    elif goto == 2 and loc == "cave":
        field1(enemy_defeated, loc)


def damageLogic(playerHealthBar, enemyHealthBar):
    playerAttack = random.randint(2, 6)
    enemyAttack = random.randint(1, 4)
    defend = random.randint(2, 3)
    print("Player health : ", playerHealthBar,
          "Enemy health :", enemyHealthBar)
    attackDecision = input("Press 1 to Attack or  2 Defend\n")
    attackDecision = validate_input(attackDecision)
    if attackDecision == 1:
        enemyHealthBar -= playerAttack
        playerHealthBar -= enemyAttack
    else:
        enemyAttack -= defend
        if enemyAttack > 0:
            playerHealthBar -= enemyAttack
    if enemyHealthBar > 0:
        print("Player health : ", playerHealthBar,
              "Enemy health :", enemyHealthBar)
    return playerHealthBar, enemyHealthBar


def fight(enemy, loc, enemy_defeated):
    enemyHealth = 10
    playerHealth = 10
    fightDecision = input("Enter 1 to Fight or 2 to run away\n")
    fightDecision = validate_input(fightDecision)
    if int(fightDecision) == 2:
        print("You ran away from ", enemy,
              "back to the field")
        choice = decisions(player_loc)
        goToLoc(choice, player_loc, enemy_defeated=0)

    else:
        print("you choose to fight")
        while enemyHealth > 0:
            print("What will you do?")
            playerHealth, enemyHealth = damageLogic(playerHealth, enemyHealth)
            if enemyHealth <= 0:
                enemyHealth = 0
                print("You defeated", enemy,
                      ". Congratulations"
                      " You received diamond sword as your reward.")
                enemy_defeated += 1
                choice = decisions(loc)
                goToLoc(choice, loc, enemy_defeated)
            elif playerHealth <= 0:
                print("You have died.\nGAME OVER!")
                break


def damageLogic2(playerHealthBar, enemyHealthBar, potion):
    playerAttack = random.randint(6, 10)
    enemyAttack = random.randint(6, 11)
    defend = random.randint(6, 8)
    print("Player health 2: ", playerHealthBar,
          "Enemy health :", enemyHealthBar)
    attackDecision = input("Enter 1 to Attack\nEnter 2 to Defend\n")
    attackDecision = validate_input(attackDecision)
    if potion == 1 and playerHealthBar <= 12:
        playerHealthBar += 8
        potion -= 1
        print("You used health potion to recover your health.")
        print("Player health : ", playerHealthBar,
              "Enemy health :", enemyHealthBar)
    elif attackDecision == 1:
        enemyHealthBar -= playerAttack
        playerHealthBar -= enemyAttack
    else:
        enemyAttack -= defend
        if enemyAttack > 0:
            playerHealthBar -= enemyAttack
    if enemyHealthBar > 0:
        print("Player health : ", playerHealthBar,
              "Enemy health :", enemyHealthBar)
    return playerHealthBar, enemyHealthBar, potion


def fight2(enemy, loc):
    healthPotion = 1
    enemyHealth = 30
    playerHealth = 20
    fightDecision = input("Enter 1 to Fight\nEnter 2 to run away\n")
    fightDecision = validate_input(fightDecision)
    if int(fightDecision) == 2:
        print("You tried to run away from", enemy,
              "but you failed to escape.")
        print("You died.\nGAME OVER!")
    else:
        print("you choose to fight")
        while enemyHealth > 0:
            print("What will you do?")
            playerHealth, enemyHealth, healthPotion = \
                damageLogic2(playerHealth, enemyHealth, healthPotion)
            if enemyHealth <= 0:
                print("You defeated,", enemy,
                      "Congratulations, You beat the game.")
                break
            elif playerHealth <= 0:
                print("You died.\nGAME OVER!\n")
                break


gameStart = True

while gameStart:
    choice = decisions(player_loc)
    goToLoc(choice, player_loc, enemy_defeated=0)
    gameStart = play_again()

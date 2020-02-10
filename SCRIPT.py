from Randoms import Randoms
from Words import Words
from FightPrepare import Fight_Prepare
from ScoreFight import Score_Fight


randoms = Randoms()
words = Words()


words.Welcome()
words.Skip()
playerHero = randoms.Heroes()
print("you will be a:", (playerHero[0]).upper(),)
print("you have:", playerHero[1], "life", playerHero[2],
      "strength", playerHero[3], "magic", playerHero[4], "gold")
EQUIPMENT = playerHero.append([])
words.Skip()
words.Summary()
words.Skip()
while True:
    answer = words.New_Game_Menu()

    if answer == "1":
        print("ok lets play MAGIC & SWORD")
        break

    elif answer == "3":
        print("muahaha! you can't run!")

    else:
        print("try one more time")


while playerHero[1] > 0:

    event = randoms.Event()
    throw = randoms.Throw()
    foundGold = randoms.Gold()
    monster = randoms.Monsters()
    playerPower = randoms.Throw()

    monsterPower = randoms.Throw()
    fight = Fight_Prepare()
    score = Score_Fight()

    if throw == 6:
        print("you throw", throw, "you can visit Town do you want to:")
        entrance = input("would you like to? (y/n) : ")
        if entrance == "y":
            print("Welcome to Ab'dendriel the city of Elfs")
            words.Skip()
            while True:
                answer = words.Town()
                if answer == "4":
                    print("Good Luck!!!")
                    break

                elif answer == "3":
                    print("Welcome to Merlin the Wizard")
                    words.Skip()
                    print("you can change 7 of your Mexp to magic point")
                    print("you have", playerHero[6], "Mexp")
                    answer = input("change for Magic Point? (y/n): ")
                    if answer == "y":
                        if playerHero[6] >= 7:
                            playerHero[6] = playerHero[6] - 7
                            playerHero[3] = playerHero[3] + 1
                            print(
                                "Now you have", playerHero[3], "MAGIC and", playerHero[6], "MEXP")
                        elif playerHero[6] < 7:
                            print("go Defeat some monsters")

                elif answer == "2":
                    print("Welcome to Arthur the Fighter")
                    words.Skip()
                    print("you can change 7 of your STRexp to strength point")
                    print("you have", playerHero[5], "STRexp")
                    answer = input("change for Strength Point? (y/n): ")
                    if answer == "y":
                        if playerHero[5] >= 7:
                            playerHero[5] = playerHero[5] - 7
                            playerHero[2] = playerHero[2] + 1
                            print(
                                "Now you have", playerHero[2], "STRENGTH and", playerHero[5], "STREXP")
                        elif playerHero[5] < 7:
                            print("go Defeat some monsters")

                else:
                    print("Welcome to Gantri the Smith")
                    words.Skip()
                    print("you can buy some good Staff xD")
                    print("you have", playerHero[4], "gold")
                    answer = input(
                        "for Dagger (+1 strength / 2 gold) press 1\nfor Wand (+1 Magic / 2 gold) press 2\nfor Potion (+1 Life / 1 gold) press 3\n: ")

                    if answer == "1":
                        if "Dagger" in playerHero[7]:
                            print("you already have Dagger")
                        elif playerHero[4] >= 2:
                            playerHero[4] = playerHero[4] - 2
                            playerHero[7].append("Dagger")
                            print("You bought Dagger")
                            if "Dagger" in playerHero[7]:
                                playerHero[2] = playerHero[2] + 1
                            if "Wand" in playerHero[7]:
                                playerHero[3] = playerHero[3] + 1

                        elif playerHero[4] < 2:
                            print("go Earn some gold")

                    elif answer == "2":
                        if "Wand" in playerHero[7]:
                            print("you already have Wand")
                        elif playerHero[4] >= 2:
                            playerHero[4] = playerHero[4] - 2
                            playerHero[7].append("Wand")

                        elif playerHero[4] < 2:
                            print("go Earn some gold")

                    elif answer == "3":
                        if playerHero[4] >= 1:
                            print("You bought Potion, your life increased")
                            playerHero[1] = playerHero[1] + 1
                            playerHero[4] = playerHero[4] - 1
                            print("You have", playerHero[1], "lifes")

                        elif playerHero[4] < 1:
                            print("go Earn some gold")

        else:
            print("Good Luck!!!")
    else:
        print("you throw", throw, "and you found:", event.upper())
        words.Skip()
        if event == "gold":
            gold = playerHero[4]

            playerHero[4] = gold + foundGold
            print("YOU'VE FOUND", foundGold, "GOLD")
            print("you have", playerHero[4], "gold")
            words.Skip()
        else:

            if monster[0] == "Skeleton":
                fight.PrepareSTR(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[2] + monsterPower) > (playerHero[2] + playerPower):
                    score.LooseSTR(playerHero)
                    words.Skip()
                else:
                    score.WinSTR(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Zombie":
                fight.PrepareSTR(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[2] + monsterPower) > (playerHero[2] + playerPower):
                    score.LooseSTR(playerHero)
                    words.Skip()
                else:
                    score.WinSTR(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Ghoul":
                fight.PrepareSTR(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[2] + monsterPower) > (playerHero[2] + playerPower):
                    score.LooseSTR(playerHero)
                    words.Skip()
                else:
                    score.WinSTR(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Vampire":
                fight.PrepareSTR(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[2] + monsterPower) > (playerHero[2] + playerPower):
                    score.LooseSTR(playerHero)
                    words.Skip()
                else:
                    score.WinSTR(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Vampire Lord":
                fight.PrepareSTR(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[2] + monsterPower) > (playerHero[2] + playerPower):
                    score.LooseSTR(playerHero)
                    words.Skip()
                else:
                    score.WinSTR(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Bone Dragon":
                fight.PrepareSTR(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[2] + monsterPower) > (playerHero[2] + playerPower):
                    score.LooseSTR(playerHero)
                    words.Skip()
                else:
                    score.WinSTR(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Ghost":
                fight.PrepareMAG(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[3] + monsterPower) > (playerHero[3] + playerPower):
                    score.LooseMAG(playerHero)
                    words.Skip()
                else:
                    score.WinMAG(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Wrath":
                fight.PrepareMAG(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[3] + monsterPower) > (playerHero[3] + playerPower):
                    score.LooseMAG(playerHero)
                    words.Skip()
                else:
                    score.WinMAG(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Necromancer":
                fight.PrepareMAG(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[3] + monsterPower) > (playerHero[3] + playerPower):
                    score.LooseMAG(playerHero)
                    words.Skip()
                else:
                    score.WinMAG(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Lich":
                fight.PrepareMAG(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[3] + monsterPower) > (playerHero[3] + playerPower):
                    score.LooseMAG(playerHero)
                    words.Skip()
                else:
                    score.WinMAG(playerHero, monster)
                    words.Skip()

            elif monster[0] == "Spectre":
                fight.PrepareMAG(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[3] + monsterPower) > (playerHero[3] + playerPower):
                    score.LooseMAG(playerHero)
                    words.Skip()
                else:
                    score.WinMAG(playerHero, monster)
                    words.Skip()

            else:
                fight.PrepareMAG(monster, monsterPower,
                                 playerHero, playerPower)
                words.Skip()
                if (monster[3] + monsterPower) > (playerHero[3] + playerPower):
                    score.LooseMAG(playerHero)
                    words.Skip()
                else:
                    score.WinMAG(playerHero, monster)
                    words.Skip()

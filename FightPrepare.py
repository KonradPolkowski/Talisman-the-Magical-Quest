
class Fight_Prepare():
    def __init__(self, monster=[], monsterPower=1, playerHero=[], playerPower=1):
        self.monster = monster
        self.monsterPower = monsterPower
        self.playerHero = playerHero
        self.playerPower = playerPower

    def PrepareSTR(self, monster, monsterPower, playerHero, playerPower):

        a = print("Beware", monster[0], "trying to kill you")
        playerAttack = playerHero[2] + playerPower
        monsterAttack = monster[2] + monsterPower
        d = print(playerHero[0].upper(), "attack is", playerAttack)
        e = print(monster[0].upper(), "attack is", monsterAttack)

        return a, playerAttack, monsterAttack, d, e

    def PrepareMAG(self, monster, monsterPower, playerHero, playerPower):

        a = print("Beware", monster[0], "trying to kill you")
        playerAttack = playerHero[3] + playerPower
        monsterAttack = monster[3] + monsterPower
        d = print(playerHero[0].upper(), "magic is", playerAttack)
        e = print(monster[0].upper(), "magic is", monsterAttack)

        return a, playerAttack, monsterAttack, d, e

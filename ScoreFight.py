
class Score_Fight():
    def __init__(self, playerHero=[], monster=[]):
        self.playerHero = playerHero
        self.monster = monster

    def LooseSTR(self, playerHero, monster=[]):
        a = print("DEFEAT")
        b = playerHero[1] = playerHero[1] - 1
        c = print("You loose 1 life point")
        d = print("you have", playerHero[1], "life's")

        return a, b, c, d
#

    def WinSTR(self, playerHero, monster):
        a = print("VICTORY")
        b = playerHero[5] = playerHero[5] + monster[5]
        c = print("Great you earn some exp")

        return a, b, c

    def LooseMAG(self, playerHero, monster=[]):
        a = print("DEFEAT")
        b = playerHero[1] = playerHero[1] - 1
        c = print("You loose 1 life point")
        d = print("you have", playerHero[1], "life's")

        return a, b, c, d

    def WinMAG(self, playerHero, monster):
        a = print("VICTORY")
        b = playerHero[6] = playerHero[6] + monster[6]
        c = print("Great you earn some exp")

        return a, b, c

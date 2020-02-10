class Words():

    def Skip(self):
        next = input("Press ENTER for Continue")
        return next

    def Welcome(self):
        a = print("Welcome Stranger")
        player = input("whats your name? :")
        b = print("Hello", player, "Lets start your adventure")
        c = print("First we need to draw a Hero for you :)")

        return a, player, b, c

    def Summary(self):
        a = print("in your journey you'll have to fight with undead monsters")
        b = print(
            "you can find a lot of gold and some treasures, become stronger and gain experience")
        c = print("you can also find a Town")
        d = print("GOOD LUCK!!!")

        return a, b, c, d

    def New_Game_Menu(self):
        answer = input(
            "for New Game press 1\nfor Load Game press 2\nfor Exit press 3\n: ")
        return answer

    def Town(self):
        answer = input(
            "for SHOP press 1\nfor FIGHTER press 2\nfor APPRENTICE press 3\nfor EXIT press 4\n: ")
        return answer

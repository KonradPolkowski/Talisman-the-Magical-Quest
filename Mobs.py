#
class Mobs():
    def __init__(self, name="name", life=0, strength=0, magic=0, gold=0, STRexp=0, Mexp=0):
        self.name = name
        self.life = life
        self.gold = gold
        self.strength = strength
        self.magic = magic
        self.STRexp = STRexp
        self.Mexp = Mexp

    def Ninja(self, name="Ninja", life=3, strength=3, magic=3, gold=2, STRexp=0, Mexp=0):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Warrior(self, name="Warrior", life=4, strength=4, magic=2, gold=1, STRexp=0, Mexp=0):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Wizard(self, name="Wizard", life=3, strength=2, magic=4, gold=2, STRexp=0, Mexp=0):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Skeleton(self, name="Skeleton", life=1, strength=2, magic=0, gold=0, STRexp=2, Mexp=0):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Zombie(self, name="Zombie", life=1, strength=3, magic=0, gold=0, STRexp=3, Mexp=0):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Ghoul(self, name="Ghoul", life=1, strength=4, magic=0, gold=0, STRexp=4, Mexp=0):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Vampire(self, name="Vampire", life=1, strength=5, magic=0, gold=0, STRexp=5, Mexp=0):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Vampire_Lord(self, name="Vampire Lord", life=1, strength=6, magic=0, gold=0, STRexp=6, Mexp=0):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Bone_Dragon(self, name="Bone Dragon", life=1, strength=7, magic=0, gold=0, STRexp=7, Mexp=0):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Ghost(self, name="Ghost", life=1, strength=0, magic=2, gold=0, STRexp=0, Mexp=2):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Wrath(self, name="Wrath", life=1, strength=0, magic=3, gold=0, STRexp=0, Mexp=3):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Necromancer(self, name="Necromancer", life=1, strength=0, magic=4, gold=0, STRexp=0, Mexp=4):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Lich(self, name="Lich", life=1, strength=0, magic=5, gold=0, STRexp=0, Mexp=5):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Spectre(self, name="Spectre", life=1, strength=0, magic=6, gold=0, STRexp=0, Mexp=6):
        return [name, life, strength, magic, gold, STRexp, Mexp]

    def Banshee(self, name="Banshee", life=1, strength=0, magic=7, gold=0, STRexp=0, Mexp=7):
        return [name, life, strength, magic, gold, STRexp, Mexp]

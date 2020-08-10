import random
from Mobs import Mobs

#


class Randoms():
    def Heroes(self):
        mobs = Mobs()
        ninja = mobs.Ninja()
        warrior = mobs.Warrior()
        wizard = mobs.Wizard()
        lists = [ninja, warrior, wizard]
        chosen = random.choices(lists)[0]
        return chosen

    def Monsters(self):
        mobs = Mobs()
        skeleton = mobs.Skeleton()
        zombie = mobs.Zombie()
        ghoul = mobs.Ghoul()
        vampire = mobs.Vampire()
        vampire_lord = mobs.Vampire_Lord()
        bone_dragon = mobs.Bone_Dragon()
        ghost = mobs.Ghost()
        wrath = mobs.Wrath()
        necromancer = mobs.Necromancer()
        lich = mobs.Lich()
        spectre = mobs.Spectre()
        banshee = mobs.Banshee()
        probability = [0.3, 0.1, 0.08, 0.01, 0.009,
                       0.001, 0.3, 0.1, 0.08, 0.01, 0.009, 0.001]
        lists = [skeleton, zombie, ghoul, vampire, vampire_lord,
                 bone_dragon, ghost, wrath, necromancer, lich, spectre, banshee]
        chosen = random.choices(lists, probability)[0]
        return chosen

    def Throw(self):
        lists = [1, 2, 3, 4, 5, 6]
        chosen = random.choices(lists)[0]
        return chosen

    def Gold(self):
        lists = [1, 2, 3, 4, 5]
        probability = [0.78, 0.2, 0.01, 0.009, 0.001]
        chosen = random.choices(lists, probability)[0]
        return chosen

    def Event(self):
        lists = ["monsters", "gold"]
        probability = [0.7, 0.3]
        chosen = random.choices(lists, probability)[0]
        return chosen

'''
13.13 PA4 Q3: Dragons and Ghosts
Construct a class “Monster” with the following attributes:

self.name (a string)
self.type (a string, default is ‘Normal’)
self.current_hp (int, start out equal to max_hp)
self.max_hp ( int, is given as input when the class instance is created, default is 20)
self.attacks (a dictionary of all known attacks)
self. possible_attacks ( a dictionary of all possible attacks)
The dictionary of possible_attacks will map the name of an attack ( the key) to how many points of damage the attack does. They must be of the following list:

sneak_attack: 1
slash: 2
ice_storm: 3
fire_storm: 3
whirlwind: 3
earthquake: 2
double_hit: 4
tornado: 4
wait: 0
Every monster will start out with only the “wait” attack within self.attacks.

You will need to construct the method add_attack and remove_attack. Both methods will take in an attack name as a parameter. A monster can only have a maximum of four attacks at a time. If you add an attack when the monster already has four, the weakest one should be dropped automatically. If there is a tie for the weakest attack, drop the attack that comes first alphabetically. If adding the attack ended successfully, return True. If you try to add an invalid attack return False. If all of a monster’s attacks are removed, “wait” should automatically be added again, so that every monster always has at least 1 attack. If removing an attack ended successfully return True. If you try to remove an invalid attack or an attack that has not been learned return False.
-----------------------------------------------------------------------------------------------
Now write a function that takes 2 instances of the monster class and makes them fight. This function should be defined outside the Monster class, i.e. it is not a Monster method. A fight goes as follows:

The monster that entered as the first function goes first.
Each monster takes a turn using one attack move. The monster selects this attack move from the strongest to the weakest in a circular function.

An attack is always successful and will decrease the opponent’s hp by the given number of points in self.attacks dictionary. The monsters continue taking turns until their current hp becomes less than or equal to zero.
At this point, the win_fight and lose_fight method should be invoked. Once this complete, return 3 things from the function.
Round_number
Monster that won (return the corresponding Monster object)
List of attacks the monster used
Special Edge Case: If both monster only have “wait” as an attack, return

-1 (round_number)
None (for monster name that won)
None (for list of attack that monster use)
------------------------------------------------------------------------------
Make 2 monster subclasses: Dragon and ghosts, both of which inherit all of the properties of the Monster class. Both should have their “type” attribute updated to ‘dragon’ and ‘ghost’ respectively.

Dragon and ghosts have the ability to level up! Every time a dragon gains 10 exp all of its attacks gain +1 damage. For Example, at 30 exp a dragon's attack will have each +3 damage total. This does NOT include any new attacks learned after gaining exp. For Ghosts, every time a Ghost gains 10exp it gains +5 to its max_hp and therefore current_hp.
'''

class Monster():
    def __init__(self, name, hp=20):
        self.exp = 0
        self.name = name
        self.type = "Normal"
        self.max_hp = hp
        self.current_hp = self.max_hp
        self.attacks = {"wait": 0}
        self.possible_attacks = {'sneak_attack': 1, 'slash': 2, 'ice_storm': 3, 'fire_storm': 3, 'whirlwind': 3,
                                 'earthquake': 2, 'double_hit': 4, 'tornado': 4, 'wait': 0}

    def add_attack(self, attack_name):
        print("add_attack for " + attack_name)
        if attack_name in self.attacks:
            return False

        if attack_name not in self.possible_attacks:
            return False

        self.attacks = dict(sorted(self.attacks.items(), key=lambda item: item[1]))  # sorts dictionary by values
        values = list(self.attacks.values())
        keys = list(self.attacks.keys())
        while len(self.attacks) >= 4:
            if values[0] == values[1] == values[2]:
                if keys[0] < keys[1] and keys[0] < keys[2]:
                    to_pop = keys[0]
                elif keys[1] < keys[0] and keys[1] < keys[2]:
                    to_pop = keys[1]
                else:
                    to_pop = keys[2]

            elif values[0] == values[1]:
                if keys[0] < keys[1]:
                    to_pop = keys[0]
                else:
                    to_pop = keys[1]
            else:
                to_pop = keys[0]
            Monster.remove_attack(self, to_pop)
        self.attacks[attack_name] = self.possible_attacks[attack_name]
        # print(self.attacks)
        return True

    def remove_attack(self, attack_name):
        print("remove attack for " + attack_name)
        if len(self.attacks) == 0:
            self.attacks['wait'] = 0
        try:
            if attack_name not in self.possible_attacks:
                raise NameError
            if attack_name not in self.attacks:
                raise NameError
            if len(self.attacks) == 1 and "wait" in self.attacks:
                return True
            self.attacks.pop(attack_name)
            return True
        except NameError:
            return False

        # print(self.attacks)

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp


def monster_fight(monster1, monster2):
    print("monster_fight function called for" + monster1.name + monster1.type + "and" + monster2.name + monster2.type)
    monster1_attacks = monster1.attacks
    monster2_attacks = monster2.attacks
    monster1_attacks = dict(sorted(monster1_attacks.items(), key=lambda item: item[1],
                                   reverse=True))  # sorts dictionary by values descending
    monster2_attacks = dict(sorted(monster2_attacks.items(), key=lambda item: item[1],
                                   reverse=True))  # sorts dictionary by values descending
    # i didn't sort alphabetically after sorting by value
    print(monster1_attacks)
    print(monster2_attacks)
    monster1_keys = list(monster1_attacks.keys())
    monster2_keys = list(monster2_attacks.keys())
    print(monster1.current_hp)
    print(monster2.current_hp)

    rounds = 0
    monster1_index = -1  # tells us which attack we will use (index for monster1_keys)
    monster2_index = -1
    m1_turn = True

    # edge case
    if len(monster1_keys) == 1 and monster1_keys[0] == "wait" and len(monster2_keys) == 1 and monster2_keys[
        0] == "wait":
        return -1, None, None

    monster1_moves = []
    monster2_moves = []
    while monster1.current_hp > 0 and monster2.current_hp > 0:  # while both monsters hp > 0
        rounds += 0.5  # 0.5 because 2 monsters going is 1 round
        print("\nRound:", rounds)

        if m1_turn:
            if monster1_index == len(monster1_keys) - 1:  # if we got to the end of monster1_keys, go to the beginning
                monster1_index = 0
            else:
                monster1_index += 1  # else iterate through monster1_keys
            key = monster1_keys[monster1_index]  # key = current attack name
            attack = monster1_attacks[key]  # attack is the points of current attack
            monster2.current_hp -= attack  # monster2's hp reduces by attack points
            monster1_moves.append(key)  # add attack to monster1_moves
            print("Monster1's Turn")
            print("Attack :", key, "Points:", attack)
            print("Monster 2 hp:", monster2.current_hp)
            print("Monster 1 index:", monster1_index)

        if not m1_turn:  # monster2's turn
            if monster2_index == len(monster2_keys) - 1:
                monster2_index = 0
            else:
                monster2_index += 1
            key = monster2_keys[monster2_index]
            attack = monster2_attacks[monster2_keys[monster2_index]]
            monster1.current_hp -= attack
            monster2_moves.append(key)
            print("Monster2's Turn")
            print("Attack :", key, "Points:", attack)
            print("Monster 1 hp:", monster1.current_hp)
            print("Monster 2 index:", monster2_index)

        m1_turn = not m1_turn  # change the turn

    if rounds % 1 != 0:  # if we stop function at monster1's turn the round number needs to round up
        rounds += 0.5
    if monster1.current_hp < monster2.current_hp:  # if monster2 wins
        monster2.win_fight()
        monster1.lose_fight()
        return int(rounds), monster2, monster2_moves
    else:  # if monster1 wins
        monster1.win_fight()
        monster2.lose_fight()
        return int(rounds), monster1, monster1_moves


class Ghost(Monster):
    def __init__(self, name, hp=20, type="ghost"):
        super().__init__(name, hp)
        self.type = type

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp
        print(self.name, "'s exp:", self.exp)
        if self.exp >= 10:
            # i had a condition to make sure hp was not added at 10 and then at 12
            # which was this in the if statement--> and self.max_hp < 20 + ((self.exp//10)*5)
            # but code does not work with this so I took it out
            self.max_hp += 5
            self.current_hp = self.max_hp  # this might be redundant
            print("new current hp is" + str(self.current_hp))

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp
        print(self.name, "'s exp:", self.exp)
        if self.exp >= 10 and self.max_hp < 20 + ((self.exp // 10) * 5):
            self.max_hp += 5
            self.current_hp += 5  # this might be redundant
            print("new current hp for" + self.name + "is" + self.current_hp)


class Dragon(Monster):
    def __init__(self, name, hp=20, type="dragon"):
        super().__init__(name, hp)
        self.type = type

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp
        print(self.name, "'s exp:", self.exp)
        keys = list(self.attacks.keys())

        if self.attacks[keys[0]] == (self.possible_attacks[keys[0]] + (self.exp // 10)):
            pass
        else:
            for key in self.attacks:
                self.attacks[key] += 1
                print("+1 attack point added for " + self.name)

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp
        print(self.name, "'s exp:", self.exp)
        keys = list(self.attacks.keys())

        if self.attacks[keys[0]] == (self.possible_attacks[keys[0]] + (self.exp // 10)):
            pass
        else:
            for key in self.attacks:
                self.attacks[key] += 1


'''
#main
monster1 = Dragon("gitu")
monster1.add_attack("ice_storm")
monster1.add_attack("whirlwind")
monster1.add_attack("slash")

monster2 = Ghost("manju")
monster2.add_attack("fire_storm")
monster2.add_attack("whirlwind")

print(monster1.type)
print(monster2.type)
print(monster2.max_hp)
print(monster2.attacks)
#print(monster_fight(monster1, monster2))
'''
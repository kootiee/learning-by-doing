class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def description(self):
        return (f"{self.name} is a "
                f"{self.type} type pokemon, "
                f"with {self.health} health")

    def battle(self, other):
        fire_table = {
            'fire': 2,
            'water': 1,
            'grass': 4
        }

        water_table = {
            'fire': 4,
            'water': 2,
            'grass': 1
        }

        grass_table = {
            'fire': 1,
            'water': 4,
            'grass': 2
        }

        damage_table = {
            'fire': fire_table,
            'water': water_table,
            'grass': grass_table
        }

        my_damage = damage_table[self.type][other.type]
        their_damage = damage_table[other.type][self.type]

        self.health = self.health - their_damage
        other.health = other.health - my_damage

        if self.health > other.health:
            return f"Yay! Your {self.name} beat their {other.name}!"
        else:
            return f"Oh no. Their {other.name} kicked {self.name}'s arse."


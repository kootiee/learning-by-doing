def create(poke, name, type, health):
    #poke = {} # creating the dictionary

    # The next three lines initialize the dictionary
    poke['name'] = name
    poke['type'] = type
    poke['health'] = health

    def describe_this_pokemon():
        return describe(poke)

    poke['description'] = describe_this_pokemon

    def battle_this_pokemon(some_other_pokemon):
        return battle(poke, some_other_pokemon)

    poke['battle'] = battle_this_pokemon

    return poke

def describe(this_pokemon):
    return (f"{this_pokemon['name']} is a "
            f"{this_pokemon['type']} type pokemon, "
            f"with {this_pokemon['health']} health")

def battle(my_pokemon, their_pokemon):
    # By default, a pokemon does 2 damage
    # If you are strong against the other, damage == 4
    # If you are weak against the other, damage == 1
    # new_health = current_health - damage
    # Pokemon with highest new health wins
    # bulbasaur, grass , 5 vs squirtle, water, 5
    # bulbasaur attacks squirtle
    # bulbasaur (grass) is strong vs squirtle (water)
    # so does 4 damage instead of 2
    # squirtles new health = 5 - 4 (i.e. 1)
    #
    # squirtle attacks bulbasaur
    # squirtle (water) is weak against bulbasaur (grass)
    # so does 1 damage instead of 2
    # bulbasaurs new health = 5 - 1 == 4
    #
    # bulbasaur (4 health) beats squirtle (1 health)

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

    my_type = my_pokemon['type']
    their_type = their_pokemon['type']
    my_damage = damage_table[my_type][their_type]
    their_damage = damage_table[their_type][my_type]

    my_pokemon['health'] = my_pokemon['health'] - their_damage
    their_pokemon['health'] = their_pokemon['health'] - my_damage

    if my_pokemon['health'] > their_pokemon['health']:
        return f"Yay! Your {my_pokemon['name']} beat their {their_pokemon['name']}!"
    else:
        return f"Oh no. Their {their_pokemon['name']} kicked {my_pokemon['name']}'s arse."


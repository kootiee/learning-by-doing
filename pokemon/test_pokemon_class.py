from pokemon_class import Pokemon

def test_pokemon():
    assert Pokemon('charmander', 'fire', 5)

def test_describe():
    squirtle = Pokemon('squirtle', 'water', 5)
    result = squirtle.description()
    assert result == 'squirtle is a water type pokemon, with 5 health'

def test_battle():
    shaams_pokemon = Pokemon('bulbasaur', 'grass', 5)
    carlas_pokemon = Pokemon('squirtle', 'water', 5)
    result = shaams_pokemon.battle(carlas_pokemon)
    assert result == 'Yay! Your bulbasaur beat their squirtle!'

def test_battle_two():
    shaams_pokemon = Pokemon('bulbasaur', 'grass', 5)
    carlas_pokemon = Pokemon('charmander', 'fire', 5)
    result = shaams_pokemon.battle(carlas_pokemon)
    assert result == "Oh no. Their charmander kicked bulbasaur's arse."


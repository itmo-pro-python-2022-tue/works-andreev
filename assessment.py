from dataclasses import dataclass
from typing import Union, Generator, Optional
from functools import lru_cache
import requests


@dataclass(frozen=True)
class BasePokemon:
    name: str


@dataclass(frozen=True)
class Pokemon(BasePokemon):
    pokemon_id: int
    height: int
    weight: int


class PokeAPI:
    @staticmethod
    @lru_cache
    def get_pokemon(name: Union[int, str]) -> Pokemon:
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
        data = requests.get(url).json()
        pokemon = Pokemon(pokemon_id=data['id'],
                          name=data['name'],
                          height=data['height'],
                          weight=data['weight'])
        return pokemon

    @staticmethod
    def get_all(get_full=False) -> Generator:
        url = 'https://pokeapi.co/api/v2/pokemon/'
        data = requests.get(url).json()
        while True:
            for info in data['results']:
                if get_full:
                    yield PokeAPI.get_pokemon(info['name'])
                else:
                    yield BasePokemon(name=info['name'])
            if data['next'] is None:
                break
            else:
                url = data['next']
                data = requests.get(url).json()


print(PokeAPI.get_pokemon('ditto'))
# print(PokeAPI.get_pokemon(97))

count = 0
fattest: Optional[Pokemon] = None
for pokemon in PokeAPI.get_all(True):
    print(pokemon)
    if fattest is not None and fattest.weight < pokemon.weight:
        fattest = pokemon
    elif fattest is None:
        fattest = pokemon
    count += 1
    if count == 50:
        break

print(fattest)

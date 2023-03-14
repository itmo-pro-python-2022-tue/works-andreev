from typing import Union, Generator, Optional
import requests


class BasePokemon:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def __str__(self):
        return f'BasePokemon(name={self._name})'


class Pokemon(BasePokemon):
    __pokemon_id: int
    __height: int
    __weight: int

    def __init__(self, pokemon_id: int, name: str, height: int, weight: int) -> None:
        super().__init__(name)
        self.__pokemon_id = pokemon_id
        self.__height = height
        self.__weight = weight

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self.__pokemon_id

    def get_weight(self) -> int:
        return self.__weight

    def get_height(self) -> int:
        return self.__height

    def __str__(self) -> str:
        return f'Pokemon(id={self.__pokemon_id}, name={self._name}, height={self.__height}, weight={self.__weight})'


class PokeAPI:
    @staticmethod
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
    if fattest is not None and fattest.get_weight() < pokemon.get_weight():
        fattest = pokemon
    elif fattest is None:
        fattest = pokemon
    count += 1
    if count == 50:
        break

print(fattest)

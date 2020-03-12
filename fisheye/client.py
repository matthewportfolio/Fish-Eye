import requests
from urllib.parse import urlencode
from .species import Species
from .constants import BASE_URL

class Client:

    def __init__(self, **options):
        self.species = {}
        self.ready = False
        self.options = options

    #starts the client and populates it's cache (if specified)
    def start(self):
        if('cache' in self.options):
            print('Populating species cache, this may take a while...')
            #5000 is the most species we can request at once
            results = self.__species_many(5000, 0)
            self.species = {**self.species, **results}
            offset = 5000

            while(len(results) == 5000):
                offset += 5000
                results = self.__species_many(5000, offset)
                self.species = {**self.species, **results}
            print(f'Done! Cache size: {len(self.species)}')
        self.ready = True

    #Get a single or multiple species
    def get_species(self, id=None, limit=100):
        if(id):
            return self.__species_single(id)
        return self.__species_many(limit, 0)
    
    def __species_single(self, id):
        if(id in self.species): 
            return self.species[id]
        request = self.__make_request(f'species/{id}')
        return Species(self, request['data'][0])
    
    def __species_many(self, limit, offset):
        request = self.__make_request('species', limit=limit, offset=offset)
        items = {}
        for x in request['data']:
            items[x['SpecCode']] = Species(self, x)
        return items

    def __make_request(self, endpoint, **parameters):
        if(parameters): 
            #turns dict of parameters into query string, e.g: {'a': 2, 'b': 4} => a=2&b=4
            parameters = urlencode(parameters)
        return requests.get(f'{BASE_URL}/{endpoint}?{parameters}').json()
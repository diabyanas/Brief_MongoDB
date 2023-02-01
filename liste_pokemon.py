import requests
import pymongo
import time
from datetime import datetime

def populate_jdg_mongodb():
    start_time = time.time()
    
    # Connection à la base MongoDB
    client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
    db = client["JDG"]
    pokemon_collection = db["pokemon"]
    
    # Selection de données à partir de l'API
    response = requests.get("https://pokebuildapi.fr/api/v1/pokemon")
    pokemon_list = response.json()
    
    # Entregistrement dans la base MongoDB
    pokemon_collection.insert_many(pokemon_list)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Populated JDG MongoDB with {len(pokemon_list)} pokemons in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    populate_jdg_mongodb()
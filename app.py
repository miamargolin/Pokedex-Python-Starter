import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def show_names(x):
    for pokemon in data:
        print(pokemon["name"][languages])        
# Add a language choice feature and print the pokemons name based on the user input
def languages():
    for language in data:
        print("Choose either english, chinese, or japanese: ")
x = input("Choose either english, chinese, or japanese: ")
if x == "english":
    languages = "english"
elif x == "chinese":
    languages = "chinese"
elif x == "japanese":
    languages = "japanese"
show_names(languages)
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
types = []

for pokemon in data :
    for pokemon_type in pokemon["type"]:
        if pokemon_type not in types:
            types.append(pokemon_type)

print("Pokemon types: ")
for pokemon_type in types:
    print(pokemon_type)

choice = input("Choose a Pokemon type: ").strip().lower()
found = False

for pokemon in data:
    for pokemon_type in pokemon["type"]:
        if pokemon_type.lower() == choice:
            print(pokemon["name"]["english"])
            found = True 
            break

if found == False:
    print("No pokemon of that type!")
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def name():
    for names in data:


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!


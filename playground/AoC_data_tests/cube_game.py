import pandas as pd

data=pd.read_table("raw_games.txt", sep=':', header=None, names=["game", "rounds"])
data["game"].str.strip("Game ")
data["round"] = data["rounds"].str.split(';') 

# print(data)

game_tables = {}

for _, row in data.iterrows():
    game_name = row["game"]
    rounds = row["rounds"]
    
    game_table = pd.DataFrame(columns=["red", "green", "blue"])
    
    for round_str in rounds:
        round_data = {}
        for cube_count in round_str.split(', '):
            colour, count = cube_count.split(' ')
            print(count)
            # round_data[colour] = int(count)
        game_tables.append(round_data, ignore_index = True)
    game_table = game_table.fillna(0).astype(int)
    
    game_tables[game_name] = game_table

print(game_tables[1])
print(data["Red"].value_counts())
        
        
# this approach seems quite 'unpandas', if that is a term
# feels like using loops is sorta undermining the whole 
# point of using sich a powerful tool; thinking like a dev,
# and falling back on well-worn tools

# i do still think there is some mileage in using the package 
# to do this kind of thing, but not like this, not 
# like a trad script.py approach. will come back to it and 
# rethink it from a more data-engineer/data-science angle

# tools for tasks, yes, but it does seem like a wall of text that needs 
# manipulation is pretty in the zone for pd

# also lol, just noticed i'm appending a dictionary
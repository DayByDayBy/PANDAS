import pandas as pd

# data=pd.read_table("raw_games.txt", sep=':', header=None, names=["game", "rounds"])
# data["game"].str.strip("Game ")
# data["round"] = data["rounds"].str.split(';') 

# # print(data)

# game_tables = {}

# for _, row in data.iterrows():
#     game_name = row["game"]
#     rounds = row["rounds"]
    
#     game_table = pd.DataFrame(columns=["red", "green", "blue"])
    
#     # for round_str in rounds:
#     #     round_data = {}
#     #     for cube_count in round_str.split(', '):
#     #         colour, count = cube_count.split(' ')
#     #         print(count)
#     #         # round_data[colour] = int(count)
#     #     game_tables.append(round_data, ignore_index = True)
#     # game_table = game_table.fillna(0).astype(int)
    
#     game_tables[game_name] = game_table

# print(game_tables)
# print(data["Red"].value_counts())
        
        
# this approach seems quite 'unpanda' (if that is a term)
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



    # red = 12
    # green = 13
    # blue = 14
    
game_list=pd.read_table("raw_games.txt", sep=':', header=None, names=["game", "rounds"])
game_list["game"] = game_list["game"].str.strip("Game ")
# game_list["rounds"] = game_list["rounds"].str.split(';') 
# game_list["round"] = game_list["rounds"].str.split(';')

print(
    game_list.to_string(
    buf=None,
    columns=None, 
    col_space=None, 
    header=True, 
    index=False, 
    na_rep="NaN", 
    formatters=None, 
    float_format=None, 
    index_names=True, 
    justify=None, 
    max_rows=None, 
    max_cols=None, 
    show_dimensions=False, 
    decimal=".", 
    line_width=None)
)



    # this sorta thing may make a better model?
    # populating it with list comp, but in this sort of shape,  
    # a multindex model

# data = {
#     'Game': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3],
#     'Round': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3],
#     'Color': ['Red', 'Blue', 'Green'] * 3,
#     'Score': [10, 15, 20, 8, 12, 18, 5, 10, 15]
# }

# # Creating a DataFrame
# df = pd.DataFrame(data)





# having a wee stab...


game_list = pd.read_table("raw_games.txt", sep=':', header=None, names=["game", "rounds"])
game_list["game"] = game_list["game"].str.strip("Game ")
game_list["rounds"] = game_list["rounds"].str.split(';')

data = []

# not sure how else to do this besides a wee loop... 
# not loving it, but popping it in as a placeholder 
#  maybe not as 'unpandonic' (ok, that's worse) as it 
# could be if it's pre-df, if it's to gather the data to _make_ the frame
# still seems a bit clumsy tho 


for _, row in game_list.iterrows():
    game = int(row["game"])
    rounds_data = row["rounds"]
    for round_data in rounds_data:
        round_info = [game]
        color_score_pairs = round_data.split(',')    
        for pair in color_score_pairs:
            color, score = pair.strip().split()
            round_info.extend([int(score), color.lower()])   
        data.append(round_info)

columns = ['Game']
for i in range(1, (len(data[0]) - 1) // 2 + 1):
    columns.extend([f'Score_{i}', f'Color_{i}'])

df = pd.DataFrame(data, columns=columns)

print(df)

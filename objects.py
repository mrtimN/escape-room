# define rooms and items

couch = {"name": "couch", "type": "furniture"}
piano = {"name": "piano", "type": "furniture"}
queen_bed = {"name": "queen bed", "type": "furniture"}
double_bed = {"name": "double bed", "type": "furniture"}
dresser = {"name": "dresser", "type": "furniture"}
dining_table = {"name": "dining table", "type": "furniture"}
poster_1 = {"name": "poster 1", "type": "furniture"}
poster_2 = {"name": "poster 2", "type": "furniture"}
note_on_the_floor = {"name": "note on the floor", "type": "furniture"}
poster_4 = {"name": "poster 4", "type": "furniture"}

door_a = {"name": "door a", "type": "door"}
door_b = {"name": "door b","type": "door"}
door_c = {"name": "door c","type": "door"}
door_d = {"name": "door d","type": "door"}

key_a = {"name": "key for door a", "type": "key", "target": door_a}
key_b = {"name": "key for door b", "type": "key", "target": door_b}
key_c = {"name": "key for door c", "type": "key", "target": door_c}
key_d = {"name": "key for door d", "type": "key", "target": door_d}

game_room = {"name": "game room", "type": "room", "explored" : False}
bedroom_1 = {"name": "bedroom 1", "type": "room", "explored" : False}
bedroom_2 = {"name": "bedroom 2", "type": "room", "explored" : False}
living_room = {"name": "living room", "type": "room", "explored" : False}
outside = {"name": "outside"}

all_furniture = [couch, piano, queen_bed, double_bed, dresser, dining_table, poster_1]
all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]
all_doors = [door_a, door_b, door_c, door_d]
all_keys = [key_a, key_b, key_c, key_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a, poster_1, poster_2, note_on_the_floor, poster_4],
    "piano": [key_a],
    "outside": [door_d],
    "door a": [game_room, bedroom_1],
    "bedroom 1": [queen_bed,door_a,door_b,door_c],
    "bedroom 2": [door_b, double_bed, dresser],
    "living room": [dining_table,door_c,door_d],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [outside,living_room],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [key_d],
}
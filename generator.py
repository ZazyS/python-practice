import random

conditions = ["burned", "frostbitten", "decaying", "waterlogged", "petrified"]
places = ["jawline", "left eye", "throat", "knuckles", "collarbone"]
extras = ["with visible bone", "still bleeding", "healing badly", "infested", "stitched shut"]

how_many = int(input("How many concepts? "))
for i in range(how_many):
    condition = random.choice(conditions)
    place = random.choice(places)
    extra = random.choice(extras)
    print(f"{condition} {place}, {extra}")  
rooms = {
    "hallway": {
        "description": "A long hallway, Dust everywhere, Doors lead north and east.", 
        "exits": {"north": "kitchen", "east": "study"}
}, 
    "kitchen": {
        "description": "Cold in here. Some thingis dripping. A door leads south.",
        "exits": {"south": "hallway"}
    },
    "study":{
        "description": "Books floor to ceiling. One of them is glowing. Exit west.",
        "exits": {"west": "hallway"},
        "item": "glowing book"
    }
}

current_room = "hallway"
inventory = []

while True:
    print(rooms[current_room]["description"])
    
    choice = input("Where do you go? ")
    
    if choice == "quit":
        print("You leave the house. Probably wise.")
        break
    
    elif choice == "take":
        if "item" in rooms[current_room]:
            item = rooms[current_room]["item"]
            inventory.append(item)
            del rooms[current_room]["item"]
            print(f"You take the {item}.")
        else:
            print("Nothing to take.")
            
    elif choice == "bag":
        print(inventory)
        
    elif choice in rooms[current_room]["exits"]: 
        current_room = rooms[current_room]["exits"][choice]
        
    else:
        print("You can't go that way.")
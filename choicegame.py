rooms = {
    "hallway": {
        "description": "A long hallway. Dust everywhere. Doors lead north and east.",
        "exits": {"north": "kitchen", "east": "study"}
    },
    "kitchen": {
        "description": "Cold in here. Something dripping. A door leads south. Stairs lead down into darkness.",
        "exits": {"south": "hallway", "down": "basement"}
    },
    "study": {
        "description": "Books floor to ceiling. One of them is glowing. Exit west.",
        "exits": {"west": "hallway"},
        "item": "glowing book"
    },
    "basement": {
        "description": "The book's glow lights up the stairs. At the bottom, a door with your name carved into it. THE END.",
        "exits": {"up": "kitchen"}
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
        next_room = rooms[current_room]["exits"][choice]

        if next_room == "basement" and "glowing book" not in inventory:
            print("The stairs vanish into total darkness. You need some light.")
        else:
            current_room = next_room
            if current_room == "basement":
                print(rooms[current_room]["description"]) 
                break
        
    else:
        print("You can't go that way.")

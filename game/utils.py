# Author: Ilmari Takkunen
# Github: ilmaritak
#
#
from items import inventory, items

def show_inventory():
    print()
    if inventory:
        print("Sinulla on mukana:")
        for item in inventory:
            print(" -", item)
    else:
        print("Sinulla ei ole mitään mukana.")

def take_item(item_name, room_name):
    if item_name not in items:
        print("Sellaista esinettä ei ole.")
        return

    if items[item_name]["location"] != room_name:
        print("Et näe sellaista täällä.")
        return

    inventory.append(item_name)
    items[item_name]["location"] = "inventory"
    print(f"Otit esineen: {item_name}")

def drop_item(item_name, room_name):
    if item_name not in inventory:
        print("Ei ole sinulla sellaista.")
        return

    inventory.remove(item_name)
    items[item_name]["location"] = room_name
    print(f"Pudotit esineen: {item_name}")

def look(room_name, room_description):
    print()
    print(room_description)
    print()

    here_items = [item for item in items if items[item]["location"] == room_name]

    if here_items:
        print("Näet täällä:")
        for i in here_items:
            print(f" - {i}: {items[i]['description']}")
    else:
        print("Täällä ei näytä olevan mitään erikoista.")

def handle_commands(room_name, room_description, valid_dirs):
    look(room_name, room_description)

    while True:
        cmd = input("> ").strip().lower()

        if cmd in ["katsele", "tutki"]:
            look(room_name, room_description)

        elif cmd == "mukana":
            show_inventory()

        elif cmd == "lopeta":
            print("Peli päättyy.")
            exit()

        elif cmd.startswith("ota "):
            take_item(cmd[4:], room_name)

        elif cmd.startswith("pudota "):
            drop_item(cmd[7:], room_name)

        elif cmd.startswith("mene "):
            direction = cmd[5]
            if direction in valid_dirs:
                return direction
            else:
                print("Et voi mennä siihen suuntaan.")

        else:
            print("En ymmärrä komentoa.")

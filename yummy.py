import time
import random

# =========================
#      beginner stats
# =========================

stats = {"hunger": 50, "energy": 50, "power": 50}

player = {
    "name": None, # will be user input
    "class": None, # choice (bard, wizard, warrior, trickster)
    "power_type": None,  # (luck, magic power, strength, chaos power)
}

history = []


last_update_time = time.time()
turn_counter = 0

RIDDLES = [
    ("What has to be broken before you can use it?", "egg"),
    ("I’m tall when I’m young, and I’m short when I’m old. What am I?", "candle"),
    ("What month of the year has 28 days?", "all of them"),
    ("What is full of holes but still holds water?", "sponge"),
    ("What question can you never answer yes to?", "are you asleep"),
    ("What is always in front of you but can’t be seen?", "future"),
    ("There’s a one-story house in which everything is yellow. What color are the stairs?", "no stairs"),
    ("What can you break, even if you never pick it up or touch it?", "promise"),
    ("What goes up but never comes down?", "age"),
    ("What gets wet while drying?", "towel"),
]

# =========================
#     basic stuffz
# =========================

def limits():
    for key in stats:
        stats[key] = max(0, min(100, stats[key]))

def log_action(action):
    history.append(action)

def time_decay():
    global last_update_time
    now = time.time()
    elapsed = now - last_update_time
    if elapsed >= 5:  # every 5 seconds
        stats["hunger"] += 3
        stats["energy"] -= 2
        last_update_time = now
        print("Time passes... you feel a bit hungrier and more tired.")

# =========================
#           intro
# =========================

def story_intro():
    print("====================================")
    print("      LEGENDS OF ELDORIA")
    print("====================================")
    print("In the ancient land of Eldoria, where dragons nap on mountaintops")
    print("a prophecy foretold the rise of a hero...")

def choose_name():
    name = input("What is your hero's name? ")
    if not name.strip():
        name = "Nameless Hero"
    player["name"] = name
    print(f"Very well, {name}.")

def choose_class():
    print("Choose your class:")
    print("1. Bard    - Artistic, lucky, not very strong (Luck)")
    print("2. Wizard  - Wise, strong magic, not very strong physically (Magic Power)")
    print("3. Warrior - Strong, not very smart (Strength)")
    print("4. Trickster - Clever, not strong, tricks bosses (Chaos Power)")

    while True:
        choice = input("> ")
        if choice == "1":
            player["class"] = "Bard"
            player["power_type"] = "Luck"
            stats["power"] = 55
            print("You are a Bard, artist of questionable decisions.")
            break
        elif choice == "2":
            player["class"] = "Wizard"
            player["power_type"] = "Magic Power"
            stats["power"] = 60
            print("You are a Wizard, master of arcane power.")
            break
        elif choice == "3":
            player["class"] = "Warrior"
            player["power_type"] = "Strength"
            stats["power"] = 65
            print("You are a Warrior, strong in muscle, but not the brain type.")
            break
        elif choice == "4":
            player["class"] = "Trickster"
            player["power_type"] = "Chaos Power"
            stats["power"] = 50
            print("You are a Trickster, clever, smug.")
            break
        else:
            print("Invalid choice. Try again.")

# =========================
#   status + history
# =========================

def show_status():
    print("------ STATUS ------")
    print(f"Name: {player['name']}  | Class: {player['class']} ({player['power_type']})")
    print(f"Hunger: {stats['hunger']}")
    print(f"Energy: {stats['energy']}")
    print(f"Power:  {stats['power']}")

def show_history():
    print("--- LAST ACTIONS ---")
    if not history:
        print("No actions yet.")
    else:
        for a in history:
            print(" -", a)


# =========================
#       basic stuffz
# =========================

def eat_food():
    print("You find some suspicious stew on the road and eat it.")
    stats["hunger"] -= 15
    stats["energy"] += 5
    log_action("Ate roadside food")

def rest():
    print("You take a short rest on a rock that is surprisingly comfy.")
    stats["energy"] += 20
    stats["hunger"] += 5
    log_action("Rested")

def train_power():
    print("You train your " + player["power_type"] + ".")
    bonus = 10
    if player["class"] == "Wizard":
        bonus += 5
    elif player["class"] == "Warrior":
        bonus += 3
    stats["power"] += bonus
    stats["energy"] -= 10
    stats["hunger"] += 5
    log_action("Trained power")

# =========================
#       gift boxes     
# =========================

def open_gift_box():
    print("A mysterious gift box appears!")
    roll = random.random()

    # Bard perk: slightly better chance for good stuff
    if player["class"] == "Bard":
        roll += 0.05
        if roll > 1:
            roll = 1

    if roll < 0.5:
        junk_items = ["a single wet sock","a rock that looks like a potato","a slightly warm carrot","a broken wand","a moldy sandwich"]
        item = random.choice(junk_items)
        print(f"You open it and find... {item}. Completely useless.")
        log_action("Found junk: " + item)
    elif roll < 0.95:
        print("You find something mildly useful!")
        reward_type = random.choice(["food", "pillow", "fruit"])
        if reward_type == "food":
            print("It's tasty food. Yum!")
            stats["hunger"] -= 10
        elif reward_type == "pillow":
            print("An extremely comfy pillow. Zzzz...")
            stats["energy"] += 10
        elif reward_type == "fruit":
            print("A glowing magic fruit..electricity zaps from your finger tips.")
            stats["power"] += 10
        log_action("Got useful item")
    else:
        print("You find the ORB OF ABSOLUTE POWER! All your stats are restored!")
        stats["hunger"] = 0
        stats["energy"] = 100
        stats["power"] = 100
        log_action("Found Orb of Absolute Power")

    limits()

# =========================
#         bosses
# =========================

def fight_blind_dragon():
    print("A villager walks up to you wailing that the dragon is threatning to burn down the village. After thinking, you decide to help. You approach a massive cave. Inside, a blind dragon roars.")
    dragon_hp = 60
    while dragon_hp > 0:
        print(f"Dragon HP: {dragon_hp}")
        print("1. Attack")
        print("2. Try to sneak")
        print("3. Tell it a joke")

        choice = input("> ")

        if choice == "1":
            base_damage = 10
            if player["class"] == "Wizard":
                base_damage += 5
            if player["class"] == "Warrior":
                base_damage += 7
            if player["class"] == "Bard":
                base_damage += 2
            if player["class"] == "Trickster":
                base_damage += 3

            print("You strike at the dragon!")
            dragon_hp -= base_damage
            stats["energy"] -= 5
            stats["hunger"] += 3
        elif choice == "2":
            if player["class"] == "Trickster":
                print("You expertly sneak around the dragon. It swipes at the air, confused.")
                dragon_hp -= 20
            else:
                print("You try to sneak, but step on a crunchy bone. The dragon roars!")
                stats["energy"] -= 5
        elif choice == "3":
            print("You tell the dragon a joke.")
            if player["class"] == "Bard":
                print("The dragon surprisingly laughs at your joke. It's demeanor lightens.")
                dragon_hp -= 15
            else:
                print("The dragon does not get it. Awkward.")
                stats["energy"] -= 3
        else:
            print("You hesitate. The dragon snorts impatiently.")

        if dragon_hp > 0:
            print("The dragon breathes fire in your general direction!")
            stats["energy"] -= 10

        limits()

        if stats["energy"] <= 0:
            print("You collapse from exhaustion in front of the dragon. Game Over.")
            return False

    print("You have defeated the blind dragon! The village thanks you for bringing them to safety.")
    log_action("Defeated blind dragon")
    return True

def troll_riddle():
    print("You arrive at a bridge. A troll blocks your path.")
    riddle, answer = random.choice(RIDDLES)
    print("Troll: Answer my riddle, or you shall not pass!")
    print("Riddle:", riddle)

    user_answer = input("> ").strip().lower()

    if player["class"] == "Trickster" and random.random() < 0.4:
        print("You distract the troll with nonsense. He forgets the question entirely.")
        success = True
    else:
        if player["class"] == "Wizard":
            print("(You think for a while... you feel like you know this.)")
        success = (answer in user_answer)

    if success:
        print("Troll: Huh. Correct. You may pass.")
        log_action("Solved troll riddle")
        return True
    else:
        print("Troll: WRONG! BONK.")
        stats["energy"] -= 15
        stats["hunger"] += 5
        limits()
        log_action("Failed troll riddle")
        if stats["energy"] <= 0:
            print("You are too weak after the bonk. Game Over.")
            return False
        return False

def go_on_adventure():
    print("You set out on an adventure...")
    boss = random.choice(["dragon", "troll"])
    if boss == "dragon":
        result = fight_blind_dragon()
    else:
        result = troll_riddle()

    if result:
        open_gift_box()
    else:
        if stats["energy"] > 0:
            open_gift_box()

# =========================
#    overall game loop
# =========================

def main():
    story_intro()
    choose_name()
    choose_class()

    global turn_counter

    while True:
        time_decay()
        limits()

        if stats["hunger"] >= 100:
            print("You collapse from hunger. Should've ate the sandwich your mother made you.. Game Over.")
            break
        if stats["energy"] <= 0:
            print("You pass out from exhaustion. Heroes need naps too. Game Over.")
            break
        if stats["power"] <= 0:
            print("You overpower yourself to the point of disintegration..Game over.")
            break
        show_status()
        print("What will you do?")
        print("1. Eat (roadside stew)")
        print("2. Rest")
        print("3. Train Power")
        print("4. Go on Adventure (Boss)")
        print("5. View History")
        print("6. Quit")

        choice = input("> ")

        try:
            if choice == "1":
                eat_food()
                open_gift_box()
            elif choice == "2":
                rest()
                open_gift_box()
            elif choice == "3":
                train_power()
                open_gift_box()
            elif choice == "4":
                go_on_adventure()
            elif choice == "5":
                show_history()
            elif choice == "6":
                print("You walk away from your adventure. See you soon...")
                break
            else:
                print("Invalid choice.")
        except:
            print("Hmm..something's wrong..try again!")
            turn_counter += 1
main()
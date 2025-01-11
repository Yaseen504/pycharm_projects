from utilities import clear_terminal, display_text


# Handle Forest Event
def handle_forest_event(player):
    """Handles the initial forest sequence after prologue."""

    forest_text_1 = """
    Because you feel bored of doing nothing but watching T.V and sleeping,
    you decide to explore nature for a change.
    You're in a desolate forest, with vibrant colors flowing through.
    While walking in small, weak steps, you witness a miracle.
    You view a huge, blue meteor strike the cliff of the forest you're
    in, demolishing the cliff and itself.
    Jerry: Woah, what is this? There's no way that happened.
    I-is this some crazy sort of dream?"""

    display_text(
        text=forest_text_1,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="italics",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    clear_terminal()
    forest_text_2 = """
    Once all the smoke wears off from the collision of the meteor,
    it reveals a scar on the ground with a sword lying in its center.
    The sword looks magical and powerful, as if it possesses
    supernatural abilities! You pick it up."""

    display_text(
        text=forest_text_2,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="italics",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    player.character.battle.grant_powers("hydra sword")
    player.character.character_stats()
    print("\t|Hydra Blade is now one of your powers!|\n")


# Explore Cave
def explore_cave(player):
    """Handles the cave exploration event."""

    cave_text = """
    You explore the cave for 20 minutes.
    While you're initially scared of it, you're able to prevail.
    You even find 3 bottles of elixir deep in the cave!
    You can't remember the last time you explored anything on your own so this
    time resonates with you. 
    Maybe life isn't so bad after all."""

    display_text(
        text=cave_text,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="italics",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    clear_terminal()

    # Add elixirs to inventory
    player.character.inventory.add_items("Elixir", 3)
    player.character.character_stats()
    # print("\t|Elixirs have been added to your inventory!|\n")


# Go Swimming


def go_swimming(player):
    """Handles the swimming event."""

    swimming_text = """
    You go out to swim in the waters. Even though you don't know how to swim, 
    you don't care since who would care about what happened to you either way.
    While swimming, you encounter a fish and decide to cook it with the
    lighter you stole from your parents.
    Even though you have little experience making anything, you kind of feel
    happy.
    After all, you made this nice fish all by yourself. It doesn't matter that
    the fish you cooked might've been burned."""

    display_text(
        text=swimming_text,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="italics",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    display_text(
        text=prologue_text,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="italics",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    clear_terminal()

    # Add cooked fish to inventory
    player.character.inventory.add_items("Cooked Fish", 1)
    player.character.character_stats()
    # print("\t|Cooked fish is now in your inventory!|\n")


# Handle Battle
def handle_battle(player, mortimer):
    """Handles the battle event in Scene 1."""

    pre_fight_text = """
    As you're nearing the end of your time in the forest, you sit for a few
    minutes on a sturdy log.
    Suddenly, a strange dragonfly ambushes. Out of instinct,
    you grab your Hydra Sword."""

    display_text(
        text=pre_fight_text,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="italics",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )

    print("Mortimer approaches you!")
    player.character.battle.fight(mortimer)

    if player.character.bars_num > 0:
        post_battle_dialogue(player)
    else:
        input("You have been defeated. GAME OVER")


# Post Battle Dialogue
def post_battle_dialogue(player):
    """Handles the dialogue and events after the battle."""

    post_fight_text = """
    Jerry: Well, encountering that dragonfly was real weird.
    I don't know what's happening, but experiencing all of these crazy events
    in this forest has made me appreciate life just the smallest bit.
    But that creature jumping out of nowhere gave me the spooks.
    After your time at the forest, you decide to head back to your parent's
    house. 
    Jerry: Hopefully mom doesn't yell at me for this."""
    display_text(
        text=post_fight_text,  # List the stores text
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="italics",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )
    clear_terminal()

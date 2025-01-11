from colorama import Fore, Style, init

init()
import os


"""
Character Class - The character class takes in all the initialization values per character
created under the Avatar Class.
"""


class Character:
    def __init__(
        self,
        name: str,
        damage: int = None,
        money_value: float = None,
        max_inventory_space: int = None,
        bars_num: int = None,
        powers: dict = None,
        items: dict = None,
        health: str = "",
        max_bars_num: int = None,
        original_bars_num: str = None,
        heal_tag: str = None,
        quantity_tag: str = None,
        price_tag: str = None,
        info_tag: str = None,
        rarity_tag: str = None,
        type_tag: str = None,
        damage_tag: str = None,
        shop_items_dict: dict = None,
        powers_dict: dict = None,
        items_undiscovered_dict: dict = None,
    ) -> None:

        if True:
            self.name = name  # NAME
            self.damage = damage or 5  # Damage response
            self.powers = powers or {}  # Powers given
            self.health = health  # Health

        if True:
            """
            Tags the dictionaries would use.
            Always update the tag per key update in dictionaries
            """
            self.heal_tag = heal_tag or "heal"
            self.price_tag = price_tag or "price"
            self.quantity_tag = quantity_tag or "quantity"
            self.info_tag = info_tag or "info"
            self.rarity_tag = rarity_tag or "rarity"
            self.type_tag = type_tag or "type"
            self.damage_tag = damage_tag or "damage"

        if True:
            """Storage of all dictionaries"""
            self.shop_items_dict = shop_items_dict or {
                "Apple": {
                    "heal": 5,
                    "quantity": 20,
                    "price": 25,
                    "info": "A juicy red apple that quenches hunger and restores health.",
                    "rarity": "Common",
                },
                "Bread": {
                    "heal": 90,
                    "quantity": 2,
                    "price": 100,
                    "info": "A loaf of bread to regain energy and stamina.",
                    "rarity": "Uncommon",
                },
                "Health Potion": {
                    "heal": 50,
                    "quantity": 5,
                    "price": 300,
                    "info": "A potion that restores a significant amount of health.",
                    "rarity": "Rare",
                },
                "Elixir": {
                    "heal": 100,
                    "quantity": 1,
                    "price": 1000,
                    "info": "A legendary elixir that restores full health and mana.",
                    "rarity": "Legendary",
                },
                "Crystal Shard": {
                    "heal": 25,
                    "quantity": 10,
                    "price": 200,
                    "info": "A rare shard of crystal that has minor restorative abilities.",
                    "rarity": "Rare",
                },
                "Golden Apple": {
                    "heal": 50,
                    "quantity": 2,
                    "price": 2000,
                    "info": "An enchanted apple that bestows immense vitality.",
                    "rarity": "Epic",
                },
            }
            self.powers_dict = powers_dict or {
                "sword": {
                    "damage": 20,  # Removed unnecessary round()
                    "type": "melee",
                    "information": "a sharp, versatile weapon",
                    "rarity": "Rare",
                },
                "bow": {
                    "damage": 15,
                    "type": "ranged",
                    "information": "a weapon for long-distance combat",
                    "rarity": "Common",
                },
                "dagger": {
                    "damage": 12,
                    "type": "melee",
                    "info": "a small, agile weapon for close-quarters combat",
                    "rarity": "Uncommon",
                },
                "stick": {
                    "damage": 10,
                    "type": "melee",
                    "info": "a simple, improvised weapon",
                    "rarity": "Common",
                },
                "rock": {
                    "damage": 5,
                    "type": "throwable",
                    "info": "a basic projectile",
                    "rarity": "Very Common",
                },
                "sling": {
                    "damage": 10,
                    "type": "ranged",
                    "information": "a weapon for hurling projectiles with greater force",
                    "rarity": "Uncommon",
                },
            }
            self.items_undiscovered_dict = items_undiscovered_dict or {
                "Apple": {"heal": 10, "quantity": 50},
                "Bread": {"heal": 15, "quantity": 3},
                "Health Potion": {"heal": 50, "quantity": 5},
                "Mana Potion": {"heal": 50, "quantity": 3},
                "Elixir": {"heal": 100, "quantity": 1},
                "Bandage": {
                    "heal": 20,
                    "quantity": 10,
                    "info": "A cloth used to bind wounds.",
                },
                "Antivenom": {
                    "effect": "Cures Poison",
                    "quantity": 2,
                    "info": "Neutralizes venomous effects.",
                },
            }

        if True:
            self.bars_num = bars_num or 100  # Health value set up
            self.max_bars_num = max_bars_num or round(
                self.bars_num * 1.25
            )  # Max potential health
            if self.bars_num > self.max_bars_num:
                self.bars_num = self.max_bars_num  # Player's health has to be limited
            self.original_bars_num = (
                original_bars_num or self.bars_num
            )  # Original health
            self.health = "=" * int(round(self.bars_num))  # Health as Bars Notation

            # Note: bars = num of bars - int - ie 5
            # Note: health = amount of health - string - ie '======'

        if True:

            self.items = items or {}  # Items in player's inventory

            """Calculates the total items"""
            total_items = sum(item[self.quantity_tag] for item in self.items.values())

            """Calculates the max space to store those items"""
            self.max_inventory_space = max_inventory_space or round(total_items * 1.25)

            """Deletes [certain] items if exceeds max space"""
            total_items = sum(item[self.quantity_tag] for item in self.items.values())

            while total_items > self.max_inventory_space:
                for item_name in list(self.items.keys()):
                    if self.items[item_name]["quantity"] > 0:
                        self.items[item_name]["quantity"] -= 1
                        if self.items[item_name]["quantity"] == 0:
                            del self.items[item_name]
                        break
                total_items = sum(
                    item[self.quantity_tag] for item in self.items.values()
                )

        if True:
            self.money_value = money_value or 250  # Money available (can be a decimal)

    if True:
        """Displays Parts Of Character's Characteristics"""

        def display_name(self):
            print(f"{Fore.GREEN}🌟 Name: {Style.BRIGHT}{self.name}{Style.RESET_ALL}")
            return self.name

        def display_damage(self, extra: bool = False):
            if extra:
                self.display_name()
            print(f"{Fore.RED}⚔️ Damage: {Style.BRIGHT}{self.damage}{Style.RESET_ALL}")
            return self.damage

        def display_powers(self, extra: bool = False):
            if extra:
                self.display_name()

            _ = ""
            if not self.powers:
                print(
                    f"{Fore.YELLOW}🌀 Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}"
                )
            else:
                print(f"{Fore.YELLOW}🌀 Powers: {Style.RESET_ALL}")
                for power, power_type in self.powers.items():
                    for attribute, information in power_type.items():
                        if _ != power:
                            print(
                                f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}"
                            )
                        print(
                            f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
                        )
                        _ = power
            return self.powers

        def display_health(self, extra: bool = False):
            if extra:
                self.display_name()

            print(
                f"{Fore.GREEN}❤️ Health: {Style.BRIGHT}{self.health}{Style.RESET_ALL} : {Fore.MAGENTA}{self.bars_num}hp{Style.RESET_ALL}"
            )
            return self.health, self.bars_num

        def display_max_health(self, extra: bool = False):
            if extra:
                self.display_name()
            print(
                f"{Fore.MAGENTA}💪 Max Health Possible: {Style.BRIGHT}{self.max_bars_num}{Style.RESET_ALL}"
            )
            return self.max_bars_num

        def display_items(self, extra: bool = False):
            if extra:
                self.display_name()
            _ = ""
            if not self.items:
                print(
                    f"{Fore.YELLOW}🎒 Items: {Style.BRIGHT}No Items Available{Style.RESET_ALL}"
                )
            else:
                print(f"{Fore.YELLOW}🎒 Items: {Style.RESET_ALL}")
                for item, item_type in self.items.items():
                    for attribute, information in item_type.items():
                        if _ != item:
                            print(
                                f"\t{Fore.CYAN}• {Style.BRIGHT}{item}{Style.RESET_ALL}"
                            )
                        print(
                            f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
                        )
                        _ = item

                total_items = sum(
                    item[self.quantity_tag] for item in self.items.values()
                )
                print(
                    f"{Fore.CYAN}📦 Total Items: {Style.BRIGHT}{total_items} / {self.max_inventory_space}{Style.RESET_ALL}"
                )

            return self.items

        def display_max_inventory_space(self, extra: bool = False):
            if extra:
                self.display_name()
            print(
                f"{Fore.MAGENTA}📚 Max Inventory Space: {Style.BRIGHT}{self.max_inventory_space}{Style.RESET_ALL}"
            )
            return self.max_inventory_space

        def display_money(self, extra: bool = False):
            if extra:
                self.display_name()
            print(
                f"{Fore.YELLOW}💰 Money: {Style.BRIGHT}{self.money_value}{Style.RESET_ALL}"
            )
            return self.money_value

    if True:
        """Displays Most Of Character's Characteristics"""

        def character_stats(self):  # Shows the overall stats
            os.system("cls" if os.name == "nt" else "clear")
            print(
                f"\n\t\t{Fore.CYAN}🌟 Stats for {Style.BRIGHT}{self.name}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.GREEN}~~!﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏!~~{Style.RESET_ALL}"
            )
            self.display_name()
            self.display_damage()
            self.display_powers()
            self.display_health()
            self.display_max_health()
            self.display_items()
            self.display_max_inventory_space()
            self.display_money()
            print(
                f"{Fore.RED}-------------------------------------------------{Style.RESET_ALL}\n"
            )

        def simple_display_stats(self):
            print(f"{Fore.GREEN}🌟 Name: {self.name}")
            print(f"{Fore.RED}❤️ HP: {self.bars_num}")
            print(f"{Fore.YELLOW}💰 Money: {self.money_value}")
            print(f"{Fore.BLUE}🎒 Inventory: {self.items}")
            print(f"{Fore.MAGENTA}🌀 Powers: {self.powers}{Style.RESET_ALL}")

            return self.name, self.bars_num, self.money_value, self.items, self.powers

    if True:

        """Few of Character's Essential Methods"""

        def update_health_by(self, delta):
            self.bars_num = min(max(0, self.bars_num + delta), self.max_bars_num)
            if self.bars_num >= self.max_bars_num:
                self.bars_num = self.max_bars_num

            self.health = "=" * int(
                round(self.bars_num)
            )  # OVERALL HEALTH as BARS NOTATION

            return self.bars_num

        def update_health_to(self, delta):
            self.bars_num = min(max(0, delta), self.max_bars_num)
            if self.bars_num >= self.max_bars_num:
                self.bars_num = self.max_bars_num

            self.health = "=" * int(
                round(self.bars_num)
            )  # OVERALL HEALTH as BARS NOTATION

            return self.bars_num

        def sum_of_character_items(self):
            total_items = sum(item[self.quantity_tag] for item in self.items.values())
            return total_items

        def return_money_value(self):
            return self.money_value

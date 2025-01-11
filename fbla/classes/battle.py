import math
import random

from fbla.classes.character import Character
from colorama import Fore, Style, init

init()


class Battle:
    def __init__(self, character: Character):
        self.character = character  # Store character object
        self.consequences = [
            "fainted",
            "died",
            "injured",
            "lost",
            "killed",
        ]  # specific consequences when battle ends

    def set_health(
        self, health
    ):  # sets the health to an integer value in relation to the character
        self.character.bars_num = health
        if self.character.bars_num > self.character.max_bars_num:
            self.character.bars_num = self.character.max_bars_num

        return self.character.bars_num

    # note the * allows the function to take as many positional arguments
    def grant_powers(
        self, *chosen_power
    ):  # grants powers in respective to the character
        for weapon_name, weapon_info in self.character.powers_dict.items():
            if weapon_name in chosen_power:
                self.character.powers[weapon_name] = weapon_info  # Use self.character
        return self.character.powers

    def delete_powers(self, *chosen_power):
        for weapon_name in self.character.powers_dict:
            if (
                weapon_name in chosen_power and weapon_name in self.character.powers
            ):  # Use self.character
                del self.character.powers[weapon_name]
        return self.character.powers

    # __ at beginning means name manging, internal use, private members (not recommended to use method outside classes folder)
    def __is_dead(
        self, character2, net_player_hp: int, net_opponent_hp: int
    ):  # use to check if someone is dead (health <= 0)
        if (self.character.bars_num <= 0) or (
            character2.character.bars_num <= 0
        ):  # Use self.character
            if (self.character.bars_num <= 0) and (character2.character.bars_num <= 0):
                self.character.bars_num = 1
                print(
                    "You have managed to use every ounce of strength for this final HP"
                )  # a bonus advantage for player

            if self.character.bars_num <= 0:  # OPPONENT WINS
                self.character.bars_num = 0
                self.display_battle_info(character2, net_player_hp, net_opponent_hp)

                print()
                print("----DEATH----")
                print()

                print(f"You have {self.consequences[0]}")
                print(f"{character2.character.name} has won!")
            else:  # PLAYER WINS
                character2.character.bars_num = 0
                self.display_battle_info(character2, net_player_hp, net_opponent_hp)

                print()
                print("----DEATH----")
                print()

                print(f"{character2.character.name} has {self.consequences[0]}")
                print("You have won!")
            print()
            return True  # death has occurred, game stops

        else:
            return False  # death has NOT occurred; game continues

    def display_powers(self):
        _ = ""
        if not self.character.powers:  # Use self.character
            print(
                f"{Fore.YELLOW}🌀 Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}"
            )
        else:
            print(f"{Fore.YELLOW}🌀 Powers: {Style.RESET_ALL}")
            for (
                power,
                power_type,
            ) in self.character.powers.items():  # Use self.character
                for attribute, information in power_type.items():
                    if _ != power:
                        print(f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}")
                    print(
                        f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
                    )
                    _ = power

    def health_limit_check(self):  # checks the limits of health that can be reached
        if self.character.bars_num >= self.character.max_bars_num:  # Use self.character
            print("Max Health Reached.")
        elif self.character.bars_num <= 0:  # Use self.character
            print("Lowest Health Reached")

    def display_attack_dmg(
        self,
    ):  # checks how much initial damage you do (like the bare minimum excluding all other aspects)
        print(
            f"Attack Potency: {Fore.GREEN}{round(self.character.damage, 2)}{Fore.RESET}"
        )  # Use self.character

    def display_health_information(self, net_player_hp):
        if net_player_hp > 0:  # positive net Health = HEAL / GAIN HEALTH
            print(
                f"Health: {Fore.BLUE}{self.character.health}{Fore.RESET} | {Fore.GREEN}{self.character.bars_num}HP{Fore.RESET} | {Fore.GREEN}You Gained: {net_player_hp}HP{Fore.RESET}"
            )  # Use self.character
        elif net_player_hp < 0:  # negative net Health = LOSE HEALTH
            print(
                f"Health: {Fore.BLUE}{self.character.health}{Fore.RESET} | {Fore.GREEN}{self.character.bars_num}HP{Fore.RESET} | {Fore.RED}You Lost: {net_player_hp}HP{Fore.RESET}"
            )  # Use self.character
        else:
            print(
                f"Health: {Fore.BLUE}{self.character.health}{Fore.RESET} | {Fore.GREEN}{self.character.bars_num}HP{Fore.RESET}"
            )  # Use self.character

    # __ at beginning means name manging, internal use, private members (not recommended to use method outside classes folder)
    @staticmethod
    def __display_power_for_opponent(character2):
        _ = ""
        if not character2.character.powers:  # Use self.character
            print(
                f"{Fore.YELLOW}🌀 Powers: {Style.BRIGHT}No Powers Available{Style.RESET_ALL}"
            )
        else:
            print(f"{Fore.YELLOW}🌀 Powers: {Style.RESET_ALL}")
            for (
                power,
                power_type,
            ) in character2.character.powers.items():  # Use self.character
                for attribute, information in power_type.items():
                    if _ != power:
                        print(f"\t{Fore.CYAN}• {Style.BRIGHT}{power}{Style.RESET_ALL}")
                    print(
                        f"\t\t{Fore.BLUE}• {attribute}{Style.RESET_ALL} : {Style.BRIGHT}{information}{Style.RESET_ALL}"
                    )
                    _ = power

    @staticmethod
    def __health_limit_check_for_opponent(character2):
        if (
            character2.character.bars_num >= character2.character.max_bars_num
        ):  # Use self.character
            print("Max Health Reached.")
        elif character2.character.bars_num <= 0:  # Use self.character
            print("Lowest Health Reached")

    @staticmethod
    def __display_attack_dmg_for_opponent(character2):
        print(
            f"Attack Potency: {Fore.GREEN}{round(character2.character.damage, 2)}{Fore.RESET}"
        )  # Use self.character

    @staticmethod
    def __display_health_information_for_opponent(character2, new_opponent_hp):
        if new_opponent_hp > 0:  # positive net Health = HEAL / GAIN HEALTH
            print(
                f"Health: {Fore.BLUE}{character2.character.health}{Fore.RESET} | {Fore.GREEN}{character2.character.bars_num}HP{Fore.RESET} | {Fore.GREEN}{character2.character.name} Gained: {new_opponent_hp}HP{Fore.RESET}"
            )  # Use self.character
        elif new_opponent_hp < 0:  # negative net Health = LOSE HEALTH
            print(
                f"Health: {Fore.BLUE}{character2.character.health}{Fore.RESET} | {Fore.GREEN}{character2.character.bars_num}HP{Fore.RESET} | {Fore.RED}{character2.character.name} Lost: {new_opponent_hp}HP{Fore.RESET}"
            )  # Use self.character
        else:
            print(
                f"Health: {Fore.BLUE}{character2.character.health}{Fore.RESET} | {Fore.GREEN}{character2.character.bars_num}HP{Fore.RESET}"
            )  # Use self.character

    def display_battle_info(
        self, character2, new_player_hp: int, net_opponent_hp: int
    ):  # Information shown through the display battle class for each character
        print(f"{Style.BRIGHT}{Fore.CYAN}*-*-*-* Battle Stats *-*-*-*{Style.RESET_ALL}")

        # PLAYER DETAILS
        print(
            f"{Fore.MAGENTA}\n{self.character.name} (YOU){Fore.RESET}"
        )  # Use self.character
        self.display_powers()
        self.display_attack_dmg()
        self.display_health_information(new_player_hp)
        self.health_limit_check()

        # OPPONENT DETAILS
        print(
            f"{Fore.RED}\n{character2.character.name} (OPPONENT){Fore.RESET}"
        )  # Use self.character
        self.__display_power_for_opponent(character2)
        self.__display_attack_dmg_for_opponent(character2)
        self.__display_health_information_for_opponent(character2, net_opponent_hp)
        self.__health_limit_check_for_opponent(character2)

    def choose_weapon(self):  # Character chooses a weapon/power/superpower

        while True:
            print(
                "Available powers:", list(self.character.powers.keys())
            )  # Use self.character
            player_power_choice = (
                input("Choose a weapon (or power) from the list above: ")
                .strip()
                .lower()
            )

            if player_power_choice in (
                key.strip().lower() for key in self.character.powers.keys()
            ):  # Use self.character
                print("You have chosen:", player_power_choice)
                break
            else:
                print("Invalid choice. Please try again.")

        return player_power_choice

    @staticmethod  # very static - no .self - local; not global
    def determine_critical_chance(
        chance: float = 0.30, multiplier: float = 1.25
    ) -> float:  # Character imposes a critical hit dmg when lucky

        base_multiplier = 1.00
        return multiplier if random.random() <= chance else base_multiplier

    def adjust_health(
        self, character2, c1: bool = True, c2: bool = True
    ):  # Adjusts the overall health method for both characters
        if c1:
            if (
                self.character.bars_num >= self.character.max_bars_num
            ):  # A defined max health limit for player # Use self.character
                self.character.bars_num = (
                    self.character.max_bars_num
                )  # Use self.character
            self.character.health = "=" * int(
                round(self.character.bars_num)
            )  # Use self.character

        if c2:
            if (
                character2.character.bars_num >= character2.character.max_bars_num
            ):  # A defined max health limit for opponent # Use self.character
                character2.character.bars_num = (
                    character2.character.max_bars_num
                )  # Use self.character
            character2.character.health = "=" * int(
                round(character2.character.bars_num)
            )  # Use self.character

    @staticmethod  # static - no. self - local; not global
    # _ at beginning means internal use only (not recommended to use method outside classes folder)
    def _initialize_fight():  # initializes the fight scene

        print("Do you want to fight?")  # Want to fight?
        while True:
            attack_result = input("Y/N: ").upper().strip()
            if attack_result == "N" or attack_result == "Y":
                break
        print()

        # convert from t/f (true/false) to y/n (yes/no)
        if attack_result == "Y":
            attack_result = True
        else:
            attack_result = False

        return attack_result

    def fight(self, character2):
        if (self.character.powers or character2.character.powers) and (
            (self.character.bars_num > 0) and (character2.character.bars_num > 0)
        ):  # NEEDS A POWER before fighting # Use self.character
            net_player_hp = 0  # local variables to calculate NET HP for opponent *relative to each attack
            new_opponent_hp = 0  # local variables to calculate NET HP for player *relative to each attack
            self.adjust_health(character2, True, True)

            while True:
                self.display_battle_info(character2, net_player_hp, new_opponent_hp)

                net_opponent_hp = 0  # reset
                net_player_hp = 0  # reset

                print()
                attack_result = self._initialize_fight()
                print("----CHOICE SCENE----")
                print()

                # PLAYER ATTACK!
                if attack_result:
                    player_power_choice = (
                        self.choose_weapon()
                    )  # What powers/weapon does the player want to choose?
                    print()
                    print("----FIGHTING SCENE----")
                    print()

                    # OVERALL DAMAGE AFFECT FOR PLAYER
                    player_critical_dmg = self.determine_critical_chance()

                    player_dmg = round(
                        self.character.powers[player_power_choice][
                            self.character.damage_tag
                        ]
                        + self.character.damage
                    )  # Use self.character
                    overall_player_dmg = round(player_dmg * player_critical_dmg)

                    if player_critical_dmg != 1.00:
                        print("CRITICAL DAMAGE!")
                        print(
                            f"({player_dmg}) to ({overall_player_dmg}) by {(player_critical_dmg - 1.00) * 100}%"
                        )

                    print(
                        f"You have used '{player_power_choice}' with attack_dmg of {overall_player_dmg}"
                    )
                    character2.character.bars_num -= overall_player_dmg
                    new_opponent_hp -= overall_player_dmg

                else:
                    # OVERALL HEALTH AFFECT FOR PLAYER
                    print(
                        f"You have skipped a turn"
                    )  # Healing affect takes place for player
                    try:
                        health_ratio = (
                            self.character.bars_num / character2.character.bars_num
                        )  # Use self.character
                    except ZeroDivisionError:
                        health_ratio = 0

                    damage_impact = self.character.damage * 0.5  # Use self.character
                    player_relative_increase = math.ceil(damage_impact * health_ratio)
                    self.character.bars_num += (
                        player_relative_increase  # Use self.character
                    )
                    net_player_hp += player_relative_increase

                    if player_relative_increase:
                        print(f"You have gained {player_relative_increase} health")

                print()

                # OPPONENT ATTACK!
                random_number = random.randint(1, 10)
                if random_number < 7:
                    opponent_power_choice = random.choice(
                        list(character2.character.powers.keys())
                    )  # Use self.character

                    # OVERALL DAMAGE AFFECT FOR OPPONENT
                    opponent_critical_dmg = self.determine_critical_chance()
                    opponent_dmg = round(
                        character2.character.powers[opponent_power_choice][
                            self.character.damage_tag
                        ]
                        + character2.character.damage
                    )  # Use self.character
                    overall_opponent_dmg = round(opponent_dmg * opponent_critical_dmg)

                    if opponent_critical_dmg != 1.00:
                        print("CRITICAL DAMAGE!")
                        print(
                            f"({opponent_dmg}) to ({overall_opponent_dmg}) by {(opponent_critical_dmg - 1.00) * 100}%"
                        )
                    print(
                        f"{character2.character.name} has used '{opponent_power_choice}' with attack_dmg of {overall_opponent_dmg}"
                    )  # Use self.character

                    self.character.bars_num -= (
                        overall_opponent_dmg  # Use self.character
                    )
                    net_player_hp -= overall_opponent_dmg

                else:
                    # OVERALL HEALTH AFFECT FOR OPPONENT
                    print(
                        f"{character2.character.name} has skipped a turn"
                    )  # Healing affect takes place for enemy # Use self.character
                    try:
                        health_ratio = (
                            character2.character.bars_num / self.character.bars_num
                        )  # Use self.character
                    except ZeroDivisionError:
                        health_ratio = 0

                    damage_impact = self.character.damage * 0.5  # Use self.character
                    opponent_relative_increase = math.ceil(damage_impact * health_ratio)
                    character2.character.bars_num += (
                        opponent_relative_increase  # Use self.character
                    )
                    net_opponent_hp += opponent_relative_increase

                    if opponent_relative_increase:
                        print(
                            f"{character2.character.name} has gained {opponent_relative_increase} health"
                        )
                # Adjusts new health for both characters
                self.adjust_health(character2, True, True)

                print()

                # use to check if someone gets defeated
                if self.__is_dead(character2, net_player_hp, net_opponent_hp):
                    break  # breaks loop if someone dies when health <= 0

        else:
            if not (self.character.powers or character2.character.powers):
                print(
                    "Ensure both plays have enough weapons or powers to battle. (At least one weapon/power)"
                )
            else:
                print("Ensure both players have enough health to battle (health > 0).")

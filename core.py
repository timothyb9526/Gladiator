from random import randint, choice
from shell import *


def new_gladiator(health, rage, damage_low, damage_high, power, weapon_name,
                  armor_name):
    gladiator = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high,
        'power': power,
        'weapon': weapon_choice(weapon_name),
        'armor': armor_rating(armor_name)
    }
    return gladiator


def weapon_choice(name):
    weapons = {
        'staff': {
            'name': 'Staff',
            'damage': 5,
            'weight': 15
        },
        'bow': {
            'name': 'Bow',
            'damage': 30,
            'weight': 20
        },
        'sword': {
            'name': 'Sword',
            'damage': 45,
            'weight': 30
        },
        'warhammer': {
            'name': 'Warhammer',
            'damage': 60,
            'weight': 60
        },
    }
    return weapons.get(name, {'name': 'Staff', 'damage': 5})


def armor_rating(name):
    armor = {
        'no_armor': {
            'name': 'no',
            'weight': 0
        },
        'light': {
            'name': 'light',
            'resiliency': .10,
            'weight': 50
        },
        'semi_light': {
            'name': 'semi_light',
            'resiliency': .20,
            'weight': 75
        },
        'heavy': {
            'name': 'heavy',
            'resiliency': .35,
            'weight': 105
        }
    }
    return armor.get(name, {'name': 'no_armor', 'resiliency': 0, 'weight': 0})


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    weapon_damage = attacker['weapon']['damage']
    damage_held = defender['armor']['resiliency']
    weapon_damage_dealt = round((damage_dealt + weapon_damage) * damage_held)
    critical_hit = weapon_damage_dealt * 2
    normal_hit = weapon_damage_dealt
    if randint(1, 100) < attacker['rage']:
        attacker['rage'] = 0
        defender['health'] = defender['health'] - critical_hit
        attacker['power'] = attacker['power'] + 40

    else:
        attacker['rage'] = attacker['rage'] + 15
        attacker['power'] = attacker['power'] + 20
        defender['health'] = defender['health'] - normal_hit

    if attacker['power'] >= 330:
        defender['health'] = defender['health'] - defender['health']


def heal(gladiator):
    if gladiator['health'] >= 200:
        print('You cannot heal if your health is at the max level.')
    elif gladiator['power'] >= 80 and gladiator['health'] <= 60:
        gladiator['power'] = gladiator['power'] - gladiator['power']
        gladiator['health'] = gladiator['health'] + 100

    else:
        gladiator['rage'] = gladiator['rage'] - 10
        gladiator['health'] = gladiator['health'] + 5
        return gladiator


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
    else:
        return False

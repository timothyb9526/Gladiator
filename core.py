from random import randint, choice
from shell import *


def new_gladiator(health, rage, damage_low, damage_high, power, weapon_name):
    gladiator = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high,
        'power': power,
        'weapon': weapon_choice(weapon_name)
    }
    return gladiator


def weapon_choice(name):
    weapons = {
        'staff': {
            'name': 'Staff',
            'damage': 5
        },
        'bow': {
            'name': 'Bow',
            'damage': 10
        },
        'sword': {
            'name': 'Sword',
            'damage': 15
        },
        'hammer': {
            'name': 'Warhammer',
            'damage': 20
        },
    }
    return weapons.get(name, {'name': 'Staff', 'damage': 5})


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    weapon_damage = attacker['weapon']['damage']
    weapon_damage_dealt = damage_dealt + weapon_damage
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

    if attacker['power'] >= 160:
        defender['health'] = defender['health'] - defender['health']


def heal(gladiator):
    if gladiator['health'] == 100:
        print('You cannot heal if your health is at the max level.')

    elif gladiator['power'] >= 50 and gladiator['health'] <= 60:
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

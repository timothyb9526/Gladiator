from random import randint
from shell import *


def new_gladiator(health, rage, damage_low, damage_high, power):
    gladiator = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high,
        'power': power
    }
    return gladiator


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    critical_hit = damage_dealt * 2
    normal_hit = damage_dealt
    if randint(1, 100) < attacker['rage']:
        attacker['rage'] = 0
        defender['health'] = defender['health'] - critical_hit
        attacker['power'] = attacker['power'] + 40

    else:
        attacker['rage'] = attacker['rage'] + 15
        attacker['power'] = attacker['power'] + 20
        defender['health'] = defender['health'] - normal_hit

    if attacker['power'] == 400:
        defender['health'] = defender['health'] - defender['health']


def heal(gladiator):
    if gladiator['health'] == 100:
        print('You cannot heal if your health is at the max level.')

    elif gladiator['health'] <= 100:
        gladiator['power'] = gladiator['power'] - 35
        gladiator['health'] = gladiator['health'] + 30

    elif gladiator['power'] >= 260 and gladiator['health'] <= 150:
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

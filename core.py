from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    gladiator = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }
    return gladiator


def new_weapons(attack_dmage):

    weapons = {'Bow':'Attack damage': 20}, {'sword': 'Attack damage': 30}


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    critical_hit = damage_dealt * 2
    normal_hit = damage_dealt
    if randint(1, 100) < attacker['rage']:
        attacker['rage'] = 0
        defender['health'] = defender['health'] - critical_hit
    else:
        attacker['rage'] = attacker['rage'] + 15
        defender['health'] = defender['health'] - normal_hit


def heal(gladiator):
    if gladiator['health'] == 100:
        print('You cannot heal if your health is at the max level.')
    else:
        gladiator['rage'] = gladiator['rage'] - 10
        gladiator['health'] = gladiator['health'] + 5
        return gladiator


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
    else:
        return False

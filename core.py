from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    gladiator = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }
    return gladiator


def attack(attacker, defender):
    damage_dealt = randint(damage_low, damage_high)
    critical_hit = damage_dealt * 2
    normal_hit = damage_dealt
    if randint(1, 100) < attacker['rage']:
        attacker['rage'] = 0
        defender['health'] = defender['health'] - critical_hit
        return defender['health'], attacker
    else:
        attacker['rage'] = attacker['rage'] + 15
         defender['health'] = defender['health'] - normal_hit
        return defender['health']


def heal(gladiator):
    if gladiator['health'] == 100:
        print('You cannot heal if your health is at the max level.')
    else:
        gladiator['rage'] = gladiator['rage'] - 10
        return gladiator


def is_dead(gladiator):
    if gladiator['health'] == 0:
        return True
    else:
        return False

from core import *


def test_new_gladiator():
    assert new_gladiator(100, 20, 15, 30) == {
        'health': 100,
        'rage': 20,
        'damage_low': 15,
        'damage_high': 30
    }


def test_attack_with_zero_rage():
    attacker = {'health': 100, 'rage': 0, 'damage_low': 15, 'damage_high': 15}

    attack(attacker, {
        'health': 100,
        'rage': 0,
        'damage_low': 15,
        'damage_high': 30
    })

    assert attacker['rage'] == 15


def test_attack_with_100_rage():
    attacker = {
        'health': 100,
        'rage': 100,
        'damage_low': 15,
        'damage_high': 15
    }
    attack(attacker, {
        'health': 100,
        'rage': 0,
        'damage_low': 15,
        'damage_high': 30
    })

    assert attacker['rage'] == 0


def test_heal():
    gladiator = {'health': 95, 'rage': 30, 'damage_low': 15, 'damage_high': 15}
    assert heal(gladiator)

    assert gladiator['rage'] == 20

    assert gladiator['health'] == 100

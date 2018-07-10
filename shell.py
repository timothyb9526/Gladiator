from core import *


def gladiator(gladiator1, gladiator2):
    while True:

        attack_method = input(
            'gladiator1 .... What would you like to do?\n- [A]ttack\n- [P]ass\n- [Q]uit\n- [H]eal\n'
        )
        if attack_method == 'a':

            attack(gladiator1, gladiator2)
            print('gladiator1', gladiator1['health'], 'HP', '|||',
                  gladiator1['rage'], 'Rage', '|||', gladiator1['power'],
                  'power')
            print('gladiator2', gladiator2['health'], 'HP', '|||',
                  gladiator2['rage'], 'Rage', '|||', gladiator2['power'],
                  'power')
            break
        elif attack_method == 'q':
            print('Gladiator1: SURVIVED!!!\nGladiator2: SURVIVED!!!')
            exit()
        elif attack_method == 'p':
            print('Gladiator1 did nothing this round.')
            break
        elif attack_method == 'h':
            heal(gladiator1)
            print('gladiator1', gladiator1['health'], 'HP', '|||',
                  gladiator1['rage'], 'Rage', '|||', gladiator1['power'],
                  'power')
            print('gladiator2', gladiator2['health'], 'HP', '|||',
                  gladiator2['rage'], 'Rage', '|||', gladiator2['power'],
                  'power')
            break


def gladiator2(gladiator1, gladiator2):
    while True:
        gladiator_2 = input(
            'gladiator2 .... What would you like to do?\n- [A]ttack\n- [P]ass\n- [Q]uit\n- [H]eal\n'
        )

        if gladiator_2 == 'a':

            attack(gladiator2, gladiator1)
            print('gladiator1', gladiator1['health'], 'HP', '|||',
                  gladiator1['rage'], 'Rage', '|||', gladiator1['power'],
                  'power')
            print('gladiator2', gladiator2['health'], 'HP', '|||',
                  gladiator2['rage'], 'Rage', '|||', gladiator2['power'],
                  'power')
            break
        elif gladiator_2 == 'q':
            print('Gladiator1: SURVIVED!!!\nGladiator2: SURVIVED!!!')

            exit()
        elif gladiator_2 == 'p':
            print('Gladiator2 did nothing this round.')
            break
        elif gladiator_2 == 'h':
            heal(gladiator2)
            print('gladiator1', gladiator1['health'], 'HP', '|||',
                  gladiator1['rage'], 'Rage', '|||', gladiator1['power'],
                  'power')
            print('gladiator2', gladiator2['health'], 'HP', '|||',
                  gladiator2['rage'], 'Rage', '|||', gladiator2['power'],
                  'power')
            break


def battle():
    g1 = {
        'health': 300,
        'rage': 0,
        'damage_low': 10,
        'damage_high': 20,
        'power': 0
    }

    g2 = {
        'health': 300,
        'rage': 0,
        'damage_low': 10,
        'damage_high': 20,
        'power': 0
    }

    while True:
        if is_dead(g1) == True:
            print('GLADIATOR2: DID NOT SURVIVE!!!')
            print('GLADIATOR1: WINS!!!')
            break
            exit()

        gladiator(g1, g2)

        if is_dead(g2) == True:
            print('GLADIATOR1: DID NOT SURVIVE!!!')
            print('GLADIATOR2: WINS!!!')
            break
            exit()

        gladiator2(g1, g2)


def main():
    battle()


if __name__ == '__main__':
    main()

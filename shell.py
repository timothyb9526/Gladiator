from core import *


def gladiator(gladiator1, gladiator2):
    while True:

        attack_method = input(
            'gladiator1 .... What would you like to do?\n- attack\n- pass\n- quit\n- heal\n'
        )

        if attack_method == 'attack':

            attack(gladiator1, gladiator2)
            print('gladiator1', gladiator1['health'], 'HP', '|||',
                  gladiator1['rage'], 'Rage')
            print('gladiator2', gladiator2['health'], 'HP', '|||',
                  gladiator2['rage'], 'Rage')
            break
        elif attack_method == 'quit':
            print('Gladiator1: SURVIVED!!!\nGladiator2: SURVIVED!!!')
            exit()
        elif attack_method == 'pass':
            print('Gladiator1 did nothing this round.')
            break
        elif attack_method == 'heal':
            heal(gladiator1)
            print('gladiator1', gladiator1['health'], 'HP', '|||',
                  gladiator1['rage'], 'Rage')
            print('gladiator2', gladiator2['health'], 'HP', '|||',
                  gladiator2['rage'], 'Rage')
            break


def gladiator2(gladiator1, gladiator2):
    while True:
        gladiator_2 = input(
            'gladiator2 .... What would you like to do?\n- attack\n- pass\n- quit\n- heal\n'
        )

        if gladiator_2 == 'attack':

            attack(gladiator2, gladiator1)
            print('gladiator1', gladiator1['health'], 'HP', '|||',
                  gladiator1['rage'], 'Rage')
            print('gladiator2', gladiator2['health'], 'HP', '|||',
                  gladiator2['rage'], 'Rage')
            break
        elif gladiator_2 == 'quit':
            print('Gladiator1: SURVIVED!!!\nGladiator2: SURVIVED!!!')

            exit()
        elif gladiator_2 == 'pass':
            print('Gladiator1 did nothing this round.')
            break
        elif gladiator_2 == 'heal':
            heal(gladiator1)
            print('gladiator1', gladiator1['health'], 'HP', '|||',
                  gladiator1['rage'], 'Rage')
            print('gladiator2', gladiator2['health'], 'HP', '|||',
                  gladiator2['rage'], 'Rage')
            break


def battle():
    g1 = {'health': 100, 'rage': 0, 'damage_low': 10, 'damage_high': 20}

    g2 = {'health': 100, 'rage': 0, 'damage_low': 10, 'damage_high': 20}

    while True:
        gladiator(g1, g2)
        gladiator2(g1, g2)


def main():
    battle()


if __name__ == '__main__':
    main()

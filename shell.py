from core import *
from random import choice


def gladiator_1_turn(gladiator1, gladiator2):
    while True:
        attack_method = input(
            'gladiator1 .... What would you like to do?\n- [A]ttack\n- [P]ass\n- [Q]uit\n- [H]eal\n'
        )
        if attack_method == 'a':

            attack(gladiator1, gladiator2)
            print('WE\'RE UNDER ATTACK!!!!')
            print('gladiator1', gladiator1['health'], 'HP |||',
                  gladiator1['rage'], 'Rage |||', gladiator1['power'],
                  'power, has\n', gladiator1['armor']['name'],
                  'Armor and has the', gladiator1['weapon']['name'])
            print('gladiator2', gladiator2['health'], 'HP |||',
                  gladiator2['rage'], 'Rage |||', gladiator2['power'],
                  'power, has\n', gladiator2['armor']['name'],
                  'Armor and has the', gladiator2['weapon']['name'])

            break
        elif attack_method == 'q':
            print('Gladiator1: SURVIVED!!!\nGladiator2: SURVIVED!!!')
            exit()
        elif attack_method == 'p':
            print('Gladiator1 did nothing this round.')
            break
        elif attack_method == 'h':
            heal(gladiator1)
            print('gladiator1', gladiator1['health'], 'HP |||',
                  gladiator1['rage'], 'Rage |||', gladiator1['power'],
                  'power, has\n', gladiator1['armor']['name'],
                  'Armor and has the', gladiator1['weapon']['name'])
            print('gladiator2', gladiator2['health'], 'HP |||',
                  gladiator2['rage'], 'Rage |||', gladiator2['power'],
                  'power, has\n', gladiator2['armor']['name'],
                  'Armor and has the', gladiator2['weapon']['name'])

            break


def gladiator_2_turn(gladiator1, gladiator2):
    while True:
        attack_method = input(
            'gladiator2 .... What would you like to do?\n- [A]ttack\n- [P]ass\n- [Q]uit\n- [H]eal\n'
        )
        if attack_method == 'a':

            attack(gladiator1, gladiator2)
            print('WE\'RE UNDER ATTACK!!!!')
            print('gladiator2', gladiator2['health'], 'HP |||',
                  gladiator2['rage'], 'Rage |||', gladiator2['power'],
                  'power, has\n', gladiator2['armor']['name'],
                  'Armor and has the', gladiator2['weapon']['name'])
            print('gladiator1', gladiator1['health'], 'HP |||',
                  gladiator1['rage'], 'Rage |||', gladiator1['power'],
                  'power, has\n', gladiator1['armor']['name'],
                  'Armor and has the', gladiator1['weapon']['name'])

            break
        elif attack_method == 'q':
            print('gladiator2: SURVIVED!!!\nGladiator1: SURVIVED!!!')
            exit()
        elif attack_method == 'p':
            print('gladiator2 did nothing this round.')
            break
        elif attack_method == 'h':
            heal(gladiator2)
            print('gladiator2', gladiator2['health'], 'HP |||',
                  gladiator2['rage'], 'Rage |||', gladiator2['power'],
                  'power, has\n', gladiator2['armor']['name'],
                  'Armor and has the', gladiator2['weapon']['name'])
            print('gladiator2', gladiator2['health'], 'HP |||',
                  gladiator2['rage'], 'Rage |||', gladiator2['power'],
                  'power, has\n', gladiator2['armor']['name'],
                  'Armor and has the', gladiator2['weapon']['name'])

            break


def computer_turn(gladiator1, gladiator2):
    while True:

        print(
            'gladiator2 .... What would you like to do?\n- [A]ttack\n- [P]ass\n- [Q]uit\n- [H]eal\n'
        )

        if gladiator2['health'] >= 100 and gladiator2['health'] <= 200:
            gladiator2_options = ['A', 'P', 'H']
            option = choice(gladiator2_options)
            if option == 'A':
                attack(gladiator2, gladiator1)
                print(option)
                print('WE\'RE UNDER ATTACK!!!!!')
                print('gladiator1', gladiator1['health'], 'HP |||',
                      gladiator1['rage'], 'Rage |||', gladiator1['power'],
                      'power, has\n', gladiator1['armor']['name'],
                      'Armor and has the', gladiator1['weapon']['name'])
                print('gladiator2', gladiator2['health'], 'HP |||',
                      gladiator2['rage'], 'Rage |||', gladiator2['power'],
                      'power, has\n', gladiator2['armor']['name'],
                      'Armor and has the', gladiator2['weapon']['name'])
                break
            elif option == 'P':
                print(option)
                print('Gladiator2 did nothing this round.')

                break
            elif option == 'H':
                heal(gladiator2)
                print(option)
                print('gladiator1', gladiator1['health'], 'HP |||',
                      gladiator1['rage'], 'Rage |||', gladiator1['power'],
                      'power, has\n', gladiator1['armor']['name'],
                      'Armor and has the', gladiator1['weapon']['name'])
                print('gladiator2', gladiator2['health'], 'HP |||',
                      gladiator2['rage'], 'Rage |||', gladiator2['power'],
                      'power, has\n', gladiator2['armor']['name'],
                      'Armor and has the', gladiator2['weapon']['name'])
                break
        elif gladiator2['health'] < 100:
            heal(gladiator2)
            print('gladiator1', gladiator1['health'], 'HP |||',
                  gladiator1['rage'], 'Rage |||', gladiator1['power'],
                  'power, has\n', gladiator1['armor']['name'],
                  'Armor and has the', gladiator1['weapon']['name'])
            print('gladiator2', gladiator2['health'], 'HP |||',
                  gladiator2['rage'], 'Rage |||', gladiator2['power'],
                  'power, has\n', gladiator2['armor']['name'],
                  'Armor and has the', gladiator2['weapon']['name'])
            break


def single_player():
    gladiator_1_turn()
    gladiator_2_turn()


def multi_player():
    gladiator_1_turn()
    computer_turn()


def battle():

    g1 = new_gladiator(200, 0, 10, 20, 0, 'bow', 'light')

    g2 = new_gladiator(200, 0, 10, 20, 0, 'sword', 'semi_light')
    while True:
        if is_dead(g1) == True:
            print('GLADIATOR1: DID NOT SURVIVE!!!')
            print('GLADIATOR2: WINS!!!')
            break
            exit()

        gladiator_1_turn(g1, g2)

        if is_dead(g2) == True:
            print('GLADIATOR2: DID NOT SURVIVE!!!')
            print('GLADIATOR1: WINS!!!')
            break
            exit()

        gladiator_2_turn(g1, g2)


def main():
    game_mode = input('Would you like to play single or multiplayer?\n')
    if game_mode == 'single':
        single_player()
    else:
        multi_player()

    battle()


if __name__ == '__main__':
    main()

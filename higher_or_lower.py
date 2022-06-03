from random import randint
import get_data
import time
import os

src_dict = get_data.get_data()

src_list = []
for x in src_dict:
    src_list.append(x)


user_attempts = 5
user_score = 0

def is_higher(lang_a, lang_b):
    """Check if language B is higher than language A."""
    rating_a = src_dict[lang_a]
    rating_b = src_dict[lang_b]
    delta = rating_b - rating_a
    if delta > 0:
        return True
    else:
        return False

def play(a):
    os.system('cls')
    global user_attempts
    global user_score
    print(f'[Higher or Lower Game]\n...attempts left: {user_attempts}\n')
    time.sleep(1)
    b = src_list[randint(0, len(src_list)-1)]
    while a == b:
        b = src_list[randint(0, len(src_list)-1)]
    print(f'\t{a} (with rating {src_dict[a]}%)')
    time.sleep(1)
    print(f'\t  VS')
    time.sleep(1)
    print(f'\t{b}\n')
    time.sleep(1)
    user_input = input(f'Is {b} higher than {a}?\nYour guess? (\'higher\' or \'lower\')\n ').lower()
    print()
    is_it_higher = is_higher(a, b)
    if user_input == 'higher' and is_it_higher == True:
        print('Correct!')
        user_score += 1
    elif user_input == 'lower' and is_it_higher == False:
        print('Correct!')
        user_score += 1
    else:
        user_attempts -= 1
        print(f'...minus one attempt')
    time.sleep(2)
    return b


def main():
    a = src_list[randint(0, len(src_list)-1)]
    while user_attempts > 0:
        b = play(a)
        a = b
    os.system('cls')
    print('...sorry, you have no attempts. Game Over!')
    print(f'Your score: {user_score}')
    print()


if __name__ == '__main__':
    main()
import random


def monster(player):
    print('Вы нарвались на монстра!')
    print(f'Ваше текущее здоровье: {player["hp"]}')

    monster_hp = random.randint(25, 50)
    monster_damage = random.randint(5, 15)

    while monster_hp > 0 and player['hp'] > 0:
        print('Выберите действие:')
        print('1. Атаковать')
        print('2. Использовать навык')
        print('3. Попытаться убежать')

        choice = input('Ваш выбор: ')

        if choice == '1':
            damage_dealt = random.randint(weapons_damage[player["weapon"]] - 3, weapons_damage[player["weapon"]] + 3)
            monster_hp -= damage_dealt
            player['hp'] -= monster_damage
            print(
                f'Вы нанесли {damage_dealt} урона монстру. У монстра осталось {monster_hp} хп\n'
                f'Монстр ударил вас в ответ, у вас осталось {player["hp"]} хп')
        elif choice == '2':
            print('Вы используете свой навык. (логика еще не прописана)')
        elif choice == '3':
            print('Вы пытаетесь убежать...')
            if random.choice([True, False]):
                print('Вы убежали успешно.')
                return
            else:
                print('Вам не удалось убежать!')


def chest(player):
    print('Вы нашли сундук!')
    loot_type = random.choice(['money', 'weapon'])

    if loot_type == 'money':
        money_found = random.randint(5, 20)
        player['money'] += money_found
        print(f'Вы нашли {money_found} монет. Теперь у вас {player["money"]} монет.')

    elif loot_type == 'weapon':
        new_weapon = random.choice(['gold sword', 'steel dagger', 'ruby blade'])
        print(f'Вы нашли новое оружие: {new_weapon}.')
        if weapons_damage[new_weapon] > weapons_damage[player['weapon']]:
            player['weapon'] = new_weapon
            print(f'Вы подобрали новое оружие: {new_weapon}.')
        else:
            print('Новое оружие не лучше вашего текущего.')


def trap(player):
    print('Вы попали в ловушку!')
    damage = random.randint(10, 20)
    player['hp'] -= damage
    print(f'Вы потеряли {damage} хп. Ваше текущее хп: {player["hp"]}')


def trader(player):
    print('Вы встретили торговца.')
    print('Торговец предлагает вам обмен:')
    print(f'У вас {player["money"]} монет и {player["hp"]} хп')
    print('1. Продать оружие за деньги')
    print('2. Купить diamond sword (30 монет)')
    print('3. Восстановление фулл хп (10 монет)')
    print('4. Купить ruby blade (50 монет)')
    print('5. Пройти мимо')
    choice = input('Выберите вариант: ')
    while choice.lower() not in ['1', '2', '3', '4', '5']:
        print('Некорректный ввод.')
        choice = input('Пожалуйста, введите число из списка: ')

    if choice == '1':
        if player['weapon'] != 'iron sword':
            sell_price = weapons_damage[player['weapon']] // 2
            print(f'Вы продали {player["weapon"]} за {sell_price} монет.')
            player['money'] += sell_price
            player['weapon'] = 'iron sword'
        else:
            print('У вас нет оружия для продажи.')

    elif choice == '2':
        if player['money'] >= 30:
            print('Вы купили новое оружие: diamond sword за 30 монет.')
            player['money'] -= 30
            player['weapon'] = 'diamond sword'
        else:
            print('У вас недостаточно монет для покупки.')
    elif choice == '3':
        if player['money'] >= 10:
            print('Вы отхилили фулл хп')
            player['money'] -= 10
            player['hp'] = 100
        else:
            print('У вас недостаточно монет для покупки.')


    elif choice == '4':
        if player['money'] >= 50:
            print('Вы купили новое оружие: ruby blade за 30 монет.')
            player['money'] -= 50
            player['weapon'] = 'ruby blade'
        else:
            print('У вас недостаточно монет для покупки.')

    elif choice == '5':
        print('Вы прошли мимо')


def rest_area(player):
    print('Вы нашли уютное место для отдыха.')
    exp_gain = random.randint(3, 10)
    player['exp'] += exp_gain
    print(f'Вы отдохнули и получили {exp_gain} опыта. Текущий опыт: {player["exp"]}')


def healing_spring(player):
    print('Вы нашли источник исцеления!')
    healing_amount = random.randint(10, 30)
    player['hp'] = min(100, player['hp'] + healing_amount)
    print(f'Вы восстановили {healing_amount} хп. Текущее хп: {player["hp"]}')


def bandit_ambush(player):
    print('Вы попали в засаду бандитов!')
    print('1. Сражаться с бандитами')
    print('2. Попытаться заплатить выкуп')
    choice = input('Выберите вариант: ')
    while choice not in ['1', '2']:
        print('Некорректный ввод. Пожалуйста, введите 1 или 2.')
        choice = input('Выберите вариант: ')

    if choice == '1':
        damage = random.randint(10, 25)
        player['hp'] -= damage
        print(f'Вы потерпели поражение. Потеряно {damage} хп. Текущее хп: {player["hp"]}')
    else:
        ransom_amount = random.randint(10, 30)
        if player['money'] >= ransom_amount:
            player['money'] -= ransom_amount
            print(f'Вы заплатили {ransom_amount} монет бандитам.')
        else:
            print('У вас недостаточно монет. Сражение начинается!')
            damage = random.randint(10, 25)
            player['hp'] -= damage
            print(f'Вы потерпели поражение. Потеряно {damage} хп. Текущее хп: {player["hp"]}')


def boss_encounter(player):
    print('--------------------------------------------------')
    print('Вы встретили могущественного босса!')
    boss_hp = random.randint(80, 120)
    boss_damage = random.randint(10, 25)
    print(f'Хп босса: {boss_hp}')
    while boss_hp > 0 and player['hp'] > 0:
        boss_hp -= weapons_damage[player['weapon']]
        player['hp'] -= boss_damage
    if player['hp'] <= 0:
        print('Вы потерпели поражение от босса. Игра окончена.')
    else:
        print('Вы победили босса! Получено много опыта и монет.')
        player['exp'] += random.randint(10, 20)
        player['money'] += random.randint(15, 25)


def turn_left(player):
    print(f'У вас {player["money"]} монет, {player["hp"]} хп, {player["exp"]} опыта.\n'
          f'Ваше оружие: {player["weapon"]}')
    choice = input('Вы нашли перекресток. Хотите повернуть налево? (да/нет): ')
    while choice.lower() not in ['да', 'нет']:
        print('Некорректный ввод. Пожалуйста, введите "да" или "нет".')
        choice = input('Вы нашли перекресток. Хотите повернуть налево? (да/нет): ')

    if choice.lower() == 'да':
        print('Вы повернули налево и...')
        random_event(player)
    else:
        print('Вы решили идти прямо.')


def turn_right(player):
    print(f'У вас {player["money"]} монет, {player["hp"]} хп, {player["exp"]} опыта.\n'
          f'Ваше оружие: {player["weapon"]}')
    choice = input('Вы нашли перекресток. Хотите повернуть направо? (да/нет): ')
    while choice.lower() not in ['да', 'нет']:
        print('Некорректный ввод. Пожалуйста, введите "да" или "нет".')
        choice = input('Вы нашли перекресток. Хотите повернуть направо? (да/нет): ')

    if choice.lower() == 'да':
        print('Вы повернули направо и...')
        random_event(player)
    else:
        print('Вы решили идти прямо.')


def dont_turn(player):
    print(f'У вас {player["money"]} монет, {player["hp"]} хп, {player["exp"]} опыта.\n'
          f'Ваше оружие: {player["weapon"]}')
    print('Вы решили идти прямо и...')
    random_event(player)


def random_event(player):
    if boss_check():
        boss_encounter(player)
    else:
        event = random.choice(['monster', 'chest', 'trap', 'trader', 'rest_area', 'healing_spring', 'bandit_ambush'])
        if event == 'monster':
            monster(player)
        elif event == 'chest':
            chest(player)
        elif event == 'trap':
            trap(player)
        elif event == 'trader':
            trader(player)
        elif event == 'rest_area':
            rest_area(player)
        elif event == 'healing_spring':
            healing_spring(player)
        elif event == 'bandit_ambush':
            bandit_ambush(player)


def turn_random(player):
    directions = ['left', 'right', 'dont_turn']
    random_direction = random.choice(directions)

    if random_direction == 'left':
        turn_left(player)
    elif random_direction == 'right':
        turn_right(player)
    elif random_direction == 'dont_turn':
        dont_turn(player)


turn_counter = 0


def boss_check():
    global turn_counter
    turn_counter += 1
    if turn_counter % 20 == 0:
        return True
    return False


player = {'money': 0,
          'hp': 100,
          'exp': 0,
          'weapon': 'iron sword'}
weapons_damage = {'iron sword': random.randint(7, 13),
                  'gold sword': random.randint(13, 19),
                  'diamond sword': random.randint(19, 31),
                  'steel dagger': random.randint(8, 15),
                  'ruby blade': random.randint(22, 35)
                  }

x = int(input("На сколько шагов создать игру?\n"))
for i in range(x):
    if player['hp'] > 0:
        print('----------------------------------------------------------------------------')
        turn_random(player)
    else:
        print('Вы умерли')
        break

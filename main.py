import random


def monster(player):
    print(
        f'Вы нарвались на монстра.\n'
        f'Ваше хп: {player["hp"]}\n'
        f'Ваше количество опыта: {player["exp"]}\n'
        f'Ваше оружие: {player["weapon"]} ')
    monster_hp = random.randint(25, 50)
    monster_hp_after_hit = monster_hp
    player_hp_after_hit = player['hp']
    print(f'Хп монстра: {monster_hp}')
    while monster_hp_after_hit > 0:
        monster_hp_after_hit -= weapons_damage[player["weapon"]]
        player_hp_after_hit -= random.randint(3, 9)
    print(f'Вы победили!\n'
          f'Ваше хп после битвы с монстром {player_hp_after_hit}')
    player['exp'] += random.randint(1, 2)
    player['money'] += random.randint(1, 2)


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
        print('Вы отхилили фулл хп')
        player['money'] -= 10
        player['hp'] = 100

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

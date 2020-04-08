class VClient:
    def __init__(self):
        import vk_api

        mounths = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентяюря', 10: 'октября', 11: 'ноября', 12: 'декабря'}

        login = input(' Login:')
        password=input(' Password: ')

        try:
            vk_session = vk_api.VkApi(login, password, app_id='2685278')
            vk_session.auth()
        except vk_api.exceptions.BadPassword:
            print('Bad password.'); exit()
        except vk_api.exceptions.AuthError:
            vk_session = vk_api.VkApi(login, password, app_id='2685278', auth_handler = lambda: [input('Two-factor auth code:'), False])
            vk_session.auth()

        # using methods: vk_session.method('method.name', {'param0': value, 'param1': value})

        acc_info = vk_session.method('account.getProfileInfo')
        acc_first_name = acc_info['first_name']
        acc_last_name = acc_info['last_name']
        acc_birthday = acc_info['bdate'].split('.')
        acc_birthday = f'{acc_birthday[0]} {mounths[int(acc_birthday[1])]} {acc_birthday[2]} года'
        acc_hometown = acc_info['home_town']
        acc_relation = acc_info['relation'] 
        try:
            acc_screen_name = acc_info['screen_name']
        except KeyError: None
        acc_sex = acc_info['sex']
        acc_status = acc_info['status']
        try:
            acc_country = acc_info['country']['title']
        except KeyError: None
        try:
            acc_city = acc_info['city']['title']
        except KeyError: None
        try:
            acc_relation_partner = acc_info['relation_partner']
        except KeyError: None
        try:
            acc_relation_requests = acc_info['relation_requests']
        except KeyError: None
        print(f'Вы вошли как пользователь с именем {acc_first_name} и фамилией {acc_last_name} ', end='')
        try:
            print(f'из города {acc_city}, ', end='')
        except NameError: None
        try:
            print(f'из страны {acc_country}. ', end='')
        except NameError: None
        try:
            print(f'У пользователя имеется короткая ссылка: {acc_screen_name}. ', end='')
        except NameError: None
        if acc_hometown != '':
            print(f'Родной город - {acc_hometown}. ', end='')
        try:
            print(f'На данный момент в отношениях с {acc_relation_partner["first_name"]} {acc_relation_partner["last_name"]}, с ID {acc_relation_partner["id"]}. ', end='')
        except NameError: None
        if acc_relation == 0:
            print('Не указан статус отношений. ', end='')
        else:
            if acc_sex == 1:
                if acc_relation == 1:
                    print('Статус отношений - не замужем. ', end='')
                elif acc_relation == 2:
                    print('Статус отношений - есть друг.  ', end='')
                elif acc_relation == 3:
                    print('Статус отношений - помолвлена. ', end='')
                elif acc_relation == 4:
                    print('Статус отношений - замужем. ', end='')
                elif acc_relation == 5:
                    print('Статус отношений - всё сложно. ', end='')
                elif acc_relation == 6:
                    print('Статус отношений - в активном поиске. ', end='')
                elif acc_relation == 7:
                    print('Статус отношений - влюблена. ', end='')
                elif acc_relation == 8:
                    print('Статус отношений - в гражданском браке. ', end='')
            elif acc_sex == 2:
                if acc_relation == 1: 
                    print('Статус отношений - не женат. ', end='')
                elif acc_relation == 2: 
                    print('Статус отношений - есть подруга.  ', end='')
                elif acc_relation == 3: 
                    print('Статус отношений - помолвлен. ', end='')
                elif acc_relation == 4: 
                    print('Статус отношений - женат. ', end='')
                elif acc_relation == 5:
                    print('Статус отношений - всё сложно. ', end='')
                elif acc_relation == 6: 
                    print('Статус отношений - в активном поиске. ', end='')
                elif acc_relation == 7:
                    print('Статус отношений - влюблён. ', end='')
                elif acc_relation == 8:
                    print('Статус отношений - в гражданском браке. ', end='')
        print(f'День рождения пользователя - {acc_birthday}. ', end='')
        if acc_sex !=0:
            if acc_sex == 1:
                print('Пол пользователя - женский. ', end='')
            elif acc_sex == 2:
                print('Пол пользователя - мужской. ', end='')
        else:
            print('У пользователя не указан пол. ', end='')
        if acc_status != '':
            print(f'У пользователя указан следующий статус: \'{acc_status}\'.')
        else:
            print('У пользователя не указан статус.')

messenger = VClient()

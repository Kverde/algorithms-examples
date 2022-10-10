def day_of_week1(num):
    if num == 0:
        dayName = 'Понедельник'
    elif num == 1:
        dayName = 'Вторник'
    elif num == 2:
        dayName = 'Среда'
    elif num == 3:
        dayName = 'Четверг'
    elif num == 4:
        dayName = 'Пятница'
    elif num == 5:
        dayName = 'Суббота'
    elif num == 6:
        dayName = 'Воскресенье'

    return dayName


def day_of_week2(num):
    if num == 0:
        dayName = 'Понедельник'
    elif num == 1:
        dayName = 'Вторник'
    elif num == 2:
        dayName = 'Среда'
    elif num == 3:
        dayName = 'Четверг'
    elif num == 4:
        dayName = 'Пятница'
    elif num == 5:
        dayName = 'Суббота'
    elif num == 6:
        dayName = 'Воскресенье'
    else:
        dayName = 'Неверный день недели'

    return dayName


def day_of_week3(num):
    if num == 0:
        dayName = 'Понедельник'
    elif num == 1:
        dayName = 'Вторник'
    elif num == 2:
        dayName = 'Среда'
    elif num == 3:
        dayName = 'Четверг'
    elif num == 4:
        dayName = 'Пятница'
    elif num == 5:
        dayName = 'Суббота'
    elif num == 6:
        dayName = 'Воскресенье'
    else:
        raise ValueError('Неверный день недели')

    return dayName


def day_of_week4(num):
    if num == 0:
        return 'Понедельник'
    if num == 1:
        return 'Вторник'
    if num == 2:
        return 'Среда'
    if num == 3:
        return 'Четверг'
    if num == 4:
        return 'Пятница'
    if num == 5:
        return 'Суббота'
    if num == 6:
        return 'Воскресенье'

    raise ValueError('Неверный день недели')


def day_of_week5(num):
    match num:
        case 0:
            return 'Понедельник'
        case 1:
            return 'Вторник'
        case 2:
            return 'Среда'
        case 3:
            return 'Четверг'
        case 4:
            return 'Пятница'
        case 5:
            return 'Суббота'
        case 6:
            return 'Воскресенье'
        case _:
            raise ValueError('Неверный день недели')

from random import shuffle  # Из библиотеки random извлекаем функцию "перемешать"

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4  # Колода карт (набор номиналов карт)
total, current = 0, 0
dealer_total, dealer_current = 0, 0


x1, x2 = 10,10

shuffle(deck)  # Перемешиваем колоду
current = deck.pop()  # Взять и удалить последний элемент из колоды
total = current  # Количество очков игрока становится равно номиналу вытащенной колоды
dealer_current = deck.pop()  # Берётся и удаляется последний элемент из колоды
dealer_total = dealer_current  # Количество очков крупье становится равно номиналу вытащенной колоды
print(f'У вас {total} очков, у дилера {dealer_total} очков.')


def victory():
    global total
    print(f'Вы выиграли, набрав {total} очков.')
    if total == 21:
        print('Twenty One! <блекджек>')
    elif total == dealer_total:
        print('Push! <ничья>')
    else:
        print('Dealer busts! <победа>')


# Вывод поражения
def lose():
    global total
    if total > 21:
        print('You busted! <перебор>')
    else:
        print('Дилер выиграл.')
    print('Better luck next time! <вы проиграли>')


while True:  # Бесконечный цикл
    if input('Enter Y to take card, N to pass: >') == 'Y' or 'y':
        current = deck.pop()  # Взять и удалить последний элемент из колоды
        print(f'Вам попалась карта достоинством {current}.')
        total += current  # К очкам прибавить номинал вытащенной карты.
        print(f'У вас {total} очков.')
        if total > 21:  # Блекджек - игра до 21 очков
            lose()
            break
        elif total == 21:  # 21!
            victory()
            break
        else:
            pass
    else:
        print(f'У вас {total} очков.')
        while True:  # Добор карт у дилера
            if dealer_total >= 17:  # Dealer draws to 16, stands on 17
                if total <= dealer_total <= 21:
                    lose()
                    print(f'У вас {total} очков.')
                else:
                    victory()
                break
            else:
                if dealer_total < 17:  # Блок добора карт у дилера
                    dealer_current = deck.pop()  # Крупье берёт случайную карту из колоды
                    dealer_total += dealer_current  # К сумме номиналов добавляется номинал карты
                    print(f'Дилер берёт карту, ему выпадает {dealer_current}, у дилера {dealer_total}.')

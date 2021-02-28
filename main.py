from tkinter import *  # Модуль GUI
from PIL import ImageTk  # Модуль для связи GUI и изображений
from PIL import Image as Img  # Модуль для  изображений
from random import shuffle  # Модуль рандом


class Main:
    # Инициализация класса.
    def __init__(self):
        self.ma1n = Tk()
        self.ma1n.title('Black Jack [21]')
        self.ma1n.iconbitmap('favicon.ico')
        self.ma1n.geometry('258x421')
        self.ma1n.resizable(False, False)
        self.ma1n.attributes('-topmost', True)
        self.flag = False
        self.cards = []
        self.load_images(self.cards)
        self.deck = list(self.cards)
        shuffle(self.deck)
        self.dealer_hand = []
        self.player_hand = []

        self.background_image = ImageTk.PhotoImage(Img.open('Background.png'))
        self.deal_image = ImageTk.PhotoImage(Img.open('Deal.png'))
        self.hit_image = ImageTk.PhotoImage(Img.open('Hit.png'))
        self.stand_image = ImageTk.PhotoImage(Img.open('Stand.png'))
        self.background_label = Label(self.ma1n, image=self.background_image)
        self.status_label = Label(self.ma1n)
        self.dealer_score_label = IntVar()
        self.dealer_label = Label(self.ma1n, textvariable=self.dealer_score_label, bg='#3b3a38', fg='#FFFFFF')
        self.dealer_card_frame = Frame(self.ma1n, bg='#FFFFFF')
        self.player_score_label = IntVar()
        self.player_label = Label(self.ma1n, textvariable=self.player_score_label, bg='#3b3a38', fg='#FFFFFF')
        self.player_card_frame = Frame(self.ma1n, bg='#FFFFFF')
        self.button_deal = Button(self.ma1n, image=self.deal_image, relief=FLAT, border='0', command=self.deal)
        self.button_hit = Button(self.ma1n, image=self.hit_image, relief=FLAT, border='0', command=self.hit)
        self.button_stand = Button(self.ma1n, image=self.stand_image, relief=FLAT, border='0', command=self.stand)

        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.dealer_label.place(x=115, y=88, width=30, height=12)
        self.dealer_card_frame.place(x=73, y=121)
        self.player_label.place(x=115, y=224, width=30, height=12)
        self.player_card_frame.place(x=73, y=255)
        self.button_deal.place(x=90, y=309)

        self.ma1n.mainloop()

    # Загрузка фотографий.
    @staticmethod
    def load_images(card_images):
        suits = ['heart', 'club', 'diamond', 'spade']
        face_cards = ['J', 'Q', 'K']

        for i in suits:
            for j in range(1, 11):
                card_images.append((j, ImageTk.PhotoImage(Img.open(f'cards/{str(j)}_{i}.png'))))
            for card in face_cards:
                card_images.append((10, ImageTk.PhotoImage(Img.open(f'cards/{str(card)}_{i}.png'))))

    # Вывод фотографий в игре.
    def deal_card(self, frame):
        next_card = self.deck.pop(0)
        self.deck.append(next_card)
        Label(frame, image=next_card[1], relief='flat', bg='#FFFFFF').pack(side='left')
        return next_card

    # Подсчёт тузов в 'руке'.
    @staticmethod
    def score_hand(hand):
        score = 0
        ace = False
        for next_card in hand:
            card_value = next_card[0]
            if card_value == 1 and not ace:
                ace = True
                card_value = 11
            score += card_value
            if score > 21 and ace:
                score -= 10
                ace = False
        return score

    # Начало игры.
    def deal(self):
        self.status_label.place_forget()
        self.button_hit.place(x=26, y=309)
        self.button_stand.place(x=155, y=309)
        self.button_deal.place_forget()
        self.dealer_card_frame.destroy()
        self.dealer_card_frame = Frame(self.ma1n, bg='#FFFFFF')
        self.dealer_card_frame.place(x=73, y=121)
        self.player_card_frame.destroy()
        self.player_card_frame = Frame(self.ma1n, bg='#FFFFFF')
        self.player_card_frame.place(x=73, y=255)
        self.status_label['text'] = ''
        self.dealer_hand = []
        self.player_hand = []
        self.player_hand.append(self.deal_card(self.player_card_frame))
        player_score = self.score_hand(self.player_hand)
        self.player_score_label.set(player_score)
        if player_score > 21:
            self.status_label.place(x=0, y=400)
            self.status_label['text'] = 'Перебор'
        self.dealer_hand.append(self.deal_card(self.dealer_card_frame))
        self.dealer_score_label.set(self.score_hand(self.dealer_hand))
        self.player_hand.append(self.deal_card(self.player_card_frame))
        player_score = self.score_hand(self.player_hand)
        self.player_score_label.set(player_score)
        if player_score > 21:
            self.status_label.place(x=0, y=400)
            self.status_label['text'] = 'Перебор'
        if player_score == 21:
            self.stand()

    # Кнопка 'Взять'.
    def hit(self):
        self.player_hand.append(self.deal_card(self.player_card_frame))
        player_score = self.score_hand(self.player_hand)
        self.player_score_label.set(player_score)
        if player_score > 21:
            self.status_label.place(x=0, y=400)
            self.status_label['text'] = 'Перебор'
            self.button_hit.place_forget()
            self.button_stand.place_forget()
            self.button_deal.place(x=90, y=309)
        if player_score == 21:
            self.stand()

    # Кнопка 'Пас'.
    def stand(self):
        dealer_score = self.score_hand(self.dealer_hand)
        while 0 < dealer_score < 17:
            self.dealer_hand.append(self.deal_card(self.dealer_card_frame))
            dealer_score = self.score_hand(self.dealer_hand)
            self.dealer_score_label.set(dealer_score)
        player_score = self.score_hand(self.player_hand)
        if player_score > 21:
            self.status_label.place(x=0, y=400)
            self.status_label['text'] = 'Перебор'
        elif dealer_score > 21 or dealer_score < player_score:
            self.status_label.place(x=0, y=400)
            if player_score == 21:
                self.status_label['text'] = 'У вас 21!'
            else:
                self.status_label['text'] = 'Вы выиграли!'
        elif dealer_score > player_score:
            self.status_label.place(x=0, y=400)
            self.status_label['text'] = 'Вы проиграли'
        else:
            self.status_label.place(x=0, y=400)
            self.status_label['text'] = 'Ничья'
        self.button_hit.place_forget()
        self.button_stand.place_forget()
        self.button_deal.place(x=90, y=309)


# Старт игры.
if __name__ == '__main__':
    _new_window = Main()

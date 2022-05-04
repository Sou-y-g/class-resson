# カードのクラス定義


class Card:

    marks = ["spades","hearts","diamonds","clubs"]
    numbers = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

    def __init__(self,n,m):
        self.number = n
        self.mark = m

    def __it__(self, c):
        if self.number < c.number:
            return True
        
        if self.number == c.nuber:
            if self.mark < c.number:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, c):
        if self.number > c.number:
            return True
        
        if self.number == c.nuber:
            if self.mark > c.number:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
         n = self.numbers[self.number] + " of " + self.marks[self.mark]
         return n

from random import shuffle

class Deck:
     
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append((i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self,name):
        self.wins = 0
        self.name = name
        self.card = None

class Game:
    def __init__(self):
        name1 = input("プレイヤー1の名前を入力してください。")
        name2 = input("プレイヤー2の名前を入力してください。")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        print(f"このラウンドは{winner}が勝ちました")

    def draw(self,p1n,p1c,p2n,p2c):
        print(f"{p1n}は{p1c}を引きました、{p2n}は{p2c}を引きました")
        
    def player_game(self):
        cards = self.deck.cards
        print("ゲームを始めます")
        while len(cards) >= 2:
            m = input("ゲームを終了しますか？q:終了")
            if m == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name

            self.draw(p1n,p1c,p2n,p2c)

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print(f"ゲーム終了、このゲームは{win}の勝利です。")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "引き分け"

game = Game()
game.player_game()
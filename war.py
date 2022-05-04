# カードのクラス定義

from telnetlib import XASCII


class Card():

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
        self.cards_list = []
        for i in range(2,15):
            for j in range(4):
                self.cards_list.append((i,j))
                shuffle(self.cards_list)

    def rm_card(self):
        if len(self.cards_list) == 0:
            return
        return self.cards_list.pop()

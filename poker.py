#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# Basic card and deck classes
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['hearts', 'diamonds', 'clubs', 'spades']
                      for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

# Poker functions
def poker_hand(player_hand, community_cards):
    return player_hand + community_cards

def print_table(player_hand, ai_hand, community_cards, hide_ai_cards=True):
    if hide_ai_cards:
        print(f"ai hand: [{'X' for _ in ai_hand]}")
    else:
        print(f"ai hand: {ai_hand}")
    print(f"your hand: {player_hand}")
    print(f"community cards: {community_cards}")

# Game loop
while True:
    # Setup
    d = Deck()
    d.shuffle()

    player_hand = [d.deal(), d.deal()]
    ai_hand = [d.deal(), d.deal()]
    community_cards = []

    # Pre-flop
    print_table(player_hand, ai_hand, community_cards)
    input("press enter to deal the flop...")

    # Flop
    for _ in range(3):
        community_cards.append(d.deal())
    print_table(player_hand, ai_hand, community_cards)
    input("press enter to deal the turn...")

    # Turn
    community_cards.append(d.deal())
    print_table(player_hand, ai_hand, community_cards)
    input("press enter to deal the river...")

    # River
    community_cards.append(d.deal())
    print_table(player_hand, ai_hand, community_cards)
    print("hand complete!")

    # Reveal AI cards
    print_table(player_hand, ai_hand, community_cards, hide_ai_cards=False)

    play_again = input("play again? (y/n): ").lower()
    if play_again != 'y':
        break


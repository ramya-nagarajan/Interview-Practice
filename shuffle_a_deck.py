#shuffle a deck of cards - CTCI
import random

def shuffle_a_deck(cards):
	print "Shuffling..."
	temp = 0
	index = 0
	for i in range(0,len(cards)):
		index = int(random.uniform(1,10) % (len(cards)-i)+i)
		print index
		temp =cards[i]
		cards[i] = cards[index]
		cards[index] = temp
	return cards

def main():
	deck =[]
	
	for i in range(1,53):
		deck.append(i)
	print deck
	deck = shuffle_a_deck(deck)
	print deck
main()
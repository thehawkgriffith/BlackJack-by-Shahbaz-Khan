from random import shuffle

print("Welcome to the game of BlackJack by Shahbaz Khan!")

class Hand():

	def __init__(self):

		self.cards_in_hand = []

	def addCard(self, card):

		self.cards_in_hand.append(card)


class Deck():
    
    def __init__(self):
    
    	self.cards = ['A', 'J', 'K', 'Q', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A', 'J', 'K', 'Q', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A', 'J', 'K', 'Q', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A', 'J', 'K', 'Q', 10, 9, 8, 7, 6, 5, 4, 3, 2]

    def shuffle(self):

    	shuffle(self.cards)


class Account():

    def __init__(self, name):
    	
    	self.balance = 30000
    	self.name = name
    	self.bet = 0

    def displayBalance(self):
        
        print(f'Hey {self.name}, your remaining balance is $' + self.balance)

    def betAmount(self, bet):

        self.bet = int(bet) + self.bet
    
        if (self.bet > self.balance):
    
        	for check in range(15):
    
        		print(f'Sorry, that bet exceeds your current balance which is ${self.balance}, try again.')
        		print('Enter an acceptable bet amount: ')
        		self.bet = int(input())
    
        		if (self.bet > self.balance):
    
        			break
    
        		else:
    
        			print('Sorry, try again.')
        			continue


class Players(Hand, Account):

	def __init__(self, name):
	
		self.name = name
		Hand.__init__(self)
		Account.__init__(self,self.name)
		self.score = 0

	def scoreCheck(self):

		self.score = 0
	
		for i in range(0, len(self.cards_in_hand)):
	
			if self.cards_in_hand[i] == 10:
	
				self.score = self.score + 10 
	
			elif self.cards_in_hand[i] == 9:
	
				self.score = self.score + 9
	
			elif self.cards_in_hand[i] == 8:
	
				self.score = self.score + 8
	
			elif self.cards_in_hand[i] == 7:
	
				self.score = self.score + 7
	
			elif self.cards_in_hand[i] == 6:
	
				self.score = self.score + 6
	
			elif self.cards_in_hand[i] == 5:
	
				self.score = self.score + 5
	
			elif self.cards_in_hand[i] == 4:
	
				self.score = self.score + 4
	
			elif self.cards_in_hand[i] == 3:
	
				self.score = self.score + 3
	
			elif self.cards_in_hand[i] == 2:
	
				self.score = self.score + 2
	
			elif self.cards_in_hand[i] == 'K':
	
				self.score = self.score + 10
	
			elif self.cards_in_hand[i] == 'Q':
	
				self.score = self.score + 10
	
			elif self.cards_in_hand[i] == 'J':
	
				self.score = self.score + 10
	
			elif self.cards_in_hand[i] == 'A':
	
				if self.score + 11 <= 21:

					self.score = self.score + 11

				else:

					self.score = self.score + 1
	
		return self.score

	def victory(self):

		self.balance = self.balance + self.bet
		print(f'Congratulations {self.name}! You have won ${self.bet}, your new balance is ${self.balance}.')

	def loss(self):

		self.balance = self.balance - self.bet
		print(f'Uh-oh! {self.name}, you have lost ${self.bet}, your new balance is ${self.balance}.')


	def showHand(self):

		print(f'Current cards with {self.name} are: \n\n')
	
		for card in self.cards_in_hand:
	
			print('\n' + str(card) + '\t')

	def showHandComputer(self):

		print('Current cards with Computer are: \n\n')
		print(str(self.cards_in_hand[0]) + '\t' + '[]')

	def checkEligibilityPlayer(self):

		self.scoreCheck()
	
		if self.score > 21:

			computer.showHand()
			contestant.showHand()
			print('YOU BUST!')
			contestant.loss()
			print('Want to play another hand? Y/N')
			choice = input()
	
			if choice == 'Y':
	
				reset()
				main()
	
			else:
	
				exit()

	def checkEligibilityComputer(self):

		self.scoreCheck()
	
		if self.score > 21:

			computer.showHand()
			contestant.showHand()
			print('YOU WIN!')
			contestant.victory()
			print('Want to play another hand? Y/N')
			choice = input()
	
			if choice == 'Y':
	
				reset()
				main()
	
			else:
	
				exit()
		

def victoryCheck():

	if ((21 - computer.scoreCheck()) < (21- contestant.scoreCheck())):
	
		computer.showHand()
		contestant.showHand()	
		print("Computer won this round!")
		contestant.loss()
	
	elif ((21 - computer.scoreCheck()) == (21 - contestant.scoreCheck())):
	
		print("No one won this round!")
		computer.showHand()
		contestant.showHand()
	
	else:
	
		print('Congratulations on winning this round.')
		computer.showHand()
		contestant.showHand()
		contestant.victory()
	   

def reset():

	computer.score = 0
	contestant.score = 0
	computer.cards_in_hand = []
	contestant.cards_in_hand = []
	playdeck.cards = ['A', 'J', 'K', 'Q', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A', 'J', 'K', 'Q', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A', 'J', 'K', 'Q', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A', 'J', 'K', 'Q', 10, 9, 8, 7, 6, 5, 4, 3, 2]
	contestant.bet = 0	


playdeck = Deck()
print("Please enter your name: ")
name = input()
contestant = Players(name)
computer = Players('Computer')
print("Let's Play!")


def main():
    
    playdeck.shuffle()
    card = playdeck.cards[0]
    computer.addCard(card)
    playdeck.cards.pop(0)
    card = playdeck.cards[0]
    computer.addCard(card)
    playdeck.cards.pop(0)
    computer.showHandComputer()
    card = playdeck.cards[0]
    contestant.addCard(card)
    playdeck.cards.pop(0)
    card = playdeck.cards[0]
    contestant.addCard(card)
    playdeck.cards.pop(0)
    contestant.showHand()
    print("Would you like to Hit or Stay? H/S")
    choice = input()
    
    while choice == 'H':
    
    	print('Please place your bet: ')
    	bet = input()
    	contestant.betAmount(bet)
    	card = playdeck.cards[0]
    	contestant.addCard(card)
    	playdeck.cards.pop(0)
    	contestant.showHand()
    	contestant.checkEligibilityPlayer()
    	print("Would you like to Hit or Stay? H/S")
    	choice = input()
    
    for play2 in range(10):
    
    	computer.showHand()
    	computer.checkEligibilityComputer()
    	
    	if computer.scoreCheck() >= 17:
    	
    		break
    	
    	else:

    		card = playdeck.cards[0]
    		computer.addCard(card)
    		playdeck.cards.pop(0)
    		computer.checkEligibilityComputer()

    victoryCheck()
    print('Would you like to play another hand? Y/N')
    choice2 = input()

    if choice2 == 'Y':

    	reset()
    	main()

    else:

    	exit()


if __name__ == '__main__':
	main()    		





import random
from project import solve
friends, transactions = [], []
def get_response(user_input: str):
	if user_input[0] == '!':
		user_input = user_input[1:]
		lowered: str = user_input.lower()
		if lowered == '':
			return 'Well, you\'all aren\'t spending enough?'
		elif lowered[0] + lowered[1] + lowered[2] == 'add':
			lowered = lowered[4:]
			if lowered not in friends:
				friends.append(lowered)
				return f'Welcome to the trip {lowered}!'
			else:
				return f'{lowered} is already added.'
		elif lowered == 'list':
			return ', '.join(friends)
		elif lowered[0] + lowered[1] + lowered[2] + lowered[3] == 'paid':
			lowered = lowered[5:]
			l = lowered.split(",")
			ow = l.pop(0)
			m = l.pop()
			x = len(l)
			if ow not in friends:
				return f'{ow} is not added in the trip'
			if l[-1] == 'everyone':
				for i in range(len(friends)):
					if friends[i] != ow:
						transactions.append([ow, friends[i], int(m) / len(friends)])
				return 'Transactions noted!'
			else:
				for i in range(x):
					if l[i] in friends:
						transactions.append([ow, l[i], int(m) / x])
					else:
						return f'{l[i]} is not added in the trip'
				return 'Transactions noted!'
		elif lowered == 'balance':
			return solve(friends, transactions)

		elif 'hello tripbot' in lowered:
			return 'Hello there'
		elif lowered == 'help':
			l = ['I\'m made for minimizing the number of transactions that happens during a trip',
				 'Here\'s how to use me:',
				 'Before a trip, add all the members that are joining by: !add yourname',
				 'To record a transaction, type: !paid name_of_payer,reciever_1,reciever_2,amount (Comma seperated without spaces, any number of recievers will work)',
				 'In case someone pays for everyone: !paid payer,everyone',
				 'IMPORTANT: MAKE SURE EVERYONE IN THE TRIP IS ADDED BEFORE USING THE \'EVERYONE\' FUNCTION',
				 'If you start all the aforementioned commands with \'?!\' instead of \'!\', I will help with that command in you DM',
				 'I hope I eradicate the hated post-trip-calculation-part of your trips :)'
				 ]
			return '\n'.join(l)
		else:
			return random.choice(['I do not understand....maybe type !help for the manual',
								'What are you talking about, you need help, type !help?',
								'I don\'t understand, type !help for manual',
								'I\'ll only be able to calculate ur transactions bruh :/, type !help to know how to use me:)'])

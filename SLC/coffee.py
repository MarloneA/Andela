""" Instructions for coffee machine
    1. Make and serve me, you and gibbs a cup of coffee (add coffee, add hot water, stir)
    2. Change how the mix is stirred
    3. A better way to make coffee with less repetition
    4. Make you coffee with milk and sugar (add sugar, add milk)
    5. Make Gibbs coffee with milk, sugar and something else (add sugar, add milk, ...)
    6. Refactor
"""

def make_coffee(*options):
	"""
		Makes coffee
		*options: 0 or more arguments
	"""
	ingredients = ['coffee', 'hot water']

	if options:
		options = ', '.join(options)
		ingredients.append(options)
		coffee = 'Tasty coffee with {}'.format(options)
	else:
		coffee = 'Tasty coffee'
	
	print('Started making coffee...')
	print('Getting cup...')
	print('Adding {}'.format(', '.join(ingredients)))
	print('Stir the mix...')
	print('Finished making the coffee...')

	return coffee

def serve_coffee(coffee, person_name):
	"""Serves coffee to a specified person"""
	print("--Here's your {} {}. Enjoy!!--\n".format(coffee, person_name))

#Make my coffee
my_coffee = make_coffee()
serve_coffee(my_coffee, 'Evans')

#Make your coffee
your_coffee = make_coffee('Milk', 'Sugar')
serve_coffee(your_coffee, 'You')

#Make Gibbs' coffee
gibbs_coffee = make_coffee('Milk', 'Sugar', 'Cream')
serve_coffee(gibbs_coffee, 'Gibbs')


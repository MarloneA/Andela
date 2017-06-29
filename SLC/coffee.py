""" Instructions for coffee machine
    1. Make and serve me, you and gibbs a cup of coffee (add coffee, add hot water, stir)
    2. Change how the mix is stirred
    3. A better way to make coffee with less repetition
    4. Make you coffee with milk and sugar (add sugar, add milk)
    5. Make Gibbs coffee with milk, sugar and something else (add sugar, add milk, ...)
    6. Refactor
"""

#Make my coffee
ingredients = ['coffee', 'hot water']
print('Started making coffee...')
print('Getting cup...')
print('Adding {}'.format(', '.join(ingredients)))
print('Stir the mix...')
print('Finished making the cofee...')
my_coffee = 'Tasty coffee'
print("--Here's your {} {}. Enjoy!!--\n".format(my_coffee, 'Evans'))

#Make your coffee
ingredients = ['coffee', 'hot water']
print('Started making coffee...')
print('Getting cup...')
print('Adding {}'.format(', '.join(ingredients)))
print('Stir the mix...')
print('Finished making the cofee...')
my_coffee = 'Tasty coffee'
print("--Here's your {} {}. Enjoy!!--\n".format(my_coffee, 'you'))

#Make Gibbs' coffee
ingredients = ['coffee', 'hot water']
print('Started making coffee...')
print('Getting cup...')
print('Adding {}'.format(', '.join(ingredients)))
print('Stir the mix...')
print('Finished making the cofee...')
my_coffee = 'Tasty coffee'
print("--Here's your {} {}. Enjoy!!--\n".format(my_coffee, 'Gibbs'))


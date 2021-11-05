# Create a 2-dimentional List, in which products and price need to be put in

products = []

while True:
	name = input('Please input the name of the product: ')
	if name == 'q':
		break
	price = input('Plase input the price of the product: ')
	products.append([name,price])
print(products)




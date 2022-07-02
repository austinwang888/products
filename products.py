products = []

while True:
	name = input ('請輸入商品名稱:')
	if name == 'q' :
		break
	price = input('請輸入價錢:')
	data = [name,price]
	products.append(data)

print(products)

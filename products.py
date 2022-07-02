products = []

while True:
	name = input ('請輸入商品名稱:')
	if name == 'q' :
		break
	price = input('請輸入價錢:')
	data = [name,price]
	products.append(data)
	
for p in products:
	print (p[0], p[1])

with open('list.txt','w') as f :
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
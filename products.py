import os #operating system
products = []

if os.path.isfile('list.csv'):
	print('yeah,找到檔案')
	with open('list.csv','r',encoding = 'utf-8') as f :
		for line in f:
			if '產品,價錢' in line:
					continue
			name,price = line.strip().split(',')
			products.append([name,price])
	print(products)
else:
	print('找不到檔案...')
	
#讓使用者輸入
while True:
	name = input ('請輸入商品名稱:')
	if name == 'q' :
		break
	price = input('請輸入價錢:')
	data = [name,price]
	products.append(data)
	
for p in products:
	print (p[0], p[1])

#寫入檔案

with open('list.csv','w',encoding = 'utf-8') as f :
	f.write('產品,價錢\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
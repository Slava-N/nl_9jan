with open('recipe.txt', encoding='utf-8') as document:
    menu={}
    for line in document:
        dish = line.strip()
        number_of_products = int(document.readline().strip())
        product_items = []
        for product in range(number_of_products):
            raw_line = document.readline().strip().split(' | ')
            product_info = {'product' : raw_line[0], 'quantity' : raw_line[1], 'unit' : raw_line[2]}
            product_items.append(product_info)
        empty_line = document.readline().strip()
        menu[dish] = product_items
    for dish in menu:
        print(dish, menu[dish], sep='\n')

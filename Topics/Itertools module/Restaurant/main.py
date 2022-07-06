import itertools

for main, dessert, drink in itertools.product(zip(main_courses, price_main_courses), zip(desserts, price_desserts),
                                              zip(drinks, price_drinks)):
    total = main[1] + dessert[1] + drink[1]
    if total <= 30:
        print(main[0], dessert[0], drink[0], total)

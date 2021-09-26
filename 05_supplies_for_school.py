peaces_of_pen_packages = int(input('Type how many pen packs will be needed: '))
peaces_of_marker_packages = int(input('Type how many marker packs will be needed: '))
liters_of_detergent = int(input('Type how many pen packs will be needed: '))
discount = int(input('Type what will be the discount:'))

price_per_pen_pack = 5.80
price_per_marker_pack = 7.20
price_per_liter_detergent = 1.20

total_money_neaded_for_purchase = peaces_of_pen_packages * price_per_pen_pack + peaces_of_marker_packages * \
                                  price_per_marker_pack + liters_of_detergent * price_per_liter_detergent
final_total_price = total_money_neaded_for_purchase - total_money_neaded_for_purchase * discount / 100

print(final_total_price)
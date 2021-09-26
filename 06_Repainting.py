nylon_sqare_meters_needed = int(input('How many sqare meters of nylon do you need: '))
liters_of_paint_needed = int(input('How many liters of paint do you need: '))
liters_of_thinner_needed = int(input('How many liters of thinner do you need: '))
hours_of_work = int(input('How many hours will take to do it: '))

price_per_nylon_square_meter = 1.5
price_per_liter_of_paint = 14.5
price_per_liter_of_tinner = 5
price_for_bags = 0.4

total_price_for_nylon = (nylon_sqare_meters_needed + 2) * price_per_nylon_square_meter
total_price_for_paint = (liters_of_paint_needed + liters_of_paint_needed * 0.1) * price_per_liter_of_paint
total_price_for_thinner = liters_of_thinner_needed * price_per_liter_of_tinner
total_price_of_materials = total_price_for_thinner + total_price_for_nylon + total_price_for_paint + price_for_bags

price_for_work = (total_price_of_materials * 0.3) * hours_of_work

total_sum = total_price_of_materials + price_for_work


print(f'Summary of your order is: {total_sum} lv')
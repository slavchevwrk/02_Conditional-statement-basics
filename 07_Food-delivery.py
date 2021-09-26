# Variable input
count_chicken_meals = int(input('How many chicken meals do you need: '))
count_fish_meals = int(input('How many fish meals do you need: '))
count_vegie_meals = int(input('How many vegetarian meals do you need: '))

# Statics
price_per_chicken_meal = 10.35
price_per_fish_meal = 12.4
price_per_vegie_meal = 8.15
price_for_shipping = 2.5

#Calculations
total_without_additional_stuff = price_per_chicken_meal * count_chicken_meals + price_per_fish_meal * count_fish_meals \
                                 + price_per_vegie_meal * count_vegie_meals

price_of_desert = total_without_additional_stuff * 0.2

total_sum = total_without_additional_stuff + price_of_desert + price_for_shipping

print(f'Summary of your order is: {total_sum} lv')
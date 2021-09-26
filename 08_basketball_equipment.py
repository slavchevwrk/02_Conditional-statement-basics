# Variable input
training_fee_per_year = int(input('What is the training fee per year: '))

#Calculation of the equipment
price_of_sneakers = training_fee_per_year - training_fee_per_year * 0.4
price_of_clothes = price_of_sneakers - price_of_sneakers * 0.2
price_of_ball = price_of_clothes * (1 / 4)
price_of_accesories = price_of_ball * (1 / 5)

total_sum = price_of_accesories + price_of_ball + price_of_clothes + price_of_sneakers + training_fee_per_year

print(f'Summary of your order is: {total_sum} lv')

# Variable input
lenght = int(input('What is the lenght: '))
width = int(input('What is the width: '))
height = int(input('What is the height: '))
percentage_fill = float(input('What is the percentage of sand: '))

#Calculations

total_volume_of_tank = (lenght * width) * height
total_volume_of_tank_in_liters = total_volume_of_tank * 0.001
percentage_fill /= 100
liters_of_water = total_volume_of_tank_in_liters - total_volume_of_tank_in_liters * percentage_fill

print(f'Liters needed: {liters_of_water} liters')

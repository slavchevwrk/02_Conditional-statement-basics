from math import floor

pages_count = int(input())
pages_per_hour_rate = int(input())
days_left_for_reading = int(input())

total_time_to_read_the_book = floor(pages_count / pages_per_hour_rate)
total_hours_per_day_to_read = floor(total_time_to_read_the_book / days_left_for_reading)
print(total_hours_per_day_to_read)
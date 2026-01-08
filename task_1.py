time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0

time_values = time_string.split(',')

for time_value in time_values:
    for time_part in time_value.split():
        if 'h' in time_part:
            hours = int(time_part.replace('h', ''))
            total_minutes += hours * 60

        elif 'm' in time_part:
            minutes = int(time_part.replace('m', ''))
            total_minutes += minutes    

        elif 's' in time_part:
            seconds = int(time_part.replace('s', ''))
            total_minutes += seconds // 60


print(f'Общее количество минут: {total_minutes}.')

# Nicole Slanina 2332374

# 1: toCelsius(fahrenheit) -> celsius
def toCelsius(f: str) -> float:
    return round((float(f) - 32) * (5 / 9), 2)

# 3: avgTempYear(d, year) -> year avg
def avgTempYear(d, year):
    try:
        sum_temp = 0
        avg = d[year]
        for temperature in avg:
            sum_temp += temperature
        return round(sum_temp / len(avg), 2)
    except KeyError:
        print('Sorry, this year was not found in the dictionary. Enter a valid year.')

# 4: topThreeYears(d) -> top 3 
def topThreeYears(d):
    avg_set = set()
    top_3 = []
    for year in d:
        avg_set.add(avgTempYear(d, year))
    for _ in range(3):
        top = max(avg_set)
        top_3.append(top)
        avg_set.remove(top)
    return top_3

# 5: avgTempMonth(d, month) -> month avg
def avgTempMonth(d, month):
    month_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
                  'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    
    if month not in month_dict:
        print('Invalid month. Please enter a valid one (ex: JAN, FEB...).')
        return
    
    m = month_dict[month] - 1  # index
    total = 0
    for year in d:
        total += d[year][m]
    return round(total / len(d), 2)

'''
MAIN
input_file = open('data.txt', 'r')
temp_dict = {}

# Ignore first 4 lines
read = input_file.readlines()[4:]
for line in read:
    line = line.split()
    year = int(line[0])
    temps = list(map(toCelsius, line[1:])) 
    temp_dict[year] = temps

input_file.close()


Tests 
print(temp_dict)
print(avgTempYear(temp_dict, 1964))
print(topThreeYears(temp_dict))
print(avgTempMonth(temp_dict, 'JAN'))
'''
# Part 2

# 6: belowFreezing(d) -> returns months below freezing
def belowFreezing(d):
    freezing_months = set()
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

    for year in d:
        for i in range(12):
            if d[year][i] < 0:
                freezing_months.add(months[i])

    return list(freezing_months)

# MAIN
input_file = open('data.txt', 'r')
lines = input_file.readlines()
input_file.close()

header = lines[:4]
data_lines = lines[4:]
temp_dict = {}

for line in data_lines:
    parts = line.strip().split()
    year = int(parts[0])
    celsius_values = list(map(toCelsius, parts[1:]))
    temp_dict[year] = celsius_values

# new file
output_file = open("data_celsius.txt", "w")

# header
for line in header:
    output_file.write(line)

# converted data
for year in temp_dict:
    output_file.write(str(year))
    for temp in temp_dict[year]:
        output_file.write(f"\t{temp}")
    output_file.write("\n")

output_file.close()

# testing
print('Months with at least one temperature sub 0°C :', belowFreezing(temp_dict))
# Nicole Slanina 2332374

# 1: toCelsius fahrenheit -> celsius
def toCelsius(f:str) -> float:
    return round((float(f) - 32)* (5/9), 2) #rounding to 2nd decimal

# 2: open for r, create dictionary of lists
'''
input_file = open('data.txt', 'r')
temp_dict = {}

read = input_file.readlines()[4:]
for line in read:
    line = line.split()
    temp_dict[int(line[0])] = list(map(toCelsius, line[1:]))
'''
# print(temp_dict)

# 3: avgTempYear(d, year), returns avg temp of year

def avgTempYear(d, year):
    try:
        sum_temp = 0
        avg = d[year]
        for temperature in avg:
            sum_temp += temperature
        return round(sum_temp/len(avg), 2)
    except KeyError:
        print('Sorry this year was not found in the dictionary. Enter a valid year')



# 4: topThreeYears(d) returns list, 3 biggest avg

def topThreeYears(d):
    avg_set = set()
    top_3 = []
    for year in d:
        avg_set.add(avgTempYear(d, year))
    for _ in range(3):
        top_3.append(avg_set.remove(max(avg_set)))

# 5: avgTempMonth(d, month), returns avg temp

def avgTempMonth(d, month):
    month_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP':9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    m = month_dict[month]
    total = 0
    for year in d:
        total += d[year][m -1]
    return round(total/len(d), 2)



# main

input_file = open('data.txt', 'r')
temp_dict = {}

read = input_file.readlines()[4:]
for line in read:
    line = line.split()
    temp_dict[int(line[0])] = list(map(toCelsius, line[1:]))

print(temp_dict)
print(avgTempYear(temp_dict, 1964))
print(topThreeYears(temp_dict))
print(avgTempMonth(temp_dict, 'JAN'))
input_file.close()
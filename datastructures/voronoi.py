
def average(x:int, y:int) -> float:
    return (x+y) / 2

num_villages = int(input("Enter the number of villages: "))

village_locations = []
for num in range(num_villages):
    village_locations.append(int(input(f"Enter village #{num+1}'s location: ")))
village_locations.sort()

neighbourhoods = []
for i in range(1, num_villages - 1):
    neighbourhood_leftmost = average(village_locations[i-1], village_locations[i])
    neighbourhood_rightmost = average(village_locations[i], village_locations[i+1])
    neighbourhoods.append(neighbourhood_rightmost - neighbourhood_leftmost)

print(min(neighbourhoods))
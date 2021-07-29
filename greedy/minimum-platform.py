# arrival time of the trains
arr = [900,940,950,1100,1500,1800]

#departure time of the trains
dep = [910,1200,1120,1130,1900,2000]

j = 0
i = 1

max_platforms = needed = 1

while i<len(arr) and j<len(dep):

	if dep[j]<arr[i]:
		j+=1
		max_platforms-=1

	else:
		i+=1
		max_platforms+=1

	if needed<max_platforms:
		needed = max_platforms

print(needed)
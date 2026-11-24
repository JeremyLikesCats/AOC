# AOC Init
import os

# Create folders in the CWD
# by year (input)
year = input("Which year? ")
year_path = f"AOC_{year}"
if os.path.isdir(year_path):
	check = input(f"This will overwrite {year_path}!? (y/n) ")
	if check != "y":
		print("Stopping!")
		exit()
else:
	os.mkdir(year_path)

# inside Days 1-12 (input)
num_days = int(input("How many days? "))
for day in range(num_days):
	path = f"{year_path}/day_{day+1:0>2}"
	if not os.path.isdir(path):
		os.mkdir(path)
	# inside main.py, data.txt
	# init main.py with starter code
	with open(f"{path}/main.py", mode='w') as main:
		main.write(f"# AOC {year} Day {day+1:0>2}\n")
		# copy from template.py
		with open("template.py") as template:
			for line in template:
				main.write(line)

	with open(f"{path}/data.txt", mode='w') as data:
		pass




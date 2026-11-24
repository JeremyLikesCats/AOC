# AOC 2019 Day 23
# DESCRIPTION:

out_1 = 0
out_2 = 0
test_out = 0

test_mode = False
test_data = 0

# load data.txt and go through line by line
with open("data.txt") as data_file:
	for line_i, line in enumerate(data_file):
		line = line.strip("\n")
		
		# Pt. 1
		if test_mode:
			test_out += 0
		else:
			out_1 += 0
		
		# Pt. 2
		if test_mode:
			test_out += 0
		else:
			out_2 += 0

		if test_mode:
			break

if test_mode:
	print(f"test: {test_out}")
else:
	print(f"pt 1: {out_1}")
	print(f"pt 2: {out_2}")

import re
import copy

all_inputs = []
single_input = input()

while(single_input != "break"):
	all_inputs.append(single_input)
	single_input = input()


# with open("wow.txt", "w") as f:
# 	for line in x:
# 		f.write(line)
# 		f.write("\n")

regex_dict = {}
for line in all_inputs:
	file_name = re.search("[A-Za-z]+.java", line)
	if file_name != None:
		file_name = file_name.group()
		char_at = re.findall(":([0-9]+)", line)
		char_at = [int(x) for x in char_at]
		issue = None
		if re.search("is not preceded with whitespace", line) != None:
			if re.search("typecast", line) == None:
				issue = "no preceding whitespace"
				adjust_value = len(re.search("'([^']+)'", line).group(1))
			else:
				issue = "no following whitespace"
				adjust_value = 1
		elif re.search("is not followed by whitespace", line) != None:
			if re.search("typecast", line) == None:
				issue = "no following whitespace"
				adjust_value = len(re.search("'([^']+)'", line).group(1))
			else:
				issue = "no following whitespace"
				adjust_value = 1
		elif re.search("Line has trailing spaces", line) != None:
			char_at.append(1000)
			issue = "has trailing whitespace"
			adjust_value = 0
		if issue != None:
			if file_name not in regex_dict.keys():
				regex_dict[file_name] = [(char_at,issue,adjust_value)]
			else:
				regex_dict[file_name].append((char_at,issue,adjust_value))

count = 1
for file_name in regex_dict.keys():
	with open(file_name, "r") as f:
		file_list = f.readlines()
	issue_list = sorted(regex_dict[file_name], key=lambda x: x[1], reverse = True)
	issue_list = sorted(issue_list, key=lambda x: x[0])
	current_line = [0,0]
	for issue in issue_list:
		print(f"issue {count}: {issue}")
		if issue[0][0] != current_line[0]:
			current_line[0] = issue[0][0]
			current_line[1] = 0
		if issue[1] == "no preceding whitespace":
			if file_list[issue[0][0]-1][issue[0][1] + current_line[1] - 2] != " ":
				file_list[issue[0][0]-1] = file_list[issue[0][0]-1][:issue[0][1] + current_line[1] - 1] + " " + file_list[issue[0][0]-1][issue[0][1] + current_line[1] - 1:]
				current_line[1] += 1
		elif issue[1] == "no following whitespace":
			if file_list[issue[0][0]-1][issue[0][1] + issue[2] - 1 + current_line[1]] != " ":
				file_list[issue[0][0]-1] = file_list[issue[0][0] - 1][:issue[0][1] + issue[2] + current_line[1] - 1] + " " + file_list[issue[0][0] - 1][issue[0][1] + issue[2] + current_line[1] - 1:]
				current_line[1] += 1
		elif issue[1] == "has trailing whitespace":
			i = 2
			while(file_list[issue[0][0]-1][-(i+1)] == " "):
				i+=1
			file_list[issue[0][0]-1] = file_list[issue[0][0]-1][:-i] + "\n"
		print(f'fixed line: "{file_list[issue[0][0]-1]}"')
		count += 1
			
	copy_file_name = file_name[:-5] + "_c.java"
	with open(copy_file_name, "w") as f:
		f.writelines(file_list)
	# with open(file_name, "w") as f:
	# 	f.writelines(file_list)
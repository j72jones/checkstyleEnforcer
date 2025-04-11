import re
file_name = input("Enter File Name: ")
while (file_name != "break"):
	with open(file_name, "r") as f:
		file_text = f.read()

	def fix_no_space_before_brace(txt):
		error_list = re.split("\{",txt)
		fixed = ""
		for segment in error_list[:-1]:
			if (segment[-1] != " "):
				segment = segment + " {"
			else:
				segment = segment + "{"
			fixed = fixed + segment
		fixed = fixed + error_list[-1]
		return(fixed)

	def fix_no_space_before_double_equal(txt):
		error_list = re.split("\=\=",txt)
		fixed = ""
		for segment in error_list[:-1]:
			if (segment[-1] != " "):
				segment = segment + " =="
			else:
				segment = segment + "=="
			fixed = fixed + segment
		fixed = fixed + error_list[-1]
		return(fixed)

	def fix_no_space_after_double_equal(txt):
		error_list = re.split("\=\=",txt)
		fixed = error_list[0]
		for segment in error_list[1:]:
			if (segment[0] != " "):
				segment = "== " + segment
			else:
				segment = "==" + segment
			fixed = fixed + segment
		return(fixed)

	def fix_no_space_before_or(txt):
		error_list = re.split("\|\|",txt)
		fixed = ""
		for segment in error_list[:-1]:
			if (segment[-1] != " "):
				segment = segment + " ||"
			else:
				segment = segment + "||"
			fixed = fixed + segment
		fixed = fixed + error_list[-1]
		return(fixed)

	def fix_no_space_after_or(txt):
		error_list = re.split("\|\|",txt)
		fixed = error_list[0]
		for segment in error_list[1:]:
			if (segment[0] != " "):
				segment = "|| " + segment
			else:
				segment = "||" + segment
			fixed = fixed + segment
		return(fixed)

	def fix_no_space_before_and(txt):
		error_list = re.split("\&\&",txt)
		fixed = ""
		for segment in error_list[:-1]:
			if (segment[-1] != " "):
				segment = segment + " &&"
			else:
				segment = segment + "&&"
			fixed = fixed + segment
		fixed = fixed + error_list[-1]
		return(fixed)

	def fix_no_space_after_and(txt):
		error_list = re.split("\&\&",txt)
		fixed = error_list[0]
		for segment in error_list[1:]:
			if (segment[0] != " "):
				segment = "&& " + segment
			else:
				segment = "&&" + segment
			fixed = fixed + segment
		return(fixed)

	def fix_no_space_after_for(txt):
		error_list = re.split("for",txt)
		fixed = error_list[0]
		for segment in error_list[1:]:
			if (segment[0] != " "):
				segment = "for " + segment
			else:
				segment = "for" + segment
			fixed = fixed + segment
		return(fixed)

	def fix_no_space_after_if(txt):
		error_list = re.split("if",txt)
		fixed = error_list[0]
		for segment in error_list[1:]:
			if (segment[0] != " "):
				segment = "if " + segment
			else:
				segment = "if" + segment
			fixed = fixed + segment
		return(fixed)

	return_text = fix_no_space_before_brace(fix_no_space_before_double_equal(fix_no_space_after_double_equal(fix_no_space_before_or(fix_no_space_after_or(fix_no_space_before_and(fix_no_space_after_and(fix_no_space_after_for(fix_no_space_after_if(file_text)))))))))

	copy_file_name = file_name[:-5] + "_copy.java"
	with open(copy_file_name, "w") as f:
		f.write(return_text)
	file_name = input("Enter File Name: ")
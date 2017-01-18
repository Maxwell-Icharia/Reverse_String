def reverse_string(string):
	string = str()
	if string == string[::-1]:
		return "true"
	elif string == "":
	  return 'None'
	else:
		return string[::-1]

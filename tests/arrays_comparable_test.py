def test_ok_1():
    string_list = ["banana", "apple", "cherry"]
    sorted_list = sorted(string_list)
    for i in sorted_list:
        print(i)

def test_violation_1():
	mixed_list = [3, "banana", 1, "apple"]

	try:
		# This will raise a TypeError because integers and strings cannot be compared
		sorted_list = sorted(mixed_list)
	except TypeError as e:
		pass
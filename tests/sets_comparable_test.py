def test_ok_1():
    string_set = {"banana", "apple", "cherry"}
    sorted_set = sorted(string_set)
    if sorted_set == ["apple", "banana", "cherry"]:
        print("sorted_set is correct")
    else:
        print("sorted_set is incorrect")

def test_violation_1():
	mixed_set = {3, "banana", 1, "apple"}

	try:
		# This will raise a TypeError because integers and strings cannot be compared
		sorted_set = sorted(mixed_set)
	except TypeError as e:
		pass
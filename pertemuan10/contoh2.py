s1 = "i love u" 
s2 = "i hate u" 
if len(s1) == len(s2): 
	for char1 in s1: 
		for char2 in s2: 
			if char1 == char2: 
				print("common letter") 
				break 

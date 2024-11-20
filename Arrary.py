			###Part1 : integer variable input. 
			###int(intput()) : Need to specify input data as integer to order properly.
			###[... or ...] Boolean Condition : if any condition true, trigger while loop.

df =[]
for n in range(0,5):
	hold = int(input("Please enter number" +str(n) + ": "))
	while(hold in df):
		hold = int(input("Choose a different number" +str(n) + ": "))	
	df.append(hold)		
	
print("\nYou have made this list, :", df)
print("I will order the list into ascending and descending order.")
print("\nWitness my computational capabiliy!( *｀ω´)")

			###Part3 : Prepare placeholder lists
order = [1, 2, 3, 4, 5] 
order2 = [1, 2, 3, 4, 5]


			###Part4 : Order variables using for loop
			###[x], [y] variables are placeholder 'counters'
for numb in df:
	x = 0
	y = 0 
	print("\nComparing ", numb)
	
	for comp in df:
		if(numb > comp):
				print(">>", numb, " is bigger than ", comp)
				x = x + 1
		elif(numb == comp):		
				x = x + 0
				y = y + 0	
		else:
				print(">>", numb, " is smaller than ", comp)
				y = y + 1
							
	print(numb, " is the [", y + 1, "]biggest number")
	print(numb, " is the [", x + 1, "]smallest number")
	order[x] = numb
	order2[y] = numb
	
print("\nThis is ascending order: ", order)
print("This is descending order: ", order2)
print("\nWhat do you think? Amazing wouldn't you agree (（＾ν＾）).")

a, b, c, d = 0, 0, 0, 0
x = input("please Enter Your Password: ")
if  len(x) >= 6 : 
	for i in x: 
		if i.islower(): 
			a+=1			

		elif i.isupper(): 
			b+=1			

		elif i.isdigit(): 
			c+=1			

		elif(i=='@'or i=='$' or i=='_'or i=="!" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")" or i=="-" or i=="+"): 
			d+=1		
if (a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d==len(x)): 
	print(" \n************** Your Password is Strong *****************") 
else: 
	print("\n!!!!!!!!!!!!!!!!! Weak Password !!!!!!!!!!!!!!!!!!!!!!!!!") 

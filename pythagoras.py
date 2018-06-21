from math import sqrt
print('a,b,c are sides and c is hypotenuse')
side= input('which side do you wish to calculate? side>')

if side== 'c':
	side_a= int(input('input lenght of side a. side_a>'))
	side_b= int(input('input lenght of side b. side_b>'))
	side_c= sqrt(side_a * side_a + side_b * side_b)
	print('the lenght of side c is=')
	print(side_c)
elif side== 'a':
	side_c= int(input('input lenght of side c. side_c>'))
	side_b= int(input('input lenght of side b. side_b>'))
	side_a= sqrt(side_c * side_c - side_b * side_b)
	print('the lenght of side a is=')
	print(side_a)

elif side== 'b':
	side_c= int(input('input lenght of side c. side_c>'))
	side_a= int(input('input lenght of side a. side_a>'))
	side_b= sqrt(side_c * side_c - side_a * side_a)
	print('the lenght of side b is=')
	print(side_b)



                

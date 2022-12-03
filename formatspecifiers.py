# format specifiers = {value:flags} format a value based on what flags are inserted

'''
.(number)f = round to that many decimal places (fixed point)
:(number) = allocate that many spaces
:03 allocate and zero pad that many spaces
:< = left justify
:> = right justify
:^ = center align
:+ = use a plus sign to indicate positive value
:= = place sign to leftmost position
: = insert a space between positive numbers 
:, = comma separator'''

price1 = 3.14564
price2 = -987.450
price3 = 1200.54

print(f"price is {price1:.2f}")# displays 2 numbers after decimal point
print(f"price is {price2:10}")# alocated 10blank spaces for the price2
print(f"price {price3:010}")# here alocated blanks are 10 and if the price3 doesnt fill them up then they are 0 padded
print(f"price {price1:<10}")# to left justify a value in the given alocated space   
print(f"price {price2:>10}")# right justify
print(f"price {price3:^10}")#to centre align
print(f"price{price1:+}")# any positive number is preceded with a + sign and any negative with -
print(f"price {price2: }")# here space if there after :,they work the same a + but doesnt display + 
print(f"price {price3:,}")# here , separates each thousands place
print(f"price {price3:,.2f}")# here we mix and matched these specifiers
# in python in for loop if we want to reverse a range we can also use reversed function
# reversed(1,10)

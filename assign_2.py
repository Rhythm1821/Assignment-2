#Ans-1
# True & False

#Ans-2
#The three types of boolean operators are: AND, OR, NOT

#Ans-3
#AND - Means both the conditions should be true
#OR  - Means one of the conditions should be true
#NOT - The condtion will be true only if it is false

#Ans-4
val1 = (5 > 4) and (3 == 5)
print(val1)

val2 = not(5>4)
print(val2)

val3 = (5 > 4) or (3 == 5)
print(val3)

val4 = not ((5 > 4) or (3 == 5))
print(val4)

val5 = (True and True) and (True == False)
print(val5)

val6 = (not False) or (not True)
print(val6)

#Ans-5
# Six comparision operators are: =, <, >, <=, >=, !=

#Ans-6
# Equal to(=) Assign value of right side of expression to left side operand - a = b + c
# += Add right side operand with left side operand and then assign to left operand - a += b 
# -= Subtract right operand from left operand and then assign to left operand: True if both operands are equal - a -= b 
# *= Multiply right operand with left operand and then assign to left operand - a *= b    
# /= Divide left operand with right operand and then assign to left operand - a/=b
# %= Takes modulus using left and right operands and assign result to left operand - a%=b
# //= Divide left operand with right operand and then assign the value(floor) to left operand - a //= b
# **= Calculate exponent(raise power) value using operands and assign value to left operand - a **= b 
# &= Performs Bitwise AND on operands and assign value to left operand - a &= b   
# |= Performs Bitwise OR on operands and assign value to left operand - a |= b   
# ^= Performs Bitwise xOR on operands and assign value to left operand - a ^= b
# >>= Performs Bitwise right shift on operands and assign value to left operand - a >>= b  
# <<= Performs Bitwise left shift on operands and assign value to left operand - a <<= b

#Ans-7
spam = 0
if spam == 10:
    print("eggs")
elif spam == 5:
    print("bacon")
else:
    print("ham")
    print("spam")
    print("spam")

# Ans-8
spam = input("Type here")
if spam == "1":
    print("Hello")
elif spam =="1":
    print("Howdy")
else:
    print("Greetings")

# Ans-9
# Ctrl + C

# Ans-10
# Break stops the function completely
# Continue starts the loop again

# Ans-11
# In a for loop, range(10) is the limit uptill which the loop should run(excluding the number)
#              ,range(0,10)is the limit starting from the first number written(including) and ending with the last(excluding) 
#              ,range(0,10,1) means the loop starting from first number(including) and ending with the last(excluding) moving number of steps further given in the last part

# Ans-12
for i in range(1,11):
     print(i)
     i+=1

i = 1
while i < 11:
    print(i)
    i+=1

# Ans-13
# spam.bacon()
"""Basic - Print all integers from 0 to 150."""
for i in range(1, 151, 1):
    print(i)
# """Multiples of 5"""
for i in range(1, 1001, 1): 
    if i % 5 == 0:
        print(i)

# print(multiples)
"""divisble"""
for i in range(1, 101, 1):
     if(i % 10 == 0):
         print("coding Dojo" + str(i))
     elif(i % 5 == 0):
         print('coding' + str(i))
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for i in range(1,500001,1):
     if(i % 2 != 0):
        sum += i
        print(sum)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range (2018, 0, -4):
    print(i)
    # Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
low_num=2
high_num=9
mult=3
for i in range (low_num,high_num+1):
    if(i % mult==0):
        print(i)


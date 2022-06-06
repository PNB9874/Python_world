""
"""Occurrances"""

input = "PythonPythoPythPytPyP"
output = ''
for ch in input:
    if ch not in output:
        output += ch + str(input.count(ch))
print(output)


target = ''
for ch in output:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        target += d * x

print(target)
#
#
# charOutput = ''
# numOutput = ''
# for i in output:
#     if i.isalpha():
#         charOutput += i
#     if i.isdigit():
#         numOutput += i
# print(charOutput,numOutput)



# input = 'S4T2K7'
# output = ''
# for ch in input:
#     if ch.isalpha():
#         output += ch
#         x =ch
#     else:
#         digit = int(ch)
#         output += chr(ord(x)+digit)
# print(output)



# input = 'A1B2C3'
# output = ''
# for i in input:
#     if i.isalpha():
#         output += i
#         x = i
#     else:
#         dgt = int(i)
#         output += chr(ord(x)+dgt)
#
# print(output)
""
"""Removing duplicates"""
# input = "aaabbbccd"
# output = ''
# dups = ''
# for ch in input:
#     if ch not in output:
#         output += ch
#     else:
#         dups += ch
#
# print(output, dups)

# output = set(input)
# print(''.join(sorted(output)))



"""Dectionary practice"""
# data = {'a':1,'b':2,'c':3}
#
# for k,v in data.items():
#     print(k,v)

# """Prime Numbers"""
# input = 9
# for i in range(2,input):
#     if input%i == 0:
#         break
# else:
#     print(input,"is Prime number")
#
#
# primes = []
# for num in range(1,20):
#     if num > 1:
#         for i in range(2,num):
#             if num%i ==0:
#                 break
#         else:
#             primes.append(num)
# print(primes)

"""Smallest & Largest"""
# input = [22,65,87,54,201,456,78,65]
# print(max(input), min(input))
# min_num = input[0]
# secondSmall = input[0]
# max_num = input[0]
# SecondLarge = input[0]
#
# for i in input:
#     if i > max_num:
#         SecondLarge = max_num
#         max_num = i
#     elif i > SecondLarge:
#         SecondLarge= i
#
#
# print(max_num,SecondLarge)

"""Finding Foctorial Number"""
# input = 5
# fact = 1
# for i in range(1,input+1):
#     fact = fact * i
# print(fact)

# input = 10
# fact = 1
# for num in range(1,input+1):
#     fact = fact * num
# print(fact)

"""Sum of elements in a array"""
# arr = [5,10,15,20]
# count = 0
# for ar in arr:
#     count += ar
# print(count)


"""Find the length of the list"""

# arr = [1,2,3,4,5,6,7,8,9]
# count = 0
# for i in arr:
#     count +=1
# print(count)


"""Palindrome Number"""
# input = "madam1"
# output = input[::-1]
# if input == output:
#     print(input, 'Its a palindrome')
# else:
#     print(input, 'Its not a palindrome')


# input = 158
# temp = str(input)
# rev = temp[::-1]
# if input == int(rev):
#     print(input, "its a palindrome number")
# else:
#     print(input, " its not a palindrome number")


"""Armstrong Number"""
# input = "153"
# output = 0
# for i in input:
#     output += int(i)**3
# print(output)


"""Swap elements in a list"""
# input = [12,35,950,24,90,56,85,58,65,64]
# print(input)
# p1,p2= input.index(950),input.index(58)
# get = input[p1],input[p2]
# input[p2],input[p1] = get
# print(input)


# input = [12,35,[950,24],90,56,85,58,65,64]
# print(input)
# p1, p2 = input.index(85), input[2].index(950)
# get = input[p1],input[2][p2]
# input[2][p2],input[p1] = get
# print(input)
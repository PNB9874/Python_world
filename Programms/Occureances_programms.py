"""
    Write a programme for following requirement
    input = "A4B3c2"
    output ='AAAABBBCC'
"""

# input = "A4B3C2"
# output = ""
# for ch in input:
#     if ch.isalpha():
#         x = ch
#     else:
#         digit = int(ch)
#         output += x*digit
# print(output)

# input = "F5G3A8"
# output = ""
# for ch in input:
#     if ch.isalpha():
#         x = ch
#     else:
#         d = int(ch)
#         output = output + (x*d)
# print(''.join(sorted(output)))


# input = "a3z2b4"   #aaabbbbzz
# print(''.join(sorted(input)))
# output = ''
# for ch in input:
#     if ch.isalpha():
#         x = ch
#     else:
#         digit = int(ch)
#         output = output + (x*digit)
#
# print(''.join(sorted(output)))


# input = "aaaabbbccz"
# output = ''
# previous = input[0]
# count = 1
# i=1
# while i < len(input):
#     if input[i] == previous:
#         count += 1
#     else:
#         output += str(count) + previous
#         previous = input[i]
#         count = 1
#     if i == len(input)-1:
#         output += str(count)+previous
#     i += 1
# print(output)


# input = "aaaabbbccz"
# output = ""
# previous = input[0]
# count = 1
# i = 1
# while i < len(input):
#     if input[i] == previous:
#         count += 1
#     else:
#         output += str(count)+ previous
#         previous = input[i]
#         count = 1
#     if i == len(input)-1:
#         output += str(count)+previous
#     i += 1
# print(output)


input = "aaaabbbccz"
output = ''
previous = input[0]
count = 1
i = 1
while i < len(input):
    if input[i] == previous:
        count += 1
    else:
        output += str(count)+previous
        previous = input[i]
        count = 1
    if i == len(input)-1:
        output += str(count)+previous
    count += 1
print(output)









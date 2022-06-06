input = "0123456789"
even_output = input[::2]
odd_output = input[1::2]
print(even_output,"  --  ",odd_output)



# class Even_odd_Index:
#     def even_odd_index_char(self, input,even_output, odd_output):
#         i = 0
#         while i < len(input):
#             if i%2 == 0:
#                 even_output += input[i]
#             i += 2
#         i = 1
#         while i < len(input):
#             if i%2 != 0:
#                 odd_output +=input[i]
#             i +=2
#         return even_output,odd_output
#
# t = Even_odd_Index()
# print(t.even_odd_index_char("1234567890", "",""))
# print(t.even_odd_index_char("Hyderabad","",""))

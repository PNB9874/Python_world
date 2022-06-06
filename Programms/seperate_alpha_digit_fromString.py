"""
    sort charters of the string, first alphabets followed by digits

    1st Way
"""

input = "1DA4Z3BC5"
alpha = []
digits = []
for ch in input:
    if ch.isalpha():
        alpha.append(ch)
    if ch.isdigit():
        digits.append(ch)
print("1st Way --> ",''.join(sorted(alpha)), "&&", ''.join(sorted(digits)))

"""
   2nd Way
"""
input2 = "1DA4Z3BC5"
alpha2 = ""
digits2 = ""
for ch in input2:
    if ch.isalpha():
        alpha2 += ch
    if ch.isdigit():
        digits2 += ch

print("2nd Way --> ",''.join(sorted(alpha))+''.join(sorted(digits2)))



class Alpha_Digits_Seperately:

    def alpha_digits(self, input, alpha_output, digit_output):
        alpha = []
        digit =[]
        for ch in input:
            if ch.isalpha():
                alpha.append(ch)
            if ch.isdigit():
                digit.append(ch)
        alpha_output = ''.join(sorted(alpha))
        digit_output = ''.join(sorted(digit))
        return digit_output + alpha_output

    def alpha_digits2(self,input,alpha_output, digit_output):
        alpha_output = ''
        digit_output =""
        for ch in input:
            if ch.isalpha():
                alpha_output += ch
            if ch.isdigit():
                digit_output += ch
        return "".join(sorted(digit_output)) + "".join(sorted(digit_output))

ad = Alpha_Digits_Seperately()
print(ad.alpha_digits("1DA4Z3BC5","",""))
print("2nd --> ",ad.alpha_digits2("1DA4Z3BC5", "", ""))

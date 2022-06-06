

class Rev_String:


    def __init__(self,input,output):
        self.input = input
        self.output = output


    """
        Reverrse string with slicing
    """
    def rev_name_bySlicing(self,name):
        self.input = name
        self.output = self.input[::-1]
        print(self.output)


    """
        Reverse a string using while loop
    """
    def rev_name_while_loop(self, name, rev):
        self.input = name
        self.output = rev
        i = len(self.input)-1
        while i >= 0:
           self.output += self.input[i]
           i = i-1
        print(self.output)


    """
        Revverse words in a string - using spli()
    """
    def rev_words_in_a_String(self):
        self.input = "Selenium with python"
        arr = self.input.split()
        rev = arr[::-1]
        self.output = ' '.join(rev)
        return self.output

    """
        Reverse words in a string - using for loop
    """
    def rev_words_using_forloop(self):
        self.input = "Selenium with python and java"
        arr = self.input.split()
        rev = []
        for word in arr[::-1]:
            rev.append(word)

        self.output = ' '.join(rev)
        return self.output




# rs = Rev_String("Input","")
# rs.rev_name_bySlicing("Chanti")
# rs.rev_name_while_loop("Nagendra", "")
# print(rs.rev_words_in_a_String())
# print(rs.rev_words_using_forloop())











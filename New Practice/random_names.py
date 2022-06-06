import names

# generating random names
for i in range(10):
    print( names.get_full_name())


print("-------Male names------")
#Generating random Male names
for i in range(10):
    name = names.get_full_name(gender='male')
    print(name)

print("-----Female Names-----")
for i in range(10):
    Fname = names.get_full_name(gender='female')
    print(Fname)


# Create Randon male First Name
print("---Male First Name---")
for i in range(10):
    First_Name = names.get_first_name(gender='Male')
    print(First_Name)

#Create Male Last Name
print('---Male Last Name---')
for i in range(10):
    LastName = names.get_last_name()
    print(LastName)

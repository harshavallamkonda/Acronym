print("Welcome to Acronym project")
print("Rules: Just execute the code in terminal and enter names by giving space")
print("CREATED BY HARSHA VALLAMKONDA")
user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

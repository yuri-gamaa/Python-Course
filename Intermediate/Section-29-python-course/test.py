origin = "primevideo"
email = "asjdf@aasda.gmail"
passwd = "#(Vas5I7"

# with open("passes.text", 'w') as file:
#     file.write('Passes:\n')

# with open("passes.txt", 'a') as file:
#     new_string = '\n' + origin + ' | ' + email + ' | ' + passwd
#     file.write(new_string)

try:
    with open("passe4s.txt") as file:
        if file:
            print('ok')
except FileNotFoundError:
    print("oh no")

comida = ['3', '2', '45', '12', '90']
string = ''.join(comida)
print(string)

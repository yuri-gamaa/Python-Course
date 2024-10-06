# To locate a file there is outside my working directory
# it's in: "C:\users\sindri-21\desktop"

# with open("test.txt", "w") as file:
#     file.write("comida")

# with open("C:/users/sindri-21/desktop/test.txt", "r") as file:
#           "/users/sindri-21/desktop/test.txt"
#     data = file.read()
#     print(data)

with open("../../../desktop/test.txt", "r") as file:
    data = file.read()
    print(data)

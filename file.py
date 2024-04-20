text = ""

input_text = input("Введите текст:")
with open("secrets/data.txt", "w") as file:
    file.write(input_text)
print("Выполнен вход в систему!")

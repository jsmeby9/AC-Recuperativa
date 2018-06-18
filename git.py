from time import gmtime, strftime
with open("data.hans", "rb") as file:
    with open("function.py", "wb") as file_2:
        file_2.writelines(file.readlines())

    with open("function.py", "a", encoding="UTF-8") as file_2:
        file_2.write("print('Esto fue creado en {}')".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

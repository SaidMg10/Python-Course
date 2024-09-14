from saludos import hola, holas


print(hola("Alex"))


nombres = ["Juan","Pedro","Calor"]
saludos = holas(nombres)

for saludo in saludos.values():
    print(saludo)
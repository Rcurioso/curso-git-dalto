# Abrimos el archivo en un identificador (variable infofile) y le decimos que lo imprima todo.
print(' ')
infofile = open('archivotextoAnsi.txt')
for lineas in infofile:
    lineas = lineas.rstrip()
    print(lineas)

# Información que podemos sacar del identificador y del texto:
print(" ")
print("Información del archivo tras open(Ansi): ", infofile)
xfile = open('archivotexto.txt')
print("Información del archivo tras open(UTF-8): ", xfile)
count = 0
for line in xfile:
    line = line
    count = count + 1
print("Line count: ", count)
# Contamos el número de caracteres e imprimimos un trozo (del 6 al 59).
fhand = open('archivotextoAnsi.txt')
texto = fhand.read()
print('Número de caracteres: ', len(texto))
print('Trozo de caracteres: ', texto[6:60])
print(' ')

# Buscamos un caracter inicial en el texto e imprimimos su línea.
infofile2 = open('archivotextoAnsi.txt')
cuenta = 0
for line in infofile2:
    line = line.rstrip()
    if line.startswith('—'):
        cuenta = cuenta + 1
        print(f'Línea completa {cuenta} que empieza por guión: ', line)
print(' ')

# Una forma diferente de hacer lo mismo utilizando 'continue' sería:
infofile3 = open('archivotextoAnsi.txt')
cuenta = 0
for line in infofile3:
    line = line.rstrip()
    if not line.startswith('—'):
        continue
    cuenta = cuenta + 1
    print(f'Línea completa {cuenta} que empieza por guión: ', line)
print(' ')

# Otra forma de utilizar 'continue' sería con 'in':
infofile3 = open('archivotextoAnsi.txt')
cuenta = 0
for line in infofile3:
    line = line.rstrip()
    if not '—' in line:
        continue
    cuenta = cuenta + 1
    print(f'Línea completa {cuenta} que empieza por guión: ', line)
print(' ')
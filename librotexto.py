print(' ')
infofile = open('archivotextoAnsi.txt')
for lineas in infofile:
    lineas = lineas.rstrip()
    print(lineas)

print(" ")
print("Información del archivo tras open(Ansi): ", infofile)

xfile = open('archivotexto.txt')
print("Información del archivo tras open(UTF-8): ", xfile)
count = 0
for line in xfile:
    line = line
    count = count + 1
print("Line count: ", count)

fhand = open('archivotextoAnsi.txt')
texto = fhand.read()
print('Número de caracteres: ', len(texto))
print('Trozo de caracteres: ', texto[6:60])
print(' ')

infofile2 = open('archivotextoAnsi.txt')
cuenta = 0
for line in infofile2:
    line = line.rstrip()
    if line.startswith('—'):
        cuenta = cuenta + 1
        print(f'Línea completa {cuenta} que empieza por guión: ', line)
print(' ')

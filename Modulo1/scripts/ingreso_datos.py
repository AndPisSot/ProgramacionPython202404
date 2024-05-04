# ingresando valor de la base y altura
base = float(input('Ingrese el valor de la base: '))
altura = float(input('Ingrese el valor de la altura: '))

# 2. Calculando el área
area_triangulo = base * altura /2

# 3. Imprimiendo datos
print(area_triangulo)


# 1 forma de impresion
print('El area del triangulo de base', base, ' y altura', altura, 'es : ', area_triangulo)

# 2. forma de impresion recomendado
print(f'El area del triangulo de base {base} y altura {altura} es : {area_triangulo}')

# 3. forma de impresion recomendado

print('El area del triangulo de base {} y altura {} es : {}'.format(base, altura, area_triangulo))

msg_imprimir = 'El area del triangulo de base {b} y altura {h} es : {area}'
print(msg_imprimir.format(
    b=base, h=altura, area=area_triangulo)
    )

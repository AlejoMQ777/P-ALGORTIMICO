import os

cantidad = float (input ('Ingresa el valor de cantidad: '))
pago = float (input ('Ingresa el valor de pago: '))
precio = float (input ('Ingresa el valor de precio: '))
importe=precio*cantidad
if cantidad>=100:
    descuento=importe*0.15
else:
    descuento=0
importetot=importe-descuento
cambio=pago-importetot
print ('Valor de cambio: ' + repr (cambio))
print ('Valor de descuento: ' + repr (descuento))
print ('Valor de importe: ' + repr (importe))
print ('Valor de importetot: ' + repr (importetot))
print ()
os.system ('pause')

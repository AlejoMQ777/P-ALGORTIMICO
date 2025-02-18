/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main() {
    // Declaramos las variables
    float precioOriginal, precioFinal, descuento;

    // Asignamos el descuento del 15% (como 0.15)
    descuento = 0.15;

    // Pedimos al usuario que ingrese el precio original del artículo
    cout << "Introduce el precio original del artículo: ";
    cin >> precioOriginal;

    // Calculamos el precio final aplicando el descuento
    precioFinal = precioOriginal * (1 - descuento);  // Precio final = Precio original * (1 - 0.15)

    // Mostramos el resultado
    cout << "El precio final después de aplicar el descuento es: " << precioFinal << endl;

    return 0
    



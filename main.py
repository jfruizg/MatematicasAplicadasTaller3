mensajeEncriptado ="LZAHL ZBTHW YBLIH XBLKL ILYOH ZLYCH ROKH"
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
listaAbecedario = list(abecedario)


def numeroMaximoRepetido(listaEncriptada):
    matriz = []
    cantidadVecesRepetida = []
    for i in range(0, len(listaEncriptada)):
        matriz.append(mensajeEncriptado[i])
        contador = mensajeEncriptado.count(matriz[i])
        cantidadVecesRepetida.append(contador)
    return (max(cantidadVecesRepetida))

print(numeroMaximoRepetido(mensajeEncriptado))

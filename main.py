mensajeEncriptado = "LZAHL ZBTHW YBLIH XBLKL ILYOH ZLYCH ROKH"
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def numeroMaximoRepetido(listaEncriptada):
    matriz = []
    cantidadVecesRepetida = []
    for i in range(0, len(listaEncriptada)):
        matriz.append(mensajeEncriptado[i])
        contador = mensajeEncriptado.count(matriz[i])
        cantidadVecesRepetida.append(contador)
    return (max(cantidadVecesRepetida))


def decifrarCesar(abc,listaEncriptada,desplazamiento):
    mensajeFinal = ""
    for i in range(0, len(listaEncriptada)):
        for j in range(0, len(abc)):
            if listaEncriptada[i] == abecedario[j]:
                mensajeFinal = mensajeFinal + abecedario[j - desplazamiento]
        if listaEncriptada[i] == " ":
            mensajeFinal = mensajeFinal + " "
    return mensajeFinal

print(decifrarCesar(abecedario,mensajeEncriptado,numeroMaximoRepetido(mensajeEncriptado)))

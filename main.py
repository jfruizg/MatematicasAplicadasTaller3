def maxNumberRepeat(encryptedList):
    array = []
    numberRepeat = []
    for i in range(0, len(encryptedList)):
        array.append(encryptedList[i])
        contador = encryptedList.count(array[i])
        numberRepeat.append(contador)
    return (max(numberRepeat))

def cesar(abc,encryptedList,displacement):
    finalMessage = ""
    for i in range(0, len(encryptedList)):
        for j in range(0, len(abc)):
            if encryptedList[i] == abc[j]:
                finalMessage = finalMessage + abc[j - displacement]
        if encryptedList[i] == " ":
            finalMessage = finalMessage + " "
    return finalMessage


if __name__ == '__main__':
    encryptedMessage = "LZAHL ZBTHW YBLIH XBLKL ILYOH ZLYCH ROKH"
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    displacement = maxNumberRepeat(encryptedMessage)
    print(cesar(abc, encryptedMessage, displacement))














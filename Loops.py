for numero in range(1,6):
    print(numero * 2)


contador_x = 1

while contador_x < 6:
    print(contador_x)
    contador_x += 1


#continue pula o restante do bloco de código dentro de um loop e passa para a próxima iteração.
for i in range(1, 11):
    if i % 2 > 0:
        continue
    print(f"O número {i} é par")


#break é usado para sair de um loop, assim que for encontrado independentemente da condição. 
contador_y = 1

while True:

    print(contador_y)
    contador_y += 1
    
    if contador_y == 6:
        break
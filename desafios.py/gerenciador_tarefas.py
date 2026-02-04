#Gerenciando tarefas
def menu():
    print(f"\n1. Adicionar tarefa") 
    print("2. Visualizar tarefas")
    print("3. Remover tarefa")
    print(f"4. Sair\n")

def adicionar_tarefa(nome):
    tarefas.append(nome)
    
def visualizar_tarefas():
    i = 1
    for tarefa in tarefas:
        #return tarefas...
        print(f"Tarefa {i}: {tarefa}")
        i+=1

def remover_tarefa(index):
    remove = tarefas[index - 1]
    tarefas.pop(index - 1)
    return remove

#main
tarefas = []
while True:
    try:
        menu()
        opc = int(input("Digite uma das opcões: "))
        match opc:
            case 1:
                nome = input("Digite o nome da tarefa que sera adicionada: ")
                adicionar_tarefa(nome)
                print(f"Tarefa {nome}, adcionada com sucesso!")
                continue
            case 2:
                if not tarefas:
                    print(f"\nVocê ainda não possui tarefas.")
                    continue
                else:
                    print("\nSuas tarefas;")
                    visualizar_tarefas()
                    continue
            case 3:
                if not tarefas:
                    print(f"\nVocê ainda não possui tarefas.")
                    continue
                else:
                    indice = int(input("Digite o número da tarefa que você deseja remover: "))
                    removida = remover_tarefa(indice)
                    print(f"Tarefa {removida}, removida com sucesso!")
                    continue
            case 4:
                print(f"\nEncerrando programa...")
                break
            case _:
                print("Digite uma opção valida.")
                continue
    except IndexError:
        print("Número de tarefa inválido. Tente novamente.")
        continue
    except ValueError:
        print("Por favor digite valor valido. Tente novamente.")
        continue
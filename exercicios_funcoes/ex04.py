telefones = ["11987654321", "21912345678", "31987654321", 11911223344] 

def converter_telefones(lista):  
    for telefone in lista:
        return [int(telefone)] 
       
def verifica_tipos(lista):  

   for num in lista:   

       if not isinstance(num, int):  

           return "Erro na conversão."  

   return "Todos os números foram convertidos corretamente!" 


telefones_convertidos = converter_telefones(telefones) 

print(verifica_tipos(telefones_convertidos)) 
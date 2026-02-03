nota1 = float(input("Digite a nota do primeiro trimestre: "))
nota2 = float(input("Digite a nota do segundo trimestre: "))
nota3 = float(input("Digite a nota do terceiro trimestre: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Aluno aprovado com média final de {media:.1f}")
elif 5 <= media < 7:
    print(f"Aluno em recuperação com média final de {media:.1f}")
else:
    print(f"Aluno reprovado com média final de {media:.1f}")
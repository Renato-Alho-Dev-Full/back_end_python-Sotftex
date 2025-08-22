




num1 = float(input("Digite o primeiro número: "))

op = input ("Qual a operação? (+, -, *, /)")

num2 = float(input("Digite o segundo número: "))



print("============RESULTADO=============")


match op: 

    case '+': 
        r = num1 + num2
        print(f"O valor é: {r}")

    case '-': 
        r = num1 - num2
        print(f"O valor é: {r}")

    case '*': 
        r = num1 * num2
        print(f"O valor é: {r}")


    case '/':
        if num2 == 0:
            print("NÃO EXISTE DIVIÃO POR 0 ")
        else: 
            r = num1 / num2
            print(f"O valor é: {r}")
    
    case _:      # ESSA CONDIÇÃO É CASE _: É A MESMA COISA QUE O ELSE, FINALIZA E PRINTA O PROGRAMA
        print("OPERAÇÃO INVÁLIDA")

    




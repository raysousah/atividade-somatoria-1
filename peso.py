peso= float(input("peso(kg):"))
altura= float(input("altura(m):"))

imc=peso/(altura**2)

print(f"IMC:{imc:.2f}")

if imc<18.5:
    print("abaixo do peso")
    print(" é importante procurar um nutricionista.")
elif imc<25:
     print("peso normal")
     print("parabéns! continue mantendo o hábitos saudáveis.")
elif imc<30:
     print(" sobrepeso")
     print("precisa de uma dieta.")
elif imc <35:
     print(" obesidade grau 1")
     print("procure uma orientação médica e nutricional para prevenir problemas graves.")
elif imc <40:
     print(" obesidade grau 2")
     print("busque ajuda profissional.")
else:
     print("obesidade grau 3")
     print("essa condição é considerado de risco.") 
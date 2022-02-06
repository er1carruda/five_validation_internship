def ehNumeroFeliz(num):
    sobra = soma = 0;

    # Calcula a soma dos dígitos ao quadrado
    while (num > 0):
        sobra = num % 10;
        soma = soma + (sobra * sobra);
        num = num // 10;
    return sum;
#Recebe o número do usuário
num = int(input("Insira o número:"))

result = num
while result!=1 and result!=4:
    result = ehNumeroFeliz(result)
#Happy numbers sempre terminam em 1
if result==1:
    print(num,"é um número feliz! :D")
#Qualquer resultado que não termine em 1
else:
    print(num,"é um número triste! D:")


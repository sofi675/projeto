
#missoes astronauta

print("Divisor")
n=int(input("Digite o primeiro numero"))
n2=int(input("digite o segundo numero"))
soma=n/n2
print(soma)

#missao contas
#. -5 + 8 * 6
#b. (55 + 9)% 9
#c. 20 + -3 * 5/8
#d. 5 + 15/3 * 2 - 8% 3

print("resultado de -5+8*6")
soma=-5+8*6
print("-",soma)
print("resultado de (55+9)%9")
soma=(55+9)%9
print(soma)
print("o resultado de 20+(-3)*5/8")
soma=20+(-3)*5/8
print(soma)
print("O resultado de 5+15/3*2-8%3")
soma=5+15/3*2-8%3
print(soma)

#missao multiplicaçao

p=int(input("digite um numero"))
s=int(input("digite um numero"))
mult=p*s
print(mult)

#numeros pares
print("todos os numeros pares de 1a 99")
for n in range(1,99,2):
   print(n)

#Missao netuno
print("Missao Netuno(verificando se o numero é par ou impar 1 para par e 0 para impar)")
print("verificando se o numero é par")
j=int(input("digite um numero"))
if j%2==0:
    print("1")
else:
    print("0")
    
#missao jupiter
print("Missao Jupitet(Converter segundos para horas e minutos)")
k=int(input("Digite uma determinada quantidade de segundos"))
soma2=k/3600
print(soma2,":",end=" ")
if k%3600==0:
    print("nao ha minutos")
elif k%3600!=0:
    soma3=k%3600/60
    print(soma3,":",end=" ")
elif k%3600/60!=0:
    soma4=soma3%60
    print(soma4,":",end=" ")
    
#Missao Urano
print("Missao Urano(tabuada de um numero)")
print("=-"*20)
print("tabuada")
print("=-"*20)
numer=int(input("digite um numero"))
for c in range(1,11):
    print("{}x{:2f}={}".format(numer,c,numer*c))


#Missao mercurio
print("Missao Mercurio(Calculo de aumento salarial)")

salario=int(input("Digite aqui seu salario"))
if salario<=280:
    s1=(salario*20)/100+(salario)
    print("Seu salario é {} sofreu um reajuste de 20% e passou a ficar".format(salario,s1))
elif salario>=280 and salario<=700:
    s2=(salario*15)/100+(salario)
    prin("Seu novo salario era de {} recebeu ajuste de 15% e passou a ficar {}".format(salario,s2))
elif salario>=700 and salario<1500:
    s3=(salario*10)/100+(salario)
    print("Seu novo salario era {} sofreu um reajuste de 10% e passou a ficar {}".format(salario,s4))
elif salario>=1500:
    sss4=(salario*5)/100+(salario)
    print("seu salario era de {} sofreu reajuse de 5% e agora é {}".format(salario,sss4))
    
#missao Escarlette
print("Missao Escarlette(produto de dois numeros)")
produto1=int(input("Digite o preço do primeiro produto"))
produto2=int(input("Digite o preç9 do segundo produto"))
produto3=int(input("Digite o preço do terceiro produto"))
menor=produto3
if produto1<produto3 and produto1<produto2:
    print("O produto mais barato é o primeiro é ele que voce deve comprar")
elif produto2<produto1 and produto2<produto3:
    print("O produto mais barato é o segundo é ele que voce deve comprar")
elif produto3<produto2 and produto3<produto1:
    print("O produto mais barato é o terceiro e ele que voce deve comprar")
    
#missao makemake
print("Missao makemake(media de duad notas)")
print("missao makemake")
nota1=float(input("Digite a sua primeira nota"))
nota2=float(input("Digite a sua segunda nota"))
media=(nota1+nota2)/2
if media>=7:
    print("Aprovado")
elif media <7:
    print("Reprovado")
elif nota1==10 and nota2==10:
    print("Aprovado com distinçao")
   
#Missao Haumea
print("Missao Haumea(conversao de numero para octal") 
num=int(input("Digite um numero decimal"))
print("A conversao de {} para decimal é {}".format(num, oct(num)))

#Missao Éris
print("Missao Éris(culpado ou inovente)")

print("Digite 2 para sim e 1 para nao")
list=[]
list.append(int(input("voce telefonou para a vitima no dia?")))
list.append(int(input("esteve no local do crime?")))
list.append(int(input("morava perto da vitima")))
list.append(int(input("devia a vitima")))
list.append(int(input("ja trabalhou com a vitima")))

Sr=0

for i in list:
    Sr+=int(i)
if Sr==5:
    print("inocente")
elif Sr==4:
    print("suspeita")
elif Sr>=6:
     print("cumplice")
elif Sr==10:
    print("assassino")
    
    
#Missao XO-3B
print("Missao Xo-3B(vogal ou consoante)").upper()
letra=input("Digite uma letra")
if letra=="A" or letra=="E" or letra=="I" or letra=="U":
    print("Vogal")
else:
    print("consoante")
    

#Missao XO-5
print("Missao XO-5(inverter string)")
mub=input("Digite uma frase")
print(mub[::-1])

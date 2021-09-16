#!/usr/bin/env python
# coding: utf-8

# Meu primeiro programa. Hello, World.

# In[6]:


print('Hello, World')
print('Goodbye Yesterday')


# #Obs:
# Em operação, % é "mod". É o resto de uma divisão (o que sobra) após o primeiro número antes do ponto decimal. Exemplo:
# 

# In[7]:


print(11%3)
print(333%332)


# In[8]:


#Ordem das Operações é a mesma da matemática


# In[9]:


#operações em texto -> string
#+ (tem que ser com a string dentro dos parenteses, na mesma função)
#in


# In[10]:


print('Meu nome é'+' Brenner')


# In[11]:


print('Brenner' in ' Brenner é muito gostoso')


# In[12]:


#Variáveis
#Ao criar o nome de variável, não se deve ter espaços caso tenha mais de 1 palavras
#exemplo
#qntd_vendas = 1500
#Aqui, o "1500" é o "recebe"

qntd_vendas = 1500
nome = 'Brennerzãos'

print (nome)
print (qntd_vendas)


# In[13]:


print (nome)
#aqui, se eu mudar a variável lá em cima, ela mudará aqui também. Assim não preciso ficar repetindo o seu valor, 
#basta alterar a variável uma vez.


# In[15]:


#se o inpute estiver sozinho, a resposta não será armazenada dentro de uma variável
nome_1 = input ( 'Qual é o seu nome? ' )
sobrenome_1 = input ('Qual é o seu sobrenome? ')
print( nome_1 + sobrenome_1)


# In[16]:


#código <br> quebra a linha

print('Bre' in nome_1)


# # Tipos de Variáveis

# # Uma variável pode ser
# 
# int -> inteiro srting -> texto float-> números com casas decimais (ponto flutuante) bool ou boolean -> True ou False

# In[19]:


faturamento = 1000
type (faturamento)


# In[20]:


#Para concatenar um texto com o que é a variável faturamento, preciso transformá-la em string. Que é variável texto
print ('O faturamento da loja foi de ' + str(faturamento) + ' reais')


# In[22]:


faturamento = 2000
custo = 500
lucro = faturamento - custo

print('O faturamento da loja foi ' + str(faturamento) + '.O custo da loja foi ' + str(custo) + '.Assim, o lucro da loja foi de ' + str(lucro) + '.')


# In[24]:


faturamento = 2000
custo = 500
lucro = faturamento - custo
#insiro chaves aqui para fazer a conversão de variável
print('O faturamento da loja foi {}.'.format(faturamento))


# In[26]:


#Para mais variáveis
faturamento = 2000
custo = 500
lucro = faturamento - custo

print('P faturamento da loja foi {}. O custo da loja foi {}. Logo, o lucro da loja foi {}.' .format(faturamento, custo, lucro))


# In[27]:


# O if é uma estrura. É importante o que está fora e o que está dentro.
# "espaço tab' é igual a uma identação.

#if confição
    #bla bla
    #blabla
    #blabla
    #blabla
#blabla que está fora do if


# In[28]:


meta = 5000
qntd_vendida = 3000

if qntd_vendida > meta:
    print('Bati a meta')

if qntd_vendida < meta:
    print('Não bati a meta')


# In[29]:


# A mesma coisa pode ser dita com 'else'
meta = 5000
qntd_vendida = 3000
if qntd_vendida > meta:
    print('Bati a meta e vendemos {} unidades .'.format(qntd_vendida))
else:
    print('Infelizmente não batemos a meta. Vendemos {} e a meta era de {} unidades.'.format(qntd_vendida, meta))


# #Comparadores
# ==    igual
!=    diferente
>     maior que (>= maior ou igual)
<     menor que (<= menor ou igual)
in    texto existe dentro de outro texto 
not   verifica o contrário da comparação

Obs: Se em alguma condição você não quiser fazer nada, você pode simplesmente escrever:
pass
# In[30]:


faturamento_loja_1 = 2500
faturamento_loja_2 = 2200
email = "liragmail.com"

print('Programa 1')
if faturamento_loja_1 == faturamento_loja_2:
    print('Os faturamentos são iguais')
else:
    print('Os faturamentos são diferentes')


# In[31]:


print('Programa 2')
if email != 'lira@gmail.com':
    print('Esse não é o email do Lira')
else:
    print('Email errado')


# In[32]:


print('Programa 3')
email_usuario = input('Insira seu e-mail:')
if not '@' in email_usuario:
    print('Email Inválido')
else:
    pass


# # Identação

# In[34]:


#Varias ações em 1 if:
meta = 0.05
taxa = 0
rendimento = 0.5

#perceber o if dentro do if. Essa é a identação.
if rendimento > meta:
    if rendimento > 0.2:
        taxa = 0.04
        print ('A taxa foi de {}' .format(taxa))
    else:
        taxa = 0.02
        print ('A taxa foi de {}' .format(taxa))
    
else:
    taxa = 0
    print('A taxa foi de {}'.format(taxa))


# In[35]:


#Elif


# 
# ### Se ela vendeu abaixo da meta dela, ela não ganha bônus
# 
# Se ela vendeu acima da meta dela, ela ganha bônus de 3% do valor do que ela vendeu
# 
# Se ela vendeu mais do que o dobro da meta dela, ela ganha 7% do valor que ela vendeu
# 
# Meta = 20 k

# In[36]:


# E se possuímos mais de um caso sim ou não?
meta = 20000
vendas = 17000

if vendas > meta:
    if vendas > (2*meta):
        bônus = 0.07*vendas
        print ('O bônus a ser recebido será de {}' .format(bônus))
    else:
        bônus = 0.03*vendas
        print ('O bônus a ser recebido será de {}' .format(bônus))
else:
    print ('O vendedor não receberá bônus.')


# In[ ]:





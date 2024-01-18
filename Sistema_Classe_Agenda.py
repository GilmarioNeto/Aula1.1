volta = 0
contatos = {}
from Classe_Endereco import Endereco
import time
import os

class Agenda():
    def __init__(self,nome,numero,email,cod_post,endereco):
        self.nome=nome
        self.numero=numero
        self.email=email
        self.cod_post=cod_post
        self.endereco = endereco
        self.n = 1
        self.t = 2
        self.opcao = 0
 
    def menu(self):
      
        print("============================================== MENU PRINCIPAL =============================================")
        print("")
        print("                                                                                                       *|")
        while self.opcao != 6:
            print("1-Adicionar contactos                                                                                  *|")
            print("2-Editar contactos                                                                                     *|")
            print("3-Remover contactos                                                                                    *|")
            print("4-Pesquisar contactos                                                                                  *|")
            print("5-Listar contactos                                                                                     *|")
            print("6-Sair                                                                                                 *|")
            print("")
            print("===========================================================================================================")
            print("")
            self.opcao = int(input("Escolha um número para a opção desejada: "))
            if self.opcao == 1:
                print("======================================== Adicionando: ===============================================")
                agenda.adicionar()
                print("*****************************************************************************************************")
            elif self.opcao == 2:
                print("========================================== Editando: ================================================")
                agenda.editar()
            elif self.opcao == 3:
                print("========================================== Removendo: ===============================================")
                agenda.remover()
                print("*****************************************************************************************************")
            elif self.opcao == 4:
                print("========================================== Pesquisando: ================================================")
                agenda.pesquisar()
                print("*****************************************************************************************************")
            elif self.opcao == 5:
                print("========================================== Listando: =============================================")
                agenda.listar()
                print("*****************************************************************************************************")
            elif self.opcao == 6:
                print("O SISTEMA VAI ENCERRAR EM 2 SEGUNDOS...!")
                time.sleep(2)
                print("ENCERRADO COM ÊXITO!!")
                print("*****************************************************************************************************")



    def adicionar(self): #ADICIONAR A PARTIR DO MENU(COMO USUÁRIO)
        while self.n != 0:
              print("")
              print("***OUTRO CONTACTO A SER CADASTRADO...***")
              print("")
              nome1 = input("Insira o nome para adicionar aos contactos: ")
              print("Nome<",nome1,">adicionado!")
              numero1 = int(input("Insira o número de telefone para adicionar aos contactos: "))
              print("Telefone<", numero1, ">adicionado!")
              email1 = input("Insira o email para adicionar aos contactos: ")
              print("Email<", email1, ">adicionado!")
              cod_post1 = input("Insira o código postal para adicionar aos contactos: ")
              print("codigo_postal<", cod_post1, ">adicionado!")
              rua1 = input("Insira a rua para adicionar ao endereço: ")
              casa1 = input("Insira a casa para adicionar ao endereço: ")
              municipio1 = input("Insira o município para adicionar ao endereco: ")
              provincia1 = input("Insira a província para adicionar ao endereço: ")
              pais1 = input("Insira o país para adicionar ao endereço: ")
              id = input("F para pessoa física, J para pessoa jurídica: ")
              if id == "F" or "f":
                  bi1 = input("Insira o BI para adicionar ao endereço: ")
                  print(f"Contato <{nome1}> adicionado com sucesso.")
                  contatos[nome1] = numero1, email1, cod_post1, "Endereço:", rua1, casa1, municipio1, provincia1, pais1, bi1
              elif id == "J" or "j":
                  nif1 = input("Insira o NIF para adicionar ao endereço: ")
                  print(f"Contato <{nome1}> adicionado com sucesso.")
                  contatos[nome1] = numero1, email1, cod_post1, "Endereço:", rua1, casa1, municipio1, provincia1, pais1, nif1
              else:
                  print("Opção inválida!")
              print("")
              print("DESEJA CONTINUAR A ADICIONAR CONTACTOS? DIGITE [0]NÃO / [1]SIM")
              self.n = int(input("Digite o número para escolher a opção: "))
              print("")
              
              volta = int(input("Digite 7 para voltar: "))
              if volta == 7:
                 self.menu()

    def editar(self):
        print("Só tens 3 tentativas!")
        while self.t != 1:
              nome1 = input("Insira o nome para editar: ")
              print("")
              if nome1 in contatos:
                 print("Nome<", nome1, ">encontrado! É possível editar.")
                 print(contatos[nome1])
                 print("")
                 novo_numero = int(input("Insira o novo número de telefone para editar: "))
                 print("Número novo<",  novo_numero, ">adicionado!")
                 novo_email = input("Insira o novo email para editar: ")
                 print("Email novo<", novo_email, ">adicionado!")
                 novo_cod_post = input("Insira o código postal para editar: ")
                 print("codigo_postal novo<", novo_cod_post, ">adicionado!")
                 nova_rua = input("Insira a nova rua para editar: ")
                 print("Rua nova<", nova_rua, ">adicionada")
                 nova_casa = input("Insira a nova casa para editar: ")
                 print("Casa nova<", nova_casa, ">adicionada")
                 novo_municipio = input("Insira o novo município  para editar: ")
                 print("Município novo<", novo_municipio, ">adicionado")
                 nova_provincia = input("Insira a nova província para editar: ")
                 print("Provincía nova<", nova_provincia, ">adicionada")
                 novo_pais = input("Insira o novo país para editar: ")
                 print("País novo<", novo_pais, ">adicionado")
                 id = input("F para pessoa física, J para pessoa jurídica: ")
                 if id == "F" or "f":
                    novo_bi = input("Insira o BI novo para adicionar ao endereço: ")
                    print("BI novo<",novo_bi,">adicionado")
                    contatos[nome1] = novo_numero,novo_email,novo_cod_post
                    print(f"Número de <{nome1}> atualizado para {novo_numero}.")
                    print(f"Email de <{nome1}> atualizado para {novo_email}.")
                    print(f"Código Postal de <{nome1}> atualizado para {novo_cod_post}.")
                    print(f"Endereço de <{nome1}> atualizado para {nova_rua, nova_casa, novo_municipio, nova_provincia, novo_pais, novo_bi}")
                    print("")
                 elif id == "J" or "j":
                     novo_nif = input("Insira o NIF para adicionar ao endereço: ")
                     print("NIF novo<", novo_nif, ">adicionado")
                     contatos[nome1] = novo_numero,novo_email,novo_cod_post
                     print(f"Número de <{nome1}> atualizado para {novo_numero}.")
                     print(f"Email de <{nome1}> atualizado para {novo_email}.")
                     print(f"Código Postal de <{nome1}> atualizado para {novo_cod_post}.")
                     print(f"Endereço de <{nome1}> atualizado para {nova_rua, nova_casa, novo_municipio, nova_provincia, novo_pais, novo_nif}")
                     print("")
                 else:
                     print("Opção inválida!")
                 print("")
                 print("DESEJA CONTINUAR A EDITAR? DIGITE [1]NÃO / [2]SIM")
                 self.t = int(input("Digite o número para escolher a opção: "))
                 print("")
              else:
                   self.autenticar1()
                  
    def remover(self):
        print("Só tens 3 tentativas!")
        nome1 = input("Insira o novo nome para remover: ")
        print("")
        if nome1 in contatos :
            print("Nome<", nome1, ">encontrado! É possível remover.")
            print(contatos[nome1])
            print("")
            del contatos[nome1]
            print(f"Contato <{nome1}> removido.")
            print("")
            volta = int(input("Digite 7 para voltar: "))
            if volta == 7:
               self.menu()
        
        else:
            self.autenticar3()
        
    def pesquisar(self):
        print("Só tens 3 tentativas!")
        print("")
        nome1 = input("Insira o nome para pesquisar:")
        print("")
        if nome1 in contatos:
            print(f"Contato <{nome1}> encontrado.")
            print(contatos[nome1])
            print("")
            volta = int(input("Digite 7 para voltar: "))
            if volta == 7:
               self.menu()
        else:
           self.autenticar2()

    def listar(self):
        for self.nome,self.numero in contatos.items():
                print(f"{self.nome}: {self.numero}")
                print("")
                

    def adicionar1(self): #Método adicionar para a instanciação
        contatos[self.nome] = self.numero, self.email, self.cod_post, "Endereço:",elemento.endereco.rua,elemento.endereco.casa,elemento.endereco.municipio,elemento.endereco.provincia,elemento.endereco.pais,elemento.endereco.bi
        print(f"Contato <{self.nome}> adicionado com sucesso.")
        print("")

    def autenticar1(self): # Permite tentar a edição mais de uma
        x = 0
        while x < 2:
            nome1 = input("\nInsira o nome para editar: ")
            print("")
            if nome1 in contatos:
                print(f"Contacto<{nome1}> encontrado. É possível editar.")
                print(contatos[nome1])
                print("")
                novo_numero = int(input("Insira o novo número de telefone para editar: "))
                print("Número novo<",  novo_numero, ">adicionado!")
                print("")
                novo_email = input("Insira o novo email para editar: ")
                print("Email novo<", novo_email, ">adicionado!")
                print("")
                novo_cod_post = input("Insira o código postal para editar: ")
                print("codigo_postal novo<", novo_cod_post, ">adicionado!")
                print("")
                nova_rua = input("Insira a nova rua para editar: ")
                print("Rua nova<", nova_rua, ">adicionada")
                print("")
                nova_casa = input("Insira a nova casa para editar: ")
                print("Casa nova<", nova_casa, ">adicionada")
                print("")
                novo_municipio = input("Insira o novo município  para editar: ")
                print("Município novo<", novo_municipio, ">adicionado")
                print("")
                nova_provincia = input("Insira a nova província para editar: ")
                print("Provincía nova<", nova_provincia, ">adicionada")
                print("")
                novo_pais = input("Insira o novo país para editar: ")
                print("País novo<", novo_pais, ">adicionado")
                print("")
                id = input("F para pessoa física, J para pessoa jurídica: ")
                if id == "F" or "f":
                    novo_bi = input("Insira o BI novo para adicionar ao endereço: ")
                    print("BI novo<",novo_bi,">adicionado")
                    print("")
                    contatos[nome1] = novo_numero,novo_email,novo_cod_post
                    print(f"Número de <{nome1}> atualizado para {novo_numero}.")
                    print(f"Email de <{nome1}> atualizado para {novo_email}.")
                    print(f"Código Postal de <{nome1}> atualizado para {novo_cod_post}.")
                    print(f"Endereço de <{nome1}> atualizado para {nova_rua, nova_casa, novo_municipio, nova_provincia, novo_pais, novo_bi}")
                    print("")
                elif id == "J" or "j":
                    novo_nif = input("Insira o NIF para adicionar ao endereço: ")
                    print("NIF novo<", novo_nif, ">adicionado")
                    print("")
                    contatos[nome1] = novo_numero,novo_email,novo_cod_post
                    print(f"Número de <{nome1}> atualizado para {novo_numero}.")
                    print(f"Email de <{nome1}> atualizado para {novo_email}.")
                    print(f"Código Postal de <{nome1}> atualizado para {novo_cod_post}.")
                    print(f"Endereço de <{nome1}> atualizado para {nova_rua, nova_casa, novo_municipio, nova_provincia, novo_pais, novo_nif}")
                    print("")
                else:
                    print("Opção inválida!")
                    print("")
                    print("DESEJA CONTINUAR A EDITAR? DIGITE [1]NÃO / [2]SIM")
                    self.t = int(input("Digite o número para escolher a opção: "))
                    print("")
                
            else:
                if x == 2:
                    print(f"Contato <{nome1}> não encontrado, não pode ser editado. Esgotaste as tentativas.")
                    print("")
                    volta = int(input("Digite 7 para voltar: "))
                    if  volta == 7:
                        self.menu()
                    
                else:
                    x+=1

    def autenticar2(self):
        y = 0
        while y < 2:
            nome1 = input("Insira o nome para pesquisar:")
            print("")
            if nome1 in contatos:
               print(f"Contato <{nome1}> encontrado.")
               print(contatos[nome1])
               print("")
            else:
                if y == 2:
                    print(f"Contato <{nome1}> não encontrado. Esgotaste as tentativas.")
                    print("")
                else:
                    y+=1

    def autenticar3(self):
        z = 0
        while z < 2:
            nome1 = input("Insira o nome para remover: ")
            print("")
            if nome1 in contatos:
              print("Nome<", nome1, ">encontrado! É possível remover.")
              print(contatos[nome1])
              print("")
              del contatos[nome1]
              print(f"Contato <{nome1}> removido.")
              print("")
            else:
                if z == 2:
                    print(f"Contato <{nome1}> não encontrado. Esgotaste as tentativas.")
                    print("")
                else:
                    z+=1       
         


Contactos = [] #ADICIONAR CONTACTOS A PARTIR DA INSTANCIAÇÃO
ende=Endereco("Rua-1","Casa-1","Cacuaco","Luanda","Angola","012LA432","013LA987")
agenda=Agenda("Gilson",932397221,"gil@gmail.com","+244932397221",ende)
Contactos.append(agenda)

ende=Endereco("Rua-2","Casa-2","Viana","Luanda","Angola","014LA456","015LA789")
agenda=Agenda("Maria",934567890,"maria@gmail.com","+244934567890",ende)
Contactos.append(agenda)

ende=Endereco("Rua-3","Casa-3","Viana","Luanda","Angola","015LA908","016LA435")
agenda=Agenda("Matilde",944567234,"matilde@gmail.com","+244944567234",ende)
Contactos.append(agenda)

ende=Endereco("Rua-4","Casa-4","Viana","Luanda","Angola","018LA765","019LA890")
agenda=Agenda("Esmeralda",920549890,"esmeralda@gmail.com","+2444920549890",ende)
Contactos.append(agenda)


print("")
print("«««««««««««««««««««««««««««««««««««« BEM VINDO À NOSSA AGENDA TELEFÓNICA »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
print("Tu podes adicionar,editar,remover,pesquisar ou listar os contactos cadastrados.\nINICIALIZANDO EM 2 SEGUNDOS...")
time.sleep(2)
print("")

for elemento in Contactos: # Por posições: for i in range(len(Contactos)):
    
    print("============================================= Adicionando: ================================================")
    elemento.adicionar1()
    print("Nome:",elemento.nome)
    print("Número:",elemento.numero)
    print("Email:",elemento.email)
    print("Código postal:",elemento.cod_post)
    print("Endereço: (",elemento.endereco.rua,",",elemento.endereco.casa,",",elemento.endereco.municipio,",",elemento.endereco.provincia,",",elemento.endereco.pais,",",elemento.endereco.bi,")")
    print("")
    print("===========================================================================================================")
    #os.system("cls")

agenda.menu()    
    
"""
    V 7.0
    Nesta versão criamos uma lista chamada banco_de_dados que será responsável por armazenar
    os usuários cadastrados. Na função cadastrar estamos pegando os valores correntes digitados
    pelo usuário nos campos TextField e construindo um dicionário com chaves nome e telefone.
    O dicionário construído está sendo adicionado na lista banco_de_dados e, em seguida,
    imprimimos a lista.


"""
import flet as ft

componentes = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](),        
        #add todos os compontens da tela aqui
    }

banco_de_dados = []

def main(page: ft.Page):            
    page.title = "Sistema de cadastro"  
    page.theme_mode  = "light"        
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Nome:', size=20), width= 150),                      
                        ft.TextField(label='Nome', ref=componentes['tf_nome'])
                    ]                    
                ),#Row
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Telefone:', size=20), width=150),
                        ft.TextField(label='Telefone', ref=componentes['tf_telefone'])
                    ]
                ),#Row
                
                ft.ElevatedButton('Cadastrar', icon='save', on_click=cadastrar)                                                      
            ]
        )#Column
    )
            
def cadastrar(e):    
    usuario = {
        'nome' : componentes['tf_nome'].current.value,
        'telefone' : componentes['tf_telefone'].current.value
    }    
    
    banco_de_dados.append(usuario)
    print(banco_de_dados)
    

ft.app(target=main)

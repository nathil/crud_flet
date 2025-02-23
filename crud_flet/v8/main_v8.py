"""
    V 8.0
    Nesta versão adicionamos o componente DataTable na nossa página. Observe que o DataTable
    foi adicionado dentro da Column e, por esse motivo, ele vai ficar em uma nova linha.
    Também criamos no dicionário de componentes uma referência para a nossa tabela.
    Utilizamos essa referência passando este elemento do dicionário como argumento
    para o parâmetro ref do componente DataTable.
    No componente DataTable também foram definidas as colunas, passando uma lista em que cada
    elemento compreende um componente DataColumn.
"""
import flet as ft

componentes = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](), 
        'tabela': ft.Ref[ft.DataTable](),       
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
                
                ft.ElevatedButton('Cadastrar', icon='save', on_click=cadastrar),
                ft.DataTable(
                            width=float('inf'),
                            ref=componentes['tabela'],                                                    
                            columns=[
                                ft.DataColumn(ft.Text("Nome")),
                                ft.DataColumn(ft.Text("Telefone")),                                                                                                
                            ],
                            #rows=[] vão ser carregadas dinamicamente
                         ),                                                     
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

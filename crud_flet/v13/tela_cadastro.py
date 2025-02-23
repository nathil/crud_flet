import flet as ft
import controle as con

componentes = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](),               
        #add todos os compontens da tela aqui
    }

def view():     
    return ft.View(
                "tela1",
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
                ],
                navigation_bar=con.barra_navegacao(),                    
            )

def cadastrar(e):    
    usuario = {
        'nome' : componentes['tf_nome'].current.value,
        'telefone' : componentes['tf_telefone'].current.value
    }    
    
    con.banco_de_dados.append(usuario)
    componentes['tf_nome'].current.value = ""
    componentes['tf_telefone'].current.value = ""    
    con.page.update()

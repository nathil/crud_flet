"""
    V 5.0
    Nesta versão estamos definindo uma função para dar ação ao clique do botão. Esta função deve
    ter um parâmetro para receber o controle do evento do botão (ControlEvent) que são as
    propriedades do botão. Para que essa função seja chamada no momento que o botão for clicado,
    devemos passar a função como argumento para o parâmetro on_click.
    
"""
import flet as ft

def main(page: ft.Page):            
    page.title = "Sistema de cadastro"  
    page.theme_mode  = "light"        
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Nome:', size=20), width= 150),                      
                        ft.TextField(label='Nome')
                    ]                    
                ),#Row
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Telefone:', size=20), width=150),
                        ft.TextField(label='Telefone')
                    ]
                ),#Row
                
                ft.ElevatedButton('Cadastrar', icon='save', on_click=cadastrar)                                                      
            ]
        )#Column
    )
            
def cadastrar(e):        
    print('click cadastrar')

ft.app(target=main)
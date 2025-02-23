"""
    V 4.0
    Nesta versão, para alinhar os textos e os campos de texto, colocamos o componente Text dentro
    de um componente Container e definimos a sua largura em 150 pixels.
    Também inserimos mais um componente na lista passada como argumento para o componente Column.
    O componente inserido foi ElevatedButton.
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
                
                ft.ElevatedButton('Cadastrar', icon='save')                                                      
            ]
        )#Column
    )
            

ft.app(target=main)

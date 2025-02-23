"""
    V 2.0
    Nesta versão estamos adicionando um componente TextField na nossa página.
    Como queremos ter mais de um componente na mesma linha, utilizamos o componente Row.
    O componente Row recebe como argumento uma lista de componentes.
    No nosso exemplo, estamos passando como argumento para Row uma lista com dois componentes,
    Text e TextField.
"""
import flet as ft

def main(page: ft.Page):            
    page.title = "Sistema de cadastro"  
    page.theme_mode  = "light"        
    page.add(
        ft.Row(
            [
                ft.Text('Nome:', size=20),
                ft.TextField()
            ]
        )#Row
    )
            


ft.app(target=main)

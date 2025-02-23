"""
    V 1.0
    Esta versão cria a estrutura básica de uma interface em Flet.
    A função main tem o parâmetro page que gerencia todos os componentes visuais.
    No escopo da função estamos definindo o título a adicinando um componente de texto na página.
    Para rodar o programa, precisamos chamar a função app e passar a nossa função main como
    argumento.
"""
import flet as ft

def main(page: ft.Page):            
    page.title = "Sistema de cadastro"          
    page.add(ft.Text('Home', size=50))
            


ft.app(target=main)

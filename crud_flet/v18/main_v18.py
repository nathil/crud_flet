"""
    V 18.0
    Nesta versão criamos a tela atualizar e a inserimos no dicionário de telas do arquivo
    controle. Na tela atualizar, criamos a função init para inicializar a variável global
    usuario, bem como os campos de texto nome e telefone. Essa função init é chamada
    quando o se clica no IconButton atualizar da tabela. Ainda na tela
    atualizar, nós criamos a função atualizar. Ela é chamada quando se clica no botão
    atualizar da tela. No momento ela não faz nada!
"""
import flet as ft
import controle as con

def main(page: ft.Page):   
    con.init(page)         
    page.title = "Sistema de cadastro"           
    page.on_route_change = con.controle_de_rota  
    page.theme_mode  = "light"
    page.go('1')


ft.app(target=main)


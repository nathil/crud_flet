"""
    V 11.0
    Nesta versão nós criamos a barra de navegação utilizando o componente NavigationBar.
    Como a barra de navegação é utilizada nas duas telas (views), definimos uma função para
    reutilizar este componente. A função definida foi a barra_navegacao.
    Considerando a função barra_navegacao, passamos o seu retorno como argumento do parâmetro
    navigation_bar do componente View.
"""
import flet as ft

def main(p: ft.Page):  
    global page , telas
    page = p    
    telas = {
        '1': view1(),
        '2': view2()
    }
    page.title = "Sistema de cadastro"           
    page.on_route_change = controle_de_rota  
    page.theme_mode  = "light"
    page.go('1')


def controle_de_rota(route_event):
    page.views.clear()    
    page.views.append(telas[route_event.route])          
    page.update()


def view1():     
    return ft.View(
                "tela1",
                [                           
                    ft.Text('Tela 1', size=20)                    
                ],
                navigation_bar= barra_navegacao(),                    
            )

def view2():     
    return ft.View(
                "tela2",
                [                           
                    ft.Text('Tela 2', size=20)                    
                ],
                navigation_bar= barra_navegacao(),                    
            )

def barra_navegacao():
    return ft.NavigationBar(
                        destinations=[
                            ft.NavigationDestination(icon=ft.icons.SAVE, label="Cadastrar"),
                            ft.NavigationDestination(icon=ft.icons.SEARCH, label="Listar"),                            
                        ],
                        on_change= lambda e: page.go(str(e.control.selected_index+1))
            )#NavigationBar


ft.app(target=main)


import flet as ft
import controle as con
def view():     
    return ft.View(
                "tela2",
                [                           
                    ft.Text('Tela 2', size=20)                    
                ],
                navigation_bar=con.barra_navegacao()                    
            )

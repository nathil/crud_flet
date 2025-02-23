"""
    V 4.0
    Nesta versão, para alinhar os textos e os campos de texto, colocamos o componente Text dentro
    de um componente Container e definimos a sua largura em 150 pixels.
    Também inserimos mais um componente na lista passada como argumento para o componente Column.
    O componente inserido foi ElevatedButton.
"""
import flet as ft

componentes = {
    'nome': ft.Ref[ft.TextField](),
    'telefone': ft.Ref[ft.TextField](),
    'cpf': ft.Ref[ft.TextField](), 
    'endereco': ft.Ref[ft.TextField](),  
    'email' : ft.Ref[ft.TextField](),
    'sexo': ft.Ref[ft.RadioGroup](),
    'uf': ft.Ref[ft.Dropdown](),
}

def main(page: ft.Page):            
    page.title = "Sistema de cadastro"  
    page.theme_mode  = "light"        
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Nome:', size=20), width= 150),                      
                        ft.TextField(label='Nome', ref=componentes['nome'])
                    ]                    
                ),#Row
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Telefone:', size=20), width=150),
                        ft.TextField(label='Telefone', ref=componentes['telefone'])
                    ]
                ),#Row
                ft.Row(
                    [
                        ft.Container(content=ft.Text('CPF:', size=20), width=150),
                        ft.TextField(label='Cpf', ref=componentes['cpf'])
                    ]
                ),#Row
                
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Endereço:', size=20), width=150),
                        ft.TextField(label='Endereço', ref=componentes['endereco'], multiline=True)
                    ]
                ),#Row
                ft.Row(
                    [
                        ft.Container(content=ft.Text('Sexo:', size=20), width=150),
                        ft.RadioGroup(ref=componentes['sexo'],
                        content=ft.Row([
                            ft.Radio(value="1", label="M"),
                            ft.Radio(value="0", label="F"),
                                ]
                            )#Row
                        )#RadioGroup
                    ]
                ),#Row
                ft.Row(
                    [
                      ft.Container(content=ft.Text('E-mail', size=20), width=150),
                      ft.TextField(label='E-mail', ref=componentes['email'])
                    ]
                ),#Row
                ft.Row(
                    [
                      ft.Container(content=ft.Text('UF', size=20), width=150),
                      ft.Dropdown(ref=componentes['uf'], 
                            width=300,
                            label='UF',
                            options=[
                                ft.dropdown.Option("PA"),
                                ft.dropdown.Option("SP"),
                                ft.dropdown.Option("RJ"),
                                ft.dropdown.Option("MA"),
                                ft.dropdown.Option("RS"),
                            ],
                        )#Dropdown
                    ]
                ),#Row
                ft.ElevatedButton('Cadastrar', icon='save')                                                      
            ]
        )#Column
    )
            

ft.app(target=main)

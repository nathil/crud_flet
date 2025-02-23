import flet as ft
import controle as con

def view():     
    return ft.View(
                "tela1",
                [                           
                    ft.Column([
                        ft.Row([
                            ft.Container(content=ft.Text('Nome:', size=20), width=150),
                            ft.TextField(label='Nome')
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Telefone:', size=20), width=150),
                            ft.TextField(label='Telefone')
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('CPF:', size=20), width=150),
                            ft.TextField(label='Cpf')
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Endereço:', size=20), width=150),
                            ft.TextField(label='Endereço', multiline=True)
                        ]),#Row 
                        ft.Row([
                            ft.Container(content=ft.Text('E-mail:', size=20), width=150),
                            ft.TextField(label='E-mail')
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Sexo:', size=20), width=150),
                            ft.RadioGroup(
                                ft.Row([
                                    ft.Radio(value='1', label='M'),
                                    ft.Radio(value='2', label='F')
                                ])
                            )
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Uf:', size=20), width=150),
                            ft.Dropdown(
                                options=[
                                    ft.dropdown.Option('PA'),
                                    ft.dropdown.Option('SP'),
                                    ft.dropdown.Option('RJ'),
                                    ft.dropdown.Option('MA'),
                                    ft.dropdown.Option('RS')
                                ]
                            )
                        ])
                    ])                  
                ],
                navigation_bar=con.barra_navegacao()             
            )

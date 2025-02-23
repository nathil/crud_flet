import flet as ft
import controle as con

componentes = {        
        'tabela': ft.Ref[ft.DataTable](),       
        #add todos os compontens da tela aqui
    }

def view():     
    return ft.View(
                "tela2",
                [                           
                    ft.DataTable(
                            width=float('inf'),
                            ref=componentes['tabela'],                                                    
                            columns=[
                                ft.DataColumn(ft.Text("Nome")),
                                ft.DataColumn(ft.Text("Telefone")),                                                                                                
                            ],
                            #rows=[] são ser carregadas dinamicamente
                         ),                                                                         
                ],
                navigation_bar=con.barra_navegacao(),                    
            )


def atualizar_tabela():
    return [
            ft.DataRow(cells=preencher_linha_tabela(cadastro)) for cadastro in con.banco_de_dados
        ]


def preencher_linha_tabela(cadastro):
    return [
                ft.DataCell(ft.Text(cadastro['nome'])),
                ft.DataCell(ft.Text(cadastro['telefone']))                                                           
        ]

import flet as ft
from flet import (
    Page,
    colors
)


def main(page: ft.Page):
    
    #stile pagina
    page.bgcolor = colors.BLUE_GREY_200
    page.window_height = 600
    page.window_max_height = 900
    page.window_width = 600
    page.window_max_width = 900
    page.padding = 30

    username = ft.Ref[ft.TextField]()
    password = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        
        greetings.current.controls.append(
            ft.Text(f"Hello, {username.current.value}!")
        )
        username.current.value = ""
        password.current.value = ""
        page.update()
        username.current.focus()

    page.add(
        ft.TextField(ref=username, label="Username", autofocus=True),
        ft.TextField(
            ref=password, label="Password", password=True, can_reveal_password=True
        ),
        ft.ElevatedButton("Accedi", on_click=btn_click),
        ft.Column(ref=greetings),
    )

ft.app(target=main)
import flet as ft

def main(pagina):
    titulo = ft.Text("Forum Test", size=32, weight=ft.FontWeight.BOLD)

    def connectar_mensagem(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(connectar_mensagem)

    titulo_janela = ft.Text('Bem vindo ao Forum!')
    nome_usuario = ft.TextField(label="Informe seu nome...")

    def enviar_mensage(evento):
        texto = f'{nome_usuario.value}: {chat_mensagem.value}'
        pagina.pubsub.send_all(texto)
        chat_mensagem.value = ""
        pagina.update()

    chat_mensagem = ft.TextField(label='Digite sua mensagem...', on_submit=enviar_mensage, width=300)
    botao_enviar = ft.ElevatedButton('Enviar mensagem', on_click=enviar_mensage)
    chat = ft.Column()

    linha = ft.Row([chat_mensagem, botao_enviar])

    def entrar_chat(evento):
        pagina.controls.clear()
        janela.open = False
        pagina.add(chat)
        pagina.add(linha)
        entrou_chat = f"{nome_usuario.value}, entrou no chat"
        pagina.pubsub.send_all(entrou_chat)
        pagina.update()

    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)

    titulo_container = ft.Container(content=titulo, alignment=ft.alignment.center)
    botao_iniciar_container = ft.Container(content=botao_iniciar, alignment=ft.alignment.center)

    conteudo_centralizado = ft.Column(
        [titulo_container, botao_iniciar_container],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=pagina.height,
        width=pagina.width
    )

    pagina.add(conteudo_centralizado)

ft.app(target=main, view=ft.WEB_BROWSER, port=8081)
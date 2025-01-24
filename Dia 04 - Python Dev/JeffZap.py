import flet as ft

#função principal para executar o aplicativo
def main(pagina):
    # Titulo da aplicação
    titulo = ft.Text('JeffZap')

    def websocket_chat(mensagem):
        print('Chat', 'Olá, em que posso ajudar?') #Parei no 1:40:00

    def enviar_mensagem(event):
        nome_usuario = text_area.value
        texto_mensagem = envia_mensagem.value
        
        mensagem = ft.Text(f"{nome_usuario}: {texto_mensagem}")
        chat.controls.append(mensagem)
        envia_mensagem.value = '' # Limpa o campo de texto
        # resposta = 'Jeff: ' + mensagem
        # chat.append(ft.Text(resposta))
        # print('Chat', mensagem)
        pagina.update()

    envia_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    linha_enviar = ft.Row([envia_mensagem, botao_enviar]) # Cria uma linha com o campo de texto e o botão
    chat = ft.Column()

    def enter_chat(event):
        popup.open = False # Fecha o modal
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)
        pagina.add(linha_enviar)
        nome_usuario = text_area.value
        texto_mensagem = ft.Text(f'{nome_usuario} entrou no chat')
        chat.controls.append(texto_mensagem)
        pagina.update()
    
    # Criar pop-up
    titulo_popup = ft.Text('Bem vindo ao JeffZap')
    text_area = ft.TextField(label='Digite seu nome')
    botao_popup = ft.ElevatedButton('Entrar no Chat', on_click=enter_chat)
    popup = ft.AlertDialog(title= titulo_popup, content= text_area, actions= [botao_popup])

    # Abre o modal
    def open_dialog(event):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print('Chat', 'Olá, em que posso ajudar?')

    # Botão inicial
    botao = ft.ElevatedButton('Iniciar Chat', on_click=open_dialog)

    # Adiciona os elementos na página
    pagina.add(titulo)
    pagina.add(botao)
    



# Executa a aplicação
ft.app(main, view=ft.WEB_BROWSER)
# SMTP

import smtplib as sm
import email.message as mensagem
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from imap_tools import MailBox, AND
from senha_google import senha_temp_google
import os
from cores import *

def enviar_email():
    msg_send = mensagem.Message()
    msg_send["Subject"] = "Email enviado com Python 🐍" # Assunto
    msg_send["From"] = "lpp2@cesar.school" #Quem envia o e-mail (remetente)
    msg_send["To"] = "seuemaildestino@gmail.com" #Quem recebe o e-mail (destinatário)
    msg_send["Cc"] = "lpp2+copia@cesar.school" #Copia Visível
    msg_send["Bcc"] = "seuemailcopiaoculta@gmail.com" #Cópia Oculta

    link_img_flask_django = r"../img/flask django.jpg"
    link_img_kivy = r"../img/kivy.png"
    link__img_python_dashboards = r"../img/python dashboards.png"

    dict_fotos = {"fotos": 
    [
        link_img_flask_django, link_img_kivy, link__img_python_dashboards
    ]
    }

    tags_fotos = " ".join(f"<img src='{foto}' width='490' alt='{os.path.splitext(os.path.basename(foto))[0]}'>" for indice_foto, foto in enumerate(dict_fotos["fotos"]))

    corpo_email = f"""<p>Boa noite,</p>
    <p>Tudo bem? Esse é meu primeiro e-mail enviado automaticamente com Python, usando a
    biblioteca <b>smtplib</b>.</p>
    <p>Segue abaixo um preview de alguns projetos que venho desenvolvendo:</p>
    {tags_fotos}
    <p>Qualquer dúvida, estou à disposição.</p>
    <p>Att.,<br>Lucas Paguetti</p>"""

    corpo_email = corpo_email.encode("latin1")

    msg_send.add_header("Content-Type", "text/html")
    msg_send.set_payload(corpo_email.capitalize())

    servidor = sm.SMTP("smtp.gmail.com", 587) #timer
    servidor.starttls()
    servidor.login(msg_send["From"], f"{senha_temp_google}")
    servidor.send_message(msg_send)
    servidor.quit()
    print(f"{CinzaClaro}Email{Reset} {Verde}enviado{Reset}{CinzaClaro} com sucesso✅{Reset}")

def enviar_email_anexo():
    msg = MIMEMultipart()
    msg["Subject"] = "Email enviado com Python" # Assunto
    msg["From"] = "lpp2@cesar.school" #Quem envia o e-mail (remetente)
    msg["To"] = "seuemaildestino@gmail.com" #Quem recebe o e-mail (destinatário)
    msg["Cc"] = "lpp2+copia@cesar.school;outroemailcopia@hotmail.com" #Copia Visível
    msg["Bcc"] = "seuemailcopiaoculta@gmail.com" #Cópia Oculta

    link_imagem = r"../img/kivy.png"

    corpo_email = f"""<p>Boa tarde,</p>
    <p>Esse é meu primeiro email com Python usando smtplib</p>
    <p>Att., Lucas Paguetti</p>
    <img src='{link_imagem}' width='490' alt='{os.path.splitext(os.path.basename(link_imagem))[0:]}'>"""

    msg.attach(MIMEText(corpo_email, "html"))

    # anexar arquivos
    lista_arquivos = os.listdir("anexos")
    for indice_nome_arquivo, nome_arquivo in enumerate(lista_arquivos):
        with open(f"anexos/{nome_arquivo}", "rb") as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=nome_arquivo))

    servidor = sm.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(msg["From"], f"{senha_temp_google}")
    servidor.send_message(msg)
    servidor.quit()
    print(f"{CinzaClaro}Email{Reset} {Verde}enviado✅{Reset}")

# IMAP

def ler_infos_email():
    usuario = "lpp2@cesar.school"
    senha = senha_temp_google

    meu_email = MailBox("imap.gmail.com").login(usuario, senha)

    # ver as pastas do meu email disponíveis
    #for pasta in meu_email.folder.list():
    #   print(pasta)

    # meu_email.folder.set('[Gmail]/E-mails enviados')

    lista_emails = meu_email.fetch(AND(from_="emailremetente@gmail.com", 
                                       to="emaildestinatario@hotmail.com"))

    for indice_email, email in enumerate(lista_emails):
        if (len(email.attachments) > 0):
            print(f"Email {indice_email + 1}: {email.subject}")
            print(email.text)
            print(email.html)
            for indice_anexo, anexo in enumerate(email.attachments):
                print(f"{indice_email + 1}º Email, Anexo {indice_anexo + 1}: ", anexo.filename)

def ler_anexos_email():
    usuario = "lpp2@cesar.school"
    senha = senha_temp_google

    meu_email = MailBox("imap.gmail.com").login(usuario, senha)

    lista_emails = meu_email.fetch(AND(from_="emailremetente@gmail.com", to="emaildestinatario@hotmail.com"))

    for indice_email, email in enumerate(lista_emails):
        if len(email.attachments) > 0:
            print(email.subject)
            print(email.text)
            print(email.html)
            for indice_anexo, anexo in enumerate(email.attachments):
                with open(f"Email {indice_email+1} - {anexo.filename}", "wb") as arquivo:
                    arquivo.write(anexo.payload)
                print("Anexo:", anexo.filename)

funcoes_email = [enviar_email, enviar_email_anexo, ler_infos_email, ler_anexos_email]

for indice_funcao, funcao in enumerate(funcoes_email):
    if not (funcao()):
        pass
    else:
        funcao()
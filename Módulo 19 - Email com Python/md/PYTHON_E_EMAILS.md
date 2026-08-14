<h1 align="center">Python & E-mails<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="45" /></h1>

<img src="https://img.shields.io/badge/Jupyter-111827?style=flat-square&logo=jupyter&logoColor=F37626" height="28"/>
<img src="https://img.shields.io/badge/Python-111827?style=flat-square&logo=python&logoColor=3776AB" height="28"/>
<img src="https://img.shields.io/badge/smtplib-built--in-3776AB?style=for-the-badge&logo=python&logoColor=white" height="28" alt="smtplib"/>
<img src="https://img.shields.io/badge/Outlook-COM%20%2F%20win32com-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white" height="28" alt="Outlook"/>
<img src="https://img.shields.io/badge/APIs%20terceiras-SendGrid%20%7C%20SES%20%7C%20Mailgun-informational?style=for-the-badge" height="28" alt="Serviços terceiros"/>

<h2 align="left">🎯 O que este guia cobre: </h2>

Existem **3 caminhos principais** para automatizar o envio de e-mails com Python. Eles não são concorrentes diretos — cada um resolve um cenário diferente (máquina pessoal com Outlook instalado vs. servidor sem interface vs. aplicação que envia milhares de e-mails transacionais). Este guia resume quando usar cada um, as bibliotecas envolvidas e os pontos de atenção.

| # | Abordagem | Biblioteca principal | Precisa de app/cliente instalado? |
|---|---|---|---|
| 1️⃣ | **SMTP puro** | `smtplib` + `email` (built-in) | ❌ Não |
| 2️⃣ | **Outlook via COM** | `win32com.client` (pywin32) | ✅ Sim (Windows + Outlook) |
| 3️⃣ | **Serviços terceiros (API)** | SDK do provedor (ex.: `sendgrid`, `boto3`, `yagmail`) | ❌ Não (precisa de conta/API key) |

---

## 1️⃣ SMTP puro (`smtplib`)

<img src="https://img.shields.io/badge/M%C3%B3dulo-smtplib-3776AB?style=for-the-badge&logo=python&logoColor=white" height="26" alt="smtplib"/>
<img src="https://img.shields.io/badge/Protocolo-SMTP-orange?style=for-the-badge" height="26" alt="SMTP"/>
<img src="https://img.shields.io/badge/Plataforma-qualquer%20SO-success?style=for-the-badge" height="26" alt="Multiplataforma"/>

### O que é

`smtplib` é o módulo **nativo** do Python para falar diretamente com um servidor SMTP (o protocolo padrão de envio de e-mail). Funciona com Gmail, Outlook.com, Yahoo, servidores corporativos — qualquer provedor que exponha um servidor SMTP e credenciais de acesso. É montado à mão junto com o módulo `email` (que constrói a mensagem: assunto, corpo, anexos, HTML).

### Exemplo mínimo

```python
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg["From"] = "seu_email@gmail.com"
msg["To"] = "destinatario@email.com"
msg["Subject"] = "Relatório automático"
msg.attach(MIMEText("Segue o relatório em anexo.", "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as file_servidor:
    file_servidor.starttls()
    file_servidor.login("seu_email@gmail.com", "senha_de_app")
    file_servidor.send_message(msg)
```

### Quando usar?

| ✅ Vantagens | ⚠️ Cuidados |
|---|---|
| Funciona em **qualquer sistema operacional** (Windows, Linux, Mac) | Provedores como Gmail exigem **"senha de app"** (não a senha normal da conta) por segurança |
| Não depende de nenhum programa de e-mail instalado — ótimo para **servidores** | Configuração de porta/TLS varia por provedor (587 com STARTTLS, 465 com SSL, etc.) |
| Ideal para **automação em nuvem** (cron jobs, scripts agendados, servidores sem interface gráfica) | Envio em volume alto pode cair em spam ou esbarrar em limites diários do provedor |
| Controle total sobre a mensagem (HTML, anexos, múltiplos destinatários, CC/BCC) | Mais verboso — é preciso montar a mensagem "na mão" com `email.mime` |

---

## 2️⃣ Outlook via automação COM (`win32com`)

<img src="https://img.shields.io/badge/M%C3%B3dulo-pywin32-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white" height="26" alt="pywin32"/>
<img src="https://img.shields.io/badge/Protocolo-COM%20Automation-orange?style=for-the-badge" height="26" alt="COM"/>
<img src="https://img.shields.io/badge/Plataforma-Windows%20%2B%20Outlook-blue?style=for-the-badge&logo=windows&logoColor=white" height="26" alt="Windows"/>

### O que é

Em vez de falar com um servidor SMTP, essa abordagem **controla o próprio aplicativo Outlook** instalado na máquina, via automação COM (a mesma tecnologia usada para automatizar Excel/Word). O e-mail sai da conta que já está logada no Outlook, usando a caixa de saída normal do usuário.

### Exemplo mínimo

```python
import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application")
email = outlook.CreateItem(0) # 0 = e-mail
email.To = "destinatario@email.com"
email.Subject = "Relatório automático"
email.Body = "Segue o relatório em anexo."
email.Attachments.Add("C:/relatorios/relatorio.xlsx")
email.Send()
```

### Quando usar?

| ✅ Vantagens | ⚠️ Cuidados |
|---|---|
| **Não precisa de senha/API key** — usa a sessão já logada no Outlook | Só funciona no **Windows** com Outlook instalado e configurado |
| Simples para quem já automatiza Excel/Word com `win32com` no mesmo fluxo | Depende de o Outlook estar aberto/instalado na máquina que roda o script |
| E-mail sai da caixa "Itens Enviados" real do usuário — fácil de rastrear | Não serve para **servidores** ou execução headless (sem interface) |
| Ótimo para relatórios internos corporativos (o cenário mais comum do curso) | Se o Outlook pedir confirmação de segurança (popup), o script pode travar esperando clique manual |

## 3️⃣ Serviços terceiros / APIs de e-mail transacional

<img src="https://img.shields.io/badge/Servi%C3%A7os-SendGrid%20%7C%20Amazon%20SES%20%7C%20Mailgun-informational?style=for-the-badge" height="26" alt="Serviços"/>
<img src="https://img.shields.io/badge/Protocolo-REST%20API%20%2F%20SDK-orange?style=for-the-badge" height="26" alt="API"/>
<img src="https://img.shields.io/badge/Plataforma-qualquer%20SO-success?style=for-the-badge" height="26" alt="Multiplataforma"/>

### O que é?

Empresas especializadas em entrega de e-mail (**SendGrid**, **Amazon SES**, **Mailgun**, **Postmark**, entre outras) oferecem uma **API/SDK Python** própria. Em vez de lidar com SMTP na mão, você usa o pacote oficial do serviço (ex.: `sendgrid`, `boto3` para SES) ou wrappers que simplificam SMTP como o `yagmail`.

### Exemplo mínimo (SendGrid)

```python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

mensagem = Mail(
    from_email="seu_email@empresa.com",
    to_emails="destinatario@email.com",
    subject="Relatório automático",
    plain_text_content="Segue o relatório em anexo.",
)

sg = SendGridAPIClient("SUA_API_KEY")
sg.send(mensagem)
```

### Quando usar?

| ✅ Vantagens | ⚠️ Cuidados |
|---|---|
| Feito para **alto volume** (milhares/milhões de e-mails), com melhor entregabilidade | Exige **conta paga/plano** no provedor (a maioria tem free tier limitado) |
| Recursos extras prontos: métricas de abertura, templates, rastreamento de cliques, bounce/spam handling | Mais uma dependência externa (SDK) e uma **API key** para gerenciar com segurança |
| Não depende de servidor SMTP nem de Outlook instalado — funciona em qualquer nuvem/CI | Curva de configuração inicial maior (verificação de domínio, DNS/SPF/DKIM) |
| Ideal para **produtos** (SaaS, e-commerce) que enviam e-mail transacional para clientes | Overkill para scripts pessoais simples — SMTP puro resolve com menos fricção |

## 🔀 Qual escolher?

| Cenário 🖼️ | Melhor opção 🔑 |
|---|---|
| Script pessoal, roda no meu PC ou em qualquer nuvem | 1️⃣ **SMTP puro** |
| Relatório corporativo, PC Windows com Outlook já configurado | 2️⃣ **Outlook (COM)** |
| Envio em massa, produto/aplicação com muitos usuários | 3️⃣ **Serviço terceiro (API)** |
| Servidor Linux sem interface gráfica | 1️⃣ **SMTP puro** ou 3️⃣ **API** (nunca Outlook/COM) |

<p align="center">
<img src="https://img.shields.io/badge/M%C3%B3dulo-19%20Email%20com%20Python-3776AB?style=for-the-badge&logo=python&logoColor=blue" height="28" alt="Módulo 19 Email com Python"/>
</p>
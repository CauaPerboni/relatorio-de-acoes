import schedule
import yfinance as yf
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


remetente = "seu_email@gmail.com"
senha = "sua_senha_de_aplicativo"
destinatarios = ["destinatario1@gmail.com", "destinatario2@gmail.com"]


def obter_info_acao(acao):
    ticker = yf.Ticker(acao)
    info = ticker.history(period="1d")

    abertura = info['Open'].iloc[0]
    fechamento = info['Close'].iloc[0]
    maximo_dia = info['High'].iloc[0]
    minimo_dia = info['Low'].iloc[0]
    volume = info['Volume'].iloc[0]

    if abertura != 0:
        variacao_dia = ((fechamento - abertura) / abertura) * 100
    else:
        variacao_dia = None 

    media_movel_5d = ticker.history(period="5d")['Close'].mean()

    return {
        'ticker': acao,
        'abertura': abertura,
        'fechamento': fechamento,
        'maximo_dia': maximo_dia,
        'minimo_dia': minimo_dia,
        'volume': volume,
        'variacao_dia': variacao_dia,
        'media_movel_5d': media_movel_5d
    }


def enviar_email(conteudo_relatorio):
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = ", ".join(destinatarios)
    msg['Subject'] = "Relatório Diário de Ações"

    msg.attach(MIMEText(conteudo_relatorio, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.send_message(msg)

def gerar_relatorio():
    acoes = ["TSLA34.SA", "BBAS3.SA", "PETR4.SA"]
    relatorio = "Relatório Diário de Ações\n\n"

    for acao in acoes:
        info = obter_info_acao(acao)
        relatorio += f"Ticker: {info['ticker']}\n"
        relatorio += f"Abertura: R${info['abertura']:.2f}\n"
        relatorio += f"Fechamento: R${info['fechamento']:.2f}\n"
        relatorio += f"Máximo do dia: R${info['maximo_dia']:.2f}\n"
        relatorio += f"Mínimo do dia: R${info['minimo_dia']:.2f}\n"
        relatorio += f"Volume: {info['volume']}\n"
        
        variacao_dia = info['variacao_dia']
        if variacao_dia is not None:
            relatorio += f"Variação no dia: {variacao_dia:.2f}%\n"
        else:
            relatorio += "Variação no dia: Dados não disponíveis\n"
        
        relatorio += f"Média móvel de 5 dias: R${info['media_movel_5d']:.2f}\n"
        relatorio += "\n" 

    enviar_email(relatorio)
    print("Relatório enviado com sucesso.")

schedule.every().day.at("17:00").do(gerar_relatorio)

try:
    while True:
        schedule.run_pending()
        time.sleep(60) 
except KeyboardInterrupt:
    print("Execução do script interrompida pelo usuário.")


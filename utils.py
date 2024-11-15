import yfinance as yf
import pandas as pd

def obter_info_acao(acao):
    ticker = yf.Ticker(acao)
    historico = ticker.history(period="5d")

    if not historico.empty:
        ultimo_dado = historico.iloc[-1]
        abertura = ultimo_dado['Open'] if not pd.isna(ultimo_dado['Open']) else 0.0
        fechamento = ultimo_dado['Close'] if not pd.isna(ultimo_dado['Close']) else 0.0
        maximo_dia = ultimo_dado['High'] if not pd.isna(ultimo_dado['High']) else 0.0
        minimo_dia = ultimo_dado['Low'] if not pd.isna(ultimo_dado['Low']) else 0.0
        volume = ultimo_dado['Volume'] if not pd.isna(ultimo_dado['Volume']) else 0

        variacao_dia = ((fechamento - abertura) / abertura) * 100 if abertura > 0 else None

        media_movel_5d = historico['Close'].rolling(window=5).mean().iloc[-1] if len(historico) >= 5 else None

        return {
            "ticker": acao,
            "abertura": abertura,
            "fechamento": fechamento,
            "maximo_dia": maximo_dia,
            "minimo_dia": minimo_dia,
            "volume": volume,
            "variacao_dia": variacao_dia,
            "media_movel_5d": media_movel_5d
        }
    else:
        return {
            "ticker": acao,
            "abertura": None,
            "fechamento": None,
            "maximo_dia": None,
            "minimo_dia": None,
            "volume": None,
            "variacao_dia": None,
            "media_movel_5d": None
        }

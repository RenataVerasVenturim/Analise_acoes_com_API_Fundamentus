# instalar bibliotecas -> pip install pandas matplotlib statsmodels yfinance

#------------------------------------------ANÁLISE TÉCNICA------------------

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import yfinance as yf

df=fundamentus.get_resultado()

#filtrar para 6%>dy<40% , 0>vp <1 , 1>pl<20 , 0>p/vp<1, liq corrente>1 , roe>15%

filtro=df[(df.dy>0.06)&(df.dy<0.40)&(df.pl>1)&(df.pl<=20)&(df.pvp<=1)&(df.pvp>0)&(df.liqc>1)&(df.roe>0.15)]

papel = filtro.index.tolist()

for item in papel:
    # Construindo o ticker da ação
    ticker = yf.Ticker(item+'.SA')
    filtro2 = ticker.history(period='10y', interval='1mo')
    decomposicao = seasonal_decompose(filtro2['Close'], model='additive', period=30, extrapolate_trend=30)
    filtro2[['Close']].plot()

    
    plt.title(f'Gráficos de {item}')
    fig,(ax1,ax2,ax3,ax4)=plt.subplots(4,1, figsize=(12,8))
    decomposicao.observed.plot(ax=ax1)
    decomposicao.trend.plot(ax=ax2)
    decomposicao.seasonal.plot(ax=ax3)
    decomposicao.resid.plot(ax=ax4)
    plt.tight_layout()
    #gráfico de tendencia
    plt.title(f'Tendência de {item}')
    ax,fig=plt.subplots(figsize=(15,8))
    plt.plot(decomposicao.observed)
    
    plt.title(f'Médica móvel de {item}')
    plt.plot(decomposicao.trend)

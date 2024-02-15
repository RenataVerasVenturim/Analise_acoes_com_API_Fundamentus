#!pip install fundamentus
#-------------------------------------ANÁLISE FUNDAMENTALISTA--------------------------------------------------

#puxar indicadores fundamentalistas de todas as ações da b3 
import fundamentus
import pandas as pd

df=fundamentus.get_resultado()

#filtrar para 6%>dy<40% , 0>vp <1 , 1>pl<20 , 0>p/vp<1, liq corrente>1 , roe>15%

filtro=df[(df.dy>0.06)&(df.dy<0.40)&(df.pl>1)&(df.pl<=20)&(df.pvp<=1)&(df.pvp>0)&(df.liqc>1)&(df.roe>0.15)]

import matplotlib.pyplot as plt

# TODOS SETORES

plt.figure(figsize=(10,8))
filtro.sort_values('dy', inplace=True)
plt.bar(filtro.index, filtro.dy)
plt.title('DY das ações filtradas')

#SETOR FINANCEIRO
setorBancario = fundamentus.list_papel_setor(20)
df.query('index in @setorBancario')

filtrarBancario=df.query('index in @setorBancario')

BancarioFiltrado=filtrarBancario[(filtrarBancario.dy>0.06)&(filtrarBancario.dy<0.40)&(filtrarBancario.pl>1)&(filtrarBancario.pl<=20)&(filtrarBancario.pvp<=1)&(filtrarBancario.pvp>0)]

plt.figure(figsize=(10,8))
BancarioFiltrado.sort_values('dy', inplace=True)
plt.bar(BancarioFiltrado.index, BancarioFiltrado.dy)
plt.title('SETOR FINANCEIRO - DY das ações filtradas')

#SETOR SANEAMENTO

setorSaneamento = fundamentus.list_papel_setor(2)
df.query('index in @setorSaneamento')
filtrarSaneamento=df.query('index in @setorSaneamento')

SaneamentoFiltrado=filtrarSaneamento[(filtrarSaneamento.dy>0.06)&(filtrarSaneamento.dy<0.40)&(filtrarSaneamento.pl>1)&(filtrarSaneamento.pl<=20)&(filtrarSaneamento.pvp<=1.05)&(filtrarSaneamento.pvp>0)]

plt.figure(figsize=(10,8))
SaneamentoFiltrado.sort_values('dy', inplace=True)
plt.bar(SaneamentoFiltrado.index, SaneamentoFiltrado.dy)
plt.title('SETOR DE SANEAMENTO - DY das ações filtradas')

#SETOR SEGUROS
setorSeguros = fundamentus.list_papel_setor(31)

filtrarSeguros=df.query('index in @setorSeguros')

SegurosFiltrado=filtrarSeguros[(filtrarSeguros.dy>0)&(filtrarSeguros.dy<0.06)&(filtrarSeguros.pl>1)&(filtrarSeguros.pl<=40)&(filtrarSeguros.pvp<=1.00)&(filtrarSeguros.pvp>0)]

plt.figure(figsize=(10,8))
SegurosFiltrado.sort_values('dy', inplace=True)
plt.bar(SegurosFiltrado.index, SegurosFiltrado.dy)
plt.title('SETOR DE SEGUROS - DY das ações filtradas')

#SETOR ELÉTRICO
setorEletricas = fundamentus.list_papel_setor(14)

filtrarEletricas=df.query('index in @setorEletricas')

EletricasFiltrado=filtrarEletricas[(filtrarEletricas.dy>0.06)&(filtrarEletricas.dy<0.40)&(filtrarEletricas.pl>1)&(filtrarEletricas.pl<=40)&(filtrarEletricas.pvp<=1.00)&(filtrarEletricas.pvp>0)]

plt.figure(figsize=(10,8))
EletricasFiltrado.sort_values('dy', inplace=True)
plt.bar(EletricasFiltrado.index, EletricasFiltrado.dy)
plt.title('SETOR DE ELÉTRICAS - DY das ações filtradas')
plt.show()

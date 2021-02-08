from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
import pandas as pd
import os
import numpy as np

def home(request):
    return render(request, 'analise/index.html')

def infoDiaEstado(request):

    if(not request.POST.get('data')):
        return redirect('/')

    dataPesquisa = request.POST.get('data')
    
    dataObject = datetime.strptime(dataPesquisa, '%Y-%m-%d').date()
    ontem = dataObject - timedelta(1)
    ontem = ontem.strftime('%Y-%m-%d')

    situacaoDataEstado = infoDataEstado(dataPesquisa)
    situacaoEstadoOntem = infoDataEstado(ontem)

    situacaoFinal = situacaoDataEstado
    situacaoFinal['percPopCasos'] = (situacaoDataEstado['casosAcumulado'] / situacaoDataEstado['populacaoTCU2019']) * 100
    situacaoFinal['obitoAnterior'] = situacaoEstadoOntem['obitosAcumulado']
    situacaoFinal['percCaso'] = ((situacaoDataEstado['casosAcumulado'] - situacaoEstadoOntem['casosAcumulado'])/situacaoDataEstado['casosAcumulado']) * 100
    situacaoFinal['percObito'] = ((situacaoDataEstado['obitosAcumulado'] - situacaoEstadoOntem['obitosAcumulado'])/situacaoDataEstado['obitosAcumulado']) * 100
    situacaoFinal['novosObitos'] = (situacaoDataEstado['obitosAcumulado'] - situacaoEstadoOntem['obitosAcumulado'])
    situacaoFinal['novosCasos'] = (situacaoDataEstado['casosAcumulado'] - situacaoEstadoOntem['casosAcumulado'])
    situacaoFinal['casoAnterior'] = situacaoEstadoOntem['casosAcumulado']

    situacaoBrasil = infoDiaBrasil(dataPesquisa)

    rakinkgCasos = situacaoFinal.sort_values(by=['casosAcumulado'],  ascending=False)
    rakingObitos = situacaoFinal.sort_values(by=['obitosAcumulado'],  ascending=False)

    rakinkgCasos['posicao'] = np.arange(1,1+len(rakinkgCasos.casosAcumulado))
    rakingObitos['posicao'] = np.arange(1,1+len(rakingObitos.casosAcumulado))

    rakinkgCasos['corrCasos'] = ((rakinkgCasos['casosAcumulado']/  situacaoDataEstado['populacaoTCU2019']))
    rakingObitos['corrObitos'] = ((rakingObitos['obitosAcumulado'] / rakingObitos['populacaoTCU2019']))

    rakinkgCasosRelacao = rakinkgCasos.sort_values(by=['corrCasos'],  ascending=False)
    rakingObitosRelacao = rakingObitos.sort_values(by=['corrObitos'],  ascending=False)

    rakinkgCasosRelacao['posicao'] = np.arange(1,1+len(rakinkgCasos.casosAcumulado))
    rakingObitosRelacao['posicao'] = np.arange(1,1+len(rakinkgCasos.casosAcumulado))

    
    return render(request, 'analise/index2.html',{
        'infoEstados': situacaoFinal.to_dict('records'),
        'infoBrasil': situacaoBrasil.to_dict('records'),
        'rakingCasos': rakinkgCasos.to_dict('records'),
        'rakingObitos': rakingObitos.to_dict('records'), 
        'rakingCorrCasos' : rakinkgCasosRelacao.to_dict('records'),
        'rakingCorrObitos' : rakingObitosRelacao.to_dict('records'),
        'data' : dataPesquisa
    })

        


# Create your views here.

def infoDataEstado(data):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'dataset.csv')

    df = pd.read_csv(file_path , sep=";")

    df['data'] = pd.to_datetime(df['data'])

    dfFiltroDataInset = df[(df['data'] == data)]

    del df

    dfpopulacao = dfFiltroDataInset.drop_duplicates(['estado'])

    dfpopulacao = dfpopulacao[['estado', 'populacaoTCU2019']]

    dfFiltroDataInset = dfFiltroDataInset.groupby(['estado'],  as_index=False)[['casosAcumulado', 'obitosAcumulado']].apply(sum)

    dfFinal = pd.merge(dfFiltroDataInset, dfpopulacao, left_on='estado', right_on='estado')

    del dfFiltroDataInset

    del dfpopulacao

    return dfFinal


def infoDiaBrasil(dataPesquisa):
    
    dataObject = datetime.strptime(dataPesquisa, '%Y-%m-%d').date()

    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'dataset.csv')

    df = pd.read_csv(file_path , sep=";")
    df['data'] = pd.to_datetime(df['data'])
    dfFiltroDataInsetBrasil = df[(df['data'] == dataPesquisa) & (df['regiao'] == 'Brasil')]

    del df

    return dfFiltroDataInsetBrasil
    






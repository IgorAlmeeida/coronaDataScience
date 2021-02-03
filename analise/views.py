from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
import pandas as pd
import os

def home(request):
    return render(request, 'analise/index.html')

def infoDiaEstado(request):
    dataPesquisa = request.POST.get('data')
    
    dataObject = datetime.strptime(dataPesquisa, '%Y-%m-%d').date()
    ontem = dataObject - timedelta(1)
    ontem = ontem.strftime('%Y-%m-%d')

    situacaoDataEstado = infoDataEstado(dataPesquisa)
    situacaoEstadoOntem = infoDataEstado(ontem)

    situacaoFinal = situacaoDataEstado
    situacaoFinal['percPopCasos'] = (situacaoDataEstado['casosAcumulado'] / situacaoDataEstado['populacaoTCU2019']) * 100
    situacaoFinal['obitoAnterior'] = situacaoEstadoOntem['obitosAcumulado']
    situacaoFinal['percCaso'] = (situacaoDataEstado['casosAcumulado'] - situacaoEstadoOntem['casosAcumulado'])/situacaoDataEstado['casosAcumulado']
    situacaoFinal['percObito'] = (situacaoDataEstado['obitosAcumulado'] - situacaoEstadoOntem['obitosAcumulado'])/situacaoDataEstado['obitosAcumulado']
    situacaoFinal['novosObitos'] = (situacaoDataEstado['obitosAcumulado'] - situacaoEstadoOntem['obitosAcumulado'])
    situacaoFinal['novosCasos'] = (situacaoDataEstado['casosAcumulado'] - situacaoEstadoOntem['casosAcumulado'])
    situacaoFinal['casoAnterior'] = situacaoEstadoOntem['casosAcumulado']

    json = situacaoFinal.to_json(orient='records')
    json = [json]

    return HttpResponse(json)


# Create your views here.



def infoDataEstado(data):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'dataset.csv')

    df = pd.read_csv(file_path , sep=";")

    df['data'] = pd.to_datetime(df['data'])

    dfFiltroDataInset = df[(df['data'] == data)]

    dfpopulacao = dfFiltroDataInset.drop_duplicates(['estado'])

    dfpopulacao = dfpopulacao[['estado', 'populacaoTCU2019']]

    dfFiltroDataInset = dfFiltroDataInset.groupby(['estado'],  as_index=False)[['casosAcumulado', 'obitosAcumulado']].apply(sum)

    dfFinal = pd.merge(dfFiltroDataInset, dfpopulacao, left_on='estado', right_on='estado')

    return dfFinal


def infoDiaBrasil(request):
    dataPesquisa = request.POST.get('data')
    
    dataObject = datetime.strptime(dataPesquisa, '%Y-%m-%d').date()

    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'dataset.csv')

    df = pd.read_csv(file_path , sep=";")
    df['data'] = pd.to_datetime(df['data'])
    dfFiltroDataInsetBrasil = df[(df['data'] == dataPesquisa) & (df['regiao'] == 'Brasil')]

    json = dfFiltroDataInsetBrasil.to_json(orient='records')

    return HttpResponse(json)
    

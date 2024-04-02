from django.shortcuts import render
from inventario.models import Año2024, Año2023, Año2022, Año2021, Año2020
import plotly.express as px
import pandas as pd


def saludar5(request):
    carros5 = Año2020.objects.all()
    df = pd.DataFrame({
        "barrio": [obj.barrio5 for obj in carros5],
        "cantidad": [obj.cantidad5 for obj in carros5],
        "mes": [obj.mes5 for obj in carros5]
    }) 

    grafico = px.bar(df, x="barrio", y="cantidad", color="mes")

    mihtml5 = grafico.to_html(full_html=False)

    context = {
        "carros": carros5,
        "grafica5": mihtml5
    }
    return render(request, "inventario/index.html", context)

def saludar4(request):
    carros4 = Año2021.objects.all()
    df = pd.DataFrame({
        "barrio": [obj.barrio4 for obj in carros4],
        "cantidad": [obj.cantidad4 for obj in carros4],
        "mes": [obj.mes4 for obj in carros4]
    }) 

    grafico = px.bar(df, x="barrio", y="cantidad", color="mes")

    mihtml4 = grafico.to_html(full_html=False)

    context = {
        "carros": carros4,
        "grafica4": mihtml4
    }
    return render(request, "inventario/index.html", context)


def saludar3(request):
    carros3 = Año2022.objects.all()
    df = pd.DataFrame({
        "barrio": [obj.barrio3 for obj in carros3],
        "cantidad": [obj.cantidad3 for obj in carros3],
        "mes": [obj.mes3 for obj in carros3]
    }) 

    grafico = px.bar(df, x="barrio", y="cantidad", color="mes")

    mihtml3 = grafico.to_html(full_html=False)

    context = {
        "carros": carros3,
        "grafica3": mihtml3
    }
    return render(request, "inventario/index.html", context)

def saludar2(request): 
    carros2 = Año2023.objects.all()
    df = pd.DataFrame({
        "barrio": [obj.barrio2 for obj in carros2],
        "cantidad": [obj.cantidad2 for obj in carros2],
        "mes": [obj.mes2 for obj in carros2]
    }) 

    grafico = px.bar(df, x="barrio", y="cantidad", color="mes")

    mihtml2 = grafico.to_html(full_html=False)

    context = {
        "carros": carros2,
        "grafica2": mihtml2
    }
    return render(request, "inventario/index.html", context)


def saludar(request):

    carros = Año2024.objects.all()
    df = pd.DataFrame({
        "barrio": [Año2024.barrio for Año2024 in carros],
        "cantidad": [Año2024.cantidad for Año2024 in carros],
        "mes": [Año2024.mes for Año2024 in carros]
    }) 

    grafico = px.bar(df, x="barrio", y="cantidad", color="mes")

    mihtml1= grafico.to_html(full_html = False)


    context = {
        "nombre": "eddy",
        "carros": carros,
        "grafica1": mihtml1
    }
    return render(request, "inventario/index.html", context)


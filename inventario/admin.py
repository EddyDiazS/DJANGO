from django.contrib import admin
from inventario.models import Año2024, Año2023, Año2022, Año2021, Año2020


class InventarioAdmin(admin.ModelAdmin):
    list_display =["barrio", "cantidad", "mes"]
    list_filter = ["mes"]

admin.site.register(Año2024,InventarioAdmin)

class InventarioAdmin2(admin.ModelAdmin):
    list_display =["barrio2", "cantidad2", "mes2"]
    list_filter = ["mes2"]

admin.site.register(Año2023,InventarioAdmin2)

class InventarioAdmin3(admin.ModelAdmin):
    list_display =["barrio3", "cantidad3", "mes3"]
    list_filter = ["mes3"]

admin.site.register(Año2022,InventarioAdmin3)

class InventarioAdmin4(admin.ModelAdmin):
    list_display =["barrio4", "cantidad4", "mes4"]
    list_filter = ["mes4"]

admin.site.register(Año2021,InventarioAdmin4)

class InventarioAdmin5(admin.ModelAdmin):
    list_display =["barrio5", "cantidad5", "mes5"]
    list_filter = ["mes5"]

admin.site.register(Año2020,InventarioAdmin5)


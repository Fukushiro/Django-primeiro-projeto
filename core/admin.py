from django.contrib import admin

from .models import (
    Pessoa,
    Marca,
    Veiculo,
    Parametros,
    MovRotativo,
    Mensalista,
    MovMensalista)


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('id', 'checkin', 'checkout', 'pago',
                    'total', 'horas_total', 'veiculoShow')


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista)

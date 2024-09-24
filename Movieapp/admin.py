from django.contrib import admin
from .models import Filme, Sessao, Assento, Reserva, Produto

admin.site.register(Filme)
admin.site.register(Sessao)
admin.site.register(Assento)
admin.site.register(Reserva)
admin.site.register(Produto)


from django.contrib import admin
from .models import *
# Register your models here.

# class detCurso(admin.ModelAdmin):
#     list_display = ('id','titulo', 'descricao','data_inicio', 'data_termino')
#     list_display_links = ('id',)
#     search_fields = ('titulo',)
#
# class detStatusVaga(admin.ModelAdmin):
#     list_display = ('id','status')
#     list_display_links = ('id',)
#     search_fields = ('status',)
#
# class detCidade(admin.ModelAdmin):
#     list_display = ('id','nome')
#     list_display_links = ('id',)
#     search_fields = ('nome',)
#
# class detDinamica(admin.ModelAdmin):
#     list_display = ('id','titulo', 'descicao','duracao')
#     list_display_links = ('id',)
#     search_fields = ('titulo',)
#
# class detCandidato(admin.ModelAdmin):
#     list_display = ('id','nome', 'email','rg', 'cpf','cidade')
#     list_display_links = ('id',)
#     search_fields = ('nome',)

admin.site.register(Curso)
admin.site.register(StatusVaga)
admin.site.register(Dinamica)
admin.site.register(Cidade)
admin.site.register(Candidato)

admin.site.register(AprovacaoDinamica)
admin.site.register(StatusEntrevista)
admin.site.register(Entrevista)
admin.site.register(Vaga)
admin.site.register(VagaDinamica)
admin.site.register(AvaliacaoDinamica)
admin.site.register(RespostaDinamica)



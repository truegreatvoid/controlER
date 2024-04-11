from django.contrib import admin
from .models import Emitente, Destinatario, Produto, Nota, ItemNota, CentroDeCusto, Categoria, RateioNota

class ItemNotaInline(admin.TabularInline):
    model = ItemNota
    extra = 1

class RateioNotaInline(admin.TabularInline):
    model = RateioNota
    extra = 1

class NotaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'data_emissao', 'emitente', 'destinatario', 'natureza_operacao', 'status', 'categoria')
    inlines = [ItemNotaInline, RateioNotaInline]

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'quantidade', 'unidade', 'valor_unitario', 'valor_total', 'codigo', 'ncm_sh')

class EmitenteAdmin(admin.ModelAdmin):
    list_display = ('nome_razao_social', 'cnpj', 'inscricao_estadual', 'endereco')

class DestinatarioAdmin(admin.ModelAdmin):
    list_display = ('nome_razao_social', 'cpf_cnpj', 'endereco')

class CentroDeCustoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')

admin.site.register(Emitente, EmitenteAdmin)
admin.site.register(Destinatario, DestinatarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Nota, NotaAdmin)
admin.site.register(ItemNota)  # Se necessário, você pode criar uma configuração de admin específica
admin.site.register(CentroDeCusto, CentroDeCustoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(RateioNota)
from django.db import models

class Emitente(models.Model):
    nome_razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    inscricao_estadual = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome_razao_social

class Destinatario(models.Model):
    nome_razao_social = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=18)
    endereco = models.TextField()

    def __str__(self):
        return self.nome_razao_social

class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=20)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.CharField(max_length=100)
    ncm_sh = models.CharField(max_length=10)

    def __str__(self):
        return self.descricao

class Nota(models.Model):
    numero = models.CharField(max_length=20)
    serie = models.CharField(max_length=20, blank=True, null=True)
    data_emissao = models.DateField()
    data_operacao = models.DateField()
    chave_acesso = models.CharField(max_length=44, blank=True, null=True)
    natureza_operacao = models.CharField(max_length=255)
    emitente = models.ForeignKey(Emitente, on_delete=models.CASCADE, related_name='notas_emitidas')
    destinatario = models.ForeignKey(Destinatario, on_delete=models.CASCADE, related_name='notas_recebidas')
    produtos = models.ManyToManyField(Produto, through='ItemNota')
    cfop = models.CharField(max_length=4)
    informacoes_adicionais = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)  # Classifica a nota

    def __str__(self):
        return f'Nota {self.numero} - {self.emitente.nome_razao_social}'
        
class RateioNota(models.Model):
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE, related_name='rateios')
    centro_de_custo = models.ForeignKey('CentroDeCusto', on_delete=models.CASCADE, related_name='rateios')
    ratio = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do rateio para esse centro de custo

    def __str__(self):
        return f'{self.centro_de_custo.nome}: {self.valor}'

class ItemNota(models.Model):
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('nota', 'produto')

    def __str__(self):
        return f'{self.quantidade} x {self.produto.descricao} em Nota {self.nota.numero}'

class CentroDeCusto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)


    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  # Por exemplo: Despesa, Entrada, Saída

    def __str__(self):
        return self.nome

# Adicionando uma relação com Categoria no modelo Nota
Nota.categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

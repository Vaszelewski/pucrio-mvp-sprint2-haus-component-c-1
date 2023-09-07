from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Item(Base):
    __tablename__ = 'item'

    artista = Column(String(50))
    nomeDoItem = Column(String(100))
    formato = Column(String(50))
    anoLancamento = Column(Integer)
    pais = Column(String(50))
    notas = Column(String(140))
    valor = Column(Float)
    codigoBarras = Column((Integer),primary_key=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, artista: str, nomeDoItem: str, formato: str, anoLancamento:int, pais: str,
                 notas: str, valor:float, codigoBarras: int, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Item

        Arguments:
            artista: nome do artista.
            nomeItem: nome do item a ser cadastrado
            formato: formato do item
            anoLancamento: ano em que o item foi lançado
            pais: pais que o item foi lançado
            notas: notar e descrição do item
            valor: valor do item
            data_insercao: data de quando o item foi inserido à base
        """
        self.artista = artista
        self.nomeDoItem = nomeDoItem
        self.formato = formato
        self.anoLancamento = anoLancamento
        self.pais = pais
        self.notas = notas
        self.valor = valor
        self.codigoBarras = codigoBarras

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

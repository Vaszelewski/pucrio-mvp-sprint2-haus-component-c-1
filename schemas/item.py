from pydantic import BaseModel
from typing import List
from model.item import Item

class ItemSchema(BaseModel):
    """ Define como um novo item a ser inserido deve ser representado
    """
    artista: str = "Lady Gaga"
    nomeDoItem: str = "Born This Way"
    formato: str = "Vinil"
    anoLancamento: int = 2011
    pais: str = "Estados Unidos"
    notas: str = "Vinil padrão Duplo"
    valor: float = 300.00
    codigoBarras: int = 375289362651


class ItemBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do item.
    """
    codigoBarras: int = 375289362651


class ListagemItemsSchema(BaseModel):
    """ Define como uma listagem de items será retornada.
    """
    items:List[ItemSchema]


def apresenta_items(items: List[Item]):
    """ Retorna uma representação do item seguindo o schema definido em
        ItemViewSchema.
    """
    result = []
    for item in items:
        result.append({
            "artista": item.artista,
            "nomeDoItem": item.nomeDoItem,
            "formato": item.formato,
            "anoLancamento": item.anoLancamento,
            "pais": item.pais,
            "notas": item.notas,
            "valor": item.valor,
            "codigoBarras": item.codigoBarras,
        })
    return {"items": result}


class ItemViewSchema(BaseModel):
    """ Define como um item será retornado: item
    """
    artista: str = "Lady Gaga"
    nomeDoItem: str = "Born This Way"
    formato: str = "Vinil"
    anoLancamento: int = 2011
    pais: str = "Estados Unidos"
    notas: str = "Vinil padrão Duplo"
    valor: float = 300.00
    codigoBarras: int = 375289362651


class ItemDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    codigoBarras: int

def apresenta_item(item: Item):
    """ Retorna uma representação do item seguindo o schema definido em
        ItemViewSchema.
    """
    return {
        "artista": item.artista,
        "nomeDoItem": item.nomeDoItem,
        "formato": item.formato,
        "anoLancamento": item.anoLancamento,
        "pais": item.pais,
        "notas": item.notas,
        "valor": item.valor,
        "codigoBarras": item.codigoBarras,
    }

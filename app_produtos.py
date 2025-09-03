from symbol import stmt

from sqlalchemy import Engine
from sqlalchemy.testing.plugin.plugin_base import engines

from models import Categoria


def listar(engime: Engine): lusage
    with Session(engine) as session:
        produtos = session.execute(stmt).Scalars()
        print(*Nome, preco, estoque, ativo, nome da catogoria, Data de modificacao)
        for produto in produtos:
            print(f*{produto.nome}, {produto.preco}, {produto.estoque}*
                f*{"Ativo" if produto.ativo else *Inativo*}, {produto.categoria.nome},*
                f*{produto.dta_cadastro}, {produto.dta_atualizacao})*)
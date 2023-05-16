
from sqlalchemy import Table
from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, MetaData, Float, Integer,ForeignKey,DateTime, Boolean, String, Column
from datetime import datetime
from sqlalchemy.orm import relationship


from getjobs.pipelines import mssql_jobs

engine = mssql_jobs()
metadata = MetaData()
metadata_obj = MetaData(schema="dbo")


empresas = Table(
"empresas",
metadata,
Column('cod_venda',Integer, primary_key=True),
Column('empresa',String),
Column('data_coleta',DateTime)
,schema="dbo",extend_existing=True,implicit_returning=False)


jobs = Table(
"jobs",
metadata,
Column('id_empresa',Integer, primary_key=True),
Column('empresa',Integer),
Column('data_coleta',Integer),
Column('empresa',Integer),
Column('url_anuncio',Integer),
Column('vaga',Boolean),
Column('id_empresa',ForeignKey("empresas.id_empresa"), nullable=False),
Column('data_coleta', DateTime),
Column('anuncio_ativo', Boolean),
schema="dbo",extend_existing=True,implicit_returning=False)





import pyodbc
import mysql.connector

# Banco de dados local (Docker), só para acompanhar as aulas do módulo.
# Em um projeto real, esses dados nunca ficariam direto no código-fonte.

SQLSERVER_HOST = "localhost,1433"
SQLSERVER_USUARIO = "sa"
SQLSERVER_SENHA = "HashtagSql#2026"
SQLSERVER_BANCO_PADRAO = "HashtagCursoSQL"

MYSQL_HOST = "127.0.0.1"
MYSQL_PORTA = 3306
MYSQL_USUARIO = "root"
MYSQL_SENHA = "HashtagSql#2024"


def nova_conexao_sqlserver(banco=None, autocommit=False):
    string_conexao = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={SQLSERVER_HOST};"
        f"UID={SQLSERVER_USUARIO};"
        f"PWD={SQLSERVER_SENHA};"
        "TrustServerCertificate=yes;"
    )
    if (banco):
        string_conexao += f"DATABASE={banco};"
    return pyodbc.connect(string_conexao, autocommit=autocommit)


def nova_conexao_mysql(banco=None):
    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORTA,
        user=MYSQL_USUARIO,
        password=MYSQL_SENHA,
        database=banco,
    )
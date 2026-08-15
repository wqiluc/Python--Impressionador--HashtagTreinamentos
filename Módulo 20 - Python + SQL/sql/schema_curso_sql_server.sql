-- Referência das tabelas criadas ao longo do módulo (banco HashtagCursoSQL, SQL Server).
-- O próprio Python cria cada uma no notebook correspondente — este arquivo é só consulta rápida.

-- Notebook 136 (Create) / usada em 137-140 (Read, Read+pandas, Update, Delete)
CREATE TABLE dbo.Vendas (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Produto VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50) NOT NULL,
    Quantidade INT NOT NULL,
    ValorUnitario DECIMAL(10,2) NOT NULL,
    DataVenda DATE NOT NULL,
    Vendedor VARCHAR(100) NOT NULL
);

-- Notebook 141 (Exercício 1) — base maior, gerada para a análise de dados
CREATE TABLE dbo.VendasEmpresa (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Produto VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50) NOT NULL,
    Quantidade INT NOT NULL,
    ValorUnitario DECIMAL(10,2) NOT NULL,
    DataVenda DATE NOT NULL,
    Vendedor VARCHAR(100) NOT NULL
);

-- Notebook 144 (Exercício 2) — controle de estoque de insumos
CREATE TABLE dbo.Estoque (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Insumo VARCHAR(100) NOT NULL UNIQUE,
    Quantidade DECIMAL(10,2) NOT NULL,
    UnidadeMedida VARCHAR(20) NOT NULL,
    Categoria VARCHAR(50) NOT NULL,
    AtualizadoEm DATETIME NOT NULL DEFAULT GETDATE()
);

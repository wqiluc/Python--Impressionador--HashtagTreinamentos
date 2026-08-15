-- Gerado a partir dos modelos SQLAlchemy em python/modelos.py
-- (CreateTable(tabela).compile(engine)) — ninguém escreveu este SQL na mão,
-- ele é só a "prova" do que Base.metadata.create_all() executa por trás.

CREATE TABLE categorias (
	id INTEGER NOT NULL,
	nome VARCHAR(50) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (nome)
);

CREATE TABLE produtos (
	id INTEGER NOT NULL,
	nome VARCHAR(100) NOT NULL,
	preco NUMERIC(10, 2) NOT NULL,
	quantidade_estoque INTEGER NOT NULL,
	categoria_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(categoria_id) REFERENCES categorias (id)
);

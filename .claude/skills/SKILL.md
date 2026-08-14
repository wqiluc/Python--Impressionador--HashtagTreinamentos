# Mapa de módulos (subpastas)

Índice do conteúdo de cada módulo do curso, com as subpastas e o que cada uma guarda. Ver visão geral do repositório em [CLAUDE.md](CLAUDE.md).

## módulo 1 — Fundamentos / tipos de variáveis
- `.ipynb/` — tipos de variáveis (aulas 1-2), método `.format` (aula 3), f-string e conversão de tipo (aula 4), exercícios do módulo.
- `.python/` — mesmas aulas em `.py`, + `cores.py`.

## módulo 2 — Estrutura condicional (if)
- `.ipynb/` — aulas 5 a 13: `if`, `if`/`elif`/`else` (variações 2-6), exercícios de if (partes 1 e 2), exercícios do módulo.
- `.python/` — mesmas aulas em `.py`, + `cores.py`.
- `__pycache__/` — bytecode de `cores.py`.

## módulo 3 — Strings
- `.ipynb/` — aulas 14 a 21: índice e tamanho de string, índice negativo/fatiamento, operações e fórmulas de texto, formatação de números, exercícios (padrão e extras).
- `.python/` — mesmas aulas em `.py`, + `cores.py`.
- `__pycache__/` — bytecode de `cores.py`.

## módulo 4 — Listas
- `.ipynb/` — aulas 22 a 35: listas 01 a 12, cartilha de métodos de lista, exercícios de listas (partes 1 e 2), lista opcional.
- `.python/` — mesmas aulas em `.py`, + `cores.py`.
- `__pycache__/` — bytecode de `cores.py`.

## módulo 5 — Laço for
- `.ipynb/` — aulas 36 a 46: for 01-04, diferentes formas de `for`, exercícios de for (1 e 3), for 08/09/11, exercícios opcionais.
- `.python/` — só tem a aula 40 (Diferentes_for) em script, + `cores.py`.
- `__pycache__/` — bytecode de `cores.py`.

## módulo 6 — Laço while
- `.ipynb/` — aulas 47 a 50: while 01/02, exercício de while, estruturas de repetição (revisão for x while).
- `.python/` — só `cores.py` (sem versão `.py` das aulas).
- `__pycache__/` — bytecode de `cores.py`.

## módulo 7 — Tuplas
- `.ipynb/` — aulas 51 a 54: tuplas 01-03, exercícios de tupla.
- `.python/` — só `cores.py`.
- `__pycache__/` — bytecode de `cores.py`.

## módulo 8 — Dicionários
- `.ipynb/` — aulas 55 a 65: cartilha de métodos de dicionário, dicionário 01-04, exercícios (1), dicionário 06-08, exercícios (2), exercícios extras.
- `.python/` — versão em script só dos exercícios extras (aula 65), + `cores.py`.
- `__pycache__/` — bytecode de `cores.py`.

## módulo 9_bônus — Outras estruturas de dados
- `.ipynb/` — aulas 66 a 68: iterable, `range`, `set`, + cartilha especial de `set`.
- `.python/` — só `cores.py`.

## módulo 10 — Funções
- `.ipynb/` — aulas 69 a 85: function 01-17, exercícios de function (1, 2 e 3), cartilha especial de erros/exceções.
- `.python/` — scripts de exercícios aplicados: `71-bebidas.py`, `77.1-Stockout_Empresa.py`, `77.2-Clientes_Devedores_porCPF.py`, + `cores.py`.
- `__pycache__/` — bytecode de `cores.py`.

## módulo 11 — List comprehensions e funções em iteráveis (parte 1)
- `.ipynb/` — aulas 86 a 92: list comprehensions 01/02/04/06, exercícios (1, 2 e 3).
- `.python/` — só `cores.py`.
- `__pycache__/` — bytecode de `cores.py`.

## módulo 12 — Módulos/bibliotecas e datetime
- `.ipynb/` — aulas 93 a 100: módulos e bibliotecas (3 aulas + exercícios), datetime, fuso horário e formatação, exercícios de datetime, desafio de datetime.
- `.python/` — `__init__.py` (pasta tratada como pacote) + `cores.py`.
- `__pycache__/` — bytecode de `cores.py`.

## módulo 13 — Projeto de fundamentos
- `ipynb/` — aulas 101 a 105: revisão "o que falta aprender", exercício de fundamentos, analisador de texto, gerador de senhas, gerador de QR code; inclui `database.py` (dados mockados) e `tabela_funcionarios.xlsx` usados nos exercícios, + `img/`.
- `python/` — `database.py` (mesmos dados mockados em script).
- Observação: aqui as subpastas são `ipynb/` e `python/` (sem o ponto no nome), diferente dos módulos anteriores.

## módulo 14 — Iteráveis e lambda
- `ipynb/` — aulas 106 a 110: list comprehensions/functions em iteráveis (continuação, aplicando função em `sort`), lambda expressions 01-03 (incluindo uso de lambda como "construtor de funções").
- `python/` — só `__init__.py`.

## Módulo 15 - pandas
- `.ipynb/` — aulas 111 a 119: introdução ao pandas, pandas 03-06, pandas 08/09, exportar para CSV, ler CSV direto da internet.
- `.python/` — só `__init__.py`.
- `spec/` — datasets de apoio (base "Contoso"): `Clientes`, `Lojas`, `Produtos Cadastro Completo`, `Produtos Resumo`, `Promocoes`, `Vendas - 2017`, `Vendas Consolidado`, além de `Vendas Produtos.csv`.

## módulo extra_de_exércicios — Exercícios avulsos
- `.ipynb/` — 2 notebooks de exercícios extras.
- `.python/` — scripts avulsos, sem numeração de aula, várias versões (`v1`/`v2`/`v3`) do mesmo exercício conforme evolução da solução:
  - Listas: `1-extra-lista_v1/v2/v3.py`
  - Relatórios: `1-extra-relatório_v1/v2/v3.py`
  - Previsão: `1-extra-previsao.py`
  - Segmentação de clientes: `1-segmentacao_clientes_v1.py`, `_v2_segmentos_lista.py`, `_v3_funcoes.py`
  - Analisador de texto: `1-texto_analisador.py`
  - Regex: `2-contrato_usando_regix.py`, `2-email_usando_regix.py`, `2-regix_url_análise.py`
  - Conversões: `2-conversão_v1/v2/v3.py`
  - Terminal/CLI: `2-banco_de_dados_terminal.py`, `to-do-list_terminal.py`
  - Diversos: `2-cobrança_curso.py`, `2-data_empresa.py`, `2-moedas 1.0/2.0.py`, `2-notas.py`/`2.0.py`, `2-países.py`, `2-pibs.py`, `2-tarifas.py`, `2-validar_senha.py`
  - `cores.py`
- `__pycache__/` — bytecode de `cores.py` e `cores2.py`.
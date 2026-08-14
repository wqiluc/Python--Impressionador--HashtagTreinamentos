<h1 align="center">
  🤖 <span style="color:#306998;">CLAUDE.md</span> — <br>
  <span style="color:#FFD43B;">Python Impressionador</span> · Hashtag Treinamentos
</h1>

<p align="center">
  Instruções de contexto para o Claude Code trabalhar neste repositório de estudos.
  <br><br>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=black" width="75"/> <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=black" width="75"/>
</p>

## 📦 Sobre o repositório

Repositório de estudos do curso **Python Impressionador** (Hashtag Treinamentos). Contém as aulas e exercícios de cada módulo do curso, em Jupyter Notebook e em script Python puro. Visão geral e showcase completo em [README.md](../README.md).

## 📐 Convenções observadas

- Numeração de arquivo = número global da aula no curso, não reinicia a cada módulo.
- Nomes de arquivos e pastas em português, com acentos — preservar ao criar/mover arquivos.
- Cada módulo é independente: `cores.py` é duplicado em cada pasta em vez de compartilhado.
- A partir do módulo 15 não há um padrão fixo de "pasta com ponto vs. sem ponto" para `ipynb`/`python`/`spec` — cada módulo pode variar; sempre rode `ls -a` antes de assumir a estrutura de um módulo novo.
- Ambiente: `.venv/` local (Python 3.14), não versionado.

## ✅ Ao trabalhar neste repositório

- Este é um repositório de estudo/aprendizado, não uma aplicação em produção — priorize clareza didática sobre abstrações genéricas.
- Ao adicionar uma nova aula/exercício, siga o padrão existente do módulo (mesma dupla notebook + script, mesmo estilo de nome de arquivo, e confira se o módulo usa pastas com ou sem ponto antes de criar arquivos).
- Pastas `spec/` (ou `.spec/`) guardam arquivos de apoio aos exercícios (CSV, XLSX, PDF, DOCX, XML) — não são lixo/output, não deletar nem mover sem necessidade.
- Não é necessário rodar testes automatizados; para validar um script ou notebook, execute-o diretamente com Python/Jupyter.
- Siga o padrão de arquitetura dos `.ipynb` (shields.io, tabelas, ícones, emojis etc.), detalhando completamente o notebook para ficar com cara de Notion.
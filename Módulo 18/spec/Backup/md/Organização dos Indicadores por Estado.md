# 🗂️ Organização dos Indicadores por Estado

![Pathlib](https://img.shields.io/badge/pathlib-111827?style=flat-square&logo=python&logoColor=3776AB)
![Shutil](https://img.shields.io/badge/shutil-111827?style=flat-square&logo=python&logoColor=3776AB)
![Módulo](https://img.shields.io/badge/módulo-18-blue)
![Origem](https://img.shields.io/badge/gerado%20por-130--Python%20para%20Navegar%20no%20seu%20Computador-orange)

> Este documento registra o que aconteceu com a pasta `spec/` depois de rodar o notebook [`130-Python para Navegar no seu Computador - pathlib e shutil - Python e Arquivos do Computador 01.ipynb`](../ipynb/130-Python%20para%20Navegar%20no%20seu%20Computador%20-%20pathlib%20e%20shutil%20-%20Python%20e%20Arquivos%20do%20Computador%2001.ipynb) até o fim: a seção **9. Aplicando na Prática** e o **Desafio** deixaram artefatos novos dentro de `spec/`, e os 216 CSVs originais (soltos, um por loja/mês) foram removidos depois de organizados.

## 📦 `spec/Backup/` — artefato da seção 9 (Aplicando na Prática)

Gerado ao demonstrar, na prática, os métodos de pastas/arquivos vistos no notebook: criar pasta (`mkdir`), copiar (`shutil.copy2`) e mover (`Path.rename`).

| Caminho | Como foi criado | O que é |
|---|---|---|
| `spec/Backup/` | `pasta_backup.mkdir(exist_ok=True)` | pasta nova, criada só pra demonstração |
| `spec/Backup/201801_Ibirapuera_SP.csv` | `shutil.copy2(...)` | cópia do arquivo original da loja Ibirapuera (SP) — **não existe mais aqui**, veja a linha abaixo |
| `spec/Backup/Arquivados/201801_Ibirapuera_SP.csv` | `arquivo_copiado.rename(...)` | a mesma cópia acima, movida pra dentro de `Arquivados/` pra demonstrar o `.rename()` |

> ⚠️ **Atenção:** é só um exemplo didático — o arquivo aqui é uma cópia, não afeta a base original. Só existe pra mostrar `mkdir`, `copy2` e `rename` funcionando em cima de um arquivo real.

## 🗺️ `spec/Por_Estado/` — solução do Desafio

É a entrega do desafio proposto no notebook: separar os indicadores das 18 lojas em uma pasta por estado, uma pra cada Gerente Geral. Feito lendo a sigla do estado direto do nome do arquivo (`arquivo.stem.split('_')[-1]`) e copiando cada CSV pra `Por_Estado/<SIGLA>/`.

| Estado | Sigla | Lojas | Arquivos (12 meses × lojas) |
|---|---|---|---|
| Amazonas | `AM` | 1 | 12 |
| Goiás | `GO` | 2 | 24 |
| Minas Gerais | `MG` | 4 | 48 |
| Rio de Janeiro | `RJ` | 5 | 60 |
| São Paulo | `SP` | 6 | 72 |
| **Total** | | **18** | **216** |

Cada subpasta (`AM/`, `GO/`, `MG/`, `RJ/`, `SP/`) já pode ser enviada isoladamente pro respectivo Gerente Geral, com só os indicadores das lojas dele.

## 🗑️ Por que os CSVs originais foram removidos

A pasta `spec/` tinha, antes, 216 arquivos `.csv` soltos (um por loja/mês, ex.: `201801_Ibirapuera_SP.csv`) — a base "crua" usada pelo notebook pra praticar `pathlib`/`shutil`. Como o próprio objetivo do desafio era justamente reorganizar esses arquivos por estado, e `Por_Estado/` já guarda uma cópia de cada um dos 216, manter a versão solta e sem organização em paralelo virou duplicidade sem propósito — por isso foram apagados, restando só a versão organizada.

> ⚠️ **Atenção:** os arquivos originais continuam disponíveis no histórico do git (commit `367a06b`), caso seja necessário recuperá-los ou rodar o notebook do zero. Depois dessa limpeza, as células de código das seções **9 (Aplicando na Prática)** e **10 (Desafio)** do notebook 130 não são mais re-executáveis do início — elas liam os arquivos direto de `spec/*.csv`, que não existe mais nessa forma. Os outputs já salvos no notebook continuam valendo como registro do que foi executado.

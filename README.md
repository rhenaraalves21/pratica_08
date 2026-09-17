# Laboratório 8 — Documentação em Python

Projeto inicial para a aula de Engenharia de Software II sobre docstrings,
comentários e geração automática de documentação. Requer Python 3.10 ou mais
recente.

## Estrutura

- `src/financeiro.py`: três funções públicas e duas privadas, todas sem
  docstrings de propósito. A turma escreverá os contratos públicos.
- `exemplos/antipadroes.py`: comentários ruins para classificação e discussão.
- `docs/`: destino do HTML gerado pelo pdoc.
- `requirements.txt`: dependência da ferramenta de documentação.

## Preparação

Na raiz do projeto, crie um ambiente virtual e instale a dependência:

```bash
python -m venv .venv
```

No Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

No macOS ou Linux:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Atividades

1. Em `src/financeiro.py`, escreva docstrings no estilo Google para as três
   funções públicas. Inclua `Args`, `Returns`, `Raises` e, quando ajudar o
   leitor, `Examples`. Descreva as unidades, as condições de erro e o
   arredondamento efetivamente praticados pelo código.
2. Discuta o comentário sobre o desconto de Natal: qual decisão ele registra?
   O número da RFC é fictício e serve apenas ao exercício.
3. Em `exemplos/antipadroes.py`, classifique os quatro exemplos e proponha
   correções. O exemplo de `usuarios()` inclui um usuário inativo de propósito.
4. Gere e abra a documentação HTML:

   ```bash
   pdoc --output-dir docs/ src/financeiro.py
   ```

   Abra `docs/financeiro.html` no navegador. Compare o resultado antes e
   depois de escrever as docstrings.

## Perguntas para discussão

- A docstring permite usar uma função pública sem abrir seu corpo?
- Quais decisões internas merecem comentário? Quais comentários apenas
  repetem o código ou podem ficar desatualizados?
- O que o HTML gerado mostra quando uma função não tem docstring?
- Em que situação um projeto maior se beneficiaria de Sphinx?

O código inicial deixa a documentação pública incompleta intencionalmente:
o HTML final e as docstrings são entregas da atividade, não deste ZIP.

# pratica_08

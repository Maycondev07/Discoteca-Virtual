# 🎵 Discoteca Virtual

Um player de músicas para o terminal, escrito em Python com [pygame](https://www.pygame.org/). Ele lista automaticamente os arquivos `.mp3` de uma pasta, deixa você escolher qual ouvir digitando o nome e para a reprodução com um simples ENTER.

## ✨ Funcionalidades

- Lista todas as músicas disponíveis na pasta `music`, numeradas
- Toca a música escolhida pelo nome
- Para a música ao apertar **ENTER** e volta ao menu inicial
- Limpa o terminal automaticamente (Windows, Linux e macOS)
- Avisa quando a música digitada não é encontrada e pede novamente

## 📋 Requisitos

- Python 3.8 ou superior
- [pygame](https://pypi.org/project/pygame/)

## 🚀 Instalação

1. Clone ou baixe este repositório.
2. Instale a dependência:

```bash
pip install pygame
```

3. Crie uma pasta chamada `music` no mesmo diretório do script e coloque nela seus arquivos `.mp3`:

```
discoteca-virtual/
├── main.py
├── README.md
└── music/
    ├── minha musica.mp3
    ├── outra musica.mp3
    └── ...
```

## ▶️ Como usar

Execute o script:

```bash
python main.py
```

Você verá o menu com as músicas encontradas:

```
====================
Discoteca virtual
====================

Atualmente suas musicas são:
1 - minha musica
2 - outra musica
digite exatamente o nome da musica que gostaria de ouvir:
```

1. Digite **exatamente** o nome da música, sem a extensão `.mp3` (respeitando maiúsculas, minúsculas e acentos).
2. A música começa a tocar.
3. Aperte **ENTER** para parar e voltar ao menu.

## ⚙️ Como funciona

| Função     | O que faz                                                                                         |
|------------|---------------------------------------------------------------------------------------------------|
| `inicio()` | Mostra o título, lista os arquivos da pasta `music` e chama `tocar()`.                            |
| `tocar()`  | Pede o nome da música, carrega o `.mp3` com `pygame.mixer.music` e inicia a reprodução.           |
| `parar()`  | Interrompe a música, limpa o terminal e retorna ao menu (`inicio()`).                             |

A pasta `music` é localizada a partir do próprio arquivo do script (`__file__`), então o programa funciona de qualquer diretório em que seja executado.

## ⚠️ Limitações conhecidas

- O nome da música precisa ser digitado exatamente igual ao do arquivo.
- Só reconhece arquivos `.mp3`; outros arquivos na pasta aparecem na lista, mas não tocam.
- Não há opção de sair: para encerrar o programa, use `Ctrl + C`.
- O fluxo entre as funções usa chamadas recursivas, então sessões extremamente longas podem, em teoria, atingir o limite de recursão do Python.

## 💡 Ideias de melhoria

- Escolher a música pelo **número** da lista, em vez de digitar o nome
- Comandos de pausar/continuar e controle de volume
- Opção "Sair" no menu
- Filtrar apenas arquivos `.mp3` (e suportar `.wav`/`.ogg`)
- Substituir as chamadas recursivas por um laço `while True`
- Trocar o `except:` genérico por `except pygame.error` / `FileNotFoundError`

## 📄 Licença

Projeto de uso livre para estudo e aprendizado. Adapte como quiser!

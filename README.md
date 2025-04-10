# 🤖 Ricardin Inteligente

Um chatbot com IA generativa que responde perguntas com base em conteúdos da Wikipedia em português.  
Roda 100% online via [Hugging Face Spaces](https://huggingface.co/spaces) usando Gradio + API de inferência!

## ✨ Funcionalidades

- Pergunte qualquer coisa!
- A IA busca contexto automaticamente na Wikipedia
- Usa um modelo de linguagem da Hugging Face para gerar respostas inteligentes
- Interface leve e intuitiva feita com Gradio

---

## 🚀 Como funciona

1. O usuário faz uma pergunta.
2. O bot busca um trecho de até 1000 caracteres na Wikipedia.
3. Gera uma resposta com base nesse contexto usando IA generativa (via API Hugging Face).
4. Exibe a resposta ao usuário.

---

## 📦 Tecnologias usadas

- [Gradio](https://gradio.app/)
- [Wikipedia (python lib)](https://pypi.org/project/wikipedia/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- Modelo: `mistralai/Mistral-7B-Instruct-v0.1` *(ou outro de sua escolha)*

---

## 🔐 Como configurar seu Space no Hugging Face

1. Vá em **Settings > Secrets**
2. Adicione uma nova secret com seu token da Hugging Face:

| Name      | Value                        |
|-----------|------------------------------|
| `HF_TOKEN` | `hf_xxxxxxxxxxxxxxxxxxxxxxx` |

---

## 🧠 Exemplo de uso

> ❓ **Pergunta:** Quem descobriu o Brasil?  
> 💬 **Resposta:** Pedro Álvares Cabral descobriu o Brasil em 1500.

---

## 📁 Arquivos principais

- `app.py` → Código principal da aplicação
- `requirements.txt` → Dependências para rodar o projeto

---

## 👤 Autor

Desenvolvido por Raul com apoio do Ricardin 🧠

---

## 📸 Interface

![screenshot](https://via.placeholder.com/800x400?text=Ricardin+Chatbot+Preview)

---


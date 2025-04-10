import gradio as gr
import wikipedia
import requests
import os

# Define idioma da Wikipedia
wikipedia.set_lang("pt")

# Token vem das variáveis secretas do Hugging Face
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

# Função para gerar resposta
def gerar_resposta(prompt):
    response = requests.post(API_URL, headers=headers, json={
        "inputs": prompt,
        "parameters": {"max_new_tokens": 300}
    })
    if response.status_code == 200:
        resultado = response.json()
        return resultado[0]["generated_text"].replace(prompt, "").strip()
    else:
        return "Erro ao consultar a IA. Verifique o token e tente novamente."

# Função principal
def responder(pergunta):
    try:
        pagina = wikipedia.page(pergunta)
        contexto = pagina.content[:1000]
    except:
        contexto = (
            "Pedro Álvares Cabral descobriu o Brasil em 1500. "
            "Brasília é a capital do Brasil. A água ferve a 100 graus Celsius. "
            "A Terra gira em torno do Sol. O oxigênio é essencial para a respiração."
        )

    prompt = f"Responda com clareza e em português a seguinte pergunta com base neste contexto:\n\nContexto:\n{contexto}\n\nPergunta: {pergunta}\n\nResposta:"
    resposta = gerar_resposta(prompt)
    return resposta

# Interface Gradio
interface = gr.Interface(
    fn=responder,
    inputs="text",
    outputs="text",
    title="Ricardin Inteligente 🤖",
    description="Pergunte qualquer coisa. Ricardin responde com base na Wikipedia e IA!"
)

interface.launch()

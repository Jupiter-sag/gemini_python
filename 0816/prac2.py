import gradio as gr
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.5-flash"


def ask_gemini(question: str) -> str:
    if not question.strip():
        return "請輸入問題"
    interaction = client.interactions.create(
        model=MODEL,
        input=question,
    )
    return interaction.output_text


with gr.Blocks(title="Gemini 問答介面") as demo:
    gr.Markdown("# Gemini 問答介面\n輸入問題，讓 Gemini 幫你回答！")
    question = gr.Textbox(
        label="你的問題",
        placeholder="例如：天空為何是藍色的？",
        lines=3,
    )
    answer = gr.Textbox(label="Gemini 的回答", lines=10, interactive=False)
    button = gr.Button("送出", variant="primary")

    button.click(fn=ask_gemini, inputs=question, outputs=answer)
    question.submit(fn=ask_gemini, inputs=question, outputs=answer)


if __name__ == "__main__":
    demo.launch()

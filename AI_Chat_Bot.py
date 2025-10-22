import openai
import gradio as gr
import matplotlib
matplotlib.use('agg')

openai.api_key = "ENTER_YOUR_API_KEY_HERE"  #API Key kept hidden for security purpose

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"
prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly"
def openai_create(prompt):

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  return response.choices[0].text


def conversation_history(input, history):
  history = history or []
  s = list(sum(history, ()))
  s.append(input)
  inp = ' '.join(s)
  output = openai_create(inp)
  history.append((input, output))
  return history, history


Blocks = gr.Blocks()

with Blocks:
  chatbot = gr.Chatbot()
  message = gr.Textbox(placeholder=prompt)
  state = gr.State()
  submit = gr.Button("Submit")
  submit.click(conversation_history, inputs=[message, state], outputs=[chatbot, state])
  Blocks.launch(debug=True)


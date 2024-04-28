from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Form
from openai import OpenAI
import os

client = OpenAI(
	api_key=os.environ.get("OPENAI_API_KEY")
	)

class Widget(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle("Chat with LLM")
		self.past_messages = []
		self.llm_messages = [
			{"role": "system", "content": "You are a helpful assistant."}
		]
		self.llm_responses = []
		self.user_send_button.clicked.connect(self.display_text)

	def display_text(self):
		text = self.user_input.text()
		if text:
			user_text = "You: \n"+text+'\n'
			self.user_input.clear()
			self.past_messages.append(user_text)
			self.store_text(text)
			self.update_canvas()

	def update_canvas(self):
			messages = '\n'.join(self.past_messages)
			self.textEdit.setText(messages)

	def store_text(self, text):
		msg = {
			"role": "user",
			"content": text
		}
		self.llm_messages.append(msg)
		self.get_response(self.llm_messages)

	def get_response(self, user_input):
		response = client.chat.completions.create(
			model="gpt-3.5-turbo",
			messages=self.llm_messages
		)
		llm_generated_response = response.choices[0].message
		self.llm_messages.append(llm_generated_response)
		llm_text = "Bot: \n" + llm_generated_response.content + '\n'
		self.past_messages.append(llm_text)




import streamlit as st
import openai
#Exercise 1: Functions

def ex1():
	st.write("Hello World")

# Exercise 2 : Input , Output and Variables
def ex2():
	name = st.text_input("Enter your name")
	# only prints the Hello {name} if input box is not empty
	if name:
		st.write("Hello " + name)

def ch2():
	name = st.text_input("Enter your name")
	gender = st.selectbox("Enter your gender",("Male","Female"))
	age = st.text_input("State your Age")

	# only prints the Hello {name} if input box is not empty
	if name:
		st.write("Hello " + name)
	if gender:
		st.write(gender)
	if age:
		st.write(age)

#Exercise 3 : Logical Conditioning
def ex3(): 
	age = st.text_input("State your age", 18)
	#if else statement
	age = int(age)
	if age >= 21:
		st.write("You are an adult")
	else:
		st.write("You are not an adult")

def ch3(): 
	gender = st.selectbox("State your gender",("Male","Female"))
	age = st.text_input("State your age", 18)
	picture = st.camera_input("Take a photo")
	#if else statement
	age = int(age)
	if age >= 21:
		if gender == 'Male':
			st.write("You are an Male adult")
		else:
			st.write("You are Female adult")
	else:
		if gender == 'Male':
			st.write("You are a Young boy")
		else:
			st.write("You are a young girl")
	
	if picture:
		st.image(picture)

# Exercise 4 : Data and Loops 
def ex4():
	# Data list
	fruits = ["apple", "banana", "orange"]

	# Dictionary
	person = {"name": "John", "age": 30, "city": "New York"}

	# For loop to show list
	st.subheader("Fruits list:")
	for fruit in fruits:
		st.write(fruit)

	#for loop to show dictionary list
	st.subheader("Person dictionary:")
	for key, value in person.items():
		st.write(key + ": " + str(value))

def ch4(): 
	name = st.text_input("Enter your name")
	gender = st.selectbox("State your gender",("Male","Female"))
	age = st.text_input("State your age", 18)
	mydict = {}
	if name:
		mydict["name"]=name
	if gender:
		mydict["gender"]=gender
	if age:
		mydict["age"]=age
	
	st.subheader("Person dictionary:")
	for key, value in mydict.items():
		st.write(key + ": " + str(value))

#Exercise 5 : Chatbot UI
def ex5():
	st.title("My first chatbot")

	if "store_msg" not in st.session_state:
		st.session_state.store_msg = []

	prompt = st.chat_input("Say something")
	if prompt:
		st.write(f"User has sent the following prompt: {prompt}")
		st.session_state.store_msg.append(prompt)
		for message in st.session_state.store_msg:
			with st.chat_message("user"):
					st.write(message)
			with st.chat_message("assistant"):
				st.write("Hello human, what can I do for you?")

#Exercise 6 : Rule-based Echo Chatbot 
def ex6():
	st.title("Echo Bot")

	# Initialize chat history
	if "messages" not in st.session_state:
		st.session_state.messages = []

	# Display chat messages from history on app rerun
	for message in st.session_state.messages:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])

	# React to user input
	if prompt := st.chat_input("What is up?"):
		# Display user message in chat message container
		st.chat_message("user").markdown(prompt)
		# Add user message to chat history
		st.session_state.messages.append({"role": "user", "content": prompt})

		response = f"Echo: {prompt}"
		# Display assistant response in chat message container
		with st.chat_message("assistant"):
			st.markdown(response)
		# Add assistant response to chat history
		st.session_state.messages.append({"role": "assistant", "content": response})
def ch6():
	st.title("Rule based Bot")

	# Initialize chat history
	if "messages" not in st.session_state:
		st.session_state.messages = []

	# Display chat messages from history on app rerun
	for message in st.session_state.messages:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])

	# React to user input
	if prompt := st.chat_input("What is up?"):
		# Display user message in chat message container
		st.chat_message("user").markdown(prompt)
		# Add user message to chat history
		st.session_state.messages.append({"role": "user", "content": prompt})

		if prompt.startswith("Hello"):
			response = f"Hi, what can i help you?"
		
		elif prompt == "How old are you":
			response = f"Today is my birthday"

		elif prompt == "What is your name":
			response = f"My Name is LH, the AI bot"
		else:
			response = f"I do not understand"

			
		
		#response = f"Echo: {prompt}"
		# Display assistant response in chat message container
		with st.chat_message("assistant"):
			st.markdown(response)
		# Add assistant response to chat history
		st.session_state.messages.append({"role": "assistant", "content": response})

def ex8():
	st.title("Api Call")
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"

	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": "Tell me about Singapore in the 1970s in 50 words."},
		],
		temperature=0,
	)

	st.markdown("**This is the raw response:**") 
	st.write(response)
	st.markdown("**This is the extracted response:**")
	st.write(response["choices"][0]["message"]["content"].strip())
	s = str(response["usage"]["total_tokens"])
	st.markdown("**Total tokens used:**")
	st.write(s)

def ch8():
	st.title("AI Chatbot")
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"

	# Initialize chat history
	if "messages" not in st.session_state:
		st.session_state.messages = []

	# Display chat messages from history on app rerun
	for message in st.session_state.messages:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])

	# React to user input
	if prompt := st.chat_input("What is up?"):
		# Display user message in chat message container
		st.chat_message("user").markdown(prompt)
		# Add user message to chat history
		st.session_state.messages.append({"role": "user", "content": prompt})

		response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": prompt},
		],
		temperature=1,
		)
		if response:
			response = response["choices"][0]["message"]["content"].strip()
		#response = f"Echo: {prompt}"
		# Display assistant response in chat message container
		with st.chat_message("assistant"):
			st.markdown(response)
		# Add assistant response to chat history
		st.session_state.messages.append({"role": "assistant", "content": response})

#Exercise 9 : Building a ChatGPT-like clone with streaming responses
def ex9():
	st.title("ChatGPT-like clone")
	openai.api_key = st.secrets["openapi_key"]

	if "openai_model" not in st.session_state:
		st.session_state["openai_model"] = "gpt-3.5-turbo"

	if "msg" not in st.session_state:
		st.session_state.msg = []

	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		if prompt := st.chat_input("What is up?"):
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				for response in openai.ChatCompletion.create(
					model=st.session_state["openai_model"],
					messages=[
						{"role": m["role"], "content": m["content"]}
						for m in st.session_state.msg
					],
					stream=True,
				):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})

	except Exception as e:
		st.error(e)

def ch10():
	st.title("ChatGPT-like clone")
	openai.api_key = st.secrets["openapi_key"]

	if "openai_model" not in st.session_state:
		st.session_state["openai_model"] = "gpt-3.5-turbo"

	if "msg" not in st.session_state:
		st.session_state.msg = []

	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		if prompt := st.chat_input("What is up?"):
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				for response in openai.ChatCompletion.create(
					model=st.session_state["openai_model"],
					messages=[{"role":"system", "content":"Imagine you are teacher"}, {"role":"user", "content":prompt}],
					stream=True,
				):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})

	except Exception as e:
		st.error(e)

def main():
		ex9()

if __name__ == "__main__":
	main()

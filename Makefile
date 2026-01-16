install-ollama:
	curl -fsSL https://ollama.com/install.sh | sh

install-llama3:
	ollama pull llama3

check-llama3:
	ollama run llama3

install:
	pip install -r requirements.txt

compile:
	uv pip compile requirements.in -o requirements.txt

start: 
	python3 app/main.py


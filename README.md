# Writing Agent

The objective is to create a writing agent that can write detailed dissertation style long form pages. The intention is to change it to LangChain, LangGraph, and LangSmith to create a robust solution that can retrieve and use information from a RAG.


### Build Instructions (so far)
- Make a python env (recommended) `python -m venv your_venv_name` in the root directory.
- Start the python env (recommended) `source your_venv_name/bin/activate` (macOS\Linux)
	- For windows, `./ your_venv_name/bin/activate.sh`
- Install the requirements `pip install -r requirements.txt`
- Make a `.env` file in root directory, with:
```bash
OPENAI_API_KEY = "<--your--openai--api--key-->"
LANGCHAIN_API_KEY = "<--your--langchain--api--key-->"
```

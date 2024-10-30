# Writing Agent

The objective is to create a writing agent that can write detailed dissertation style long form pages using LangChain. However for the sake of getting started quick, I will be using fetch.ai's uagent framework. The intention is to change it to LangChain, LangGraph, and LangSmith to create a robust solution.


### Build Instructions (so far)
- The compatible version of python is 3.9.[<=4], install using `pyenv install 3.9.2` and then set the version locally by `pyenv local 3.9.2`
- Make a python env (recommended) `python -m venv your_venv_name` in the root directory.
- Start the python env (recommended) `source your_venv_name/bin/activate` (macOS\Linux)
	- For windows, `./ your_venv_name/bin/activate.sh`
- Install the requirements `pip install -r requirements.txt`

**Basically the QS from fetch.ai

- `poetry init -n && poetry shell`
- `poetry add uagents`

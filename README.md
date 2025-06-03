# Local LLM Assignment

This project demonstrates how to interact with a locally running Large Language Model (LLM) using [Ollama](https://ollama.com/). The script sends prompts to the LLM and prints the AI's responses.

## Requirements

- Python 3.7 or higher
- [Ollama](https://ollama.com/) installed and running locally
- The `llama3` model downloaded in Ollama
- The `ollama` Python package

## Installation

1. **Install Ollama**  
   Download and install Ollama from [https://ollama.com/download](https://ollama.com/download) for Windows.

2. **Download the llama3 Model**  
   Open PowerShell and run:

   ```powershell
   ollama run llama3
   ```

3. **Install Python Dependencies**  
   Install the `ollama` Python package:
   ```powershell
   pip install ollama
   ```

## Usage

1. Start the Ollama server (if not already running):

   ```powershell
   ollama serve
   ```

2. Run the script:

   ```powershell
   python ollama_prompt.py
   ```

3. Enter your prompt when prompted. The script will send your prompt to the local LLM and print the response.

## Example

```
Enter your prompt for the AI: Explain the concept of quantum entanglement in simple terms.
Prompt sent to AI: "Explain the concept of quantum entanglement in simple terms."

AI Response: Quantum entanglement is a phenomenon where two or more particles become linked, so that the state of one instantly influences the state of the other, no matter how far apart they are...
```

## Script Overview

- `ollama_prompt.py`:  
  Contains the logic to send a prompt to the local LLM using the `ollama` Python package and print the response.

## Troubleshooting

- If you see an error like `An error occurred: ...`, make sure:
  - Ollama is running (`ollama serve`)
  - The `llama3` model is downloaded (`ollama run llama3`)
  - The `ollama` Python package is installed

## License

This project is for educational purposes.

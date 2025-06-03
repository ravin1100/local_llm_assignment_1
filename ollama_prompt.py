import ollama

def run_local_llm_prompt(prompt_text):
    """
    Sends a prompt to a local LLM running via Ollama and prints the response.
    """
    try:
        # Print the prompt
        print(f"Prompt sent to AI: \"{prompt_text}\"")

        # Make the programmatic call to Ollama
        response = ollama.chat(model='llama3', messages=[
            {'role': 'user', 'content': prompt_text},
        ])

        # Print the AI's response
        print(f"\nAI Response: {response['message']['content']}")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure Ollama is running and the 'llama3' model is available.")
        print("You can download the model by running 'ollama run llama3' in your terminal.")

# if __name__ == "__main__":
#     my_prompt = "Explain the concept of quantum entanglement in simple terms."
#     run_local_llm_prompt(my_prompt)

if __name__ == "__main__":
    user_prompt = input("Enter your prompt for the AI: ")
    run_local_llm_prompt(user_prompt)

    # You can try another prompt:
    # another_prompt = "Write a short poem about a rainy day."
    # run_local_llm_prompt(another_prompt)
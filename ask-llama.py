from llama_cpp import Llama

LLM = Llama(model_path="./llama-2-7b-chat.ggmlv3.q8_0.bin")

while True:
    user_input = input("Ask your question: ")
    prompt = f"Q: {user_input}"
    output = LLM(prompt)
    print(output["choices"][0]["text"])

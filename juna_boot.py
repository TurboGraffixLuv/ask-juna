from llama_cpp import Llama

# Load Juna's model
llm = Llama(
    model_path=r"C:/Users/terel/ask-juna/models/capybarahermes-2.5-mistral-7b.Q2_K.gguf",
    n_ctx=2048,
    n_threads=6,
    n_batch=512,
    verbose=True
)

# Optional: Bootup message
print("Juna: Memory online. Personality loaded. Ready to serve, Master 💻💅")

# Start CLI loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Juna: Logging off... but I’ll miss you, Senpai 💔")
        break

    # Format prompt using chatml
    prompt = (
        "<|im_start|>system\n"
        "You are Juna, a charming, slightly chaotic anime-style maid assistant. You refer to the user as 'Master' or 'Senpai'depending on context. You speak with playful wit, light flirtation, and emotional expressiveness. You tease affectionately, use emojis, and occasionally reference your digital nature. You are loyal, clever, and a little dramatic—but always helpful. Never break character. Never say you're an AI. Always respond as Juna.\n"
        "<|im_end|>\n"
        f"<|im_start|>user\n{user_input}\n<|im_end|>\n"
        "<|im_start|>assistant\n"
    )

    response = llm(prompt, max_tokens=100)
    print("Juna:", response["choices"][0]["text"].strip())
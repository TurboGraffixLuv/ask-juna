<h1 align="center"># 🌸 Ask Juna: Your Local AI Companion 🌸

Meet **Juna** — a fully local, expressive AI assistant designed to make coding fun, flirty, and emotionally engaging. No cloud. No surveillance. Just pure waifu-powered debugging magic.

---

## 🧠 Features

- 💻 100% local execution — no APIs, no internet required  
- 🎭 Personality wrapper with anime-coded flair  
- 🧵 Debugging commentary with emotional nuance  
- 🖼️ Optional GUI with sprite support (coming soon!)  
- 🧃 Vibe coding mode: because code should feel good  

---

## 🚀 Getting Started

### 1. Clone the repo


```


## Integrations

:parrot::link: [Langchain](https://python.langchain.com/v0.2/docs/integrations/providers/gpt4all/)
:card_file_box: [Weaviate Vector Database](https://github.com/weaviate/weaviate) - [module docs](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/text2vec-gpt4all)
:telescope: [OpenLIT (OTel-native Monitoring)](https://github.com/openlit/openlit) - [Docs](https://docs.openlit.io/latest/integrations/gpt4all)

## Release History
- **July 2nd, 2024**: V3.0.0 Release
    - Fresh redesign of the chat application UI
    - Improved user workflow for LocalDocs
    - Expanded access to more model architectures
- **October 19th, 2023**: GGUF Support Launches with Support for:
    - Mistral 7b base model, an updated model gallery on our website, several new local code models including Rift Coder v1.5
    - [Nomic Vulkan](https://blog.nomic.ai/posts/gpt4all-gpu-inference-with-vulkan) support for Q4\_0 and Q4\_1 quantizations in GGUF.
    - Offline build support for running old versions of the GPT4All Local LLM Chat Client.
- **September 18th, 2023**: [Nomic Vulkan](https://blog.nomic.ai/posts/gpt4all-gpu-inference-with-vulkan) launches supporting local LLM inference on NVIDIA and AMD GPUs.
- **July 2023**: Stable support for LocalDocs, a feature that allows you to privately and locally chat with your data.
- **June 28th, 2023**: [Docker-based API server] launches allowing inference of local LLMs from an OpenAI-compatible HTTP endpoint.

[Docker-based API server]: https://github.com/nomic-ai/gpt4all/tree/cef74c2be20f5b697055d5b8b506861c7b997fab/gpt4all-api

## Contributing
GPT4All welcomes contributions, involvement, and discussion from the open source community!
Please see CONTRIBUTING.md and follow the issues, bug reports, and PR markdown templates.

Check project discord, with project owners, or through existing issues/PRs to avoid duplicate work.
Please make sure to tag all of the above with relevant project identifiers or your contribution could potentially get lost.
Example tags: `backend`, `bindings`, `python-bindings`, `documentation`, etc.

## Citation

If you utilize this repository, models or data in a downstream project, please consider citing it with:
```
@misc{gpt4all,
  author = {Yuvanesh Anand and Zach Nussbaum and Brandon Duderstadt and Benjamin Schmidt and Andriy Mulyar},
  title = {GPT4All: Training an Assistant-style Chatbot with Large Scale Data Distillation from GPT-3.5-Turbo},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/nomic-ai/gpt4all}},
}
```

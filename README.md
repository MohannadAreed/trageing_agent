# trageing_agent

This repository contains code examples for interacting with websites and extracting data using [LangChain](https://github.com/hwchase17/langchain) and large language models (LLMs).

## Example: Extract data with LangChain

The `examples/extract_with_langchain.py` script downloads the contents of a web page and uses an LLM to process the text. The script expects an OpenAI-compatible API key through the `OPENAI_API_KEY` environment variable.

### Requirements

- `requests`
- `beautifulsoup4`
- `langchain`
- `openai`

Install dependencies with pip:

```bash
pip install requests beautifulsoup4 langchain openai
```

### Usage

Set the target URL and the question you want the LLM to answer. Optionally, you can rely on the defaults shown below. Ensure `OPENAI_API_KEY` is set in your environment.

```bash
export OPENAI_API_KEY=your-openai-key
python examples/extract_with_langchain.py \
    # optional overrides
    # TARGET_URL="https://example.com" \
    # QUESTION="Summarize the main content of this page in one sentence."
```

The script fetches the web page, sends the text along with your question to the LLM, and prints the model's response.

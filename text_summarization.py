import streamlit as st
from sumy.parsers.plaintext import PlaintextParser  # convert text into processed document
from sumy.nlp.tokenizers import Tokenizer

from sumy.summarizers.lsa import LsaSummarizer  # mathematical approach
from sumy.summarizers.luhn import LuhnSummarizer  # ranking based on word frequency
from sumy.summarizers.lex_rank import LexRankSummarizer  # graph based (sentences)
from sumy.summarizers.text_rank import TextRankSummarizer  # graph based (words + sentences)


st.title("Text Summarization APP")
text = st.text_area("Enter text to summarize...", height=150)
model_name = st.selectbox(
    "Choose summarizer model",
    ["LsaSummarizer", "LuhnSummarizer", "LexRankSummarizer", "TextRankSummarizer"],
)
sen_count = st.slider(
    "Select number of sentences for summary", min_value=1, max_value=10, value=5
)


def summarize_text(text: str, model_name: str = "LsaSummarizer", sen_count: int = 5) -> str:
    """Return a summary of `text` using the selected Sumy summarizer."""
    if not text.strip():
        return ""

    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    if model_name == "LsaSummarizer":
        summarizer = LsaSummarizer()
    elif model_name == "LuhnSummarizer":
        summarizer = LuhnSummarizer()
    elif model_name == "LexRankSummarizer":
        summarizer = LexRankSummarizer()
    else:
        summarizer = TextRankSummarizer()

    summary_sentences = summarizer(parser.document, sen_count)
    return " ".join(str(sentence) for sentence in summary_sentences)


if st.button("Summarize"):
    if not text:
        st.warning("Please enter text to summarize.")
    else:
        try:
            summary_text = summarize_text(text, model_name, sen_count)
            if summary_text:
                st.subheader("Summarized Text")
                st.write(summary_text)
            else:
                st.info("No summary produced (input may be too short).")
        except Exception as e:
            st.error(f"Error during summarization: {e}")
# Music Summarizer | BART

 Youtube video summary, using local llm

Please note that due to limited resources, the usage capacity of the Music Summarizer is currently constrained. Additional resources are nedded to support increased usage :) . https://musicsummarizer.onrender.com/

In this task, i'll work on creating a simple youtube video summarizer using a free Huggingface BART transformer model and streamlit.

Video extracts key information from videos, saving time and effort. We'll be using Python and a Huggingface BART encoder-decoder model with the pipeline class and also qdrant for vectore storage database also locally.

The model I used was "sshleifer/distilbart-cnn-12-6"" but it is flexible to change and choose any other model from huggingface.co.

Features:

1)You can add a song  URL
2)once the song has been processed by the app, you can see a summary of the
song's lyrics
3)You can see a list of countries if they are mentioned mentioned in the song (or an empty string if no
countries are mentioned)
4)Local LLm
5)you can save in qdrant vector database







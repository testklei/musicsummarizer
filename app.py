import streamlit as st
from transc import get_transcript
from transformers import pipeline

# ----------------------------------------------------------------------------
# Set up the Streamlit app header
st.header("Video Summarizer 🎬")

# Input field for YouTube video link
full_yt = st.text_input("Enter video link", "")

# Button to trigger the summarization process
if st.button("Get song Summary"):
    # Extract video ID from the YouTube link
    video_id = full_yt.split("=")[1]
    
    # Get the transcript for the given video ID
    get_transcript(video_id)

    # Read the transcript from a file
    with open("ms_kitco.txt", "r") as f:
        tx = f.read()

    # Initialize the summarizer pipeline
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    
    # Summarize the first 1000 characters of the transcript
    x3 = summarizer(tx[:1000], max_length=230)

    # Extract the summary text from the summarization result
    res = x3[0]["summary_text"]

    # Display the summary in the Streamlit app
    st.write(res)

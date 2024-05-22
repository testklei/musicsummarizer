from youtube_transcript_api import YouTubeTranscriptApi  # Import the YouTubeTranscriptApi module

def get_transcript(video_id: str):
    """
    Function to get transcript and save the text values from each dict

    :param video_id: the full link of the video
    :type video_id: str
    """
    # Fetch the transcript for the given video ID
    ls = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Extract the text from each dictionary in the list and concatenate with a space
    tx = [d["text"] + " " for d in ls]
    
    # ----------------------------------------------------------------------------
    # Open a file named 'ms_kitco.txt' in write mode
    with open("ms_kitco.txt", "w") as f:
        # Write the concatenated transcript text to the file
        f.write("".join(tx))

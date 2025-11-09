import os
import difflib
from googleapiclient.discovery import build

API_KEY = "AIzaSyBkGjcj7P83le3HaTQo5BL9mkWKlnplpg0"  # ur key for YouTube Data API v3
youtube = build("youtube", "v3", developerKey=API_KEY)

def search_official_audio(query):
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=3,
        videoCategoryId="10"
    )
    response = request.execute()
    items = response.get("items", [])
    if not items:
        return None, "No results"

    # look 4 "Provided to YouTube by"
    for item in items:
        desc = item["snippet"]["description"].lower()
        if "provided to youtube by" in desc:
            video_id = item["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"

    # look 4 official Topic uploads
    for item in items:
        channel_title = item["snippet"]["channelTitle"].lower()
        if " - topic" in channel_title:
            video_id = item["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"

    #  fuzzy match on "official audio"
    for item in items:
        title = item["snippet"]["title"].lower()
        if "official audio" in title:
            video_id = item["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"

    # fuzzy title match fallback
    titles = [item["snippet"]["title"] for item in items]
    best_match = difflib.get_close_matches(query, titles, n=1, cutoff=0.5)
    if best_match:
        for item in items:
            if item["snippet"]["title"] == best_match[0]:
                video_id = item["id"]["videoId"]
                return f"https://www.youtube.com/watch?v={video_id}"

    return None

def process_song_list(file_path, output_path):
    with open(file_path, "r", encoding="utf-8") as f:
        songs = [line.strip() for line in f if line.strip()]

    results = []
    for song in songs:
        print(f"Searching: {song}")
        url = search_official_audio(song)
        if url:
            print(f"Found {song}")
            results.append(url)
        else:
            print(f"Unable to find {song}")
            results.append(f"Not found: {song}")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    print(f"\nProcessing complete. Saved URLs to {output_path}")

# Example usage
process_song_list("songs.txt", "youtube_urls.txt")


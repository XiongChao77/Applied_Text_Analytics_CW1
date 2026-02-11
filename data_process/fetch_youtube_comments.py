import os
import time
import pandas as pd
from googleapiclient.discovery import build

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.normpath(os.path.join(current_dir, "..", "data"))

def get_comments_for_video(youtube, video_id, max_comments=500):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText",
    )

    while request and len(comments) < max_comments:
        try:
            response = request.execute()
        except Exception as e:
            print(e)
            break

        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]
            #only top-level comments , reduce the noise
            comments.append({
                "video_id": video_id,
                "comment": comment.get("textDisplay"),
                "likes": comment.get("likeCount"),
                "published_at": comment.get("publishedAt"),
            })

        request = youtube.commentThreads().list_next(request, response)

    return comments


def main(input_csv=None, api_key=None, max_comments=500, output=None, sleep=1.0):
    df = pd.read_csv(input_csv, dtype=str)
    if "video_id" not in df.columns:
        raise SystemExit("Input CSV must contain a 'video_id' column")

    video_ids = df["video_id"].dropna().unique().tolist()

    youtube = build("youtube", "v3", developerKey=api_key)

    all_comments = []
    i = 0
    for vid in video_ids:
        print(f"Fetching comments for {vid} , counted {i} videos so far.")
        comments = get_comments_for_video(youtube, vid, max_comments=max_comments)
        all_comments.extend(comments)
        time.sleep(sleep)
        i += 1
        if len(all_comments) > 5000:
            print(f"Reached 5000 comments, stopping further fetch to avoid excessive API usage. {i} video used.")
            break

    out_df = pd.DataFrame(all_comments)
    os.makedirs(os.path.dirname(output), exist_ok=True) if os.path.dirname(output) else None
    out_df.to_csv(output, index=False, encoding="utf-8")
    print(f"Saved {len(out_df)} comments to {output}")

if __name__ == "__main__":
    COMPANY_NAME = "AMAZON".lower() #  AMAZON/MICROSOFT/GOOGLE
    API_KEY = "AIzaSyCXQAtU3J_UDEt2XtY0NC_XJXP4SvDIJso"
    video_csv_file = os.path.join(current_dir,'..', "data",f"{COMPANY_NAME.lower()}_videos_filtered.csv")
    output = os.path.join(data_dir, f"{COMPANY_NAME.lower()}_comments.csv")
    main(input_csv=video_csv_file, api_key=API_KEY, max_comments=500, output=output, sleep=0.5)

import requests
import csv
import os

current_working_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_working_dir,'..' ,"data")
os.makedirs(output_dir, exist_ok=True)

API_KEY = "AIzaSyCXQAtU3J_UDEt2XtY0NC_XJXP4SvDIJso"
COMPANY_NAME = "AMAZON".lower() #  AMAZON/MICROSOFT/GOOGLE
MaxResultsOnePage = 50
MaxPage = 2

SEARCH_KEYWORDS = [
    f"{COMPANY_NAME} employee experience",
    f"Working at {COMPANY_NAME} warehouse",
    f"{COMPANY_NAME} work culture review",
    f"{COMPANY_NAME} workplace conditions",
    f"Ex {COMPANY_NAME} employee interview",
    f"{COMPANY_NAME} warehouse working conditions",
    f"{COMPANY_NAME} job review experience"
]

#filter video by title
TITLE_FILTER_KEYWORDS = [
    "employee",
    "working",
    "work",
    "warehouse",
    "culture",
    "conditions",
    "experience",
    "quit"
]

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"


def is_relevant_title(title):
    title_lower = title.lower()

    if COMPANY_NAME.lower() not in title_lower:
        return False

    #filter out videos that are not likely to be about employee experience, e.g. news, product reviews, etc.
    if not any(word in title_lower for word in TITLE_FILTER_KEYWORDS):
        return False

    return True

def search_videos(query, max_pages):
    videos = []
    next_page_token = None

    for _ in range(max_pages):
        params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": MaxResultsOnePage,
            "order": "relevance",
            "key": API_KEY,
            "pageToken": next_page_token
        }

        response = requests.get(SEARCH_URL, params=params).json()

        if "error" in response:
            raise RuntimeError(f"YouTube API Error:{response["error"]}")

        for item in response.get("items", []):
            title = item["snippet"]["title"]

            if is_relevant_title(title):
                video_data = {
                    "video_id": item["id"]["videoId"],
                    "title": title,
                    "description": item["snippet"]["description"],
                    "published_at": item["snippet"]["publishedAt"]
                }
                videos.append(video_data)

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return videos

def fetch_video_ids():
    all_videos = []

    for keyword in SEARCH_KEYWORDS:
        print(f"Searching: {keyword}")
        results = search_videos(keyword, MaxPage)
        all_videos.extend(results)

    unique_videos = {video["video_id"]: video for video in all_videos}
    unique_videos = list(unique_videos.values())

    # save to CSV
    with open(os.path.join(output_dir,f"{COMPANY_NAME.lower()}_videos_filtered.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["video_id", "title", "description", "published_at"]
        )
        writer.writeheader()
        writer.writerows(unique_videos)

    print(f"Saved {len(unique_videos)} filtered videos.")

if __name__ == "__main__":
    fetch_video_ids()

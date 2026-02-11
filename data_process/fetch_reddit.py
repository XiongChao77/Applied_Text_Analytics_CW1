import praw
import pandas as pd

# ======  Reddit API configuration ======
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="F20AA-CW1-Employee-Analysis"
)

# ======  Parameters ======
subreddits = ["cscareerquestions", "antiwork", "jobs"]
company_keywords = ["google", "amazon", "microsoft"]
post_limit = 300     # post number for subreddit
comment_limit = 100  # comments for each post

data = []

# ======  Data fetch ======
for sub in subreddits:
    subreddit = reddit.subreddit(sub)
    for post in subreddit.hot(limit=post_limit):
        post.comments.replace_more(limit=0)
        for comment in post.comments[:comment_limit]:
            text = comment.body.lower()
            if any(keyword in text for keyword in company_keywords):
                data.append({
                    "subreddit": sub,
                    "post_title": post.title,
                    "comment": comment.body,
                    "score": comment.score
                })

# ======  save to CSV ======
df = pd.DataFrame(data)
df.to_csv("reddit_employee_comments.csv", index=False, encoding="utf-8")

print(f"Saved {len(df)} comments.")

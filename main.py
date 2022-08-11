import praw
import os

reddit = praw.Reddit(
  client_id = os.environ['client_id'],
  client_secret = os.environ['client_secret'],
  username = os.environ['username'],
  password = os.environ['password'],
  user_agent = ("AskDavinciBot v1.0 by u/AskDavinci")
)

subreddit = reddit.subreddit("AskReddit")

for comment in subreddit.stream.comments(skip_existing=True):
  print(comment.body)
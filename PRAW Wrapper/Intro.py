import praw 

reddit = praw.Reddit(client_id = "dwNA76dNq8sFQA" ,
                     client_secret= "IhY0WqPwdQXqxGG61l9EUnEJUno" ,
                     username = "madarahokage",
                     password = "dontguess",
                     user_agent = "prawv1")

subreddit = reddit.subreddit("gameofthrones")

hot_catalogue = subreddit.hot(limit=5)

for submission in hot_catalogue:
    if not submission.stickied:
       print("Title : {}, ups : {}, downs: {}".format(submission.title,
       	                                                 submission.ups,
                                                         submission.downs))
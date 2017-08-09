import praw 

reddit = praw.Reddit(client_id = "dwNA76dNq8sFQA" ,
                     client_secret= "IhY0WqPwdQXqxGG61l9EUnEJUno" ,
                     username = "madarahokage",
                     password = "dontguess",
                     user_agent = "prawv1")

subreddit = reddit.subreddit("python")

hot_catalogue = subreddit.hot(limit=4)

for submission in hot_catalogue:
    if not submission.stickied:
       print("Title : {}, ups : {}, downs: {}".format(submission.title,
       	                                                 submission.ups,
                                                         submission.downs))
       comments = submission.comments
       for comment in comments:
       	print(20*'-')
       	print(comment.body)
       	if len(comment.replies) > 0:
       		for reply in comment.replies:
       			print("REPLY: ",reply.body)

   
    	    
    	    
    	       
    		       



    
    
    	
    	


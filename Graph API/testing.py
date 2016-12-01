import facebook
import module
import json

my_token = module.get_token()

i = 0

graph = facebook.GraphAPI(access_token=my_token, version='2.7')

profile = graph.get_object("me")
print(profile)
likes = graph.get_connections("me", "likes")

page_ids = []

for i in range(0, len(likes['data'])):
    page_ids.append(likes['data'][i]['id'])

attachement = {
	'link' : 'http://www.lipsum.com/'
}
try:
	graph.put_wall_post(message="Hello",profile_id=page_ids[1])
	print("Sent Message")
except Exception as e:
	print(e)




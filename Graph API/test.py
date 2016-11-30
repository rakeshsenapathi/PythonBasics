import facebook
import module
token = module.get_token()
graph = facebook.GraphAPI(access_token= token ,version= '2.7')
profile = graph.get_object("me")
posts = graph.get_connections("me", "likes")

attachment = {
	'link': 'https://goo.gl/e4cqdp'
}
graph.put_wall_post("Makes sense",attachment)


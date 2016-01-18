from instagram.client import InstagramAPI

access_token = "access token goes here"
client_secret = "client secret goes here"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
print(api.media_comments(media_id))

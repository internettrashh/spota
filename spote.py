from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json



load_dotenv()
os.environ['CLIENT_ID'] = "09a400c1a0f74874b8b37c72980815b3"
os.environ['CLIENT_SECRET'] = "4572945c233447d99ec85abd18b0912c"

clid = os.getenv("CLIENT_ID")
clscrt = os.getenv("CLIENT_SECRET")  
#print(clid, clscrt)

def get_token():            #this function is responsible for encoding the client id and secret to the spotify auth server in order to get a refresh token.
    auth_string = clid + ":" + clscrt
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")


    url = "https://accounts.spotify.com/api/token"  #url for spotify auth service
    headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded" 
    }
    data =  {"grant_type":"client_credentials"}
    result =  post(url,headers=headers,data=data)
    json_result = json.loads(result.content)
    token = json_result[ "access_token" ]
    return token



def get_auth_headder(token):
    return{"Authorization": "bearer " + token}

# shady chat gpt fied code 
def get_user_top_tracks(token):
    headers = get_auth_headder(token)
    url = "https://api.spotify.com/v1/me/top/tracks"
    response = get(url, headers=headers)
    #top_tracks = json.loads(response.content)["items"]
    json_result = json.loads(response.content)

    top_tracks = json_result
    return top_tracks



token = get_token()
top = get_user_top_tracks(token)
print (top)
print(token)



 

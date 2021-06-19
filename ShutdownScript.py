import requests

Time = 5 #Seconds
url = "url" #Url here

KillScriptRequest = requests.post(f"{url}/KillScript?time={Time}&auth1=Key1", headers = {
  'auth2': "Key2"
})

if KillScriptRequest.text == "Worked":
  print("Script has been shut down")

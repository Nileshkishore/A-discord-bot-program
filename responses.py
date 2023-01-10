import requests
import json
from datetime import datetime,date

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

def handle_response(message) -> str:  
  msg = message.lower()
  if msg == 'hello':
    return "Hello"
  if msg=='hi':
    return "Hi!"

  if msg=="good morning":
    return "Good Morning"
  if msg=="good night":
    return "Good Night"
    
  if msg.startswith("inspire"):
    quote = get_quote()
    return quote

  if msg=="time":
    return datetime.now()
  if msg=='date':
    return date.today()
    
    
  return "bye"
    

import requests
  
def send_message(d):
    uid = d['username']
    pwd = d['password']
    msg = d['message']
    phone = d['send_to']
    url = 'https://site2sms.p.mashape.com/index.php'
    headers = { "X-Mashape-Key": "ErtPbuBuAqmshuJifa96cTgfxRiWp1c3MI9jsnfC2mlB5XaBDc"}
    payload = {'uid':uid,'pwd':pwd,'msg':msg,'phone':phone} 
    res = requests.get(url,headers = headers,params = payload)
    if res.status_code == 200:
      return True
    return False
      

inp = {'username':'','password':'','send_to':'','message':''}
for key in inp.keys():
  inp[key] = raw_input('Enter %s: '%(key))

if send_message(inp):
  print 'successfully sent the message'
else:
  print 'message delivery failed'
  

import pickle

Edit your custom data
d={'uid':'your_site2sms_phno','pwd':'your_site2sms_password','no':'target_phone_no'}

//We are pickling custom data here into a file
pickle.dump(d,open('smsdetail.pickle','w'))

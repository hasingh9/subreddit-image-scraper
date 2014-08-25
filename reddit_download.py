import requests
import sys
import json
import re

def download(sub):
	url="http://www.reddit.com/r/"+sub+".json"
	target=requests.get(url)
	print(target.status_code)
	if target.status_code!=200:
		print("Cannot connect")
		sys.exit()
	
	text=target.text
	data=json.loads(text)
	info=data['data']['children']
	temp=[i['data']['url'] for i in info]
	names=[i['data']['title'] for i in info]
	for i,elem in enumerate(names):
		#set name as per linux restrictions
		names[i]=re.sub(r'[^A-Za-z0123456789._-]',"",names[i]).replace(' ','_').strip('_')
	
	for en,i in enumerate(temp):
		if '.jpg' not in i:
			continue
		target=requests.get(i)
		if target.status_code!=200:
			print(status_code)
			sys.exit()
		title=names[temp.index(i)]
		with open(title+".jpg","wb") as handle:
			print("Downloading :  ",title,"  ",en+1,"\n")
			for chunk in target.iter_content(1024):
				handle.write(chunk)


if __name__ == "__main__":
	sub="earthporn"
	download(sub)

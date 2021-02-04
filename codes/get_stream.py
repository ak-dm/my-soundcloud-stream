import soundcloud
import datetime

client = soundcloud.Client(
    client_id="***",
    client_secret="***",
    redirect_uri='***'
)
user_list = client.get('/users/75602319/followings?linked_partitioning=true&page_size=50')

time = (datetime.datetime.now() - datetime.timedelta(hours=9,days=1)).time()
today = (datetime.datetime.now() - datetime.timedelta(hours=9,days=1)).date()

#today = today  - datetime.timedelta(days=1)

today_format = "{}/{:02}/{:02} {} +0000".format(today.year,today.month,today.day,str(time)[:8])
print(today_format)

f = open('index.html', 'w')
f.write("")
f.close()

while True:
	embed_list = []
	print(len(user_list.obj["collection"]))
	for user in user_list.obj["collection"]:
		track_list = client.get('/users/{}/tracks'.format(user['id']),limit=3)
		if len(track_list)>0:
			if track_list[0].obj["created_at"]>today_format:
				print(track_list[0].obj["permalink_url"])
				embed_info = '<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/{}&color=%23b5b5b5&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"></div>'.format(track_list[0].obj["id"])
				embed_list.append(embed_info)
	f = open('index.html', 'a')
	f.writelines(embed_list)
	f.close()
	if user_list.obj['next_href'] is None:
		break
	else:
		user_list = client.get(user_list.obj['next_href'])
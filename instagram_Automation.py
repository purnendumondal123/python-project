# from instabot import Bot
# bot=Bot()
# bot.login(username="purnendu.123",password="bapon123@")
# bot.follow('suparna_das_70')

from instagrapi import Client

cl = Client()
cl.login("purnendu.123", "bapon123@")

#+++++++ view your profile info ++++++++++ 
# profile = cl.account_info()
# print(profile.dict())

#+++++++ Flow any body in instagram +++++++++++
# user_id = cl.user_id_from_username("suparna_das_70")
# cl.user_follow(user_id)

#+++++++ Like a one post(image) in insta +++++++++++
# media_id = cl.media_id(cl.media_pk_from_url("https://www.instagram.com/p/DD5JlllB8kC/"))
# cl.media_like(media_id)

#+++++++ UnLike a one post(image) in insta +++++++++++
# media_id = cl.media_id(cl.media_pk_from_url("https://www.instagram.com/p/DD5JlllB8kC/"))
# cl.media_unlike(media_id)

#+++++++ direst sending the message ++++++++++ 
# user_id = cl.user_id_from_username("m_loser_rii")
# cl.direct_send("Hello i'm purnendu!", [user_id])

#++++++++++
import time
import random
post_urls = [
    "https://www.instagram.com/p/CzJovOuhsl5/",
    "https://www.instagram.com/p/DD5JlllB8kC/",
    "https://www.instagram.com/p/CzHMLZAya7l/",
]
for url in post_urls:
    try:
        media_pk = cl.media_pk_from_url(url)
        cl.media_unlike(media_pk)
        print(f"✅ Liked: {url}")
        # time.sleep(random.randint(5, 10))  # ৫-১০ সেকেন্ড delay: safe
    except Exception as e:
        print(f"❌ Failed: {url} | Reason: {e}")
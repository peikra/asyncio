import asyncio
import json
import time
import aiohttp


start = time.time()

async def fetch_post(session, url):
    async with session.get(url, ssl=False) as response:
        return await response.json()




async def fetch_all_posts():
    async with aiohttp.ClientSession() as session:
        urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 78)]
        tasks = [fetch_post(session, url) for url in urls]
        posts = await asyncio.gather(*tasks)


        with open('posts.json', 'w') as f:
            json.dump(posts, f, indent=4)



asyncio.run(fetch_all_posts())
end = time.time()
print(end-start)

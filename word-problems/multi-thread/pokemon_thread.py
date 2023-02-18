import aiohttp
import asyncio
import time

start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon["name"]


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 151):
            url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            tasks.append(asyncio.to_thread(asyncio.run(), get_pokemon(session, url)))
            # tasks.append(asyncio.create(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather()
        for pokemon in original_pokemon:
            print(pokemon)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

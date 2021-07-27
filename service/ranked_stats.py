import requests
import aiohttp

import config

from performance_measurement import measure_performance


@measure_performance
def get_ranked_data_with_requests_lib(summoner_id: str):
    try:
        summoner_data_url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_id}?api_key={config.api_key}'
        summoner_id = requests.get(summoner_data_url).json()["id"]
        ranked_stats_url = f'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={config.api_key}'
        ranked_stats = requests.get(ranked_stats_url)
        return ranked_stats.json()
    except KeyError:
        print("API key is probably invalid")


@measure_performance
async def get_ranked_data_with_aiohttp_lib(summoner_id: str):
    async with aiohttp.ClientSession() as session:
        summoner_data_url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_id}?api_key={config.api_key}'
        async with session.get(summoner_data_url) as summoner_data:
            summoner_data = await summoner_data.json()
            hidden_id = summoner_data['id']
            ranked_stats_url = f'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{hidden_id}?api_key={config.api_key}'
            async with session.get(ranked_stats_url) as ranked_stats:
                ranked_stats = await ranked_stats.json()
                print(ranked_stats)
                return ranked_stats

"""Coin observer with asyncio event loop."""

import asyncio
import datetime
import os

import aiohttp
import django
from django.conf import settings


async def get_coin_pairs(coin_pair_model):
    """Get coin pairs from db."""

    coin_pairs = {}
    '''Find default pair in db or create new.'''
    default_pair = settings.DEFAULT_COIN_PAIR
    base, target = default_pair.split('-')
    default_pair_exist = coin_pair_model.objects.filter(
        base=base, target=target).first()
    if not default_pair_exist:
        coin_pair_model.objects.create(base=base, target=target)

    '''Add all coin pairs from db.'''
    coin_pairs_from_db = coin_pair_model.objects.all()
    for cp in coin_pairs_from_db:
        coin_pairs[str(cp.id)] = cp.__str__()
    print('get_coin_pairs', coin_pairs)
    return coin_pairs


def save_ticker(coin_pair_id, result, ticker_model, coin_pair_model):
    """Save coin pair ticker to db."""
    try:
        coin_pair = coin_pair_model.objects.get(id=coin_pair_id)
        ticker_model.objects.create(
            coin_pair=coin_pair,
            price=result.get('price', ''),
            volume=result.get('volume', ''),
            change=result.get('change', ''),
        )
    except Exception as err:
        print(str(err))


async def fetch(session, url):
    async with session.get(url, ssl=False) as response:
        return await response.json()


async def main():
    """Run event loop."""

    await asyncio.sleep(30)  # wait for postgres
    django.setup()  # hook for work with django env
    from coin_rates.models import CoinPair, CoinPairTicker

    while True:
        coin_pairs = await get_coin_pairs(coin_pair_model=CoinPair)
        async with aiohttp.ClientSession() as session:
            await asyncio.sleep(10)
            for coin_pair_id, slug in coin_pairs.items():
                url = f"https://api.cryptonator.com/api/ticker/{slug}"
                r = await fetch(session, url)
                result = r.get('ticker', '')
                if result:
                    save_ticker(
                        coin_pair_id,
                        result,
                        ticker_model=CoinPairTicker,
                        coin_pair_model=CoinPair,
                    )
                if settings.DEBUG:
                    print(datetime.datetime.now(), result)


if __name__ == '__main__':
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "how_much_the_coin.settings")
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(main())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()

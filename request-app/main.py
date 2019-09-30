import requests
from yaml import load as yaml_load
from yaml import Loader
from pathlib import Path
from time import time
import asyncio


async def make_request(url):
    '''
    make the request
    '''
    res = requests.get(url)
    print(res.text)


async def make_requests(urls):
    '''
    create a "queue" of request processes and wait for a response from all of them
    '''
    # Async might be slightly off here, bit rusty

    gets = (make_request(url) for url in urls)
    asyncio.gather(*gets)



async def main():
    '''
    loads a list of urls from a yaml file, then starts async processes to make get requests
    to provided urls
    '''
    fp = Path('./urls.yml')
    if not fp.exists():
        print('No url.yml file!')
        return 1
    urls = yaml_load(fp.read_bytes(), Loader=Loader)
    await make_requests(urls)
    return 0


if __name__ == '__main__':
    '''
    this is where execution starts it you run python main.py in the directory
    get_event_loop gives us the context to run what we pass to "run_until_complete"
    '''
    l = asyncio.get_event_loop()
    start_time = time()
    l.run_until_complete(main())
    print(f'Time for requests: {time() - start_time}\n')

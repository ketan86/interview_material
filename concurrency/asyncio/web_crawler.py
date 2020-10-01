"""
From what we have learnt so far, asyncio is an excellent choice for blocking
operations. Usually, there are two kinds of blocking operations:

network I/O

disk I/O

Let's start with implementing a simple web crawler. A web crawler is a program
that systematically browses the world wide web, typically with the intent to
index it. For our purposes, we'll dumb down our crawler and limit its
capability to fetch the HTML for a list of URLs. The downloaded HTML is passed
onto a consumer which then performs the indexing but we'll not implement that
part.

The meat of the problem lies in asynchronously downloading the given URLs.
We'll be using the aiohttp module for asynchronous REST GET calls. If we were
to serially download the URLs, we'll unnecessarily be wasting CPU cycles as a
network request is usually the slowest form of I/O. Let's start with the serial
version of the code.

Serial Download:

In our example, we'll pass three URLs to be downloaded. The serial version of
the code uses the following snippet to make the network requests:

    # url is a string such as www.cnn.com
    html = urlopen(url)
    text = html.read()
The complete code appears in the code widget below. Run the code and observe
the total time taken to download the URLs in the output.
"""
import time
import requests

def get_urls_to_crawl():
    urls_list = list()
    urls_list.append('http://www.example.com/')
    urls_list.append('http://www.example.com/')
    urls_list.append('http://www.example.com/')
    urls_list.append('http://www.example.com/')
    urls_list.append('http://www.example.com/')
    urls_list.append('http://www.example.com/')
    urls_list.append('http://www.example.com/')
    urls_list.append('http://www.example.com/')
    urls_list.append('http://www.example.com/')
    
    return urls_list


if __name__ == "__main__":
    
    # urls_to_crawl = get_urls_to_crawl()
    # start = time.time()

    # for url in get_urls_to_crawl():
    #     html = requests.get(url).text

    # elapsed = time.time() - start
    # print("\n{} URLS downloaded in {:.2f}s".format(len(urls_to_crawl), elapsed))
    pass

"""
Asynchronous Download:

Next we'll code an asynchronous version of the crawler.
The snippet of code that does the actual download is shown below:
"""
import asyncio
import aiohttp
import time

async def crawl_url(url, session):
    response = await session.get(url)
    return await response.text()

async def crawl_urls(urls):
    session = aiohttp.ClientSession()
    work_to_do = list()

    for url in urls:
        task = asyncio.create_task(crawl_url(url, session))
        work_to_do.append(task)

    # resp = await asyncio.gather(*work_to_do)
    for t in work_to_do:
        print(await t)
    await session.close()

def main():
    t0 = time.time()
    urls_to_crawl = get_urls_to_crawl()
    asyncio.run(crawl_urls(urls_to_crawl))
    elapsed = time.time() - t0
    print("\n{} URLS downloaded in {:.2f}s".format(len(urls_to_crawl), elapsed))


if __name__ == '__main__':
    main()
 
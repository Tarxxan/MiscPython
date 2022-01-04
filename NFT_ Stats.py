import time
import discord
import requests


def import_proxies():
    # proxy_file = open("proxies.txt", "r", 1)
    proxy_list = []
    with open("proxies.txt") as file:
        for lines in file:
            lines = lines.replace('\n', '')
            temp = lines.split(':')
            proxies = {
                "http": 'http://' + temp[2] + ':' + temp[3] + '@' + temp[0] + ':' + temp[1] + '/',
                "https": 'https://' + temp[2] + ':' + temp[3] + '@' + temp[0] + ':' + temp[1] + '/'}
            proxy_list.append(proxies)
    return proxy_list


def import_openseas_collection():
    with open("openseas.txt") as file:
        openseas_collection = []
        for lines in file:
            lines = lines.replace('\n', '')
            openseas_collection.append(lines)
    return openseas_collection


def call_api(proxy, opensea):
    headers = {"Accept": "application/json"}
    # curr_time = int(time.time())
    for link in opensea:
        r = requests.get(link, headers=headers, proxies=proxy)
        r = r.json()
        for i in range(100):
            # Print name of each sold NFT
            nft_name = (r['asset_events'][i]['asset']['name'])
            nft_image = (r['asset_events'][i]['asset']['image_url'])
            nft_token_id = (r['asset_events'][i]['asset']['token_id'])
            nft_contract_address = (r['asset_events'][i]['asset']['asset_contract']['address'])
            r2 = requests.get("https://api.opensea.io/api/v1/asset/" + nft_contract_address + '/' + nft_token_id + "/",
                              headers=headers, proxies=proxy)
            r2 = r2.json()
            nft_floor_price = (r2['collection']['stats']['floor_price'])


def main():
    finished_time = int(time.time() - 86400)
    proxy_list = import_proxies()
    opensea = import_openseas_collection()
    while True:
        for proxy in proxy_list:
            call_api(proxy, opensea)
            time.sleep(30)
            # finished_time = int(time.time())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

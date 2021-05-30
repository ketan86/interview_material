"""
The people who buy ads on our network don't have enough data about how ads are
working for their business. They've asked us to find out which ads produce the
most purchases on their website.

Our client provided us with a list of user IDs of customers who bought something
on a landing page after clicking one of their ads:

Each user completed 1 purchase. 

completed_purchase_user_ids = [
"3123122444","234111110", "8321125440", "99911063"]


And our ops team provided us with some raw log data from our ad server showing
every time a user clicked on one of our ads:

ad_clicks = [
#"IP_Address,Time,Ad_Text",
"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
"122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

The client also sent over the IP addresses of all their users.

all_user_ips = [
#"User_ID,IP_Address",
"2339985511,122.121.0.155",
"234111110,122.121.0.1",
"3123122444,92.130.6.145",
"39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
"8321125440,82.1.106.8",
"99911063,92.130.6.144"
]

Write a function to parse this data, determine how many times each ad was
clicked, then return the ad text, that ad's number of clicks, and how many of
those ad clicks were from users who made a purchase.


Expected output:

1 of 2 2017 Pet Mittens
0 of 1 The Best Hollywood Coats
3 of 4 Buy wool coats for your pets

purchases: number of purchase IDs
clicks: number of ad clicks
ips: number of IP addresses

"""
from collections import defaultdict


def find_ad_stats(user_ids, ad_clicks, all_user_ips):

    # item to ip address map
    item_ip_map = defaultdict(list)
    for ad_click in ad_clicks:
        ip, _, item = ad_click.split(',')
        item_ip_map[item].append(ip)

    # ip to userid map
    user_ip_map = {}
    for item in all_user_ips:
        user_id, ip = item.split(',')
        user_ip_map[ip] = user_id

    result = []
    # iterate over item<->ip map
    for item, ips in item_ip_map.items():
        # consider all clicks that are coming from all ip addresses regardless
        # of ip being present in userid<->ip map.
        clicks = len(ips)
        # find purchase
        purchases = 0
        # loop over all ips
        for ip in ips:
            # if ip in user_ip_map and that user id is in list of users who
            # purchased, increment the purchase count.
            if ip in user_ip_map and user_ip_map[ip] in user_ids:
                purchases += 1

        # append result
        result.append(f'{purchases} of {clicks} {item}')

    return result


user_ids = [
    "3123122444", "234111110", "8321125440", "99911063"]

ad_clicks = [
    # "IP_Address,Time,Ad_Text",
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
    # "User_ID,IP_Address",
    "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]


print(find_ad_stats(user_ids, ad_clicks, all_user_ips))

"""
************* Variation **************
different user clicks using the same ip address : use ip -> user_id list
"""

user_ids = [
    "3123122444", "234111110", "8321125440", "99911063", "2339985512"]

ad_clicks = [
    # "IP_Address,Time,Ad_Text",
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
    "122.121.0.155,2017-01-01 03:18:55,2017 Pet Mittens",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
    # "User_ID,IP_Address",
    "2339985511,122.121.0.155",
    "2339985512,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]


def find_ad_stats(user_ids, ad_clicks, all_user_ips):

    # item to ip address map
    item_ip_map = defaultdict(list)
    for ad_click in ad_clicks:
        ip, _, item = ad_click.split(',')
        item_ip_map[item].append(ip)

    # ip to userid map
    user_ip_map = defaultdict(list)
    for item in all_user_ips:
        user_id, ip = item.split(',')
        user_ip_map[ip].append(user_id)

    result = []
    # iterate over item<->ip map
    for item, ips in item_ip_map.items():
        # consider all clicks that are coming from all ip addresses regardless
        # of ip being present in userid<->ip map.
        clicks = len(ips)
        # find purchase
        purchases = 0
        # loop over all ips
        for ip in ips:
            # if ip in user_ip_map and that user id is in list of users who
            # purchased, increment the purchase count.
            if ip in user_ip_map:
                for user_id in user_ip_map[ip]:
                    if user_id in user_ids:
                        purchases += 1

        # append result
        result.append(f'{purchases} of {clicks} {item}')

    return result


print(find_ad_stats(user_ids, ad_clicks, all_user_ips))

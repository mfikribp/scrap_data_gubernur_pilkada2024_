import pandas as pd
import requests
import json
from libs import lib_pilkada as lp
from time import sleep
import random


headers = {
    'authority':'sirekappilkada-obj-data.kpu.go.id',
    'method':'GET',
    'path':'/pilkada/hhcw/pkwkk/32/3207/320701/3207012010/3207012010001.json',
    'scheme':'https',
    'accept':'application/json, text/plain, */*',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'id,id-ID;q=0.9,en;q=0.8,en-US;q=0.7',
    'origin':'https://pilkada2024.kpu.go.id',
    'priority':'u=1, i',
    'referer':'https://pilkada2024.kpu.go.id/',
    'sec-ch-ua':'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-site',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36}'
}
url_prov = 'https://sirekappilkada-obj-data.kpu.go.id/wilayah/pilkada/pkwkp/32.json'


res = lp.get_response(requests, url_prov, sleep, random)
unique_kab = lp.get_unique_number(res)

data = []
for prov in range(0, len(unique_kab)):
    kode_kab = unique_kab[prov][0]
    nama_kab = unique_kab[prov][1]

    url_kab = f'https://sirekappilkada-obj-data.kpu.go.id/wilayah/pilkada/pkwkp/32/{kode_kab}.json'
    res = lp.get_response(requests, url_kab, sleep, random)
    unique_kec = lp.get_unique_number(res)
    for kab in range(0, len(unique_kec)):
        kode_kec = unique_kec[kab][0]
        nama_kec = unique_kec[kab][1]

        url_kec = f'https://sirekappilkada-obj-data.kpu.go.id/wilayah/pilkada/pkwkp/32/{kode_kab}/{kode_kec}.json'
        res = lp.get_response(requests, url_kec, sleep, random)
        unique_kel = lp.get_unique_number(res)

        for kec in range(0, len(unique_kel)):
            kode_kel = unique_kel[kec][0]
            nama_kel = unique_kel[kec][1]
        
            url_kel = f'https://sirekappilkada-obj-data.kpu.go.id/wilayah/pilkada/pkwkp/32/{kode_kab}/{kode_kec}/{kode_kel}.json'
            res = lp.get_response(requests, url_kel, sleep, random)
            unique_tps = lp.get_unique_number(res)

            for kel in range(0, len(unique_tps)):
                kode_tps = unique_tps[kel][0]
                nama_tps = unique_tps[kel][1]

                url_kel = f'https://sirekappilkada-obj-data.kpu.go.id/pilkada/hhcw/pkwkp/32/{kode_kab}/{kode_kec}/{kode_kel}/{kode_tps}.json'
                res = lp.get_response(requests, url_kel, sleep, random)
                data_pilkada = lp.get_data(nama_kab,nama_kec,nama_kel, nama_tps, res)
                data.append(data_pilkada)

df = lp.get_dataframe(pd, data)
print(df)
lp.savetoxlsx(df)

import pandas as pd
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




def get_response(requests, url, sleep, random):
    for i in range(100):
        print(url)
        try:
            response = requests.request("GET", url).json()
            return response
        except:
            pass
        sleep(random.randint(3, 6))
    


def get_data(nama_kab, nama_kec, nama_kel, nama_tps, res):
    try:
        pemilih_dpt_j = res['tungsura']['administrasi']['pemilih_dpt_j'] 
    except:
        pemilih_dpt_j = 0
    try:
        pengguna_dpt_j = res['tungsura']['administrasi']['pengguna_dpt_j']
    except:
        pengguna_dpt_j = 0
    try:
        suara_total = res['tungsura']['administrasi']['suara_total']
    except:
        suara_total = 0
    try:
        suara_sah = res['tungsura']['administrasi']['suara_sah']
    except:
        suara_sah = 0
    try:
        suara_t_sah = res['tungsura']['administrasi']['suara_tidak_sah']
    except:
        suara_t_sah = 0
    try:
        suara_acep = res['tungsura']['chart']['1000026']
    except:
        suara_acep = 0
    try:
        suara_jeje = res['tungsura']['chart']['1000027']
    except:
        suara_jeje = 0
    try:
        suara_ahmad = res['tungsura']['chart']['1000028']
    except:
        suara_ahmad = 0
    try:    
        suara_dedi = res['tungsura']['chart']['1000029']
    except:
        suara_dedi = 0
    return(nama_kab,nama_kec, nama_kel,nama_tps, pemilih_dpt_j, pengguna_dpt_j, suara_total, suara_sah, suara_t_sah, suara_acep, suara_jeje, suara_ahmad, suara_dedi)

def get_unique_number(res):
    dt=[]
    for i in range(0, len(res)):
        kode = res[i]['kode']
        nm = res[i]['nama']
        dt.append(
            (kode, nm)
        )
    return dt

def get_dataframe(pd, data):
    df = pd.DataFrame(data, columns=["Kabupaten","Kecamatan","Kelurahan","Nama TPS", "Pemilih Terdaftar", "Pengguna Pemilih", "Total Suara", "Suara Sah", "Suara Tidak Sah", "Pemilih Acep", "Pemilih Jeje", "Pemilih Ahmad", "Pemilih Dedi"])
    return df

def savetoxlsx(df):
    df.to_excel('Gubernur2024.xlsx', index=False)
    print("Data Telah tersimpan di Folder ini")
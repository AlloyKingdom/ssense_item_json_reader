# settings
# how to convert curl commands to Python? Watch this website: https://curlconverter.com/

# File saving folder, better create it first, name what you like
SAVE_FOLDER = "download_json/ssense_"

# Define constants
URL_MEN = "https://www.ssense.com/en-jp/men"
URL_WOMEN = "https://www.ssense.com/en-jp/women"
URL_OTHER = "https://www.ssense.com/en-jp/everything-else"
JSON_PAGE = ".json?page="
PAGE = 1
SSENSE_MEN = "men"
SSENSE_WOMEN = "women"
SSENSE_OTHER = "everything-else"

EAZY_MODE = 0
HARD_MODE = 1

# choose your crawler and url
mode = HARD_MODE
type = SSENSE_MEN

COOKIES = {
    'FPID': 'FPID2.2.3aiCjKmRvVqWBseNspJAgfe49QMeVJSLEYgCzIbae7I%3D.1645508984',
    'visitorId': 'd0b306db5326e72e81e2839866140113db68e088ba29454938b9f29459ba1c9f',
    'preferredLanguage': 'en',
    'exp_size_gql': 'false',
    'exp_cognito_service': 'true',
    'exp_is_klarna_osm_on_cart_enabled': 'false',
    'one_trust_eu': 'false',
    'exp_plp_sharpen_desktop': 'false',
    'exp_desktop_dpr': 'false',
    'isp': 'softbank corp.',
    'sid': 'e2c80edff751121ba1ea0c18bed03000',
    '_pxvid': 'd255e6ba-65d8-11ee-b118-4df31ab1cd94',
    '_gcl_au': '1.1.1217543276.1696769244',
    'shopping_bag': '6522a4dc8a105f07e0ed8efc',
    '__zlcmid': '1IEmBFxTa5s9uue',
    '_gid': 'GA1.2.1699751417.1696769246',
    'rskxRunCookie': '0',
    'rCookie': '1fmfwtg8t835paat7d1gnjlnhgllvu',
    'lang': 'en_US',
    '_pin_unauth': 'dWlkPU9XTmhNek0yWkRZdFpUWXpZUzAwTVRjeExUbGhOVFF0WldSak1qSXpOekExTlRSaw',
    '_gcl_aw': 'GCL.1696771610.Cj0KCQjwpompBhDZARIsAFD_Fp-60xQZ-uEFhKk1K_o_wAl34evjG5x1yMIFXofjFFKHEXY77doDcxYaAr9zEALw_wcB',
    'country': 'JP',
    '_gac_UA-519637-1': '1.1696771611.Cj0KCQjwpompBhDZARIsAFD_Fp-60xQZ-uEFhKk1K_o_wAl34evjG5x1yMIFXofjFFKHEXY77doDcxYaAr9zEALw_wcB',
    '_fbp': 'fb.1.1696850328455.1969321186',
    '_derived_epik': 'dj0yJnU9QkY2Yy1lTW5tdWVDQ3dISEt5MFZBUkdObk1rckd3amwmbj03RWxoYnU2d0lwM3N3bzRvaC1oYjJ3Jm09ZiZ0PUFBQUFBR1VqOG1BJnJtPWYmcnQ9QUFBQUFHVWo4bUEmc3A9Mg',
    'gdprCountry': 'false',
    '__cf_bm': '5ux7Oikn2AWXSHoakPdjpvN1QnRc7IGK_P1n.EZk3_Q-1696865481-0-Acul5d5YM8WXYQH4ulGONwq1cDkpfAdeFtGlrhSVmxmKoZcfZiLBP+FJnoplrefTPSHdpXq2DO70HM86ooM5Xus=',
    '_sp_ses.c6c8': '*',
    'pxcts': 'e6330819-66b8-11ee-a243-fe541dca4687',
    'ab.storage.deviceId.e352e6f5-ea92-41e0-be85-df1e6a76e0b7': '%7B%22g%22%3A%224956c53a-7198-6558-1935-2c43a9aec382%22%2C%22c%22%3A1665077934915%2C%22l%22%3A1696865482882%7D',
    '_gat': '1',
    'wcs_bt': 's_15f8bbc72b9c:1696865728',
    '_sp_id.c6c8': 'f9696ffe-d52a-4d1a-8f61-2fdc63b2e760.1645508983.23.1696865728.1696854637.f8b52110-db60-477f-943b-fef973986418',
    '_pxhd': 'xnBMlRTg0zNPq23AX8QBYtBnSJXOZwk2g75elB-SV9hH2nU81JA7k4calKZHvAWxFfUjfHeWmcPY7CU-F6x7Lw==:Lbzz0EkQRqJK7g4Hhq6G8Lqg-whrhZVK2scmaMVj4dqq7FE974Pla04r-D0zFvRqHC9H//IHQ21p662QYukJLC2Eohmyc2J5Zl/O0FnS-hw=',
    '_px2': 'eyJ1IjoiNzhmOTIxYzAtNjZiOS0xMWVlLWE5ZTAtNWYzYTdhZTg1ODU5IiwidiI6ImQyNTVlNmJhLTY1ZDgtMTFlZS1iMTE4LTRkZjMxYWIxY2Q5NCIsInQiOjE2OTY4NjYwMjkxNDAsImgiOiJkY2UwNDNiNjBmMjZhZDMzN2ZiZTgxMjc4MWNkNjA1YWFjZWJlNGM5NmMzODY5OWUzZmVjZThhYWVmMDhkNGY3In0=',
    '_ga_3L9QF4WT0T': 'GS1.1.1696865482.4.1.1696865729.0.0.0',
    '_ga': 'GA1.2.987313726.1696769244',
    'lastRskxRun': '1696865729189',
    'ab.storage.sessionId.e352e6f5-ea92-41e0-be85-df1e6a76e0b7': '%7B%22g%22%3A%22b42b4ab1-cf02-0637-9592-21dd55661e1f%22%2C%22e%22%3A1696867529223%2C%22c%22%3A1696865482881%2C%22l%22%3A1696865729223%7D',
    '_dd_s': 'rum=0&expire=1696866634173&logs=1&id=ebd274d2-2b3e-4a5a-b604-464cc01debc3&created=1696865481984',
}

HEADERS_HARD_MODE = {
    'authority': 'www.ssense.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7,fr;q=0.6',
    # 'cookie': 'FPID=FPID2.2.3aiCjKmRvVqWBseNspJAgfe49QMeVJSLEYgCzIbae7I%3D.1645508984; visitorId=d0b306db5326e72e81e2839866140113db68e088ba29454938b9f29459ba1c9f; preferredLanguage=en; exp_size_gql=false; exp_cognito_service=true; exp_is_klarna_osm_on_cart_enabled=false; one_trust_eu=false; exp_plp_sharpen_desktop=false; exp_desktop_dpr=false; isp=softbank corp.; sid=e2c80edff751121ba1ea0c18bed03000; _pxvid=d255e6ba-65d8-11ee-b118-4df31ab1cd94; _gcl_au=1.1.1217543276.1696769244; shopping_bag=6522a4dc8a105f07e0ed8efc; __zlcmid=1IEmBFxTa5s9uue; _gid=GA1.2.1699751417.1696769246; rskxRunCookie=0; rCookie=1fmfwtg8t835paat7d1gnjlnhgllvu; lang=en_US; _pin_unauth=dWlkPU9XTmhNek0yWkRZdFpUWXpZUzAwTVRjeExUbGhOVFF0WldSak1qSXpOekExTlRSaw; _gcl_aw=GCL.1696771610.Cj0KCQjwpompBhDZARIsAFD_Fp-60xQZ-uEFhKk1K_o_wAl34evjG5x1yMIFXofjFFKHEXY77doDcxYaAr9zEALw_wcB; country=JP; _gac_UA-519637-1=1.1696771611.Cj0KCQjwpompBhDZARIsAFD_Fp-60xQZ-uEFhKk1K_o_wAl34evjG5x1yMIFXofjFFKHEXY77doDcxYaAr9zEALw_wcB; _fbp=fb.1.1696850328455.1969321186; _derived_epik=dj0yJnU9QkY2Yy1lTW5tdWVDQ3dISEt5MFZBUkdObk1rckd3amwmbj03RWxoYnU2d0lwM3N3bzRvaC1oYjJ3Jm09ZiZ0PUFBQUFBR1VqOG1BJnJtPWYmcnQ9QUFBQUFHVWo4bUEmc3A9Mg; gdprCountry=false; __cf_bm=5ux7Oikn2AWXSHoakPdjpvN1QnRc7IGK_P1n.EZk3_Q-1696865481-0-Acul5d5YM8WXYQH4ulGONwq1cDkpfAdeFtGlrhSVmxmKoZcfZiLBP+FJnoplrefTPSHdpXq2DO70HM86ooM5Xus=; _sp_ses.c6c8=*; pxcts=e6330819-66b8-11ee-a243-fe541dca4687; ab.storage.deviceId.e352e6f5-ea92-41e0-be85-df1e6a76e0b7=%7B%22g%22%3A%224956c53a-7198-6558-1935-2c43a9aec382%22%2C%22c%22%3A1665077934915%2C%22l%22%3A1696865482882%7D; _gat=1; wcs_bt=s_15f8bbc72b9c:1696865728; _sp_id.c6c8=f9696ffe-d52a-4d1a-8f61-2fdc63b2e760.1645508983.23.1696865728.1696854637.f8b52110-db60-477f-943b-fef973986418; _pxhd=xnBMlRTg0zNPq23AX8QBYtBnSJXOZwk2g75elB-SV9hH2nU81JA7k4calKZHvAWxFfUjfHeWmcPY7CU-F6x7Lw==:Lbzz0EkQRqJK7g4Hhq6G8Lqg-whrhZVK2scmaMVj4dqq7FE974Pla04r-D0zFvRqHC9H//IHQ21p662QYukJLC2Eohmyc2J5Zl/O0FnS-hw=; _px2=eyJ1IjoiNzhmOTIxYzAtNjZiOS0xMWVlLWE5ZTAtNWYzYTdhZTg1ODU5IiwidiI6ImQyNTVlNmJhLTY1ZDgtMTFlZS1iMTE4LTRkZjMxYWIxY2Q5NCIsInQiOjE2OTY4NjYwMjkxNDAsImgiOiJkY2UwNDNiNjBmMjZhZDMzN2ZiZTgxMjc4MWNkNjA1YWFjZWJlNGM5NmMzODY5OWUzZmVjZThhYWVmMDhkNGY3In0=; _ga_3L9QF4WT0T=GS1.1.1696865482.4.1.1696865729.0.0.0; _ga=GA1.2.987313726.1696769244; lastRskxRun=1696865729189; ab.storage.sessionId.e352e6f5-ea92-41e0-be85-df1e6a76e0b7=%7B%22g%22%3A%22b42b4ab1-cf02-0637-9592-21dd55661e1f%22%2C%22e%22%3A1696867529223%2C%22c%22%3A1696865482881%2C%22l%22%3A1696865729223%7D; _dd_s=rum=0&expire=1696866634173&logs=1&id=ebd274d2-2b3e-4a5a-b604-464cc01debc3&created=1696865481984',
    'if-none-match': '"43e53-ElEUj/3Vvu/b/DzcUNIJzPXkVqI"',
    'referer': 'https://www.ssense.com/en-jp',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

HEADERS_EAZY_MODE = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}

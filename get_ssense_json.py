import httpx
import json

url = "https://www.ssense.com/en-jp/women"
json_name = ".json?page="
page = 1
file_name = "ssense_women"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}

res = httpx.get(url="https://www.ssense.com/en-jp/women.json", headers=headers, timeout=10, verify=False)

totalPages = json.loads(res.text)["pagination_info"]["totalPages"]

for page in range(152, totalPages + 1):

    if page == 1:
        json_url = url + ".json"
    else:
        json_url = url + json_name + str(page)

    json_file = httpx.get(url=json_url, headers=headers, timeout=10, verify=False)
    products = json.loads(json_file.text)["products"]
    save_name = "download_json/" + file_name + "page_" + str(page) + ".json"
    with open(save_name, "w", encoding="utf-8") as outfile:
        js = json.dumps(products, indent=4, ensure_ascii=False)
        outfile.write(js)
    print(json_url)


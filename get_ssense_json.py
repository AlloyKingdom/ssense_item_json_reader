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

for page in range(1, totalPages + 1):

    if page == 1:
        json_url = url + ".json"
        json_file = httpx.get(url=json_url, headers=headers, timeout=10, verify=False)
        products = json.loads(json_file.text)["products"]
        with open("download_json/" + file_name + "page_" + str(page) + ".json", "w") as outfile:
            outfile.write(json.dumps(products))
        print(json_url)

    else:
        json_url = url + json_name + str(page)
        json_file = httpx.get(url=json_url, headers=headers, timeout=10, verify=False)
        products = json.loads(json_file.text)["products"]
        with open("download_json/" + file_name + "page_" + str(page) + ".json", "w") as outfile:
            outfile.write(json.dumps(products))
        print(json_url)


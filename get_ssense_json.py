import httpx
import json

from settings import *


json_name = ".json?page="
page = 1


def get_ssense_items_to_json(mode: int, type: str):

    if type == SSENSE_MEN:
        url = URL_MEN
        file_name = SSENSE_MEN

    if type == SSENSE_WOMEN:
        url = URL_WOMEN
        file_name = SSENSE_WOMEN

    if type == SSENSE_OTHER:
        url = URL_OTHER
        file_name = SSENSE_OTHER

    if mode == EAZY_MODE:

        res = httpx.get(url=url + ".json", headers=HEADERS_EAZY_MODE, timeout=10, verify=False)
        totalPages = json.loads(res.text)["pagination_info"]["totalPages"]

        for page in range(1, totalPages + 1):

            if page == 1:
                json_url = url + ".json"
            else:
                json_url = url + json_name + str(page)

            json_file = httpx.get(url=json_url, headers=HEADERS_EAZY_MODE, timeout=10, verify=False)
            products = json.loads(json_file.text)["products"]
            save_name = SAVE_FOLDER + file_name + "_page_" + str(page) + ".json"

            with open(save_name, "w", encoding="utf-8") as outfile:
                js = json.dumps(products, indent=4, ensure_ascii=False)
                outfile.write(js)
            print(json_url)

    if mode == HARD_MODE:

        res = httpx.get(url=url + ".json", headers=HEADERS_HARD_MODE, cookies=COOKIES, timeout=10, verify=False)
        print(res.status_code)
        totalPages = json.loads(res.text)["pagination_info"]["totalPages"]

        for page in range(1, totalPages + 1):

            if page == 1:
                json_url = url + ".json"
            else:
                json_url = url + json_name + str(page)

            json_file = httpx.get(url=json_url, headers=HEADERS_HARD_MODE, cookies=COOKIES, timeout=10, verify=False)
            products = json.loads(json_file.text)["products"]
            save_name = SAVE_FOLDER + file_name + "_page_" + str(page) + ".json"

            with open(save_name, "w", encoding="utf-8") as outfile:
                js = json.dumps(products, indent=4, ensure_ascii=False)
                outfile.write(js)
            print(json_url)


if __name__ == "__main__":

    mode = HARD_MODE
    type = SSENSE_MEN
    get_ssense_items_to_json(mode, type)

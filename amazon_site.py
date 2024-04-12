import csv
from bs4 import BeautifulSoup
import requests


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    baseurl = 'https://www.amazon.eg'
    productlinks = []
    productdict = []

    for x in range(1, 3):
        site = requests.get(f'https://www.amazon.eg/s?i=electronics&rh=n%3A21832907031&fs=true&qid=1712544597&ref=sr_pg_{x}', headers=headers, timeout=10)
        soup = BeautifulSoup(site.content, 'lxml')
        productlist = soup.find_all('div', class_='s-asin')
        for item in productlist:
            for link in item.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal', href=True):
                productlinks.append(baseurl + link['href'])

    print(len(productlinks))

    def item_scraping(productlinks):
        for link in productlinks:
            try:
                testlink = link
                r = requests.get(testlink, headers=headers, timeout=10)
                soup = BeautifulSoup(r.content, 'lxml')

                pname = soup.find('span', id='productTitle').text.strip()

                prate = []
                for rate in soup.find_all('i', class_='a-icon a-icon-star a-star-3 cm-cr-review-stars-spacing-big'):
                    prate.append(rate.find('span', class_='a-icon-alt').text.strip())

                pprice = soup.find('span', class_='a-price-whole').text.strip()

                brandname = soup.find('tr', class_='po-brand').find('span', class_='a-size-base po-break-word').text.strip()

                modelname = soup.find('tr', class_='po-model_name').find('td', class_="a-span9").text.strip()

                size = soup.find('tr', class_='po-display.size').find('span', class_="a-size-base po-break-word").text.strip()

                color =  soup.find('tr', class_='a-spacing-small po-color').find('td', class_="a-span9").text.strip()

                ramsize = soup.find('tr', class_='a-spacing-small po-ram_memory.installed_size').find('span', class_="a-size-base po-break-word").text.strip()

                harddisk = soup.find('tr', class_='a-spacing-small po-hard_disk.size').find('span', class_="a-size-base po-break-word").text.strip()

                productdict.append({
                    "Product Name": pname,
                    "Product Price": pprice,
                    "Product Rate": prate,
                    "Product Brand Name": brandname,
                    "Product Model Name": modelname,
                    "Product Size": size,
                    "product color": color,
                    "Product RAM Size": ramsize,
                    "Product Harddisk Size": harddisk,
                })
            except AttributeError as e:
                print(f"Error scraping product from {link}: {e}")

    item_scraping(productlinks=productlinks)

    keys = productdict[0].keys()
    with open('C:/Noor_work/Projects/Wep_Scraping/Scraping-amazon-items/product_file.csv', 'w', encoding='UTF-8') as product_file:

        dict_writer = csv.DictWriter(product_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(productdict)
        print("file created successfully")
main()

from bs4 import BeautifulSoup
import requests
import csv


def main():

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    baseurl = 'https://www.amazon.eg'
    productlinks = []
    productdict = []

    for x in range(1,15):
        site = requests.get(f'https://www.amazon.eg/s?i=electronics&rh=n%3A21832907031&fs=true&qid=1712544597&ref=sr_pg_{x}', headers=headers)
        soup = BeautifulSoup(site.content, 'lxml')
        productlist = soup.find_all('div', class_='s-asin')
        for item in productlist:
            for link in item.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal', href=True):
                productlinks.append(baseurl + link['href'])

    print(len(productlinks))
    for link in productlinks:
        print('start')
        testlink = link #'https://www.amazon.eg/-/en/Lenovo-V15-Laptop-Integrated-Anti-glare/dp/B0BZSTQMCL/ref=sr_1_1?dib=eyJ2IjoiMSJ9._h90RsCd-5DVJiSKTaFIxhHiZcQ8Vg_oB0nrgEyGDRhY7Bf7ZJT2SXzrHuhxeOsQOk_tGd1p4jutX0HTRLN9bvIM04HUabNSEm8nMIkm47s0GnDQLz4iEaIjhcxuMDrX6UwWSl4TM7AKCv0orG9rVOOlJx7E2zQmvV0HQ-nMVKI2exnBnYWMzkCmmprXlUkf6RH7rjV8bRXjF0QQw8laoVLAWhdxwSGV4jwqi7IZllntpQ9TPXIoH_0o8J2eenDmiXIbHuTX4HUev_Br6GuKDP5orxYgxThSAHxA-iH6cBU.KEBXlK4tZrMM1GZWnG_a0Nqi70SzXjf1Tyx8mRwXC9k&dib_tag=se&qid=1712553679&s=computers&sr=1-1&th=1'
        r = requests.get(testlink, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        pname = soup.find('span', id = 'productTitle').text.strip()
        prate = soup.find_all('i', class_= 'a-icon a-icon-star a-star-3 cm-cr-review-stars-spacing-big')#.find('span', class_='a-icon-alt').text.strip()
        pprice = soup.find('span', class_='a-price-whole').text.strip()
        brandname =  soup.find('tr', class_='po-brand').find('span', class_='a-size-base po-break-word').text.strip()

        modelname =  soup.find('tr', class_='po-model_name').find('td', class_="a-span9").text.strip()
        size =  soup.find('tr', class_='po-display.size').find('span', class_="a-size-base po-break-word").text.strip()
        #color =  soup.find('tr', class_='a-spacing-small po-color').find('td', class_="a-span9").text.strip()
        ramsize =  soup.find('tr', class_='a-spacing-small po-ram_memory.installed_size').find('span', class_="a-size-base po-break-word").text.strip()
        harddisk =  soup.find('tr', class_='a-spacing-small po-hard_disk.size').find('span', class_="a-size-base po-break-word").text.strip()

        productdict.append({
            "Product Nmae": pname,
                "Product price": pprice,
                "product rate": prate,
                "product brand name": brandname,
                "product model name": modelname,
                "product size": size,
                #"product color": color,
                "product RAM size": ramsize,
                "product Harddisk size": harddisk,
        })
    def item_scraping():
       pass
    print(productdict)
main()
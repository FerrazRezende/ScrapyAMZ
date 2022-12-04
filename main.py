from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
from SendEmail import SendEmailCSV, SendEmailJson


class ScrapyAmz:

    def __init__(self):
        self.inputs()
        self.scrap()
        self.converting_to_dataframe()
        self.sending_to_email()


    def inputs(self):
        self.archive_format = str(input("Select archive format (CSV or Json):\n"))
        self.send_email = str(input("Insert e-mail to recive the archive!\n"))

    def scrap(self):
        print("Script started!")

        price_list = []
        title_list = []
        ratings_list = []
        notes_list = []
        link_list = []
        self.dict_products = {}
        pages = 401
        for i in [x for x in range(pages) if x != 0]:

            hdrs = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

            while True:
                try:
                    req = Request(f'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&page={pages}&qid=1660815519&ref=sr_pg_2', headers=hdrs)
                    response = urlopen(req)
                    self.html = response.read()
                    if response.getcode() == 200:
                        break
                except Exception as inst:
                    print(inst)

            soup = BeautifulSoup(self.html, "lxml")
            block_scrap = soup.find('span', attrs={'class': 's-latency-cf-section'})

            title = block_scrap.find_all('span', {'class': 'a-size-base-plus'})
            price = block_scrap.find_all('span', {'class': 'a-offscreen'})
            ratings = block_scrap.find_all('span', {'class': 's-underline-text'})
            notes = block_scrap.find_all('span', {'class': 'a-icon-alt'})
            links = block_scrap.find_all('h2', {'class': 'a-size-mini'})

            for l in links:
                product_link = l.find('a')['href']
                link_list.append(str(f'amazon.com{product_link}'))

            for t in title:
                title_list.append(str(t.get_text()))

            for p in price:
                price_list.append(str(p.get_text()))

            for r in ratings:
                ratings_list.append(str(r.get_text()))

            for n in notes:
                notes_list.append(str(n.get_text()))

            self.dict_products['Title'] = title_list
            self.dict_products['Price'] = price_list
            self.dict_products['Ratings'] = ratings_list
            self.dict_products['Notes'] = notes_list
            self.dict_products['Product link']= link_list

            print("Page {}/{}".format(i, pages -1))

        else:
            return("Data collected!")

    def converting_to_dataframe(self):
        if self.archive_format == "CSV":
            df = pd.DataFrame.from_dict(self.dict_products, orient='index').T
            df_2 = df.dropna()
            df_2.to_csv('./output/amazon_products.csv')
            return print("Archive CSV saved on directory output!")
            
        elif self.archive_format == "Json":
            df = pd.DataFrame.from_dict(self.dict_products, orient='index').T
            df_2 = df.dropna()
            df_2.to_json('./output/amazon_products.json')
            return print("Archive Json saved on directory output!")

        else:
            return print("Insert a valid option!")

    def sending_to_email(self):
        if self.archive_format == "CSV":
            return SendEmailCSV(self.send_email)

        elif self.archive_format == "Json":
            return SendEmailJson(self.send_email)

        else:
            print(f"Insert a valid e-mail. You digited: {self.send_email}")
ScrapyAmz()
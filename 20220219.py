import requests
from bs4 import BeautifulSoup

class Stock:
    #Constructor
    #*args參數，將傳入的多個股票代碼打包成一個元組(Tuple)
    def __init__(self, *stock_numbers):
        self.stock_numbers = stock_numbers
        print(self.stock_numbers)
 
    #爬取
    def scrape(self):

        result = list()  # 最終結果

        for stock_number in self.stock_numbers:
            response = requests.get("https://tw.stock.yahoo.com/quote/3037")
            # 使用【lxml】解析器來建立BeautifulSoup物件
            soup = BeautifulSoup(response.text, "lxml")

            #網頁打開 f12看html參考
            #公司名稱在 <h1>標籤
            stock_name = soup.find('h1', {'class': 'C($c-link-text) Fw(b) Fz(24px) Mend(8px)'}).getText()
            # print(stock_name)

            stock_date = soup.find('span', {'class': 'C(#6e7780) Fz(14px) As(c)'}).getText().replace('資料時間：', '')
            # print(stock_date)

            market_date = stock_date[0:10] #日期
            market_time = stock_date[11:16]#時間
            # print(market_date)
            # print(market_time)

            ul = soup.find('ul', {"class": "D(f) Fld(c) Flw(w) H(192px) Mx(-16px)"})
            # print(ul)

            items = ul.find_all('li', {
                    'class': "price-detail-item H(32px) Mx(16px) D(f) Jc(sb) Ai(c) Bxz(bb) Px(0px) Py(4px) Bdbs(s) Bdbc($bd-primary-divider) Bdbw(1px)"})
            # print(items)
            
            #tuple = ()  list = []  why suing tuple -> tuple is faster than list, tuple 是不可變 (Immutable) 的資料型態。 
            #這寫法記下來!!!
            data = tuple(item.find_all('span')[1].getText() for item in items)
            # print(data)

            #打包成tuple
            a = (market_date, stock_name, market_time) + data
            result.append(a)
            # print(a)
        return result



stock = Stock("3037","2603","2337")  #Constructor 輸入 需要的股票代碼
my_search = stock.scrape()
for entry in my_search:
    print(entry)
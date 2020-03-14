import requests
from bs4 import BeautifulSoup
from datetime import date

class GevolutionCrawl:
    def __init__(self):
        self.All_List=[]

    def addresscrawl(self, address):
        req = requests.get(address)
        try:
            req.raise_for_status()
        except:
            print("fail to access")
            return False
        print("success to access "+address)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        list = soup.select(
        "#imgload > table > tbody> tr"
        )
        self.ranked_list = []
        rank = 0
        for item in list :
            rank = rank+1
            if(rank>len(list)-1) :
                break;
            classname = "rank1"
            GameList = item.find_all("td")

            FreeGame = GameList[1].find("span", {"class":classname}).find("a").contents[0]
            try :
                FreeGameCompany = GameList[1].find("em").find("a").contents[0]
            except :
                FreeGameCompany = "NA"
            ChargeGame = GameList[2].find("span", {"class":classname}).find("a").contents[0]

            try :
                ChargeGameCompany = GameList[2].find("em").find("a").contents[0]
            except :
                ChargeGameCompany = "NA"

            SalesGame = GameList[3].find("span", {"class":classname}).find("a").contents[0]
            try :
                SalesGameCompany = GameList[3].find("em").find("a").contents[0]
            except :
                SalesGameCompany = "NA"

            today = date.today()

            FreeGameItem = {"Rank" :rank, "Name": FreeGame, "Company" : FreeGameCompany, "Date":today.strftime("%y/%m/%d")}
            ChargeGameItem = {"Rank":rank ,"Name": ChargeGame, "Company" : ChargeGameCompany, "Date":today.strftime("%y/%m/%d")}
            SalesGameItem = {"Rank":rank, "Name": SalesGame, "Company" : SalesGameCompany, "Date":today.strftime("%y/%m/%d")}

            if(address == "http://www.gevolution.co.kr/rank/aos") :
                FreeGameItem["Category"]="AosKorFree"
                ChargeGameItem["Category"]="AosKorCharge"
                SalesGameItem["Category"]="AosKorSales"
                self.All_List.append(FreeGameItem)
                self.All_List.append(ChargeGameItem)
                self.All_List.append(SalesGameItem)


            if(address == "http://www.gevolution.co.kr/rank/ios") :
                FreeGameItem["Category"] = "IosKorFree"
                ChargeGameItem["Category"] = "IosKorCharge"
                SalesGameItem["Category"] = "IosKorSales"
                self.All_List.append(FreeGameItem)
                self.All_List.append(ChargeGameItem)
                self.All_List.append(SalesGameItem)

            if(address == "http://www.gevolution.co.kr/rank/aos_us") :
                FreeGameItem["Category"] = "AosUsaFree"
                ChargeGameItem["Category"] = "AosUsaCharge"
                SalesGameItem["Category"] = "AosUsaSales"
                self.All_List.append(FreeGameItem)
                self.All_List.append(ChargeGameItem)
                self.All_List.append(SalesGameItem)

            if (address == "http://www.gevolution.co.kr/rank/ios_us.asp?c=us"):
                FreeGameItem["Category"] = "IosUsaFree"
                ChargeGameItem["Category"] = "IosUsaCharge"
                SalesGameItem["Category"] = "IosUsaSales"
                self.All_List.append(FreeGameItem)
                self.All_List.append(ChargeGameItem)
                self.All_List.append(SalesGameItem)

    def crawl(self):
        self.addresscrawl("http://www.gevolution.co.kr/rank/aos")
        self.addresscrawl("http://www.gevolution.co.kr/rank/ios")
        self.addresscrawl("http://www.gevolution.co.kr/rank/aos_us")
        self.addresscrawl("http://www.gevolution.co.kr/rank/ios_us.asp?c=us")

    def get_all_list(self):
        return self.All_List



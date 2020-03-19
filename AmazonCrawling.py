import requests
from bs4 import BeautifulSoup
from datetime import date

class AmazonCrawl:
    def __init__(self, address, parent_category):
        self.address = address
        self.parent_category = parent_category

    def crawl(self):
        req = requests.get(self.address)
        try:
            req.raise_for_status()
        except:
            print("fail to access")
            return False
        print("success to access " + self.address)

        html = req.text

        soup = BeautifulSoup(html, 'html.parser')

        self.selected_category= soup.find("span",{"class":"zg_selected"}).contents[0].strip()

        secondpage = soup.select("#zg-center-div > div.a-row.a-spacing-top-mini > div > ul > li.a-normal >a")
        self.secondurl = secondpage[0]["href"]

        list = soup.select(
        '#zg-ordered-list>Li'
        )

        self.ranked_list = []
        today = date.today()

        for item in list :
            name = item.select("span>div>span>a>div")
            rank = item.select("span>div>div>span.a-size-small.aok-float-left.zg-badge-body.zg-badge-color > span")
            #review = item.select("span>div>span>div.a-icon-row.a-spacing-none>a.a-size-small.a-link-normal")
            # zg-ordered-list > li:nth-child(26) >
            # zg-ordered-list > li:nth-child(26) > span > div > span > div.a-icon-row.a-spacing-none > a.a-size-small.a-link-normal
            #print(name)
            #print(review)
            try :
                name = name[0].text.strip()
                dictionary = {"Name" : name, "Brand" : name.split()[0], "Rank" : rank[0].text.replace("#",""), "Selected_category" : self.selected_category, 'Date' : today.strftime("%y/%m/%d")}
            except :

                dictionary = {"Name":"NA", "Rank" : "NA", "Selected_category" : self.selected_category, 'Date' : today.strftime("%y/%m/%d")}
            self.ranked_list.append(dictionary)

        self.second_page_crawl()

        return True

    def second_page_crawl(self):
        req = requests.get(self.secondurl)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        list = soup.select(
            '#zg-ordered-list>Li'
        )
        self.FiftytoHundred = {"Zinus" : 0, "Sleep" : 0, "bigLUCID" : 0, "Linenspa" : 0, "bigLINENSPA" : 0, "Lucid" : 0, "AmazonBasics" : 0, "Casper" : 0}
        today = date.today()

        for item in list:
            name = item.select("span>div>span>a>div")
            # review = item.select("span>div>span>div.a-icon-row.a-spacing-none>a.a-size-small.a-link-normal")
            # zg-ordered-list > li:nth-child(26) >
            # zg-ordered-list > li:nth-child(26) > span > div > span > div.a-icon-row.a-spacing-none > a.a-size-small.a-link-normal
            # print(name)
            # print(review)
            try:
                name = name[0].text.strip()
                brand = name.split()[0]
                if brand in self.FiftytoHundred :
                    self.FiftytoHundred[brand] = self.FiftytoHundred[brand] + 1
            except:
                if "NA" in self.FiftytoHundred :
                    self.FiftytoHundred["NA"] = self.FiftytoHundred["NA"] + 1
                else :
                    self.FiftytoHundred["NA"] = 1
        self.FiftytoHundred["Selected_category"] = self.selected_category
        self.FiftytoHundred["Date"] = today.strftime("%y/%m/%d")

    def get_FiftytoHundred(self) :
        return self.FiftytoHundred
    def get_children_category_address(self) :
        req = requests.get(self.address)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        parent_selected_tag = soup.find("span",{"class":"zg_selected"}).parent.parent
        try:
            category_list = parent_selected_tag.find("ul").find_all("li")
        except:
            return []
        self.children_category_address = []
        for children_address in category_list :
            if(children_address.find("a")==None) :
                break
            self.children_category_address.append(children_address.find("a")["href"])
        return self.children_category_address

    def get_selected_category(self) :
        return self.selected_category

    def get_parent_category(self):
        return self.parent_category

    def get_ranked_list(self) :
        return self.ranked_list
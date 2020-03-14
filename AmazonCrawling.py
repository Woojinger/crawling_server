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

        list = soup.select(
        '#zg-ordered-list>Li'
        )

        self.ranked_list = []
        today = date.today()

        for item in list :
            name = item.select("span>div>span>a>div")
            rank = item.select("span>div>div>span.a-size-small.aok-float-left.zg-badge-body.zg-badge-color > span")
            try :
                name = name[0].text.strip()
                dictionary = {"Name" : name, "Brand" : name.split()[0], "Rank" : rank[0].text.replace("#",""), "Selected_category" : self.selected_category, "Parent_category" : self.parent_category, 'Date' : today.strftime("%y/%m/%d")}
            except :

                dictionary = {"Name":"NA", "Rank" : "NA", "Selected_category" : self.selected_category, "Parent_category" : self.parent_category, 'Date' : today.strftime("%y/%m/%d")}
            self.ranked_list.append(dictionary)
        return True

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
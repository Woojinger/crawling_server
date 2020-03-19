from AmazonCrawling import AmazonCrawl
from GevolutionCrawling import GevolutionCrawl
import os
import django
from datetime import datetime, timedelta
from threading import Timer


# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawling_server.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
django.setup()

from server.models import Amazon, Gevolution, Fiftytohundred




def AmazonCrawling(now, number) :
    if(number >3):
        return False
    now.crawl()
    category = now.get_selected_category()
    children_address_list = now.get_children_category_address()
    list = now.get_ranked_list()
    for item in list :
        Amazon(Name=item["Name"], Brand = item["Brand"], Rank =item["Rank"], Selected_category = item["Selected_category"], Date = item["Date"]).save()
    fiftylist = now.get_FiftytoHundred()

    Fiftytohundred(Zinus=fiftylist["Zinus"], Sleep=fiftylist["Sleep"], bigLUCID = fiftylist["bigLUCID"], Lucid = fiftylist["Lucid"],
                   bigLINENSPA = fiftylist["bigLINENSPA"], Linenspa = fiftylist["Linenspa"], AmazonBasics = fiftylist["AmazonBasics"],
                   Casper = fiftylist["Casper"], Selected_category = fiftylist["Selected_category"], Date = fiftylist["Date"]).save()

    if len(children_address_list) != 0:
        for address in children_address_list:
            now = AmazonCrawl(address, category)
            AmazonCrawling(now, number+1)
        return True
    else :
        return False

def GevolutionCrawling():
    AppStart = GevolutionCrawl()
    AppStart.crawl()
    list = AppStart.get_all_list()
    for item in list:
        Gevolution(Name=item["Name"], Rank=item["Rank"], Company=item["Company"], Date=item["Date"], Category=item["Category"]).save()

if __name__ =='__main__':

    #Amazon Crawl
    start = AmazonCrawl(
        "https://www.amazon.com/Best-Sellers-Home-Kitchen-Bedroom-Furniture/zgbs/home-garden/1063308/ref=zg_bs_unv_hg_3_3733271_1",
        "Furniture")
    now = start
    AmazonCrawling(now, 1)
    #GevolutionCrawling()
    #Gevolution Crawl

#install scrapy package
pip install scrapy
#start crawl webpages from national gallery of art
scrapy crawl museum
# if you want to store the data into json file
scrapy crawl museum -o items.json

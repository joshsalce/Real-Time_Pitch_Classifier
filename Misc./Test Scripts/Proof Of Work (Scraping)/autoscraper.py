from autoscraper import AutoScraper

url = 'https://theathletic.com/' 
wanted_list = ["NHL"]


scraper = AutoScraper()

# Here we can also pass html content via the html parameter instead of the url (html=html_content)
result = scraper.build(url, wanted_list)

#scraper.get_result_similar('https://www.worldometers.info/world-population/')

print(result)
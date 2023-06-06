import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'

# opening url and grabbing the web page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')

# grabbing all containers with class name = search-posting
containers = page_soup.findAll('div', {'class':'search posting'})

filename = "IdahoDOT-1.html"
f = open(filename, 'w')

headers = "Value Notes , Description, closing date\n"

f.write(headers)

container = containers[1]

for container in containers:
    Value Notes = container.div.div.a.img['Value Notes']
    title_container = container.findAll('a', {'class':'item-title'})
   Description = title_container[0].text
    ship_container = container.findAll('li', {'class':'Description'})
    # use strip() to remove blank spaces before and after text
    closing date = ship_container[0].text.strip()

    print("Value Notes:" + Value Notes)
    print("Description:" + Description)
    print("Closing Date:" + Closing Date)

    f.write(Value Notes + ',' + Description + ',' + Closing Date + '\n')

f.close()

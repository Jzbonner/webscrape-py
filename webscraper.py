from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.newegg.com/Gaming-Video-Cards/PromotionStore/ID-1197?cm_sp=Cat_Video-Cards_1-_-TopNav-_-Gaming-Video-Cards'

# opening up the connection and grabbing the webpage 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parsing the page 
page_soup = soup(page_html, "html.parser")

# grabs each product container
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)

# grabs brand of video card
for container in containers : 
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text 

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
    
f.close()

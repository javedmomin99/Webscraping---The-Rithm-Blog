# https://www.rithmschool.com/blog
from bs4 import BeautifulSoup
import requests
from csv import writer

response= requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("article") #find_all using tag name

with open("blog_data.csv", "w") as csv_file:   #Will create a new file if file does not exists. If file exists, then it will override the new data
    csv_writer = writer(csv_file)
    csv_writer.writerow(["name", "link", "description", "date_time", "date"])  #Defining the Headers

    for article in articles:
        blog_name = article.find("a").get_text()  # Since we are looping each time, we will use find instead of find_all   #find using tag name
        # print(f"blog_name : {blog_name}")
        blog_link = article.find("a")  # Since we are looping each time, we will use find instead of find_all   #find using tag name
        # print(f"blog_link : {blog_link}")
        blog_link_text_form = article.find("a")["href"]  # Also, Below Code Works the same
        blog_link_text_form = article.find("a").attrs["href"]  # However, Above Code is preferred
        # print(f"blog_link_text_form : {blog_link_text_form}")
        blog_description = article.find("p")  # find using tag name
        # print(f"blog_description : {blog_description}")
        date_time = article.find("time")
        # print(f"date_time : {date_time}")
        date_time = article.find("time")["datetime"]  # Since it is not a text and an attribute, so using this method. #Also, Below Code Works the same
        date_time = article.find("time").attrs["datetime"]  # Since it is not a text and an attribute, so using this method.  #However, Above Code is preferred
        # print(f"date_time : {date_time}")
        date = article.find("small").get_text()
        # print(date)
        print(blog_name, blog_link, blog_description, date_time, date)  #This will print in python console.
        csv_writer.writerow([blog_name, blog_link_text_form, blog_description, date_time, date])  #This will append to csv file.







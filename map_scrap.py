from serpwow.google_search_results import GoogleSearchResults
import json
import mysql.connector

# create the serpwow object, passing in our API key
serpwow = GoogleSearchResults("83173830806343AAA69BB41313C11844")

# set up a dict for the search parameters
categories = ['Cafe', 'Grocery Store','Bank','Liquor Store','Gas Station','Pharmacy','Restaurant','Hospital','Retail Store']
    
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS BUSINESS_DB")
mydb = mysql.connector.connect(host = "localhost", user = 'root', passwd = '', database='business_db', port="3306")
cursor = mydb.cursor()


def save_mysql(tablename, data):
    cursor.execute("CREATE TABLE IF NOT EXISTS" + " `"+tablename+"`(`name` TEXT,`address` TEXT,`latitude` TEXT,`longitude` TEXT)")
    insertstring = "INSERT INTO"+ " " + "`"+ tablename + "`(`name`,`address`,`latitude`,`longitude`) VALUES (%s,%s,%s,%s)"
    
    cursor.executemany(insertstring, data)
    mydb.commit()

for i in categories:

    params = {
        "q" : i,
        "gl" : "ca",
        "hl" : "en",
        "location" : "Canada",
        "google_domain" : "google.ca",
        "search_type" : "places",
        "total_pages" : "20"
    }

    # retrieve the search results as JSON
    result = serpwow.get_json(params)
    value = []
    page_urls = []
    for j in result['places_results']:
        value.append((j['title'],j['address'],j['gps_coordinates']['latitude'],j['gps_coordinates']['longitude']))
    save_mysql(i,value)
    
    
        
        
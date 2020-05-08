from serpwow.google_search_results import GoogleSearchResults
import csv

serpwow = GoogleSearchResults("")
categories = ['Cafe', 'Grocery Store','Bank','Liquor Store','Gas Station','Pharmacy','Restaurant','Hospital','Retail Store']
    
with open("results.csv","w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Business Name", "Business Address","Latitude","Longitude"])
    
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
        result = serpwow.get_json(params)
        value = []
        page_urls = []
        for j in result['places_results']:
            writer.writerow([j['title'],j['address'],j['gps_coordinates']['latitude'],j['gps_coordinates']['longitude']])
    
    
        
        
        6061EC093F314BDAB34CE98E26A9A4D0
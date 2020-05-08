
1. Please install mySQL
2. Please open https://app.serpwow.com/ , create account and get api_key.

3. Please change parameter of "GoogleSearchResults" method in 6th line of "map_scrap.py" to api_key.
4. Please type the following command

    first.   pip freeze > requirements.txt 
    second.  pip install -r requirements.txt
    third.   python map_scrap.py
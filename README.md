# NBA-data-scrapping
Data scrapping using "Pandas" and HTTP Python Library "Requests" 

Step 1: go to https://www.nba.com/stats

Step 2: There are many filters on the website for example you can go to and select "Official Leaders" under the "Leaders" tab
After selecting you will see a tabular data, To further scrap this data

Step 3: Right-click on the page and select inspect, then select Fetch/XHR on the network tab 
there you will find the JSON file, Double-click and open the file
![JSON](https://github.com/00-gmail/NBA-data-scrap/assets/96058881/587279e8-8a3f-4af7-9a0c-e02186b664f6)

Step 4: To find the request headers, just click the json file and under the Headers section we will find the request headers
Copy all the headers and convert them into the dictionary, which used in the given code repo.

![data-api_url](https://github.com/00-gmail/NBA-data-scrap/assets/96058881/f1a63c82-9859-49ae-a21e-66235d27a71f)

Note: if you are working on vscode run "pip install xlrd openpyxl" on your terminal

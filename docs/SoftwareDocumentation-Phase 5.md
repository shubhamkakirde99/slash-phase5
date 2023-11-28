## SLASH PHASE 5

## Motivation:
Slash was envisioned as a console application which was meant to be used as a standalone native Python desktop application. Even though a native application is good in usecases such as heavy processing and zero downtime but in the bigger picture, it fades in comparison to an online web application. Our efforts in phase-II were to convert a native desktop Python application to a web application(APIs) and expand the horizon by bringing in more e-commerce websites support as well as support for API calls to sites that don't support scraping. Our vision is to provide a one-stop abstraction for all web scraping needs which is packaged in a sleek and easy to implement cloud pipeline. Integrating CI/CD to our API was crucial to our goal as we believe the next phase should not dwell in the past but rather focus on the future. 

## Introduction:
Slash is a publicly accessible web API framework that allows one to scrape the most popular e-commerce websites to get the best deals on the searched items across multiple e-commerce websites. Currently supported websites include [Walmart](https://www.walmart.com/), [Target](https://www.target.com/), [BestBuy](https://www.bestbuy.com/) and [EBay](https://www.ebay.com/).
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash introduces easy to use public APIs to filter, sort and search through the search results
- **Powerful**: Produces JSON responses that can be easily customised to bring about the desired output

## Steps for Execution
1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/MeryHarikaG/slash-phase5.git
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip3 install -r requirements.txt
```
3. To run this project, you must install PostgreSQL on your system. If you haven't already installed it, you can download the latest version of PostgreSQL from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/).

### Configuring Database Connection

Once you've installed PostgreSQL, follow these steps to set up the database connection in your project:

i. Open the database.py file in your project directory.

ii. Locate the top section of the code where you define the database connection settings. It might look something like this:

   ```
   username = 'postgres'
   password = 'pass'
   ```
Replace username and password value from 'postgres', 'pass' with your PostgreSQL username password, respectively.

4. Once all the requirements are installed, you will have to ```cd``` into the ```src``` folder. Once in the ```src``` folder, use the python command to run the ```main.py``` file. (/MeryHarikaG/slash-phase5/src => you should be at this level)
```
cd src

For Mac
python3 main.py

For Windows
python main.py
```
5. While the above is running, go to new terminal and run streamlit application. Firstly go up one directory level using ```cd ..``` and use the following command:  (/MeryHarikaG/slash-phase5 => you should be at this level)
```
For Mac
python3 -m streamlit run slash_user_interface.py

For Windows
streamlit run slash_user_interface.py
```


## Technology Used
---
- Streamlit [https://streamlit.io/]
- Python
- Fast API
- Postgre SQL

## Output

The below images shows the websites developed for Slash Phase 5
<img src = 'https://github.com/MeryHarikaG/slash-phase5/blob/main/media/Website_1.png?raw=true'>
<img src = 'https://github.com/MeryHarikaG/slash-phase5/blob/main/media/Login%20page.png?'>
<img src = 'https://github.com/MeryHarikaG/slash-phase5/blob/main/media/Register.png?raw=true'>
<img src = 'https://github.com/MeryHarikaG/slash-phase5/blob/main/media/Website_2.png?raw=true'>
<img src = 'https://github.com/MeryHarikaG/slash-phase5/blob/main/media/Website_3.png?raw=true'>
<img src = 'https://github.com/MeryHarikaG/slash-phase5/blob/main/media/Wishlist%20page.png'>

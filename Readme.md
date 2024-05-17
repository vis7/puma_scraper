This Project Scrap Puma shoose data from [here](https://in.puma.com/in/en/mens/mens-shoes/mens-shoes-sneakers)

# Setup
Perform below steps to setup Project
```
# clone git repository
git clone git@github.com:vis7/puma_scraper.git
cd puma_scrapper

# create virtualenv and activate it
virtualenv venv
source venv/bin/activate

# install all dependency in virtualenv
pip install -r requirements.txt
```

# Run
Run crawler and store data in csv
```
scrapy crawl puma -O puma.csv
```

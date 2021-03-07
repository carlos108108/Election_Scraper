# Project3_election_scraper
my third project at Online Python Academy

# Description of this project:
this project is useful for extraction of parliamentary election results in the Czech Republic in 2017 

libraries which are used in this code are saved in the file: requirements.txt; the new virtual environment is recommended for their installation; launching via Manager:

pip3 --version

pip3 --install requirements.txt


# Launching this code:
launching of the file elect.py within command line requires 2 arguments:

python elect.py "URL of the territorial self-governing unit" "final file" (the first one must be in double quotes!!!)

file will be saved as CSV file (.csv)

# Project display:

resulsts for Prostějov region

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2. argument: election_prostejov.csv

launching this code:

![radek s argumenty](https://user-images.githubusercontent.com/75171974/109416632-bf4ad900-79bf-11eb-8d92-e348ba4e68ef.png)

running:

![prubeh_stahovani](https://user-images.githubusercontent.com/75171974/110236719-af8b4180-7f37-11eb-834b-c05a800f4b7c.png)


partial output:

![election_tabulka](https://user-images.githubusercontent.com/75171974/109416848-e81f9e00-79c0-11eb-84e4-f6e484e14160.png)







# Tableau visualisation
https://public.tableau.com/app/profile/karel.nov.k/viz/Election_scraper/Election2017ProstjovNUTSlevel4-districttotal

# Descriptiont:
this project is useful for extraction of parliamentary election results in the Czech Republic in 2017 

libraries which are used in this code are saved in the file: requirements.txt; the new virtual environment is recommended for their installation; launching via Manager:

pip3 --version

pip3 --install requirements.txt


# Launching the code:
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

![prubeh stahovani](https://user-images.githubusercontent.com/75171974/110236740-d6497800-7f37-11eb-8b4b-abe0055a4979.png)



partial output:   '-' means no ballot of this party in this NUTS level 5(commune)

![prubeh_stahovani_list](https://user-images.githubusercontent.com/75171974/110328008-0ae23000-801b-11eb-8eb5-eb47e20f1ecc.png)


![election_tab](https://user-images.githubusercontent.com/75171974/110236830-52dc5680-7f38-11eb-8258-7f821b3a865e.png)








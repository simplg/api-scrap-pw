# Mise en situation #1 - API & Scrapping [![Build Status](https://travis-ci.com/simplg/api-scrap-pw.svg?branch=main)](https://travis-ci.com/simplg/api-scrap-pw)
L’idée de cette mise en situation est de valider ta maîtrise de Python et Git.
Je te propose donc de faire un très rapide programme qui tu hébergeras sur Heroku (https://www.heroku.com/; c’est gratuit).

L’objectif est de programmer un petit programme Python qui va scrapper le site https://coinmarketcap.com/ et qui va retourner une liste au format JSON constituée des crypto-monnaies dont le prix a le plus évolué dans les dernières 24h ou 7j. 
En hébergeant sur Heroku tu auras une url du genre api-scrap-pw.herokuapp.com
L’idée est que quand on fait une requête GET sur https://api-scrap-pw.herokuapp.com/?tf=1 on a le résultat des 10 coins qui on le plus monté & les 10 coins qui ont le plus baissé (soit 20 résultats) dans les 24 dernières heures et la même chose pour https://api-scrap-pw.herokuapp.com/?tf=7 mais avec les 7 derniers jours.
Le 1 étant pour 24h et le 7 pour 7j.
Si le paramètre “tf” est absent, renvoyez une erreur 400
Si le paramètre “tf” prend une autre valeur que 1 ou 7, vous pouvez renvoyer une erreur 418
Pour appeler ton application je le ferai depuis Postman.

Pour soumettre ta réponse, je t’invite à me partager dans le champs correspondant à la mise en situation #1 :
le lien vers ton programme héberger sur Heroku (pour que je puisse le tester directement)
le lien vers ton code (hébergé où tu le souhaites)

# Installation
1. First you need to clone this repository:
```sh
git clone https://github.com/simplg/api-scrap-pw
cd api-scrap-pw
```
2. Once you have cloned this repo, you need to create a virtual environment:
```sh
python -m venv venv
```
3. Then you have to activate it:

**For Linux**:
```sh
source venv/bin/activate
```
**For windows**:
```sh
./venv/Scripts/activate.ps1
```
4. Then you need to install the dependancies:
```sh
pip install -r requirements.txt
```
# Usage
To run this app, you just have to run it within your virtual environment by typing:
```sh
flask run
```

# Api Documentation
You have one api endpoint which have a mandated argument tf that can take only one of the two values: "1" or "7".
/?tf=1 for the last 24 hours result and /?tf=7 for the last 7 days result.
The result is a json object with two lists, one which is the first 10 value for percentage price changes and the other is the last 10.

# Docker
The app can also be built into a container.

# Exercice Back-end Python

## Execution
1. Construire l'image Docker 
```sh
docker-compose build
```
2. Lancer les conteneurs
```sh
docker-compose up
```
3. Ouvrir l'API  
```
http://localhost:5000
```

## Description 

| Méthode | URL | Description |
|---|---|---|
| GET | /get_games | Retourne la liste des jeux |
| POST | /add_game | Ajoute un jeu |
| PUT | /modif_game | Modifie un jeu existant |
| DELETE | /del_game | Supprime un jeu existant |
| GET | /dashboard | Dashboard simplifié |

## Tests

J'ai effectué mes tests à l'aide de **Postman** et en voici des captures d'écran:
###/get/games
![test get](tests/test_get.PNG)
###/add_games 
![test post](tests/test_post.PNG)
Sans nom: 
![test post](tests/test_post_invalide.PNG)
###modif_game
![test put](tests/test_put.PNG)
###del_game
![test del](tests/test_del.PNG)
###dashboard
![test dashboard](tests/test_dashboard.PNG)

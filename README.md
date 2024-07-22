# API RESTful pour la gestion des projets et des tickets

## Description

Ce projet est une API RESTful développée avec Django et Django REST Framework. Elle permet de gérer des projets, des tickets (issues) et des commentaires. Les utilisateurs peuvent s'inscrire, se connecter, créer des projets et des tickets, et commenter des tickets. Les administrateurs ont des privilèges supplémentaires pour la création des tickets.

## Installation


1. **Clonez le dépôt :**

   ```bash
   git clone <votre-url-depot>
   cd <nom-du-repertoire>
   ```

2. **Installez Pipenv si ce n'est pas déjà fait :**

    ```bash
    pip install pipenv
    ```

3. **Créez et activez un environnement virtuel avec Pipenv :**

    ```bash
    pipenv install
    pipenv shell
    ```


4. **Appliquez les migrations :**

    ```bash
    python manage.py migrate
    ```

5. **Créez un superutilisateur :**

    ```bash
    python manage.py createsuperuser
    ```

6. **Lancez le serveur de développement :**

    ```bash
    python manage.py runserver
    ```


## Endpoints disponibles


### JWS Token :
POST /api/token/ : Génération du token.


### Projets :

GET /api/project/ : Liste de tous les projets pour lequel l'user est contributeur.
POST /api/project/ : Création d'un nouveau projet.

GET /api/project/{id}/ : Détails d'un projet spécifique.

PUT /api/project/{id}/ : Mise à jour d'un projet (réservé à l'auteur du projet).

DELETE /api/project/{id}/ : Suppression d'un projet (réservé à l'auteur du projet).

### Tickets d'un projet :

GET /api/issue/ : Liste de tous les tickets accessibles par l'utilisateur.
GET /api/project/{id}/issues/ : Liste de tous les tickets d'un projet.

POST /api/project/{id}/issues/ : Création d'un nouveau ticket.
POST /api/issue/ : Création d'un nouveau ticket (réservé aux administrateurs).

GET /api/issue/{issue_id}/ : Détails d'un ticket spécifique.
GET /api/project/{id}/issues/{issue_id}/ : Détails d'un ticket spécifique.

PUT /api/issue/{issue_id}/ : Mise à jour d'un ticket (réservé à l'auteur du ticket).

DELETE /api/issue/{issue_id}/ : Suppression d'un ticket (réservé à l'auteur du ticket).

### Commentaires :

GET /api/project/{id}/issues/{issue_id}/comments/ : Liste de tous les commentaires d'un ticket.
GET /api/comment/ : Liste de tous les commentaires accessibles à l'utilisateur.

POST /api/comment/ : Création d'un nouveau commentaire sur un ticket.(réservé aux administrateurs).
POST /api/project/{id}/issues/{issue_id}/comments/ : Création d'un nouveau commentaire.

GET /api/comment/{comment_id}/ : Détails d'un commentaire spécifique. 
GET /api/project/{id}/issues/{issue_id}/comments/{comment_id}/ : Détails d'un commentaire spécifique. 

PUT /api/comment/{comment_id}/ : Mise à jour d'un commentaire (réservé à l'auteur du commentaire).

DELETE /api/comment/{comment_id}/ : Suppression d'un commentaire (réservé à l'auteur du commentaire).

### Todo liste :

GET /api/todo/ Liste de tous les tickets accessibles par l'utilisateur dont il est le worker !

GET /api/todo/{issue_id} Détail du ticket dont il est le worker

GET /api/todo/{issue_id}/comments/ : Liste de tous les commentaires d'un ticket.
GET /api/todo/{issue_id}/comments/{comment_id}/ : Détails d'un commentaire spécifique. 
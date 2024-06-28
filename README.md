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

4. **Installez les dépendances :**

    ```bash
    pipenv install
    ```

5. **Appliquez les migrations :**

    ```bash
    python manage.py migrate
    ```

6. **Créez un superutilisateur :**

    ```bash
    python manage.py createsuperuser
    ```

7. **Lancez le serveur de développement :**

    ```bash
    python manage.py runserver
    ```


## Endpoints disponibles

### Authentification :

POST /api/auth/register/ : Inscription d'un nouvel utilisateur.
POST /api/auth/login/ : Connexion d'un utilisateur.
POST /api/auth/logout/ : Déconnexion d'un utilisateur.

### JWS Token :
POST /api/token/ : Génération du token.


### Projets :

GET /api/project/ : Liste de tous les projets pour lequel l'user est contributeur.
POST /api/project/newprojet/ : Création d'un nouveau projet.

GET /api/project/{id}/ : Détails d'un projet spécifique.

PUT /api/project/{id}/ : Mise à jour d'un projet (réservé à l'auteur du projet).

DELETE /api/project/{id}/ : Suppression d'un projet (réservé à l'auteur du projet).

### Tickets d'un projet:

GET /api/ticket/ : Liste de tous les tickets accessibles par l'utilisateur.
GET /api/project/{id}/tickets/ : Liste de tous les tickets d'un projet.

POST /api/project/{id}/newticket/ : Création d'un nouveau ticket.
POST /api/ticket/ : Création d'un nouveau ticket (réservé aux administrateurs).

GET /api/ticket/{ticket_id}/ : Détails d'un ticket spécifique.
GET /api/project/{id}/tickets/{ticket_id}/ : Détails d'un ticket spécifique.

PUT /api/ticket/{ticket_id}/ : Mise à jour d'un ticket (réservé à l'auteur du ticket).

DELETE /api/ticket/{ticket_id}/ : Suppression d'un ticket (réservé à l'auteur du ticket).

### Commentaires :

GET /api/project/{id}/tickets/{ticket_id}/commentaires/ : Liste de tous les commentaires d'un ticket.
GET /api/commentaire/ : Liste de tous les commentaires d'un ticket.

POST /api/commentaire/ : Création d'un nouveau commentaire sur un ticket.(réservé aux administrateurs).
POST /api/project/{id}/tickets/{ticket_id}/newcommentaire/ : Création d'un nouveau commentaire.

GET /api/commentaire/{comment_id}/ : Détails d'un commentaire spécifique. 
GET /api/project/{id}/tickets/{ticket_id}/commentaires/{comment_id}/ : Détails d'un commentaire spécifique. 

PUT /api/commentaire/{comment_id}/ : Mise à jour d'un commentaire (réservé à l'auteur du commentaire).

DELETE /api/commentaire/{comment_id}/ : Suppression d'un commentaire (réservé à l'auteur du commentaire).


*titre : system gestion bibliotheque

*les requêtes de mysql:

-base de donnée des utilisateur:
achraf

-table:
register:CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

 -base de donnée des livre:
 library_management

-table:
 book_list:CREATE TABLE books (
  book_id INT NOT NULL AUTO_INCREMENT,
  book_name VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  edition VARCHAR(50) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  qty INT NOT NULL,
  image VARCHAR(255),
  PRIMARY KEY (book_id)
);

*les fonctionnalitées:
register(): permet de l'utilisateur de crée un compt
login(): permet au utilisateur de se connecter a son compte
addbook(): permet a l'utilisateur d'ajouter un livre.
deletebook(): permet a l'utilisateur de supprimer un livre.
updatebook(): permet a l'utilisateur de supprimer un  livre 
serchbook(): permet a l'utilisateur de chercher un livre
showimage(): permet a l'utilisateur d'affiher l'image d'un livre.



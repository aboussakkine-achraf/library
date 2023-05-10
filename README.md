*titre : system gestion bibliotheque

*les requêtes de mysql:
![4](https://github.com/aboussakkine-achraf/library/assets/114268936/f49953b9-44cb-446c-a1e6-5b830b4a766c)
-base de donnée des utilisateur:
achraf

-table:
register:CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
![5](https://github.com/aboussakkine-achraf/library/assets/114268936/624c6c77-db3b-4c35-95ba-8befa64a3590)
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
*interface login:
![1](https://github.com/aboussakkine-achraf/library/assets/114268936/9f3fc4b4-7f0d-4a9c-b8aa-dc8f80cbe115)
*interface register:
![2](https://github.com/aboussakkine-achraf/library/assets/114268936/2b0f3e2d-8f10-4e7e-996c-4f80aaab050c)
*interface book:
![3](https://github.com/aboussakkine-achraf/library/assets/114268936/f7773139-859c-4159-ad73-3207303fb5f8)
*les fonctionnalitées:
register(): permet de l'utilisateur de crée un compt
login(): permet au utilisateur de se connecter a son compte
addbook(): permet a l'utilisateur d'ajouter un livre.
deletebook(): permet a l'utilisateur de supprimer un livre.
updatebook(): permet a l'utilisateur de supprimer un  livre 
serchbook(): permet a l'utilisateur de chercher un livre
showimage(): permet a l'utilisateur d'affiher l'image d'un livre.



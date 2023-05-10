*titre : system gestion bibliotheque

*les requêtes de mysql:

-base de donnée des utilisateur:

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



*achraf

-table:

register:CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
<div>
<img width="245" alt="usertable" src="https://github.com/aboussakkine-achraf/library/assets/80420443/bb3a671c-72b7-4326-8b88-e34c4c54c9c4">
 <img width="692" alt="booktable" src="https://github.com/aboussakkine-achraf/library/assets/80420443/6ffd70d6-a67a-4e4b-8ca2-fa53bd1a7bf0">
 </div>

 *-base de donnée des livre:

* library_management
 

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
*diagramme de cas d'utilisation:
![usecasee](https://github.com/aboussakkine-achraf/library/assets/114268936/eee87aa9-8fe9-4299-a0e9-959da25a600b)
*diagramme de class:
![WhatsApp Image 2023-05-10 at 14 09 03](https://github.com/aboussakkine-achraf/library/assets/114268936/f19a9953-23f3-4aac-af7d-d3718789239d)




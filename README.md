*titre : system gestion bibliotheque

*les requêtes de mysql:
*achraf
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
<img width="566" alt="signin" src="https://github.com/aboussakkine-achraf/library/assets/80420443/82b0a6fd-cfaa-423d-a00e-66f261a1950c">
<img width="105" alt="signup" src="https://github.com/aboussakkine-achraf/library/assets/80420443/f351be81-011c-4df6-8d36-3113d4d7eba8">
<img width="586" alt="interface de gestion" src="https://github.com/aboussakkine-achraf/library/assets/80420443/c40e9b4f-24ea-4693-bc98-a7620e934d56">
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




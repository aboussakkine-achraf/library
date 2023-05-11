*titre : system gestion bibliotheque

*les requêtes de mysql:
*achraf
 
-base de donnée des utilisateur:

-table:
 book_list:CREATE TABLE book (
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

register:CREATE TABLE register (
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
<div>
<img width="200" height="200" alt="signin" src="https://github.com/aboussakkine-achraf/library/assets/80420443/82b0a6fd-cfaa-423d-a00e-66f261a1950c">
<img width="200"height="200" alt="signup" src="https://github.com/aboussakkine-achraf/library/assets/80420443/f351be81-011c-4df6-8d36-3113d4d7eba8">
<img width="200"height="200" alt="interface de gestion" src="https://github.com/aboussakkine-achraf/library/assets/80420443/c40e9b4f-24ea-4693-bc98-a7620e934d56">
</div>
*les fonctionnalitées:
register(): permet de l'utilisateur de crée un compt
login(): permet au utilisateur de se connecter a son compte
addbook(): permet a l'utilisateur d'ajouter un livre.
deletebook(): permet a l'utilisateur de supprimer un livre.
updatebook(): permet a l'utilisateur de supprimer un  livre 
serchbook(): permet a l'utilisateur de chercher un livre
showimage(): permet a l'utilisateur d'affiher l'image d'un livre.
*diagramme de cas d'utilisation + diagramme de classe:
<div>
<img width="300" height="300" alt="image" src="https://github.com/aboussakkine-achraf/library/assets/80420443/6e3df757-596c-4250-9d0f-2f8cfbc63b09">

<img width="300" height="300" alt="image2" src="https://github.com/aboussakkine-achraf/library/assets/80420443/9ef21bfc-f331-4d8e-8081-34107db9e07e">
</div>



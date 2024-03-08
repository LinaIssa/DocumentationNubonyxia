Premiers pas avec Nubonyxia
============================

Cette page offre une visite guidée de `Nubonyxia`_ et donne une desciption *pas à pas* des différentes étapes du lancement d'un service sur la plateforme. 
 

1- Ajout du certificat dans le navigateur
-----------------------------------------

Dans un premier temps, avec d’accéder à la plateforme, il est nécessaire d’ajouter le certificat, acccessible `ici <https://nubonyxia.incubateur.finances.rie.gouv.fr/statics/bercyCA.crt>`_, dans le navigateur de votre choix. En effet, nous travaillons pour le moment avec un certificat auto-signé. 


.. note::

	Cette manipulation est à faire une seule fois.



.. tab-set::

	.. tab-item:: avec Firefox 

		* Aller dans le menu Paramètres, rechercher Certificats 
		* Cliquer sur le bouton Afficher les certificats 
		* Aller dans l'Onglet Autorités 
		* Cliquer sur le bouton Importer et sélectionner le certificat bercyCA.crt	

	.. tab-item:: avec Edge  

		* Aller dans les paramètres du navigateur, chercher Certificats 
		* Cliquer sur Gérer les certificats qui devrait ouvrir une fenêtre Windows
		* Sélectionner l'onglet Autorités de certification racine de confiance 
		* Importer le certificat bercyCA.crt

2- Connexion à la plateforme 
----------------------------


L'accès à la plateforme se fait en utilisant l'identifiant et mot de passe que l'on vous aura communiqué. Nous utilisons `keycloak <https://www.keycloak.org>`_ pour gérer l'authentification. 

.. note:: 
	Nous travaillons actuellement à intégrer **agent connect** à la plateforme. Pour le moment, nous gérons à la main les comptes utilisateurs (pas de fédérateur d'identité).

3- Vue générale de la plateforme 
--------------------------------

L'interface du datalab `Nubonyxia`_ est très largement inspirée de celle du `SSP Cloud`_. 
insérer schéma relation entre différentes composantes 

A la disposition de l'utilisateur : 

.. dropdown:: un espace de stockage
    :animate: fade-in-slide-down 

    `Nubonyxia`_ n'échappe pas à la tendance de fond observée dans la Data et le Cloud, qui consiste à séparer l'espace de stockage des données des services où elles sont traitées. Pour plus d'informations sur le bucket S3 basé sur `MinIO`_ mis à la disposition des utilisateurs, consulter cette :doc:`page <minio>`.   

    Cette séparation entre l'espace de stockage des données et l'envrionnement où elles sont traitées offre plusieurs avantages : 

    * découpler le stockage et le calcul,
    * garantir une **reproductibilité des analyses**, 
    * permettre une **optimisation des coûts**. En effet, on peut dès lors adapter les ressources en fonction des besoins de stockage et calcul.

     

.. dropdown:: un catalogue de services 
	:animate: fade-in-slide-down

	
	Les services mis à la disposition des utilisateurs sont dans l'onglet :menuselection:`Catalogue de services`. Ces derniers se répartissent selon plusieurs catégories et permettent de répondre à un large spectre de cas d'usages *data*. 

	.. tab-set:: 

		.. tab-item:: IDE

			* Vscode 
			* Notebook

		.. tab-item:: Gestion de base de données

			* PostgreSQL 
			* Cloudbeaver 
			* NocoDB 

		.. tab-item:: Data Visualisation 

			* Superset

		.. tab-item:: Automation

			* Argo-cd 
			* Argo-workflows 


	.. note::
	
		Si vous avez besoin d'un service en particulier qui est indisponible dans notre catalogue, n'hésitez pas à nous en faire part. Nous sommes à l'écoute de nos utilisateurs pour enrichir notre catalogue !
	
	Vous trouverez :doc:`ici <services>` les explications sur la configuration des différents services. Des exemples de cas d'usages sont présentés dans cette :doc:`page <usecase>`.

	Les services lancés par l'utilisateur apparaissent dans l'onglet :menuselection:`Mes services`. Il est possible de lancer à la demande plusieurs services à la fois.   

	.. important:: 
		Les services ont des tokens d'expiration. Lorsqu'ils ne sont plus utilisés, pensez à bien les supprimer, voir :doc:`guide des bonnes pratiques <methode>`. 



.. dropdown:: une connexion git intégré 
	:animate: fade-in-slide-down

	`Nubonyxia`_ est connectée à la *forge interministérielle* de la DGFiP. Cette dernière est hébergée sur une instance GitLab.
	Dans l'onglet :menuselection:`Mon Compte --> Services Externes ---> Configuration Git`
	Nous recommendons l'utilisation de la `forge`_ pour stocker vos codes et déployer des applications. Consulter le :doc:`guide des bonnes pratiques <methode>` pour plus d'informations sur l'utilisation de git et la :doc:`page <app>` pour le déploiement d'applications. 


.. dropdown:: une gestion de secret  
	:animate: fade-in-slide-down

	Certains usages requiert de fournir à un service des *crédentials* sous forme de secret - sans les écrire en clair dans le code de chaque service. Cela est géré par `Vault`_ dans notre cluster.



4- Lancement d'un service 
-------------------------

Utilsation : pip install grace au Nexus mis en place par la DGFIP 

L'interface utilisateur permet de configurer le service que l'on va lancer.
Onyxia facilite cette configuration en injectant directement certaines valeurs (token S3, token Git, secrets ...).
Pour une configuration plus détaillée, consulter :doc:`ici <services>`. 


Pour aller plus loin 
---------------------



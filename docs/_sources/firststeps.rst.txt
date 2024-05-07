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


			* `Vscode-python` : Vscode avec Python, Julia et une collection de packages *data science* intégrée  
			* `Vscode-pytorch`: Vscode enrichi avec le framework de *deep learning* :python:`pyorch`  
			* `Vscode-nodejs` : Vscode enrichi de `NodeJs runtime` et donc adapté pour le développement web. 
			* `jupyter-python`: JupterLab avec Python, Julia et une collection de packages *data science* intégrée 
			* `jupyter-pyspark`: JupyterLab intégrant `Apache Spark <https://spark.apache.org/docs/latest/api/python/index.html>`_ pour réaliser du calcul distribué avec Python.  
			* `R studio` : RStudio avec les packages de *data science* intégrés

		.. tab-item:: Gestion de base de données

			* `PostgreSQL <https://www.postgresql.org>`_
			* `Cloudbeaver <https://github.com/dbeaver/cloudbeaver>`_ 
			* `NocoDB <https://data-apis-v2.nocodb.com>`_ 

		.. tab-item:: Data Visualisation 

			* `Superset <https://superset.apache.org>`_

		.. tab-item:: Automation
			* GitlabRunner : pour le déploiement sur le cluster `Kubernetes`_ d'un job CI lancé sur la `forge`_. Voir la :doc:`page <app>` pour le déploiement d'applications.
			* Argo-cd 
			* Argo-workflows 


	.. note::
	
		Si vous avez besoin d'un service en particulier qui est indisponible dans notre catalogue, n'hésitez pas à nous en faire part. Nous sommes à l'écoute de nos utilisateurs pour enrichir notre catalogue !
	
	Vous trouverez :doc:`ici <services>` les explications sur la configuration des différents services. Des exemples de cas d'usages sont présentés dans cette :doc:`page <usecase>`.

	Les services lancés par l'utilisateur apparaissent dans l'onglet :menuselection:`Mes services`. Il est possible de lancer à la demande plusieurs services à la fois.   

	.. important:: 
		Les services ont des tokens d'expiration. Lorsqu'ils ne sont plus utilisés, pensez à bien les supprimer, voir :doc:`guide des bonnes pratiques <methode>`. 


.. _target to paragraph:

.. dropdown:: une connexion git intégrée
	:animate: fade-in-slide-down

	La sauvegarde des codes ainsi que la gestion des versions sont assurées par une instance **Git**. Le datalab de `Nubonyxia`_ facilite son implémentation en offrant une connexion à la *forge interministérielle* de la DGFiP. Cette dernière est hébergée sur une instance GitLab. La plateforme autorise également une connexion à GitHub. Nous recommendons toutefois l'utilisation de la `forge`_ pour stocker vos codes et déployer des applications afin de bénéficier du `RIE_ (ie, le réseau interministériel).


	
 	La configuration d'un serveur Git sur `Nubonyxia`_ ainsi que son utilisation sont détaillées dans la section :doc:`guide des bonnes pratiques <methode>`.
 

.. dropdown:: une gestion de secret  
	:animate: fade-in-slide-down

	Certains usages requiert de fournir à un service des *crédentials* sous forme de secret - sans les écrire en clair dans le code de chaque service. Cela est géré par `Vault`_ dans notre cluster.



4- Lancement d'un service 
-------------------------

Nous avons mis à disposition sur la `forge`_ un repo nommé `Quick Start <https://forge.dgfip.finances.rie.gouv.fr/bercyhub/nubonyxia/quick-start>`_ avec des scripts de *data visualisation* prêt-à-être exécutés. 

Pour lancer un service, il suffit de se rendre dans l'onglet :menuselection:`Catalogue de services`. Vous pouvez lancer le service IDE de votre choix. Le service lancé apparaît alors dans la page `Mes Services <https://nubonyxia.incubateur.finances.rie.gouv.fr/my-services>`_. L'accès au service se fait en cliquant sur le bouton :python:`Ouvrir`. Un mot de passe est alors fourni pour pouvoir accéder au service. Les informations relatives aux tokens peuvent être consultés en cliquant sur l'icône information en bas à gauche du service instancié. 

L'interface Onyxia permet de configurer le service que l'on va lancer comme le montre en détail la section :doc:`Configuration de services <services>`.

.. note::
	Les **tokens S3** et **git** sont déjà pré-configurés. 


Après avoir renseigné son token d'accès Gitlab dans le datalab (voir section :ref:`gitConfig`), l'utilisateur peut directement cloner le repo en s'identifiant avec son token stocké sous forme de variable d'environnement :python:`$GIT_PERSONAL_ACCESS_TOKEN` à l'aide de la ligne de commande suivante :  

.. code:: python

	git clone https://<gitlab-user>:$GIT_PERSONAL_ACCESS_TOKEN@forge.dgfip.finances.rie.gouv.fr/<owner>/<repo>.git

où :program:`<owner>` et :program:`<repo>` sont à remplacer respectivement par le nom d'utilisateur et le nom du repo Git.  


Il est également possible de cloner le repo au lancement du service dans l'interface, comme le montre la section :ref:`gitService`. 


Dans le service IDE , il est possible de télécharger en complément des librairies Python ou R, grâce au `Nexus` mis en place par la DGFIP. En effet bien que la plateforme soit isolée d'internet, un point d'accès à Pypi (librairies Python) et CRAN (packages R)est mis en place grâce à un mirroir (Nexus de la DGFiP). Il est ainsi possible de réaliser :program:`pip install` suivi de la librairie de votre choix pour Python et :program:`install.package("")` pour R.


4- Suppression d'un service 
-------------------------

Les services de développement comme :python:`vscode` ou :python:`jupyter-notebook` lancés sur la plateforme n'ont pas pour vocation d'être utilisés *ad vitam eternam*. De fait, les tokens d'accès expirent au bout d'un certain temps. Il faut donc supprimer le service et en relancer un autre. Pour ce faire, cliquer sur l'icône poubelle figurant en dessous du sevice instancié.    

.. important::
	Les ressources nécessaires à la bonne exécution des services sont partagées au sein de la communauté des utilisateurs. Pensez donc à bien supprimer les services que vous n'utlisez plus afin de libérer des ressources.


.. warning:: 
	Avant de supprimer un service, pensez à bien sauvegarder vos codes et vos données comme illustré dans la section :doc:`methode`. En effet, pour certains services, la suppression d'une instance est susceptible d'entraîner la suppression de toutes les données associées. 


Pour aller plus loin 
---------------------



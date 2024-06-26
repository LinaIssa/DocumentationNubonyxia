Premiers pas avec Nubonyxia
============================

Cette page offre une visite guidée de `Nubonyxia`_ et donne une description *pas à pas* des différentes étapes du lancement d'un service sur la plateforme. 

.. role:: bash(code)

    :language: bash 

1- Ajout du certificat dans le navigateur
-----------------------------------------

Dans un premier temps, avant d’accéder à la plateforme, il est nécessaire d’ajouter le certificat, accessible `ici <https://nubonyxia.incubateur.finances.rie.gouv.fr/statics/bercyCA.crt>`_, dans le navigateur de votre choix. En effet, nous travaillons pour le moment avec un certificat auto-signé. 


.. note::

	Cette manipulation est à faire une seule fois.



.. tab-set::

	.. tab-item:: avec Firefox 

		* Aller dans le menu :menuselection:`Paramètres --> Certificats`
		* Cliquer sur le bouton :python:`Afficher les certificats`
		* Aller dans l'onglet :python:`Autorités`  
		* Cliquer sur le bouton :python:`Importer` et sélectionner le certificat **bercyCA.crt**

	.. tab-item:: avec Edge  

		* Aller dans les paramètres du navigateur, chercher Certificats 
		* Cliquer sur :python:`Gérer les certificats` qui devrait ouvrir une fenêtre Windows
		* Sélectionner l'onglet Autorités de certification racine de confiance
		* Importer le certificat **bercyCA.crt**

2- Connexion à la plateforme 
----------------------------


L'accès à la plateforme se fait en utilisant **l'identifiant** et le **mot de passe** fourni par l'équipe support de Nubonyxia. Nous utilisons `keycloak <https://www.keycloak.org>`_ pour gérer l'authentification. 

.. note:: 
	Nous travaillons actuellement à intégrer **agent connect** à la plateforme. Pour le moment, en l'absence de fédérateur d'identité, nous gérons à la main les comptes utilisateurs.


3- Vue générale de la plateforme 
--------------------------------

L'interface du datalab `Nubonyxia`_ est très largement inspirée de celle du `SSP Cloud`_. Son architecturelle fonctionnelle peut se résumer schématiquement comme le montre  :numref:`schema`.

.. _schema:


.. figure:: images/nubonyxia-architecture-fonctionnelle.png
  :width: 800
  :alt: Alternative text

  Architecture Fonctionnelle de Nubonyxia 




A la disposition de l'utilisateur : 


.. dropdown:: un espace de stockage
    :animate: fade-in-slide-down 

    `Nubonyxia`_ n'échappe pas à la tendance de fond observée dans la Data et le Cloud, qui consiste à séparer l'espace de stockage des données des services où elles sont traitées. Pour plus d'informations sur le bucket S3 basé sur `MinIO`_, consulter cette :doc:`page <minio>`.   

    Cette séparation entre l'espace de stockage des données et l'environnement où elles sont traitées offre plusieurs avantages : 

    * découpler le stockage et le calcul,
    * garantir une **reproductibilité des analyses**, 
    * permettre une **optimisation des coûts**. En effet, on peut dès lors adapter les ressources en fonction des besoins de stockage et de calcul.

     

.. dropdown:: un catalogue de services 
	:animate: fade-in-slide-down

	
	Les services mis à la disposition des utilisateurs sont dans l'onglet :menuselection:`Catalogue de services`. Ces derniers se répartissent selon plusieurs catégories et permettent de répondre à un large spectre de cas d'usages *data*. 

	.. tab-set:: 

		.. tab-item:: IDE


			* :python:`Vscode-python` : Vscode avec Python, Julia et une collection de packages *data science* intégrés
			* :python:`Vscode-pytorch`: Vscode enrichi avec le framework de *deep learning* :python:`pyorch`  
			* :python:`Vscode-nodejs` : Vscode enrichi de `NodeJs runtime` et donc adapté pour le développement web. 
			* :python:`jupyter-python`: JupterLab avec Python, Julia et une collection de packages *data science* intégrés
			* :python:`jupyter-pyspark`: JupyterLab intégrant `Apache Spark <https://spark.apache.org/docs/latest/api/python/index.html>`_ pour réaliser du calcul distribué avec Python.  
			* :python:`R studio` : RStudio avec les packages de *data science* intégrés

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
		Certains tokens de configuration expirent au bout d'un certain temps, comme le token d'accès `MinIO`_ . Pour mettre à jour le token, il suffit de reprendre les scripts disponibles dans :menuselection:`Mon compte --> Connexion au stockage` (voir :ref:`tokenMinio` pour plus d'explications) et de les intégrer au service. Une autre option consiste simplement à supprimer le service, après sauvegarde de ses données dans `le bucket S3 <https://nubonyxia.incubateur.finances.rie.gouv.fr/my-files/>`_ d'une part et les codes dans une instance Git d'autre part. Consulter le :doc:`guide des bonnes pratiques <methode>` pour plus d'informations sur la méthodologie recommandée.  



.. dropdown:: une connexion git intégrée
	:animate: fade-in-slide-down

	La sauvegarde des codes ainsi que la gestion des versions sont assurées par une instance **Git**. Le datalab de `Nubonyxia`_ facilite son implémentation en offrant une connexion à la *forge interministérielle* de la DGFiP. Cette dernière est hébergée sur une instance GitLab. La plateforme autorise également une connexion à GitHub. Nous recommendons toutefois l'utilisation de la `forge`_ pour stocker vos codes et déployer des applications afin de bénéficier du `RIE`_ (ie, le réseau interministériel).


	
 	La configuration d'un serveur Git sur `Nubonyxia`_ ainsi que son utilisation sont détaillées dans la section :doc:`guide des bonnes pratiques <methode>`.

 
.. _secretCreate:

.. dropdown:: une gestion de secret  
	:animate: fade-in-slide-down
	

	Certains cas d'usages justifent de fournir à un service des variables d'environnement sous forme de secret - sans les écrire en clair dans le code de chaque service. Cela est géré par `Vault`_ dans notre plateforme. 
	Se référer à la section :ref:`gestionVault` pour la création et la gestion des variables d'environnement.

4- Lancement d'un service 
-------------------------

Nous avons mis à disposition sur la `forge`_ un repo nommé `Quick Start <https://forge.dgfip.finances.rie.gouv.fr/bercyhub/nubonyxia/quick-start>`_ avec des scripts de *data visualisation* prêt-à-être exécutés. 

Pour lancer un service, il suffit de se rendre dans l'onglet `Catalogue de services <https://nubonyxia.incubateur.finances.rie.gouv.fr/my-services/>`_. Vous pouvez lancer le service IDE de votre choix. Le service lancé apparaît alors dans la page `Mes Services <https://nubonyxia.incubateur.finances.rie.gouv.fr/my-services>`_. L'accès au service se fait en cliquant sur le bouton :python:`Ouvrir`. Un mot de passe est alors fourni pour pouvoir accéder au service. Les informations relatives aux tokens peuvent être consultés en cliquant sur l'icône information en bas à gauche du service instancié. 

.. important::
	Il est possible de lancer différentes instances d'un même service. Ainsi on peut avoir différent services :python:`vscode` qui tournent en même temps sur la plateforme. Cela ne s'applique pas pour les services reposant sur des *permanent virtual circuit* (PVC) à l'instar des services de la catégorie **base de données** comme :python:`Postgresql`. Autrement dit, si un service :python:`Postgresql` est déjà ouvert, il faut d'abord le supprimer avant d'en lancer un nouveau. Il en est de même pour le service :python:`Superset`.



L'interface Onyxia permet de configurer le service que l'on va lancer comme le montre en détail la section :doc:`Configuration de services <services>`.

.. note::
	Les **tokens S3** et **git** sont déjà pré-configurés. 


Après avoir renseigné son token d'accès Gitlab dans le datalab (voir section :ref:`gitConfig`), l'utilisateur peut directement cloner le repo en s'identifiant avec son token stocké sous forme de variable d'environnement :python:`$GIT_PERSONAL_ACCESS_TOKEN` à l'aide de la ligne de commande suivante :  


.. code:: bash

	git clone https://<gitlab-user>:$GIT_PERSONAL_ACCESS_TOKEN@forge.dgfip.finances.rie.gouv.fr/<owner>/<repo>.git

où :program:`<owner>` et :program:`<repo>` sont à remplacer respectivement par le nom d'utilisateur et le nom du repo Git.  


Il est également possible de cloner le repo au lancement du service dans l'interface, comme le montre la section :ref:`gitService`. 


Dans le service IDE , il est possible de télécharger en complément des librairies Python ou R, grâce au `Nexus` mis en place par la DGFIP. En effet bien que la plateforme soit isolée d'internet, un point d'accès à Pypi (librairies Python) et CRAN (packages R) est mis en place grâce à un miroir (Nexus de la DGFiP). Il est ainsi possible de réaliser :program:`pip install` suivi de la librairie de votre choix pour Python et :program:`install.package("")` pour R.
	 



4- Suppression d'un service 
-------------------------

Les services de développement comme :python:`vscode` ou :python:`jupyter-notebook` lancés sur la plateforme n'ont pas pour vocation d'être utilisés *ad vitam eternam*. De fait, les tokens d'accès expirent au bout d'un certain temps. Il faut donc supprimer le service et en relancer un autre. Pour ce faire, cliquer sur l'icône poubelle figurant en dessous du sevice instancié.    

.. important::
	Les ressources nécessaires à la bonne exécution des services sont partagées au sein de la communauté des utilisateurs. Pensez donc à bien supprimer les services que vous n'utlisez plus afin de libérer des ressources.


.. warning:: 
	Avant de supprimer un service, pensez à bien sauvegarder vos codes et vos données comme illustré dans la section :doc:`methode`. En effet, pour certains services, la suppression d'une instance est susceptible d'entraîner la suppression de toutes les données associées. 


Les services de bases de données s'appuyant sur des PVC, la suppression complète se fait avec la ligne de commande :program:`kubectl delete PVC` suivi du nom du volume. Cette dernière est indiquée dans la fenêtre qui s'ouvre lors du lancement du service, comme le montre l'image ci-après. 



.. image:: images/deletepvc.png
  :width: 800
  :alt: Alternative text

.. important:: 
	Pour exécuter la ligne de commande :program:`kubectl delete PVC`, il faut ouvrir un vscode et sélectionner le role *admin* dans l'onglet **Kubernetes** présent dans la configuration (voir section :ref:`servicesConfig`)


Pour aller plus loin 
---------------------



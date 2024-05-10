Configuration des services
==========================


`Nubonyxia`_ met à la disposition des utilisateurs des services ainsi que des ressources en CPU et en RAM. Par exemple, pour les services *data science* comme `RStudio` ou `Vscode`, il est possible de réserver jusqu'à **30 000 milliCPU** et **32Gi de RAM** 

Une fois un nouveau service lancé, il apparait dans l'onglet :menuselection:`Mes services`.  

Au moment du lancement d'un service, en plus des ressources évoquées, différentes options de configurations sont possibles. 
Cette section s'attache à couvrir ces différentes options. 

.. important::

	Donner un nom personnalisé à son service permet de s'y retrouver lorsque l'on a plusieurs services :python:`RStudio` ou :python:`VScode` ouverts en parallèle. 
	
.. _servicesConfig:

Options de configurations 
-------------------------

Suivant le service lancé, différents onglets de configurations sont disponibles. Cette section présente les options les plus couramment utilisées. 

.. tab-set::

	.. tab-item:: S3 

		La connection du service à son espace de stockage S3 est déjà configurée. On peut laisser tel quel cet onglet. 
		
	.. tab-item:: Kubernetes   

		Pour pouvoir utiliser les commandes :program:`kubectl`, il faut sélectionner le role *admin*. Par défaut, *role* est sur *viewer*. Cela peut être utile lorsque l'on souhaite par exemple vérifier l'état des pods. Consulter la section :ref:`commandKubectl` pour avoir un aperçu des commandes que vous pouvez exécuter. 

	.. tab-item:: Init   

		Il est possible de fournir un script d'initialisation qui va s'exécuter à l'ouverture du service. Cela permet d'automatiser des configurations spécifiques d'un service. 

		* `PersonalInit`: lien vers un script shell. 

		* `PersonalInitArgs`: options correspondant aux variables :python:`$1` :python:`$2` dans le script init

		Par exemple, si *PersonalInitArgs* corresponde à :python:`fichier1.txt fichier2.txt` et que le script init soit le suivant: 

		.. code:: python

  			#!/bin/bash
			touch $1
			touch $2

		alors le script va créer les fichiers :python:`fichier1.txt` et :python:`fichier2.txt` grâce à la commande :program:`touch`

	.. tab-item:: Onyxia 

	.. tab-item:: Ressources  

		Déplacer le curseur pour définir la plage de ressources souhaitée 

		* CPU
		* RAM

		.. note:: 

			Les ressources du cluster étant mutualisées, il est de bon ton de réserver les ressources adaptées à ses besoins et son cas d'usage. 


	.. tab-item:: Networking 


   
	.. tab-item:: Security 

		Il est possible de partager de manière ponctuelle un service lancé à un autre agent. Pour ce faire, il faut décocher *Enable IP protection* et *Enable network policy*. 

		.. note::
			L'utilisation simultannée d'un service est impossible. Une seule personne à la fois peut se connecter à un service.

		.. warning::
			Il est recommandé de définir un mot de passe propre au service que l'on souhaite partager dans *Password*. 



	.. tab-item:: Git

		* `Token` : Il s'agit du jeton d'accès défini sur la plateforme Git utilisée (GitLab, GitHub ou bien la `forge`_)
		* `Repository` : Il s'agit de l'url du repo à cloner, obtenue à partir de la plateforme git utilisée (GitLab, GitHub ou bien la `forge`_) en cliquant sur :menuselection:`Cloner --> HTTPS`. 


	.. tab-item:: Service


	.. tab-item:: Persistence





	.. tab-item:: Vault  



	


Gestion des secrets 
--------------------


Configurer le proxy 
--------------------


Pour accéder à Internet, il faut recourir au **proxy** du SNUM. Des exemples de code sont inclus ci-dessous pour lancer une requète http sur Internet.

L'adresse IP du proxy est **172.16.0.53**.

.. tab-set::

    .. tab-item:: R

                
        .. code:: R

         	proxy_host <- "172.16.0.53"
			proxy_port <- "3128"

			url <- "http://example.com"

			output_file <- "output.txt"

			curl_command <- sprintf(
			'curl -x %s:%s %s -o %s',
			proxy_host, proxy_port, url, output_file
			)

			system(curl_command)
          

    .. tab-item:: Python

        
        .. code:: python

        	import requests
        	import os

        	PROXY = '172.16.0.53:3128'
        	proxies = { "http": PROXY,
        		    "https": PROXY
        		    }

        	URL='monURL'
        	AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"

        	session = requests.Session()
        	session.get_adapter("https://").proxy_manager_for(f"http://{PROXY}").proxy_headers["User-Agent"] = AGENT
        	session.proxies.update(proxies)

        	req  = requests.Request("GET", URL)
        	preq = req.prepare()
        	r    = session.send(preq)

        	print(r.content)


Le proxy peut s'employer lorsque l'on cherche à récupérer des données via API, comme le montre le notebook disponible sur ce `repo git <https://forge.dgfip.finances.rie.gouv.fr/bercyhub/nubonyxia/python-demonstration/-/blob/main/UseCase_API.ipynb?ref_type=heads>`_



Configuration des services
==========================


`Nubonyxia`_ met à la disposition des utilisateurs des services ainsi que des ressources en CPU et en RAM. Par exemple, pour les services *data science* comme `RStudio` ou `Vscode`, il est possible de réserver jusqu'à **30 000 milliCPU** et **32Gi de RAM** 

lister extension disponible dans vscode 

Au moment du lancement d'un service, en plus des ressources évoquées, différentes options de configurations sont possibles. 
Cette section s'attache à couvrir ces différentes options. 

.. important::

	Donner un nom personnalisé à son service permet de s'y retrouver lorsque l'on a plusieurs services `RStudio` ou `VScode` ouverts en parallèle. 
	
Partager le service

Connecter son service à l'espace de stockage S3

Kubernetes

Init 

PersonalInit 
Onyxia 
Ressources 
Networking 
Security 
Git 
Vault 

.. warning:: 
Les services de bases de données s'appuient sur PVC -> penser à delete PVC si le service ne se lance pas 


Une fois un nouveau service lancé, il apparait dans l'onglet :menuselection:`Mes services`.  

Connexion Proxy
---------------


Pour accéder à Internet, il faut recourir au proxy du SNUM. Des exemples de code sont inclus ci-dessous pour lancer une requète http sur Internet.

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



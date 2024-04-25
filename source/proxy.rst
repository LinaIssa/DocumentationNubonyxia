Connexion Proxy
===============


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



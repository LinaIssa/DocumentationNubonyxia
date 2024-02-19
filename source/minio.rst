Stockage de données dans Nubonyxia 
====================================

exemples : création de liens permanents, lignes de commande mc utiles 

Principes de fonctionnement
----------------------------

def espace de stockage S3 
attribution d'un bucket S3 personnel accessible dans la plateforme, dans l'onglet Mon Compte 

 

La création d'un compte Nubonyxia donne accès à un *bucket S3* personnel, porté par `MinIO <https://min.io>`_. 
Ce dernier correspond à une solution de stockage de données de type objets compatible avec l'API S3 d'Amazon. 

Gestion de son bucket S3 
----------------------------------

Il est possible d'intéragir avec son espace de stockage en se rendant dans l'onglet `Mes fichiers` : on peut téléverser directement des données depuis son ordinateur local et télécharger des données. 



Utilisation des données depuis un service 
----------------------------------

.. tab-set::

    .. tab-item:: R

       	En R, l'interaction avec un système de fichiers compatible S3 est rendu possible par la librairie `aws.s3`.
                
        .. code:: R

        	library(aws.s3)

                
 		
        Then, we can initialise the :py:class:`~.CigaleSED` object as follows:
        

    .. tab-item:: Python

    	En Python, l'interaction avec un système de fichiers compatible S3 est rendu possible par deux librairies :

		* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), une librairie créée et maintenue par Amazon ;
		* [S3Fs](https://s3fs.readthedocs.io/en/latest/), une librairie qui permet d'interagir avec les fichiers stockés à l'instar d'un _filesystem_ classique.

		Pour cette raison et parce que S3Fs est utilisée par défaut par la librairie [pandas](https://pandas.pydata.org) pour gérer les connections S3, nous allons présenter la gestion du stockage sur MinIO via Python à travers cette librairie.

        
        
        .. code:: python
       

            import os
			import s3fs

			# Create filesystem object
			S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
			fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': S3_ENDPOINT_URL})
	
        
    	where :python:`'example'` is the name of the directory within which the output files will be stored, :python:`['F435W', 'F606W', 'F775W']` is the list of filters to use for the SED fitting. The argument :python:`uncertainties` can be used to define for which filters the uncertainties should be used in the fit. 



    .. tab-item:: mc


		MinIO propose un client en ligne de commande (`ùc`) qui permet d’interagir avec le système de stockage à la manière d'un _filesystem_ UNIX classique. Ce client est installé par défaut et accessible via un terminal dans les différents services du Datalab.

		Le client MinIO propose les commandes UNIX de base, telles que ls, cat, cp, etc. La liste complète est disponible dans la [documentation du client](https://docs.min.io/docs/minio-client-complete-guide.html).

        
            
   
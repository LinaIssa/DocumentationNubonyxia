Stockage de données dans Nubonyxia 
====================================

mettre comment créer  des tokens d'accès permanents, lignes de commande mc utiles 

Les espaces de stockages sur Nubonyxia 
-------------------------------------------

def espace de stockage S3 
attribution d'un bucket S3 personnel accessible dans la plateforme, dans l'onglet Mon Compte 

La plateforme Nubonyxia utilise `MinIO <https://min.io>`_ comme solution cloud de stockage objet. Cette dernière, compatible avec  l'API S3 d'Amazon, offre la possibilité d'intéragir avec les fichiers stockés depuis n'importe quel service lancé sur la plateforme.  

La création d'un compte Nubonyxia donne accès à un *bucket S3* individuel. Sur demande uniquement, nous pouvons créer un bucket S3 partagé. 

De plus,chaque service de développement (VSCode, etc) dispose d'un espace de stockage **NFS** (*Network File System*). Ce dernier, par construction local et temporaire, a la même durée de vie que le service.

Enfin, il est possible de créer des services de base de données comme **PostgreSQL**, qui ouvre accès à un espace de stockage persistent **PVC** (*Permanent Virtual Circuit*)


Gestion de son bucket S3 
----------------------------------


Espace de stockage S3 
#####################

La plateforme dispose d'un `explorateur de fichiers` accessible dans l'onglet :menuselection:`Mes fichers` où est représenté le bucket S3 de l'utilisateur. 

A partir de cet onglet, il est possible d'intéragir avec son espace de stockage en : 
	* important des données depuis son repo local vers son bucket S3
	* créant des dossiers 
	* téléchargeant de la donnée 

Partage des données 
#####################################

.. note::
        
    TO DO : vérifier partage de liste de diffusion sur Nubonyxia comme sur Onyxia :https://docs.sspcloud.fr/onyxia-guide/stockage-de-donnees#partager-des-donnees  


Utilisation des données depuis un service 
#####################################

La connexion à son espace de stockage S3 depuis un service se fait grâce à un `token` d'accès. Ce dernier est intégré sous forme de `variable d'environnement` dans le service. 

.. warning::
        
    Le token d'accès à MinIO expire au bout de .... 





.. tab-set::

    .. tab-item:: R

       	En R, l'interaction avec un système de fichiers compatible S3 est rendu possible par la librairie `aws.s3`.
                
        .. code:: R

        	library(aws.s3)

                
 	        

    .. tab-item:: Python

    	En Python, l'interaction avec un système de fichiers compatible S3 est rendu possible par deux librairies :

    	* :python:`Boto3`, une librairie créée et maintenue par Amazon
    	* :python:`S3Fs` une librairie qui permet d'interagir avec les fichiers stockés à l'instar d'un *filesystem* classique.

		Pour cette raison et parce que S3Fs est utilisée par défaut par la librairie :python:`pandas` pour gérer les connections S3, nous allons présenter la gestion du stockage sur MinIO via Python à travers cette librairie.
		<https://boto3.amazonaws.com/v1/documentation/api/latest/index.html>
		<https://s3fs.readthedocs.io/en/latest/>
		<https://pandas.pydata.org>

        
        .. code:: python

            import os
            import s3fs

	Create filesystem object

		.. code:: python

			S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
			fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': S3_ENDPOINT_URL})


	Pour lister les fichiers d'un bucket: 

		.. code:: python
       
			BUCKET = "donnees-insee"
			fs.ls(BUCKET)


	Importer des données dans Python


		Le package :python:`S3Fs` permet d'interagir avec les fichiers stockés sur MinIO comme s'il s'agissait de fichiers locaux. La syntaxe est donc très familière pour les utilisateurs de Python. Par exemple, pour importer/exporter des données tabulaires via :python:`pandas`:

		.. code:: python
       

			BUCKET = "donnees-insee"
			FILE_KEY_S3 = "BPE/2019/BPE_ENS.csv"
			FILE_PATH_S3 = BUCKET + "/" + FILE_KEY_S3

			with fs.open(FILE_PATH_S3, mode="rb") as file_in:
 		    df_bpe = pd.read_csv(file_in, sep=";")
	
		Exporter des données vers MinIO


		.. code:: python
  
			BUCKET_OUT = "<mon_bucket>"
			FILE_KEY_OUT_S3 = "mon_dossier/BPE_ENS.csv"
			FILE_PATH_OUT_S3 = BUCKET_OUT + "/" + FILE_KEY_OUT_S3

			with fs.open(FILE_PATH_OUT_S3, 'w') as file_out:
		    df_bpe.to_csv(file_out)

    .. tab-item:: mc


		MinIO propose un client en ligne de commande (`mc`) qui permet d’interagir avec le système de stockage à la manière d'un *filesystem* UNIX classique. Ce client est installé par défaut et accessible via un terminal dans les différents services du Datalab.

		Le client MinIO propose les commandes UNIX de base, telles que ls, cat, cp, etc. La liste complète est disponible dans la [documentation du client](https://docs.min.io/docs/minio-client-complete-guide.html).







        
            
   
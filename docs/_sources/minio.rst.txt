Stockage de données dans Nubonyxia 
====================================


Les espaces de stockages sur Nubonyxia 
-------------------------------------------


La plateforme Nubonyxia utilise `MinIO`_ comme solution cloud de stockage objet. Cette dernière, compatible avec  l'API S3 d'Amazon, offre la possibilité d'intéragir avec les fichiers stockés depuis n'importe quel service lancé sur la plateforme.  

La création d'un compte Nubonyxia donne accès à un *bucket S3* individuel de **50 Go**.

De plus,chaque service de développement (VSCode, etc) dispose d'un espace de stockage **NFS** (*Network File System*). Ce dernier, par construction local et temporaire, a la même durée de vie que le service.

Enfin, il est possible de créer des services de base de données comme **PostgreSQL**, qui ouvre accès à un espace de stockage persistent **PVC** (*Permanent Virtual Circuit*)


Gestion de son bucket S3 
----------------------------------


Espace de stockage S3 
#####################

La plateforme dispose d'un `explorateur de fichiers` accessible dans l'onglet :menuselection:`Mes fichers` qui permet de visualiser le bucket S3 de l'utilisateur. 

A partir de cet onglet, il est possible d'intéragir avec son espace de stockage en : 
	* important des données depuis son repo local vers son bucket S3
	* créant des dossiers 
	* téléchargeant de la donnée 

Partage des données 
#####################################


Il est possible de partager de façon ponctuelle un fichier en partageant l'url du serveur *minio.lab.incubateur.finances.rie.gouv.fr*. Cette dernière s'obtient en cliquant sur un fichier dans son bucket personnel, puis en se rendant sur le menu déroulant contenant la ligne de commande :program:mc. Ce lien est partageable à toute personne ayant accès au RIE.



Espace de stockage commun
***************************

Si vous souhaitez disposer d'un **espace de stockage commun**, n'hésitez pas à nous écrire car nous pouvons créer un bucket S3 partagé **sur demande uniquement**.  

.. note:: 
	Le bucket partagé n'est pas accessible depuis l'explorateur de fichiers se trouvant dans l'onglet :menuselection:`Mes fichers` de la plateforme.  L’accès se fait uniquement une fois le service lancé, en ligne de commande.


Une fois le bucket partagé crée, un **bucket name**, **Access Key**  et **Secret Key** vous seront communiqués. La connexion se fait dans le terminal de n'importe quel service lancé. La configuration se fait comme pour accéder à son MinIO personnel, en s’aidant des scripts disponibles dans l’onglet :menuselection:`Mon Compte --> Connexion de stockage`. 
Voici un exemple, en utilisant la librairie :py:class:`~.Boto3` avec python:

.. code:: python

	s3 = boto3.client("s3",
	endpoint_url="https://"+os.environ["AWS_S3_ENDPOINT"],
	aws_access_key_id= os.environ["AWS_ACCESS_KEY_ID"],
	aws_secret_access_key= os.environ["AWS_SECRET_ACCESS_KEY"],
	aws_session_token = "",
	verify=False)

    # Construction de l'objet
 
	BUCKET = "my_bucket_name" # à remplacer par le bucket name fourni 
	FILE_PATH_S3 = "rie" + "/" + file_name
	obj = s3.get_object(Bucket=BUCKET, Key=FILE_PATH_S3)



avec **AWS_ACCESS_KEY_ID** correspond à l’Access Key fourni et **AWS_SECRET_ACCESS_KEY** à **Secret Key**

.. note:: 
	A la différence du bucket personnel, on ne met rien dans session token.
 



Utilisation des données depuis un service 
#####################################

La connexion à son espace de stockage S3 depuis un service se fait grâce à un `token` d'accès. Ce dernier est intégré sous forme de `variable d'environnement` dans le service. 

.. warning::
        
    Le token d'accès à MinIO expire au bout de **24 heures**. Les variables d'environnement sont automatiquement mises à jour. 





.. tab-set::

    .. tab-item:: R

       	En R, l'interaction avec un système de fichiers compatible S3 est rendue possible grâce à la librairie `aws.s3`.
                
        .. code:: R

        	library(aws.s3)

                
 	        

    .. tab-item:: Python

    	En Python, l'interaction avec un système de fichiers compatible S3 est rendue possible grâce à deux librairies :

    	* :py:class:`~.Boto3`, une librairie créée et maintenue par Amazon 
    	* :py:class:`~.S3Fs` une librairie qui permet d'interagir avec les fichiers stockés à l'instar d'un *filesystem* classique. S3Fs est utilisée par défaut par la librairie `pandas <https://pandas.pydata.org>`_ pour gérer les connections S3.

	Dans la suite, nous allons utiliser la librairie :python:`S3Fs` pour la gestion du stockage sur MinIO. 
        
        .. code:: python

            import os
            import s3fs
            S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
            fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': S3_ENDPOINT_URL})


	**Pour lister les fichiers d'un bucket**: 

	.. code:: python
       
		BUCKET = "donnees-insee"
		fs.ls(BUCKET)


	**Pour importer des données** en utilisant la librairie :python:`pandas` :


	.. code:: python
       

		BUCKET = "donnees-insee"
		FILE_KEY_S3 = "BPE/2019/BPE_ENS.csv"
		FILE_PATH_S3 = BUCKET + "/" + FILE_KEY_S3

		with fs.open(FILE_PATH_S3, mode="rb") as file_in:
 		df_bpe = pd.read_csv(file_in, sep=";")
	
	**Pour exporter des données vers son bucket S3**


	.. code:: python
  
		BUCKET_OUT = "<mon_bucket>"
		FILE_KEY_OUT_S3 = "mon_dossier/BPE_ENS.csv"
		FILE_PATH_OUT_S3 = BUCKET_OUT + "/" + FILE_KEY_OUT_S3

		with fs.open(FILE_PATH_OUT_S3, 'w') as file_out:
		df_bpe.to_csv(file_out)

	L'intéraction avec MinIO est illustrée dans ce `notebook <https://forge.dgfip.finances.rie.gouv.fr/bercyhub/nubonyxia/python-demonstration/-/blob/main/UseCase_MinIO.ipynb?ref_type=heads>`_ disponible sur la forge. 

    .. tab-item:: mc


		Avec la commande :program:`mc`, il est possible d’interagir avec le système de stockage à la manière d'un *filesystem* UNIX classique. Cette commande est installée par défaut et est accessible via un terminal dans les différents services de Nubonyxia. Elle s'utilise avec les commandes UNIX de base, telles que :program:`ls`, :program:`cat`, :program:`cp`, etc. La liste complète est disponible dans la `documentation <https://docs.min.io/docs/minio-client-complete-guide.html>`_.



.. _miniokeys:

Création des clés d'accès à `MinIO`_
####################################

Nubonyxia utilise `MinIO`_ pour stocker les caches nécessaires à la bonne exécution de la chaîne d'intégration de l'application que l'on cherche à déployer, voir la page :doc:`app` sur la mise en place d'une chaîne CI/CD. Il faut alors fournir les clés d'accès **AccessKey** et **SecretKey** à l'engin d'intégration continue, en l'occurence le `gitlab-runner` instancié depuis la plateforme. Ces clés sont crées une seule fois en se connectant à `MinIO`_. 

Pour ce faire, choisir le mode **STS** lors de sa connexion à `MinIO`_. Les tokens STS sont à récupérer dans :menuselection:`Mon compte --> Connexion au stockage` (https://nubonyxia.incubateur.finances.rie.gouv.fr/account/storage). 
Plus spécifiquement: 

* *STS Username*  correspond à **Access key id**
* *STS Secret*  correspond à **Secret access key**
* *STS Token*  correspond à **Session token**

.. note::
	Cliquez sur l'icône 'copier dans presse-papier' présente dans l'interface afin de copier les codes d'accès à `MinIO`_. 



Une fois connectée, il suffit de se rendre dans :menuselection:`Access Keys --> Create access key` 


.. warning:: 
	Pensez à bien sauvegarder les codes d'accès, dans un gestionnaire de mots de passe par exemple. 
 


        
            
   
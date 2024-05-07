Guide des bonnes pratiques 
===========================


Gestion de versions avec Git 
-----------------------------

.. _gitConfig:

Configuration du Git pour la première fois 
#########################################

Afin de pouvoir synchroniser ses codes avec un dépôt distant, il faut tout d'abord connecter `Nubonyxia`_ à un compte Git. La création d'un compte sur une forge Git est donc indispensable si l'on veut bénéficier de ce service. 

.. note::
 	Il est possible de créer un compte sur la forge Git de son choix, soit la forge interministérielle `GitLab <https://forge.dgfip.finances.rie.gouv.fr/>`_  accessible via `RIE`_, soit la forge `GitHub <https://github.com/signup>`_ exposé sur internet. 

1 - **création d'un token à partir de son compte git** : Sur son compte Git, générer un jeton d'accès personnel ou `token` permettant l'authentification auprès de la forge. Une fois généré, le token n'apparait qu'une seule fois. Il faudra alors bien le noter.    

2 - **configuration de git sur la plateforme**: Sur sa plateforme `Nubonyxia`_, se rendre dans l'onglet :menuselection:`Mon Compte --> Services Externes --> Configuration Git` et renseigner ses identifiants Git et le token. Ainsi, ce dernier sera accessible aux services lancés sur la plateforme.   


.. image:: images/configGIT.png
  :width: 800
  :alt: Alternative text

.. _gitService:

Utilisation de Git avec les services du Datalab 
###############################################


.. image:: images/configService.png
  :width: 800
  :alt: Alternative text




.. A retenir::
    -> Versionner son code à l'aide de Git 
    -> Sauvegarder ses données régulièrement dans le système de stockage S3. 


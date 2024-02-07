Déploiement CI/ CD d'applications
================================

.. important::

    Dans sa conception actuelle, **Nubonyxia** ne gère pas la mise en production des applicatifs webs déployés sur la plateforme. Si vous souhaitez la péréniser une application déployée sur notre plateforme, adressez vous directement à nous. 


Cette section décrit les étapes dans le déploiement d'une application développée en **R** et **Python**. 



Prérequis pour exécution d'un pipeline GitLab-CI
--------------------------------------------------


Les templates à utiliser sont disponibles pour `Python`_ <> et `R`_ <> -> insérer les liens correspondants 
Vous pouvez forker le repo qui vous intéresse et ajouter vos scripts dans le dossier *app*.

 
1. Configuration Onyxia
########################
Pour le bon fonctionnement du pipeline décrit dans le fichier :file:.gitlab-ci.yml`, il est nécessaire de respecter une certaine **convention de configuration**.

a. Mes secrets 
**************

Dans [Mes Secrets](https://nubonyxia.incubateur.finances.rie.gouv.fr/my-secrets/) de votre compte [NubOnyxia](https://nubonyxia.incubateur.finances.rie.gouv.fr), il doit y avoir un **secret**, par défaut choisissez comme nom `registries`. Dans ce secret, définissez deux variables :
- `USERNAME` correspond à votre `username` présent dans le menu **User Profile** de [Harbor](https://harbor.lab.incubateur.finances.rie.gouv.fr)
- `PASSWORD` correspond à votre `CLI secret` présent dans le menu **User Profile** de [Harbor](https://harbor.lab.incubateur.finances.rie.gouv.fr)

b. Runners
**********


Les jobs d'un pipeline GitLab-CI sont pris en charge et exécutés par un ou plusieurs `GitLab-Runners`. Il est possible de voir les runners actifs au niveau des paramètres du CI/CD du projet GitLab (menu `Settings / CI/CD / Runners`, une ligne avec un point vert apparaît si un runner est détecté).

Si aucun runner n'est déjà détecté, il faut en créer un. Pour cela, depuis la plateforme Onyxia, il est possible de lancer un service `GitLab-Runner` (catalogue `Automation Services`). Durant le paramétrage du service, il y a plusieurs champs à compléter : 

- dans l'onglet `Cache`, il faut remplir les champs `AccessKey` et `SecretKey` avec les clés d'accès à son bucket Minio (qui sera utilisé pour stocker les artefacts entre les différents jobs dans la pipeline). Pour obtenir sa clé d'accès Minio, se connecter à Minio : https://minio-console.lab.incubateur.finances.rie.gouv.fr/ (se connecter en mode STS et chercher les clés de connexion dans `Connexion au stockage` dans Onyxia). Puis dans l'onglet "Access Keys", cliquer sur "Create access key" et copier-coller les clés lors de la création du runner.

- dans l'onglet `Registration` dans la création du Gitlab runner, il faut renseigner le `Registration token` qui est trouvable dans GitLab (menu `Settings / CI/CD / Runners` du projet, cliquer sur les trois petits points à côté du bouton bleu `New project runner`).

- vous pouvez ensuite lancer votre `gitlab-runner.



2. Configuration GitLab
########################

a. Variables de projet
**********************
Il faut créer la variable `VAULT_TOKEN` depuis le menu `Settings / CI/CD / Variables` de votre projet GitLab : 

- `VAULT_TOKEN` correspond à la valeur **Vault Token** précisée dans [Mon compte / Vault](https://nubonyxia.incubateur.finances.rie.gouv.fr/account/vault) de la plateforme [NubOnyxia](https://nubonyxia.incubateur.finances.rie.gouv.fr). Cochez `protected` et `masked`.

b. Fichier :file:`gitlab-ci.yml`
*************************
Dans votre fichier `.gitlab-ci.yml`, il faut renseigner plusieurs variables :

- `NUBONYXIA_ID` correspond à votre identifiant Nubonyxia disponible dans [Mon Compte](https://nubonyxia.incubateur.finances.rie.gouv.fr/account) de la plateforme [NubOnyxia](https://nubonyxia.incubateur.finances.rie.gouv.fr)

- `NUBONYXIA_REGISTRY_SECRET` : par défaut, valeur à définir à `registries`, correspond au nom du secret créé précédemment [Mes Secrets](#mes-secrets)

- `REGISTRY_PROJECT` : durant l'étape de **deliver**, l'image générée dans l'étape **build** sera publiée dans Harbor dans le *registre* précisé dans cette variable. S'il n'existe pas dans Harbor, ll faut le créer (`Nouveau projet`).

- `REGISTRY_PROJECT_PUBLIC_ACCESS` : le registre du projet est considéré comme privé par défaut (ie `REGISTRY_PROJECT_PUBLIC_ACCESS: "false"`). Si le registry est public, il faut mettre cette variable à `true`.

- `USE_HELM` : la valeur doit être à `true`.

- `APPLICATION_NAME` : cette variable définit le nom d'application, cette variable a peu d'impact et sera visible dans Harbor dans le registre. Cette variable doit être composée de caractères alphanumériques minuscules.

- `CHART_NAME` : le nom du chart utilisé pour déploiement de l'application. Vous pouvez laisser la valeur par défaut `demo`. Si vous changez cette valeur, il faudra également changer la valeur dans le fichier `chart/Chart.yml`.


c. Fichier :file:`values.yaml`
***********************
Dans le fichier: 

- `imagePullSecrets\name`: mettre le même nom que `NUBONYXIA_REGISTRY_SECRET` (ex : `registries`)

- `ingress\hosts\host` : il faut choisir une URL pour votre application.

d. Dockerfile
*************

Dans le fichier, ajouter les dépendances R à installer dans la fonction `install.packages` ligne 8. 

3. Configuration Kubernetes
############################


Il faut ajouter un secret dans Kubernetes. Pour cela, ouvrir un service VSCode dans Onyxia, en prenant soin dans l'onglet Kubernetes de choisir le mode admin. Puis ouvrir un terminal dans VSCode et exécuter les commandes suivantes en remplaçant les variables `HARBOR_USERNAME`, `HARBOR_PASSWORD`. De plus ajouter, pour les variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, ajouter les clés Minio que [vous avez récupérées ici ](https://forge.dgfip.finances.rie.gouv.fr/bercyhub/nubonyxia/nubonyxia-r-app-example#b-runners): 

```
HARBOR_AUTH=$(echo -n "HARBOR_USERNAME:HARBOR_PASSWORD" | base64)

cat <<EOF > dockerconfig.json
{"auths":
  {"harbor.lab.incubateur.finances.rie.gouv.fr": {"auth": "<HARBOR_AUTH>"}
}}
EOF

kubectl create secret generic registries \
  --from-literal=AWS_DEFAULT_REGION=us-east-1 \
  --from-literal=AWS_S3_ENDPOINT="minio.lab.incubateur.finances.rie.gouv.fr" \
  --from-literal=AWS_ACCESS_KEY_ID="" \
  --from-literal=AWS_SECRET_ACCESS_KEY=""
```

Exécution de la pipeline
-------------------------

Une fois tous les prérequis remplis, la pipeline devrait se lancer automatiquement. Il est possible de voir son exécution dans l'onglet "Build" puis "Pipelines". Si tout se passe bien, chaque étape sera marquée d'une coche verte. Sinon, se reporter à la partie suivante.

Commande pour debugger 
-------------------------





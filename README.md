# Guide d'Installation et d'Utilisation : Python 3.13 & Pygame dans Docker (Windows)

Ce guide vous explique comment configurer votre environnement Windows pour développer avec Python et Pygame à l'intérieur d'un conteneur Docker, y compris l'affichage graphique.

## 1. Prérequis : WSL 2

Docker Desktop sur Windows fonctionne mieux avec le sous-système Windows pour Linux (WSL 2).

1.  Ouvrez **PowerShell** en tant qu'administrateur.
2.  Exécutez la commande suivante pour installer WSL :
    ```powershell
    wsl --install
    ```
3.  **Redémarrez votre ordinateur** si demandé.

## 2. Installation de Docker Desktop

1.  Téléchargez **Docker Desktop pour Windows** depuis le site officiel : [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2.  Lancez l'installateur (`Docker Desktop Installer.exe`).
3.  Assurez-vous que l'option **"Use WSL 2 instead of Hyper-V"** est cochée lors de l'installation.
4.  Une fois installé, lancez **Docker Desktop**.
5.  Allez dans les **Settings (roue dentée)** -> **Resources** -> **WSL integration** et assurez-vous que l'intégration est activée pour votre distribution Linux par défaut (ex: Ubuntu).

## 3. Configuration de l'Affichage Graphique (X Server)

Les conteneurs Docker n'ont pas d'écran. Pour voir la fenêtre Pygame, nous devons rediriger l'affichage vers Windows.

1.  Téléchargez et installez **VcXsrv Windows X Server** : [https://sourceforge.net/projects/vcxsrv/](https://sourceforge.net/projects/vcxsrv/)
2.  Lancez **XLaunch** (installé avec VcXsrv).
3.  Suivez l'assistant de configuration :
    *   **Display settings** : Choisissez "Multiple windows" (par défaut). Cliquez sur Suivant.
    *   **Client startup** : Choisissez "Start no client" (par défaut). Cliquez sur Suivant.
    *   **Extra settings** : **IMPORTANT !** Cochez la case **"Disable access control"**. Cela permet au conteneur de se connecter à votre écran.
    *   Cliquez sur Suivant, puis sur **Finish**.
    *   *Note : Vous devriez voir une icône "X" apparaître dans votre barre des tâches (zone de notification).*

## 4. Récupération du Projet

Si vous souhaitez utiliser ce projet comme base pour le vôtre, vous pouvez le cloner puis détacher l'historique Git pour repartir de zéro.

1.  Ouvrez un terminal (PowerShell ou Git Bash).
2.  Clonez le dépôt :
    ```bash
    git clone https://github.com/e-baloo/docker-python-dev-env.git
    ```
3.  Entrez dans le dossier :
    ```bash
    cd docker-python-dev-env
    ```
4.  Supprimez le dossier `.git` pour effacer l'historique et délier le projet du dépôt d'origine :
    *   **PowerShell** : `Remove-Item -Recurse -Force .git`
    *   **Bash** : `rm -rf .git`

## 5. Lancer le Projet dans le Dev Container

1.  Ouvrez ce dossier (`python-dev-env` ou `docker-python-dev-env`) dans **VS Code**.
2.  Assurez-vous d'avoir l'extension **Dev Containers** installée dans VS Code (Microsoft).
3.  Une notification devrait apparaître en bas à droite : *"Folder contains a Dev Container configuration file. Reopen folder to develop in a container"*. Cliquez sur **Reopen in Container**.
    *   *Alternative :* Appuyez sur `F1` (ou `Ctrl+Shift+P`), tapez `Dev Containers: Reopen in Container` et sélectionnez-le.
4.  Attendez que VS Code construise l'image Docker (cela peut prendre quelques minutes la première fois).

## 6. Exécuter l'Exemple Pygame

Une fois le conteneur lancé (vous verrez "Dev Container: Python..." en bas à gauche de VS Code) :

1.  Ouvrez un terminal intégré dans VS Code (`Ctrl+ù` ou Terminal -> New Terminal).
2.  Configurez la variable d'affichage pour pointer vers votre hôte Windows :
    ```bash
    export DISPLAY=host.docker.internal:0
    ```
3.  Lancez le script :
    ```bash
    python main.py
    ```

Une fenêtre blanche avec un cercle bleu devrait apparaître sur votre bureau Windows !

---

### Dépannage

*   **Erreur "cannot connect to X server"** : Vérifiez que VcXsrv est bien lancé et que vous avez bien coché **"Disable access control"**. Vérifiez aussi que votre pare-feu Windows autorise VcXsrv.
*   **Lenteur** : L'affichage via X Server peut parfois être un peu lent par rapport à une exécution native, mais c'est suffisant pour du développement simple.

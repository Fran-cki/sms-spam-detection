1. Une application web accessible via une URL 
	https://spam-detection-ai.vercel.app/

2 Un modèle ML entraîné ou un script d’entraînement reproductible 
	Dans la repository (Dossier "Construction")

3. Le code source accessible sur GitHub. En particulier, un README.md contant notamment : 
	a. Le nom de notre institut : ISPM – Institut Supérieur Polytechnique de Madagascar et l’adresse de 
	notre site web
	=> www.ispm-edu.com 


	b. Ne nom de chaque membre de l’équipe et son rôle respectif 
		- IMTICIA5 : VELOMITASAONA Francki Aldo (Rôle : Data science)
		- IMTICIA5 : RAKOTONDRAMANANA Mamisoa Désiré (Rôle : Dévéloppeur frontend)
		- IMTICIA5 : RAMAMPIANDRA Andriiaina Landry (Rôle : Dévéloppeur backend)
		- IGGLIA5 : BEZARA Donatien Jamie (Rôle : Collecte dataset)
		- IMTICIA5 : RAKOTOMAMONJY Sitrakiniaina José (Rôle : Designer)
		- ESIIA5 : ANDRIARIMANANA Andy Andriniaina (Rôle : DevOps)

	c. La description du stack technologique 
		Pour ce projet, nous avons choisi un stack moderne, robuste et orienté "Production" :
	
		Langage : Python 3.x (Le standard pour la Data Science).

		Environnement : Jupyter Notebook (Développement et visualisation).

		Manipulation de données : Pandas (Chargement et nettoyage du CSV).

		Machine Learning : Scikit-Learn (Création du pipeline, vectorisation et modèle).

		Traitement du langage (NLP) : NLTK (Pour la gestion spécifique des Stop Words français).

		Visualisation : Matplotlib et Seaborn (Matrices de confusion et courbes d'apprentissage).

		Déploiement : FastAPI & Uvicorn (Pour transformer le modèle en service web ultra-rapide).

		Export : Joblib (Sérialisation du pipeline complet).


	d. La description du processus et du modèle  
		Nous avons implémenté un Pipeline de bout en bout pour garantir la cohérence des données entre l'entraînement et l'application réelle.

		Prétraitement : Nettoyage des textes, mise en minuscules et suppression des mots vides (Stop Words) français.

		Vectorisation (TF-IDF) : Transformation du texte en vecteurs numériques en utilisant des unigrammes et des bigrammes (n-grams).

		Le Modèle : Multinomial Naive Bayes (MNB). C'est un modèle probabiliste basé sur le théorème de Bayes. Il est particulièrement efficace pour la 		classification de textes courts (SMS) car il traite très bien les fréquences d'apparition des mots.

		Décision : Utilisation d'un seuil de probabilité personnalisé (0.85) au lieu du seuil par défaut (0.50) pour minimiser drastiquement les Faux Positifs 		(messages importants bloqués par erreur).


	e. Les méthode ML 
		Notre projet combine plusieurs concepts clés du Machine Learning :

		Apprentissage Supervisé : Le modèle apprend à partir d'exemples déjà annotés (Spam/Ham).

		Classification Binaire : La tâche consiste à classer une donnée dans l'une des deux catégories possibles.

		NLP (Natural Language Processing) :

		Tokenisation : Découpage du texte en mots.

		TF-IDF (Term Frequency-Inverse Document Frequency) : Une méthode qui valorise les mots "clés" et pénalise les mots trop fréquents.

		n-grams : Analyse de groupes de mots (ex: "cliquez ici") pour capturer le contexte.

		Évaluation Statistique : Utilisation de la Matrice de Confusion, du Rapport de Classification (Précision/Rappel) et de la Courbe d'apprentissage.

	f. Les datasets utilisés 
		Source : "SMS Spam Collection" disponible sur Kaggle.

		Composition : Un ensemble de plus de 5 000 messages textuels étiquetés comme "ham" (légitime) ou "spam".

		Adaptation : Bien que le dataset source soit majoritairement en anglais, nous avons adapté le processus pour traiter la langue française en intégrant 		des dictionnaires de mots vides français et en préparant le modèle à identifier des structures de phrases propres aux spams francophones.

		Répartition : 80% des données pour l'entraînement (Train Set) et 20% pour l'évaluation finale (Test Set).

	g. Le lien vers l’application web hébergée. 
		https://spam-detection-ai.vercel.app/

	h. Le lien vers la vidéo de démonstration (facultatitif) 
		https://spam-detection-ai.vercel.app/explication#demo-video
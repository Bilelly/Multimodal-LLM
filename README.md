# 🚀 Multimodal-LLM

Une plateforme complète en Python pour des applications d'IA multimodale basées sur des modèles de langage Hugging Face et des transformers de vision.

## 📋 À propos

**Multimodal-LLM** est une application  qui combine les capacités des Grands Modèles de Langage (LLMs) et des Modèles Vision-Langage (VLMs) pour effectuer des tâches avancées de traitement du langage naturel et de vision par ordinateur. Cette plateforme offre une interface intuitive pour traiter du texte, des images et des documents via une API unifiée.

### ✨ Fonctionnalités principales

- 🖼️ **Conversion Image vers Texte** : Générez des descriptions textuelles à partir d'images avec BLIP
- 🔍 **Reconnaissance d'Entités Nommées** : Extrayez et classifiez les entités du texte
- 📝 **Résumé de Texte** : Résumez automatiquement du contenu long et extrayez les points clés
- 🧠 **RAG** : Interrogez des documents PDF avec recherche sémantique via FAISS
- 🎯 **Analyse d'Images Avancée** : Combinez la génération de légendes avec la résumé pour une analyse approfondie

## 🛠️ Stack Technologique

- **Interface** : Streamlit
- **Framework LLM** : Hugging Face Inference API
- **Modèles Vision** : Salesforce BLIP (génération de légendes)
- **Base de Données Vectorielle** : FAISS 
- **Embeddings** : Sentence Transformers
- **Traitement Documentaire** : PyPDF2

## 📦 Installation

### Prérequis
- Python 3.8 ou supérieur
- Un token API Hugging Face (obtenez-le sur https://huggingface.co/settings/tokens)

### Configuration

1. **Clonez le dépôt**
   ```bash
   git clone https://github.com/Bilelly/Multimodal-LLM.git
   cd Multimodal-LLM
   ```

2. **Créez un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installez les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez votre token Hugging Face**
   - Option A : Créez `.streamlit/secrets.toml`
     ```toml
     HF_TOKEN = "votre_token_hugging_face_ici"
     ```
   - Option B : Définissez une variable d'environnement
     ```bash
     export HF_TOKEN="votre_token_hugging_face_ici"
     ```


### Fonctionnalités disponibles dans l'interface

1. **Reconnaissance d'Entités** : Extrayez les entités nommées (personnes, lieux, organisations) du texte
2. **Image vers Texte** : Convertissez des images en descriptions textuelles
3. **Image vers Texte Avancé** : Analyse d'image améliorée avec résumé automatique
4. **Résumé et Points Clés** : Générez des résumés et des points clés sous forme de listes à puces
5. **Requête RAG** : Posez des questions sur vos documents et recevez des réponses contextualisées

## 📚 Structure du Projet

```
Multimodal-LLM/
├── multimodal/
│   ├── app.py                 # Application Streamlit principale
│   ├── src/
│   │   ├── api_call.py        # Fonctionnalités API centrales
│   │   └── local_blip.py      # Inférence BLIP locale
│   ├── utils/
│   │   ├── client.py          # Wrapper du client Hugging Face
│   │   └── load_pdf.py        # Chargement PDF et recherche sémantique
│   └── data/
│       ├── demo.jpg           # Image 
│       └── article_2502.15214v1.pdf  # PDF pour RAG
└── requirements.txt           # Dépendances Python
```


## 👨‍💻 Auteur

**Bilal SAYOUD** - [Profil GitHub](https://github.com/Bilelly)

---

**Dernière mise à jour** : 6 février 2026  
**Version Python** : 3.8+  
**Statut** : Développement Actif ✅

# Animation Manim - Évolution de la Température de Brillance

Ce dépôt contient des exemples d'animations scientifiques créées avec Manim, en particulier une visualisation de l'évolution de la température de brillance (Tᴮ) lors du gel de l'eau salée dans l'océan arctique.

## À propos de Manim

[Manim](https://www.manim.community/) est une bibliothèque Python pour créer des animations mathématiques précises, développée initialement par Grant Sanderson (3Blue1Brown). Elle permet de créer des visuels élégants pour expliquer des concepts scientifiques et mathématiques.

## Installation avec Conda

### Prérequis

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) ou [Anaconda](https://www.anaconda.com/products/distribution)
- Git

### Étapes d'installation

1. Clonez ce dépôt:
   ```bash
   git clone https://github.com/tofunori/manim-temperature-brillance.git
   cd manim-temperature-brillance
   ```

2. Créez un environnement conda à partir du fichier environment.yml:
   ```bash
   conda env create -f environment.yml
   ```

3. Activez l'environnement:
   ```bash
   conda activate manim-env
   ```

### Dépendances système

Manim nécessite certaines dépendances système pour fonctionner correctement:

#### Pour Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg
```

#### Pour macOS:
```bash
brew install cairo pango ffmpeg
```

#### Pour Windows:
Installez [MiKTeX](https://miktex.org/download) et [FFmpeg](https://ffmpeg.org/download.html).

## Exécution des exemples

Tous les exemples sont dans le dossier `examples/`. Pour exécuter l'exemple de la température de brillance:

```bash
cd examples
manim -pqh temperature_brillance.py EvolutionTemperatureBrillance
```

Les options:
- `-p`: Affiche l'animation une fois rendue
- `-q`: Qualité (l=low, m=medium, h=high)
- `-s`: Exporte l'animation en dernier frame seulement

## Description de l'exemple

L'animation "Évolution de Tᴮ lors du gel de l'eau salée" illustre comment la température de brillance (Tᴮ) augmente significativement lorsque l'eau salée de l'océan arctique commence à geler en automne, même si la température physique reste constante. Cette augmentation est due au changement d'émissivité qui passe de celle de l'eau de mer (≈ 0.45-0.65 selon la fréquence) à celle de la nouvelle glace (≈ 0.92).

## Personnalisation de l'animation

Vous pouvez modifier le fichier `examples/temperature_brillance.py` pour adapter l'animation à vos besoins. Consultez la [documentation de Manim](https://docs.manim.community/en/stable/) pour plus de détails sur les possibilités offertes par la bibliothèque.
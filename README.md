# Animation Manim - Télédétection Micro-onde & Température de Brillance

Ce dépôt contient des exemples d'animations scientifiques créées avec Manim, centrées sur la télédétection micro-onde et la visualisation de l'évolution de la température de brillance (Tᴮ) lors du gel de l'eau salée dans l'océan arctique.

## À propos de la Télédétection Micro-onde

La télédétection micro-onde est une technique qui utilise le rayonnement électromagnétique dans le domaine des micro-ondes (fréquences de 1 à 100 GHz) pour obtenir des informations sur la surface terrestre et son atmosphère. Cette technique est particulièrement utile pour l'observation des régions polaires car :

- Elle fonctionne indépendamment de la lumière solaire (jour/nuit)
- Elle pénètre les nuages, la brume et certains types de précipitations
- Elle est sensible aux propriétés diélectriques des matériaux (eau, glace, neige)
- Elle permet d'observer des paramètres comme la température, l'humidité, et l'état des surfaces

La température de brillance (Tᴮ) est un concept fondamental en télédétection micro-onde, définie comme la température qu'aurait un corps noir émettant la même quantité d'énergie que la surface observée. Elle est liée à la température physique de la surface par son émissivité :

```
Tᴮ(θ, ν) = ε(θ, ν) × Tphysique
```

où :
- Tᴮ est la température de brillance
- ε est l'émissivité (qui dépend de l'angle d'observation θ et de la fréquence ν)
- Tphysique est la température physique de la surface

## Animations disponibles

Ce dépôt contient plusieurs animations :

1. **EvolutionTemperatureBrillance** : Animation simple montrant la relation entre émissivité et température de brillance pendant le gel de l'eau
2. **BrightnessTemperatureEvolutionImproved** : Version améliorée avec disposition claire des éléments et explications scientifiques détaillées
3. **MicrowaveRemoteSensing** : Animation complète sur les principes de la télédétection micro-onde
4. **SatelliteMicroResonaTechnology** : Présentation des technologies satellitaires utilisées en télédétection micro-onde
5. **RadarBasics**, **SoilRoughnessEffect**, **SoilMoistureEffect**, **IncidenceAngleEffect** : Série d'animations sur l'humidité du sol avec radar

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

Manim nécessite certaines dépendances système pour fonctionner correctement. Ces dépendances sont incluses dans le fichier environment.yml, mais certaines peuvent nécessiter une installation séparée sur certains systèmes:

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
Si vous rencontrez des problèmes avec FFmpeg après l'installation via conda, vous pouvez télécharger manuellement [FFmpeg](https://ffmpeg.org/download.html) et l'ajouter à votre PATH.

## Exécution des exemples

Tous les exemples sont dans le dossier `examples/`. Pour exécuter les animations:

```bash
# Pour utiliser le script d'aide (Linux/macOS)
chmod +x run_example.sh
./run_example.sh temperature_brillance.py h
# ou
./run_example.sh microwave_remote_sensing.py h MicrowaveRemoteSensing

# Ou manuellement
cd examples
manim -pqh temperature_brillance.py EvolutionTemperatureBrillance
manim -pqh improved_temperature_brillance.py BrightnessTemperatureEvolutionImproved
manim -pqh microwave_remote_sensing.py BrightnessTemperatureEvolution
manim -pqh microwave_remote_sensing.py MicrowaveRemoteSensing
manim -pqh microwave_remote_sensing.py SatelliteMicroResonaTechnology
manim -pqh soil_moisture_radar.py RadarBasics
```

Les options:
- `-p`: Affiche l'animation une fois rendue
- `-q`: Qualité (l=low, m=medium, h=high)
- `-s`: Exporte l'animation en dernier frame seulement

## Gestion des mises à jour GitHub

### Récupérer les dernières modifications du dépôt

Pour mettre à jour votre copie locale avec les dernières modifications du dépôt GitHub :

1. Assurez-vous d'être dans le répertoire du projet :
   ```bash
   cd chemin/vers/manim-temperature-brillance
   ```

2. Récupérez les dernières modifications :
   ```bash
   git pull origin main
   ```

3. Si vous avez fait des modifications locales que vous souhaitez conserver mais qui sont en conflit :
   ```bash
   # Sauvegarde de vos modifications locales
   git stash
   
   # Récupération des dernières modifications
   git pull origin main
   
   # Réapplication de vos modifications
   git stash pop
   ```

### Appliquer les mises à jour de l'environnement conda

Si le fichier `environment.yml` a été mis à jour, mettez à jour votre environnement conda :

```bash
conda env update -f environment.yml
```

### Exécuter un nouveau script ou une version mise à jour

1. Activez l'environnement conda (si ce n'est pas déjà fait) :
   ```bash
   conda activate manim-env
   ```

2. Exécutez le script mis à jour :
   ```bash
   cd examples
   manim -pqh nom_du_script.py NomDeLaClasse
   ```

### Contribution au projet

Si vous souhaitez contribuer au projet avec vos propres modifications :

1. Créez une branche pour vos modifications :
   ```bash
   git checkout -b ma-nouvelle-fonctionnalite
   ```

2. Faites vos modifications et validez-les :
   ```bash
   git add .
   git commit -m "Description de mes modifications"
   ```

3. Poussez vos modifications vers GitHub :
   ```bash
   git push origin ma-nouvelle-fonctionnalite
   ```

4. Créez une Pull Request sur GitHub pour proposer l'intégration de vos modifications.

## Description scientifique

### Température de brillance et formation de glace de mer

Lorsque l'eau salée de l'océan arctique commence à geler en automne, la température de brillance (Tᴮ) augmente significativement. Ce phénomène s'explique par l'augmentation de l'émissivité qui passe de celle de l'eau de mer (≈ 0.45-0.65 selon la fréquence) à celle de la nouvelle glace (≈ 0.92).

Cette transition entraîne une forte hausse de Tᴮ malgré une température physique constante ou en légère baisse. Cette propriété est utilisée par les satellites de télédétection pour cartographier l'étendue de la glace de mer, suivre sa formation, et étudier ses propriétés.

### Applications en sciences climatiques

- Suivi de l'étendue de la glace de mer arctique et antarctique
- Détection des zones de polynya (eau libre entourée de glace)
- Cartographie des différents types de glace (récente, pluriannuelle)
- Étude des tendances à long terme liées aux changements climatiques
- Navigation maritime dans les régions polaires

## Références scientifiques

- Comiso, J. C. (2010). Polar Oceans from Space. Springer.
- Ulaby, F. T., & Long, D. G. (2014). Microwave Radar and Radiometric Remote Sensing. University of Michigan Press.
- Shokr, M., & Sinha, N. (2015). Sea Ice: Physics and Remote Sensing. John Wiley & Sons.
- Lubin, D., & Massom, R. (2006). Polar Remote Sensing: Volume I: Atmosphere and Oceans. Springer.

## Personnalisation des animations

Vous pouvez modifier les fichiers Python dans le dossier `examples/` pour adapter les animations à vos besoins. Consultez la [documentation de Manim](https://docs.manim.community/en/stable/) pour plus de détails sur les possibilités offertes par la bibliothèque.
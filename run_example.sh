#!/bin/bash
# run_example.sh

# Vérifie si l'environnement conda est activé
if [[ -z "$CONDA_DEFAULT_ENV" || "$CONDA_DEFAULT_ENV" != "manim-env" ]]; then
    echo "L'environnement conda 'manim-env' n'est pas activé."
    echo "Veuillez exécuter 'conda activate manim-env' d'abord."
    exit 1
fi

# Vérifie si un argument a été fourni
if [ $# -eq 0 ]; then
    echo "Usage: ./run_example.sh [nom_du_fichier] [qualité] [classe]"
    echo "Exemple: ./run_example.sh temperature_brillance.py h"
    echo "Exemple: ./run_example.sh microwave_remote_sensing.py h BrightnessTemperatureEvolution"
    echo ""
    echo "Qualités disponibles: l (basse), m (moyenne), h (haute)"
    echo ""
    echo "Animations disponibles:"
    echo "  • Dans temperature_brillance.py:"
    echo "    - EvolutionTemperatureBrillance (défaut)"
    echo "  • Dans microwave_remote_sensing.py:"
    echo "    - MicrowaveRemoteSensing"
    echo "    - BrightnessTemperatureEvolution"
    echo "    - SatelliteMicroResonaTechnology"
    exit 1
fi

# Extraire le nom du fichier sans l'extension
filename=$(basename -- "$1")
filename="${filename%.*}"

# Qualité par défaut (haute)
quality=${2:-h}

# Classe par défaut selon le fichier
if [ "$filename" == "temperature_brillance" ]; then
    default_class="EvolutionTemperatureBrillance"
elif [ "$filename" == "microwave_remote_sensing" ]; then
    default_class="MicrowaveRemoteSensing"
else
    default_class=""
fi

# Utiliser la classe spécifiée ou la classe par défaut
class=${3:-$default_class}

# Si aucune classe n'est spécifiée et qu'aucune classe par défaut n'est trouvée
if [ -z "$class" ]; then
    echo "Erreur: Aucune classe spécifiée et aucune classe par défaut pour ce fichier."
    echo "Veuillez spécifier une classe."
    exit 1
fi

# Vérifier si le dossier 'examples' existe
if [ ! -d "examples" ]; then
    echo "Erreur: Le dossier 'examples' n'existe pas."
    echo "Veuillez vérifier que vous êtes dans le répertoire racine du projet."
    exit 1
fi

# Exécution de l'exemple
cd examples

# Vérifier si le fichier existe
if [ ! -f "$1" ]; then
    echo "Erreur: Le fichier '$1' n'existe pas dans le dossier 'examples'."
    echo "Fichiers disponibles:"
    ls -l *.py
    exit 1
fi

echo "Exécution de '$class' dans le fichier '$1' avec la qualité '$quality'..."
manim -pq$quality "$1" "$class"

if [ $? -eq 0 ]; then
    echo "Animation rendue avec succès !"
else
    echo "Une erreur s'est produite lors du rendu de l'animation."
    echo "Veuillez vérifier que la classe '$class' existe dans le fichier '$1'."
fi
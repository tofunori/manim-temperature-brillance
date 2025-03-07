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
    echo "Usage: ./run_example.sh [nom_du_fichier] [qualité]"
    echo "Exemple: ./run_example.sh temperature_brillance.py h"
    echo "Qualités disponibles: l (basse), m (moyenne), h (haute)"
    exit 1
fi

# Extraire le nom du fichier sans l'extension
filename=$(basename -- "$1")
filename="${filename%.*}"

# Qualité par défaut (haute)
quality=${2:-h}

# Exécution de l'exemple
cd examples
manim -pq$quality $1 EvolutionTemperatureBrillance

echo "Animation rendue avec succès !"
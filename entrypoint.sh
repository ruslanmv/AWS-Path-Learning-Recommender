#!/bin/bash

# Source the virtual environment
source /app/venv/bin/activate

# Starting server
echo "Starting Ollama server"
ollama serve &
sleep 1

# Try to get the model environment variable
if [ -n "${MODEL}" ]; then
  # Split the MODEL variable into an array
  IFS=',' read -ra MODELS <<< "${MODEL}"
else
  # Use the default list of models
  MODELS=(llama3 ) #gemma:2b phi3 mistral
fi


# Splitting the models by comma and pulling each
#IFS=',' read -ra MODELS <<< "$model"
for m in "${MODELS[@]}"; do
    echo "Pulling $m"
    ollama pull "$m"
    sleep 5
done


ollama create aws-path-learning -f ./Modelfile

# Run the Python application
#streamlit run ./src/app.py

# Run the Python application
streamlit run --server.address 0.0.0.0 ./src/app.py

# Keep the script running to prevent the container from exiting
#wait
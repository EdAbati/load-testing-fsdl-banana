# Load testing the FSDL Text Recognizer on GPUs using 🍌 `banana`

This repository contains the code used to execute a load test of the GPU deployment of the FSDL Text Recognizer using [🍌 banana](https://banana.dev/).


## Execute the load test
1. Deploy the service on GPUs using the [guide in the FSDL repo](https://github.com/full-stack-deep-learning/gpu-deployments/tree/banana/)
2. Create a conda environment and install requirements
    ```bash
    make create-conda-env
    ```
3. Activate the conda environment
    ```bash
    conda activate load-testing-fsdl
    ```
4. Test the API
    ```bash

    curl -X POST "https://api.banana.dev/start/v4/" \
    -H "Content-Type: application/json" \
    -d \
    '
    {
        "apiKey": "<your-api-key>",
        "modelKey": "<your-model-key>",
        "modelInputs": {"image": "https://fsdl-public-assets.s3-us-west-2.amazonaws.com/paragraphs/a01-077.png"}
    }'
    ```
5. Create your `.env` file using the `env.template` as a template:
    ```bash
    cp env.template .env
    ```
    Fill in the values for the `API_KEY` and `MODEL_KEY` variables in the `.env` file.
6. Run the load test loading the env variables from the `.env` file:
    ```bash
    dotenv run locust --config=locust.conf
    ```
    You can change the test configurations in the `locust.conf` file.


## Contributing
1. (Optional) Install pre-commit hooks
    ```bash
    pre-commit install
    ```
2. Create a conda environment and install requirements
    ```bash
    make create-conda-env
    ```
3. Make your changes


## Useful resources
To learn about `locust` and how to write load tests for ML models, check out the following resources:
- [FSDL 2022 course repo](https://github.com/full-stack-deep-learning/fsdl-text-recognizer-2022/blob/main/notebooks/lab99_loadtesting.ipynb)
- https://github.com/sayakpaul/deploy-hf-tf-vision-models/tree/main/hf_vision_model_tfserving_gke/locust

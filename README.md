# ModalScaling

Testing the Modal service for elasticity and scalability.

## Installation

Clone the repository, and navigate to the root directory:

```bash
git clone https://github.com/FreddyWordingham/ModalScaling.git
cd ModalScaling
```

Then install the package and its dependencies:

```bash
poetry env use python3.10
poetry install
```

## Usage

### Parallel Compute Example

Run the parallel compute example:

```bash
poetry run modal run scripts/parallel_compute.py
```

### Web Endpoints Example

Run the web endpoints example:

```bash
poetry run modal serve scripts/web_endpoints.py
```

> Note: You'll need to note down the generated endpoint URL.

You can then trigger the endpoints using `Curl`:

```bash
curl -X POST -H 'Content-Type: application/json' --data-binary '{"x": 2}' https://freddywordingham--scripts-web-endpoints-py-square-dev.modal.run
```

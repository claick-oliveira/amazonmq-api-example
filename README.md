# AmazonMQ API Example

![Github Workflow](https://github.com/claick-oliveira/amazonmq-api-example/workflows/Run%20RabbitMQ%20messaging%20tests/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This is an example for python api to publish/consume RabbitMQ messages.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project.

### Prerequisites

- git
- python 3.9
- pip
- vscode
- docker (to run local tests)

### Installing

First of all you need to clone this repository:

``` bash
git clone https://github.com/claick-oliveira/amazonmq-api-example.git
```

After clone access the folder and create your virtual env:

``` bash
cd amazonmq-api-example
```

To start to code you need to install the requirements and de dev requirements:

``` bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

## Running the tests

To run the you will need a container running rabbitmq. To start the container you need to execute:

``` bash
docker run -d --rm  --hostname mock-rabbit --name mock-rabbit -e RABBITMQ_DEFAULT_USER=mock -e RABBITMQ_DEFAULT_PASS=mock -p 5671:5671 -p 5672:5672 rabbitmq:latest
```

Now you can run the tests:

``` bash
tox
```

> **_NOTE:_**  After the tests you can stop the container with the command `docker stop mock-rabbit`.

### And coding style tests

In this project we'll use [PEP 8](https://www.python.org/dev/peps/pep-0008/) as style guide.

## Clean

To clean the files generated as coverage, builds, env you can use:

``` bash
make clean
```

If you prefer to clear all, use:

```bash
make cleanfull
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/claick-oliveira/amazonmq-api-example/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Claick Oliveira** - *Initial work* - [claick-oliveira](https://github.com/claick-oliveira)

See also the list of [contributors](https://github.com/claick-oliveira/python-api-example/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

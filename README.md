# ArithmeticService

This repository contains a small example application to showcase how to design a service in a reusable way, so that it can be consumed as both a CLI and a web service.

All of the core processing logic for this simple service is contained within [`src/arithmeticsvc/arithmetic.py`](./src/arithmeticsvc/arithmetic.py).

## Quickstart

> Note, this project uses Poetry for dependency management and environment isolation. I highly recommend you use [Poetry](https://python-poetry.org/) for these purposes. If you are using `pip`, replace the initial install command with `pip install`, and you can follow along by omitting the `poetry run` parts of the commands. The testing steps will not work, however, since `pip` does not install the test dependencies.

1. Clone this repository
1. Install dependencies with `poetry install`
1. Run the tests with `poetry run pytest`
1. Try out the CLI by running `poetry run arcli --help`.
   - Example: `poetry run arcli add 45 50`
   - With binary output: `poetry run arcli -o bin 12 5123`
1. Try making calls to the server (while it's not running) with `poetry run arcli web --help`
   - You should get "ConnectError" issues
1. Start up the web server with `poetry run fastapi dev src/arithmeticsvc/api.py`
   - By default, this will start up the server with `dec` output type. To start with `hex` output type (for example), you can run `ARITHMETIC_OUTPUT_TYPE=hex poetry run fastapi dev src/arithmeticsvc/api.py`
1. In a different shell, make calls to the web server with `poetry run arcli web`
   - You can change the output type of the running service with `poetry run arcli web output`
   - Try calling the multiply API with `poetry run arcli web multiply 50 3`

## Exercises

If you're interested in giving a try to improve this basic app, try out some of the following exercises! Most can be done without having to fork the repository, but I recommend doing so to track the changes you've made in your own git history.

1. Currently, only tests for the service itself are available. As an exercise, try adding tests for the CLI and the API by following the documentation for [`typer`](https://typer.tiangolo.com/tutorial/testing/) and [`fastapi`](https://fastapi.tiangolo.com/tutorial/testing/) respectively.
1. The `ArithmeticService` naively computes with the values given. Can you think of a way that this service might produce errors? Find the spot where there is a bug in the server that would cause a runtime exception, and fix the bug! This can be done in many ways, so feel free to pick whichever way works best for you.
1. Expand the `ArithmeticService` to support more operations.
1. Add support for running the API with [Docker](https://docs.docker.com/guides/docker-overview/)! Write a [Dockerfile](https://docs.docker.com/reference/dockerfile/)
   - As an extra challenge, write a [`docker-compose.yaml`](https://docs.docker.com/compose/compose-file/) file that spins up the service. Test that you can access the container from the CLI!
1. Currently, the [`cli`](./src/arithmeticsvc/cli.py) bundles both the [service](./src/arithmeticsvc/arithmetic.py) and the [web client](./src/arithmeticsvc/client.py). Try to separate the two by moving the web client to its own CLI, then try running the new CLI!
1. This repository doesn't have any automated testing involved in it. Fork this repository and try to write a [Github Actions](https://github.com/features/actions) workflow to run the following tests and checks:
   - `pytest`
   - `ruff`
   - `bandit` <-- Note! You will need to make sure it only scans `src/` since the `tests` diretory uses `asserts`, which causes low-level security scan failures
   - `mypy`

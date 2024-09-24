<!--
SPDX-FileCopyrightText: © 2024 Romain Brault <mail@romainbrault.com>

SPDX-License-Identifier: MIT OR Apache-2.0
-->

# 🛠️ Contributor Guide

Thank you for your interest in improving this project. The code is open-source
under the license [MIT OR Apache-2.0] and we welcome contributions in any
form.

As a contibutor, you must respect our [Code of Conduct].

[MIT OR Apache-2.0]: https://spdx.org/licenses/
[Code of Conduct]: CODE_OF_CONDUCT.md

## Core members

The list of [core members], also known as [maintainers] is available in the
file [MAINTAINERS.md](MAINTAINERS.md)

## How to report a vulnerability

See [SECURITY.md](SECURITY.md).

## How to report an identified bug

Report identified bugs by filling a [GitHub bug report issue](https://github.com/whiteprints/test-map-linux-py312-test/issues/new?template=bug_report.yml).

When filing a bug or any other issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.

## How to request a feature

Request a feature by [opening a discussion](https://github.com/whiteprints/test-map-linux-py312-test/discussions/categories/ideas)

Once the enhancement has been discussed, fill a [GitHub feature issue](https://github.com/whiteprints/test-map-linux-py312-test/issues/new?template=feature_request.yml).

## How to report a problem

If you have any problem with the project please contact by email [core members].

[core member]: MAINTAINERS.md
[core members]: MAINTAINERS.md
[Maintainer]: MAINTAINERS.md
[Maintainers]: MAINTAINERS.md

## How to set up your development environment

You simply need [uv] and a copy of the repository.

[uv]: https://docs.astral.sh/uv/

To install python and setup your environment run

```console
uv python install
uv sync --all-extras
```

You can now run an interactive Python session:

```console
uv run python
```

If you whish to use a specific Python version you can use

```console
uv python pin ...
```

Please see [uv]'s documentation for more advanced usage.

## How to test the project

The test suite is managed by [Tox].

Run the full test suite:

```console
uvx tox run
```

List the available [Tox] sessions:

```console
uvx tox list
```

You can also run a specific [Tox] session.
For example, invoke the unit test suite like this:

```console
uvx tox run -m test
```

Unit tests are located in the _tests_ directory,
and are written using the [pytest] testing framework.

[pytest]: https://docs.pytest.org/en/stable/
[Tox]: https://tox.wiki/en/stable/

Please see [Tox]'s documentation for more advanced usage.

## Project tree

Here is a list of important resources for contributors:

- The licences: located in the `LICENCES/` directory.
- The project source code: located in the `src/` directory.
- The tests: located in the `tests/` directory.
- The documentation source code: located in the `docs/` directory.
- `tox.ini` contains [Tox]'s configuration
- `pyproject.toml` contains the [project metadata] and the [build system]

[project metadata]: https://peps.python.org/pep-0621/
[build system]: https://peps.python.org/pep-0518/

## Tools

The project relies on the following tools for development:

- [pip-audit]: used to find vulnerabilities in the supply chain.
- [pre-commit]: used to identifying simple issues before submission.
- [pyright]: used for type checking and as [LSP].
- [reuse]: check the licenses compliance.
- [ruff]: check and fix the Python's code format and syntax.
- [cyclonedx-bom]: generate a [bill of material] of the supply chain.
- [tox]: orchestrate tools and tests.

[pip-audit]: https://github.com/pypa/pip-audit
[pre-commit]: https://pre-commit.com/
[pyright]: https://microsoft.github.io/pyright/
[reuse]: https://reuse.software/
[ruff]: https://docs.astral.sh/ruff/
[cyclonedx-bom]: https://cyclonedx-bom-tool.readthedocs.io/en/latest/
[LSP]: https://en.wikipedia.org/wiki/Language_Server_Protocol
[bill of material]: https://en.wikipedia.org/wiki/Software_supply_chain

You may install all the tools using [uv]:

```console
uv tool install pip-audit
uv tool install pre-commit --with "pre-commit-uv"
uv tool install pyright
uv tool install reuse
uv tool install ruff
uv tool install cyclonedx-bom
uv tool install tox --with "tox-uv"
```

## How to submit changes

Create a new [Git] branch to submit changes to this project.

```console
git switch -c my-contribution
```

Then commit and push your modifications on your branch.

Your contribution needs to meet the following guidelines for acceptance:

- The [Tox] test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

To run linting and code formatting checks before committing your change, you
can install [pre-commit] as a Git hook by running the following command:

```console
uvx pre-commit install
```

Ensure that your contribution is resolving a known [issue]. If not, please
create an associated [issue] first.

Once your code and your issue are ready, create a [GitHub] [Pull Request]
containing your modification and referencing the associated [issue].

If you don't know or are not sure on how to create a Pull Request, follow
the tutorial: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request.

[GitHub]: https://github.com/
[Pull Request]: https://github.com/whiteprints/test-map-linux-py312-test/pulls
[issue]: https://github.com/whiteprints/test-map-linux-py312-test/issues

[Git]: https://git-scm.com/

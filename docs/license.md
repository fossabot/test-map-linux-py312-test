<!--
SPDX-FileCopyrightText: © 2024 Romain Brault <mail@romainbrault.com>

SPDX-License-Identifier: MIT OR Apache-2.0
-->

# 📝 License

Each file in the repository should have a valid [SPDX] header composed of
- a copyright text (SPDX-FileCopyrightText)
- a license identifier (SPDX-License-Identifier)

The LICENSES directory in the project root contains all the licenses that are
used in the project. The project's metadata follow [PEP639].

This project use [REUSE] to make licensing easy for humans and machines alike.

You can generate a [bill of material] listing each file of the project with its
repsective license using:

```console
tox run -m BOM
```

[SPDX]: https://spdx.dev/
[REUSE]: https://reuse.software/tutorial/
[PEP639]: https://peps.python.org/pep-0639/
[bill of material]: https://en.wikipedia.org/wiki/Software_supply_chain


## Code License

:::{attention}
:name: test map linux py312-test's Code License
The _code_ of this project is released under **[MIT OR Apache-2.0]**.

In case of doubt, please check the [SPDX] header of each individual code file.
:::


[MIT OR Apache-2.0]: https://spdx.org/licenses/


A copy of the license should always be distributed along with the code files.

## FAQ

Many of your questions about copyrights and licenses might find their answers
here: <https://reuse.software/faq/>.

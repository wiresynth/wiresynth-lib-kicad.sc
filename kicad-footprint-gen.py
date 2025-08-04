#!/usr/bin/env python3

import sys


def ident(name: str):
    to_be_replaced = set[str]()

    name = name.replace(".", "p")

    for c in name:
        if not (c.isdigit() or c.isalpha() or c == "_"):
            to_be_replaced.add(c)

    for c in to_be_replaced:
        name = name.replace(c, "_")

    if name[0].isdigit():
        name = f"_{name}"

    return name


def main():
    if sys.argv.__len__() < 3:
        print(
            f"Usage: {sys.argv[0]} (output directory) (library.pretty/footprint.kicad_mod)*"
        )
        return

    libAndSymNames: dict[str, list[str]] = {}

    for item in sys.argv[2:]:
        lib, name = item.replace(".pretty", "").split("/")
        if libAndSymNames.get(lib) is None:
            libAndSymNames[lib] = []
        libAndSymNames[lib].append(name.replace(".kicad_mod", ""))

    for lib, names in libAndSymNames.items():
        lib = ident(lib)
        f = open(f"{sys.argv[1]}/{lib}.scala", "x")

        def fprint(s: str):
            print(s, file=f)

        fprint(f"package wiresynth.lib.kicad.footprint\n\nobject {lib}:")
        for name in names:
            fprint(f'  val {ident(name)} = "{name}"')


if __name__ == "__main__":
    main()

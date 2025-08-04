#!/usr/bin/env python3

import kiutils.symbol as ks
import sys


def maybeIdent(s: str):
    for c in s:
        if c.isalpha() or c.isnumeric():
            return True
    return False


def isNumber(s: str):
    for c in s:
        if not c.isdigit():
            return False
    return True


def autoQuote(s: str):
    if isNumber(s):
        return s

    return f'"{s}"'


def process(filepath: str):
    libName = filepath.replace(".kicad_sym", "").split("/")[-1]

    f = open(f"{libName}.scala", "x")

    def fprint(s: str):
        print(s, file=f)

    fprint("package wiresynth.lib.kicad.part")
    fprint("import wiresynth.dsl.*")

    fprint(f"object `{libName}` {{")

    lib = ks.SymbolLib.from_file(filepath)
    for sym in lib.symbols:
        pins = list[ks.SymbolPin]()
        pins += sym.pins
        for unit in sym.units:
            pins += unit.pins

        nameAndPos = dict[str, list[str]]()

        for pin in pins:
            if maybeIdent(pin.name):
                if nameAndPos.get(pin.name) is None:
                    nameAndPos[pin.name] = []
                nameAndPos[pin.name].append(pin.number)
            else:
                nameAndPos[pin.number] = [pin.number]

        if sym.extends is None:
            fprint(f"  case class `{sym.entryName}`() extends Part {{")

            for pinName, pinList in nameAndPos.items():
                fprint(
                    f"    val `{pinName}` = Pin() @@ {' @@ '.join(map(autoQuote, pinList))}"
                )

            fprint("  }")
        else:
            fprint(f"  type `{sym.entryName}` = `{sym.extends}`")

    fprint("}")


def main():
    if sys.argv.__len__() < 2:
        print(f"Usage: {sys.argv[0]} (symbol library file)*")
        return
    for f in sys.argv[1:]:
        print(f"Processing: {f}")
        process(f)


if __name__ == "__main__":
    main()

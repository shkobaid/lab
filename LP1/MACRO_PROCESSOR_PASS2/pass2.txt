MNT = {
    "ONE": 1,
    "TWO": 5
}

MDT = {
    1: "MOVER &E, &O",
    2: "ADD &E, &N",
    3: "MOVEM &E, &O",
    4: "MEND",
    5: "MOVER &O, &T",
    6: "ADD &O, &W",
    7: "MOVEM &O, &T",
    8: "ONE O, 9, CREG",
    9: "MEND"
}

ALA = {
    "ONE": {"params": ["&O", "&N", "&E"], "defaults": {"&E": "AREG"}},
    "TWO": {"params": ["&T", "&W", "&O"], "defaults": {"&O": "DREG"}}
}


def expand_macro(macro_name, arguments):
    start = MNT[macro_name]
    ala_data = ALA[macro_name]
    params = ala_data["params"]
    defaults = ala_data["defaults"]

    arg_map = {}

    for i in range(len(params)):
        if i < len(arguments) and arguments[i]:
            arg_map[params[i]] = arguments[i]
        elif params[i] in defaults:
            arg_map[params[i]] = defaults[params[i]]
        else:
            arg_map[params[i]] = None

    i = start
    while MDT[i] != "MEND":
        line = MDT[i]

        for key, val in arg_map.items():
            if val is not None:
                line = line.replace(key, val)

        tokens = line.strip().split()
        if tokens and tokens[0] in MNT:
            nested_macro = tokens[0]
            args_part = " ".join(tokens[1:])
            args = [a.strip() for a in args_part.split(",")]
            expand_macro(nested_macro, args)
        else:
            print(line)

        i += 1


def pass2(source_code):
    for line in source_code:
        words = line.strip().split()
        if not words:
            continue
        name = words[0]

        if name in MNT:
            args = [a.strip() for a in " ".join(words[1:]).split(",")]
            expand_macro(name, args)
        else:
            print(line.strip())


source_code = [
    "START",
    "READ O",
    "READ T",
    "TWO T, 7",
    "PRINT O",
    "PRINT T",
    "STOP",
    "O DS 1",
    "T DS 1",
    "END"
]

pass2(source_code)

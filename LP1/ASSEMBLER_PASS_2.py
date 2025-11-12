class PassIIAssembler:
    SymTab = {}
    LitTab = {}

    def load_symbol_table(filename):
        PassIIAssembler.SymTab.clear()
        with open(filename) as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 3:
                    idx = int(parts[0])
                    addr = int(parts[2])
                    PassIIAssembler.SymTab[idx] = addr

    def load_literal_table(filename):
        PassIIAssembler.LitTab.clear()
        with open(filename) as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 3:
                    idx = int(parts[0])
                    addr = int(parts[2])
                    PassIIAssembler.LitTab[idx] = addr

    def resolve_symbol_operand(token):
        base = 0
        offset = 0
        if '+' in token:
            part, off = token.split('+')
            offset = int(off)
        elif '-' in token:
            part, off = token.split('-')
            offset = -int(off)
        else:
            part = token
        if part.startswith("(S,"):
            idx = int(part[3:-1])
            base = PassIIAssembler.SymTab.get(idx, 0)
        elif part.startswith("(L,"):
            idx = int(part[3:-1])
            base = PassIIAssembler.LitTab.get(idx, 0)
        elif part.startswith("(C,"):
            base = int(part[3:-1])
        return base + offset

    def generate_machine_code(line):
        tokens = line.strip().split()
        if not tokens or len(tokens) < 2:
            return ""
        try:
            loc = int(tokens[0])
        except ValueError:
            return ""
        instr = tokens[1]
        if instr.startswith("(AD"):
            return ""
        if instr.startswith("(DL"):
            if len(tokens) >= 3 and tokens[2].startswith("(C,"):
                val = tokens[2][3:-1]
                return f"{loc}\t0000\t000\t{val}"
            return ""
        if instr.startswith("(IS"):
            op = int(instr[4:-1])
            reg = 0
            mem = 0
            for t in tokens[2:]:
                if t.startswith("(R,"):
                    reg = int(t[3:-1])
                elif t.startswith("(S,") or t.startswith("(L,") or t.startswith("(C,"):
                    mem = PassIIAssembler.resolve_symbol_operand(t)
            return f"{loc}\t{op:02d}\t{reg}\t{mem:03d}"
        return ""

    def main():
        ic_file = "IC.txt"
        sym_file = "SYMTAB.txt"
        lit_file = "LITTAB.txt"
        out_file = "MACHINE_CODE.txt"

        PassIIAssembler.load_symbol_table(sym_file)
        PassIIAssembler.load_literal_table(lit_file)

        with open(ic_file) as ic, open(out_file, "w") as out:
            for line in ic:
                code = PassIIAssembler.generate_machine_code(line)
                if code:
                    out.write(code + "\n")
                    print(code)

PassIIAssembler.main()

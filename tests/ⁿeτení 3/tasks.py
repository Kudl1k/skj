from typing import Tuple
import re


class ProgramException(BaseException):
    pass


# noinspection SpellCheckingInspection
def check_copilot(program: str) -> Tuple[str, int]:
    """
    Úkol 1

    Studenti předmětu APPS se pokoušejí použít službu Copilot pro vygenerování řešení zadaných
    úloh v x86 assembly, aby nemuseli přemýšlet. Bohužel se ale ukázalo, že AI občas generuje
    kód, který není správně naformátován, nebo přímo obsahuje nesmyslné instrukce.
    Pomozte nebohým studentům naimplementováním funkce `check_copilot`, která obdrží vygenerovaný
    program, opraví v něm formátování, chybné názvy instrukcí a zduplikované instrukce, a poté
    pro jistotu i program vykoná a zjistí jeho výsledek, aby šlo ověřit, že byl program vygenerován
    korektně.

    Funkce by měla vrátit dvojici hodnot. První hodnotou bude zformátovaný a opravený program,
    a druhou hodnotou bude obsah registru R0 po provedení opraveného programu.

    Assembly programy se skládají z řádků, řádek může být buď prázdný nebo může obsahovat jednu
    instrukci. Každá validní instrukce se skládá z opcodu a dvou výrazů:
    `<OPCODE> <ARG0> <ARG1>`

    Například:
    `MOV R0 5`

    <OPCODE> může být buď `MOV` nebo `ADD`.
    Výraz (argument) může být:
    - Konstanta: celé číslo
        - Hodnota tohoto výrazu odpovídá zadané konstantě.
    - Registr: `R<int>`, kde `<int>` je celé číslo v rozsahu 0 až 15.
        - Hodnota tohoto výrazu odpovídá současné hodnotě registru s daným indexem.
    - Index: `[<int>]` nebo `[R<int>]`.
        - Hodnota tohoto výrazu odpovídá současné hodnotě paměti na adrese dané hodnotou výrazu v
        hranatých závorkách.

    Pravidla formátování:
    - V řádku s instrukcí může být libovolné množství mezer. Při formátování znormalizujte
    instrukci tak, aby na začátku ani konci řádku mezery nebyly, a aby mezi třemi členy instrukce
    byla právě jedna mezera.
    `    MOV        R0  5    ` -> `MOV R0 5`
    - Ve vstupu se mohou vyskytnout prázdné řádky. Ty při formátování odstraňte.
    - Opcode může být vygenerovaný s chybou. opcode s chybou je definován tak, že má tři znaky,
    a liší se právě v jednom znaku od jedné ze známých instrukcí (MOV/ADD). Pokud naleznete opcode
    s chybou, tak jej opravte.
    `MXV R0 5` -> `MOV R0 5`
    `ADZ R0 5` -> `ADD R0 5`
    - Pokud se po zformátování ve vstupu vyskytnou stejné řádky za sebou, tak tyto duplicity vyraďte
    z výstupu.
    ```
    ADD R0 5
    ADX R0 5
    ADZ R0 5

    vvv

    ADD R0 5
    ```
    - Pokud bude ve vstupu jakýkoliv jiný obsah (chybějící argument, argumentů je moc, opcode nemá
    tři znaky nebo je moc vzdálen od známých instrukcí atd.), tak vyvolejte `ProgramException`.

    Jakmile bude program zformátován a opraven, tak jej vykonejte. Vytvořte si paměť (1000 čísel
    indexovaných od nuly) a registry (16 čísel indexovaných od nuly) a inicializujte vše na nulu.

    Poté vykonejte všechny instrukce, jednu po druhé.
    - Instrukce MOV <A> <B> načte hodnotu výrazu <B> a uloží jej do <A>.
    - Instrukce ADD <A> <B> načte hodnotu výrazu <B> a přičte jej k hodnotě umístění v <A>.

    V obou případech může <A> být buď registr nebo místo v paměti. Při pokusu o uložení do konstanty
    vyvolejte `ProgramException`.

    Příklad:
    ```
    MOV R0 5     # Ulož hodnotu 5 do registru R0
    ADD R0 1     # Přičti k registru R0 hodnotu 1 (v registru R0 poté bude hodnota 6)
    MOV R1 R0    # Ulož hodnotu registru R0 (6) do registru R1
    MOV [5] 8    # Ulož hodnotu 8 do paměti na adrese 5
    MOV [6] R0   # Ulož hodnotu registru R0 (6) do paměti na adrese 6
    MOV [R0] 5   # Ulož hodnotu 5 do paměti na adrese dané hodnotou registru R0 (6)
    MOV R1 [R0]  # Ulož hodnotu paměti na adrese dané hodnotou registru R0 (6) do registru R1
    ADD R0 R1    # Přičti k registru R0 hodnotu registru R1 (5)
    ```
    Po provedení tohoto programu by v registru R0 měla být hodnota 11.

    Po vykonání programu vraťte n-tici `(opravený a zformátovaný program, hodnota registru R0)`.
    """

    memory = {}
    for i in range(1000):
        memory[i] = 0

    regs = {}
    for i in range(16):
        regs['R' + str(i)] = 0

    output = []
    for line in program.splitlines():
        newLine = ""
        space = 0

        # Remove extra spaces
        for char in line:
            if char == " ":
                if space == 0:
                    space = 1
                    newLine += char
                    continue
                else:
                    continue

            space = 0
            newLine += char

        # Strip new line of starting and ending spaces
        newLine = newLine.strip()

        # Ignore new lines
        if newLine == "":
            continue

        # Parse args into types
        lineArgs = newLine.split(" ")

        if len(lineArgs) != 3:
            raise ProgramException()

        opcode = lineArgs[0].upper()
        arg1 = lineArgs[1]
        arg2 = lineArgs[2]

        # Just some random regex that might work :D
        if len(opcode) != 3:
            raise ProgramException()
        else:
            if re.match(r"AD.", opcode):
                opcode = "ADD"
            if re.match(r"A.D", opcode):
                opcode = "ADD"
            if re.match(r".DD", opcode):
                opcode = "ADD"

            if re.match(r"MO.", opcode):
                opcode = "MOV"
            if re.match(r"M.V", opcode):
                opcode = "MOV"
            if re.match(r".OV", opcode):
                opcode = "MOV"

            if opcode not in ["ADD", "MOV"]:
                raise ProgramException()

        # If accessing to constant
        if arg1.isnumeric():
            raise ProgramException()

        # Checking correct syntax
        for i, arg in enumerate([arg1, arg2]):
            if arg.startswith("[") or arg.endswith("]"):
                if (arg.count("[") != 1) or (arg.count("]") != 1):
                    raise ProgramException()

                # Check if accessing to right memory
                if i == 0 and 0 > int(arg[1:-1]) < 1000:
                    raise ProgramException()

            # Check if accessing to right register
            if arg.startswith("R"):
                if not arg[1:].isdigit() or int(arg[1:]) > 15:
                    raise ProgramException()

        output.append(f"{opcode} {arg1} {arg2}")

    # Removing duplicates
    for i in range(len(output) - 1):
        if output[i] == output[i + 1]:
            output[i] = ""
    output = [x for x in output if x != ""]

    # Calculate
    for line in output:
        lineArgs = line.split(" ")
        opcode = lineArgs[0]

        reg1 = lineArgs[1]
        isReg1 = False

        if reg1.startswith("[") and reg1.endswith("]"):
            reg1 = reg1[1:-1]
            isReg1 = True

        reg2 = lineArgs[2]
        isReg2 = False

        if reg2.startswith("[") and reg2.endswith("]"):
            reg2 = reg2[1:-1]
            isReg2 = True

        #Aaaaaaaaaaaaaaaaaa
        if reg2.isnumeric():
            if opcode == "ADD":
                regs[reg1] += int(reg2)
            else:
                regs[reg1] = int(reg2)
        else:
            if reg2.startswith("[") and reg2.endswith("]"):
                reg2 = reg2[1:-1]

                if reg2.isnumeric():
                    if opcode == "ADD":
                        regs[reg1] += int(reg2)
                    else:
                        regs[reg1] = int(reg2)
                else:
                    if reg2 in regs:
                        if opcode == "ADD":
                            regs[reg1] += regs[reg2]
                        else:
                            regs[reg1] = regs[reg2]
            else:
                if reg2 in regs:
                    if opcode == "ADD":
                        regs[reg1] += regs[reg2]
                    else:
                        regs[reg1] = regs[reg2]

    return "\n".join(output) + "\n", regs["R0"]


class StudyDatabase:
    """
    Úkol 2

    Zkrácený semestr, spousta projektů a domácích úloh stresuje studenty! Někteří učitelé nedávají
    feedback na úlohy, zapisují jej do různých systémů (Edison, Kelvin, Excel) a studenti pak neví,
    na čem jsou. Pomozte jim tím, že naimplementujete třídu `StudyDatabase`, která bude uchovávat
    informace o získaných bodech studenta v jednotlivých předmětech a typech úloh
    ("lesson", "project", "test").

    Třída bude poskytovat následující rozhraní:
    ```python
    # Vytvoření databáze
    db = StudyDatabase()

    # Metoda `add_points` zaznamená jednotlivé získané body pro daný předmět a typ úlohy
    # ("project", "lesson", "test"). Zároveň vrátí celkový počet bodů pro daný předmět a typ úlohy
    # (včetně nově přidaných bodů).
    db.add_points("SKJ", "lesson", 5)    # 5
    db.add_points("SKJ", "lesson", 10)   # 15

    # Metoda `total_points_per_subject` vrátí slovník s celkovým počtem bodů pro každý
    # zaznamenaný předmět.
    db.total_points_per_subject()        # {"SKJ": 15}

    db.add_points("SKJ", "test", 40)     # 40
    db.add_points("UTI", "lesson", 10)   # 10

    # Této metodě můžeme předat typ úlohy. V tom případě vrátí pouze body tohoto typu úlohy.
    db.total_points_per_subject("lesson") # {"SKJ": 15, "UTI": 10}
    db.total_points_per_subject()         # {"SKJ": 55, "UTI": 10}

    # Metoda `average_points_per_type` vrátí průměrný počet bodů pro daný typ úlohy pro jednotlivé
    # předměty. Průměr zaokrouhlete dolů (směrem k nule) na celé číslo.
    db.average_points_per_type("lesson")  # {"SKJ": 7, "UTI": 10}

    db.add_points("C++ I", "project", 40) # 40
    db.add_points("C++ I", "lesson", 60)  # 60

    # Metoda `passed_subjects` vrátí seznam předmětů, ze kterých student již získal dohromady
    # alespoň 51 bodů. Seznam navrácených předmětů seřaďte vzestupně dle jejich jména.
    db.passed_subjects()                  # ["C++ I", "SKJ"]
    ```
    """

    def __init__(self):
        self.subjects = {}
        self.count = {}

    # It is what it is :( I don't like it either
    def add_points(self, subject, tyype, points):
        if subject not in self.subjects:
            self.subjects[subject] = {}
            self.count[subject] = {}
        if tyype not in self.subjects[subject]:
            self.subjects[subject][tyype] = 0
            self.count[subject][tyype] = 0
        self.subjects[subject][tyype] += points
        self.count[subject][tyype] += 1

        return self.subjects[subject][tyype]

    def total_points_per_subject(self, tyype=None):
        if tyype is None:
            return {subject: sum(self.subjects[subject].values()) for subject in self.subjects}
        else:
            for subject in self.subjects:
                if tyype not in self.subjects[subject]:
                    self.subjects[subject][tyype] = 0

            return {subject: self.subjects[subject][tyype] for subject in self.subjects}

    def passed_subjects(self):
        passed = [subject for subject in self.subjects if sum(self.subjects[subject].values()) >= 51]
        return sorted(passed)

    def average_points_per_type(self, target):
        out = {}

        for subject in self.subjects:
            out[subject] = 0

            if target not in self.subjects[subject]:
                continue
            else:
                for tyype in self.subjects[subject]:
                    if tyype == target:
                        out[subject] += self.subjects[subject][tyype]

                out[subject] //= self.count[subject][target]

        return out

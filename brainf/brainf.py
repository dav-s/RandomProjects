from __future__ import print_function

# SCOPE
s = {
    "a": [0],
    "ptr": 0,
    "stdin": ""
}


def shift_ptr(i):
    if s["ptr"] + i >= len(s["a"]):
        s["a"].append(0)
    elif s["ptr"] + i < 0:
        print("ERROR: Ptr < 0")
        quit()
    s["ptr"] += i


def add_to_spot(i):
    s["a"][s["ptr"]] += i


def add_int_to_outp(i):
    print(str(i), end="")


def add_char_to_outp(c):
    print(chr(c), end="")


def add_from_stdin():
    if len(s["stdin"]) == 0:
        return
    add_to_spot(s["stdin"][0])
    s["stdin"] = s["stdin"][1:]

commands = {
    ".": lambda: add_char_to_outp(s["a"][s["ptr"]]),
    ":": lambda: add_int_to_outp(s["a"][s["ptr"]]),
    ",": lambda: add_from_stdin(),
    ">": lambda: shift_ptr(1),
    "<": lambda: shift_ptr(-1),
    "+": lambda: add_to_spot(1),
    "-": lambda: add_to_spot(-1),
    "[": lambda: print("ERROR: Something Went Wrong"),
    "]": lambda: print("ERROR: Something Went Wrong")
}


# Separates brackets:
#    >+..           -->    None
#    >+[<]>.        -->    [">+", "<", ">."]
#    +[+[-]+[-].]   -->    ["+", "+[-]+[-].", ""]
def separatep(s):
    if "[" in s:
        if "]" not in s:
            print("ERROR: No Matching ]")
            quit()
        fp = s.index("[")
        lparc = 0
        lp = len(s)-1
        for i in xrange(fp + 1, len(s)):
            if s[i] == "]":
                if lparc == 0:
                    lp = i
                    break
                else:
                    lparc -= 1
            elif s[i] == "[":
                lparc += 1
            elif i+1 == len(s):
                print("ERROR: No Matching ]")
                quit()
        return [s[0:fp], s[fp + 1:lp], s[lp + 1:]]
    elif "]" in s:
        print("ERROR: Extra ]")
        quit()
    return None


# Executes a basic string not including brackets
def basicexec(s):
    for c in s:
        commands[c]()


# Executes a bracket subsection
def execss(ss):
    while s["a"][s["ptr"]]:
        psr = separatep(ss)
        lp = ss
        while psr:
            basicexec(psr[0])
            execss(psr[1])
            lp = psr[2]
            psr = separatep(lp)
        basicexec(lp)


# Executes any BF string
def execbf(bf):
    psr = separatep(bf)
    lp = bf
    while psr:
        basicexec(psr[0])
        execss(psr[1])
        lp = psr[2]
        psr = separatep(lp)
    basicexec(lp)
    print()

# TODO Input from a file
# TODO Multiline Programs

inp = "".join([c for c in raw_input("Input BF Code: ") if c in commands])

s["stdin"] = [ord(c) for c in raw_input("Standard Input: ")]

execbf(inp)

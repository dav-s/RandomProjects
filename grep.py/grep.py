import clip
import re
import sys

app = clip.App()


@app.main(description="A small low-featured implementation of grep.")
@clip.arg("pattern", required=True, help="The regex pattern to match on the input.")
@clip.opt("-f", "--file", help="The file to match lines on. If not specified: stdin.")
@clip.flag("-o", "--only-matching", help="Only print the matching section.")
@clip.flag("-i", "--ignore-case", help="Only print the matching section.")
def grep(pattern, file, only_matching, ignore_case):
    inpt = open(file) if file else sys.stdin
    inpt = inpt.read().splitlines()

    for line in inpt:
        if ignore_case:
            s = re.search(pattern, line, flags=re.IGNORECASE)
        else:
            s = re.search(pattern, line)
        if s is not None:
            if only_matching:
                clip.echo(s.group(0))
            else:
                clip.echo(line)


if __name__ == '__main__':
    try:
        app.run()
    except clip.ClipExit:
        pass

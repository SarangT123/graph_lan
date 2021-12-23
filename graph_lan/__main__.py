import sys
import compiler
if len(sys.argv) < 3:
    print("Usage: python3 main.py -r <filename> <compiled or interpreted(-i/-c)>")
    sys.exit(1)
if sys.argv[1] == '-r':
    if len(sys.argv) >= 4:
        if sys.argv[3] == '-R':
            compiler.run(sys.argv[2]).run()
            with open("compiled.py", "r") as f:
                exec(f.read())
    else:
        compiler.run(sys.argv[2]).run()

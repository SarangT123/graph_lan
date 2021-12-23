import sys
import compiler
import interpreter
if len(sys.argv) < 4:
    print("Usage: python3 main.py -r <filename> <compiled or interpreted(-i/-c)>")
    sys.exit(1)
if sys.argv[1] == '-r':
    if sys.argv[3] == '-i':
        interpreter.run(sys.argv[2]).run()
    if sys.argv[3] == '-c':
        compiler.run(sys.argv[2]).run()

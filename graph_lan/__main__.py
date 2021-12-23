import sys
import compiler
if len(sys.argv) < 4:
    print("Usage: python3 main.py -r <filename> <compiled or interpreted(-i/-c)>")
    sys.exit(1)
if sys.argv[1] == '-r':
    compiler.run(sys.argv[2]).run()

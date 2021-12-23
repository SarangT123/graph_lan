from graph_lan import compiler, interpreter
import sys.argv as arg

if arg[1] == '-v':
    print('graph_lan version 0.1')
    print('Copyright (c) 2019, 2020, by Maximilian Schlueter')
    print('License: MIT')
if arg[1] == '-r':
    compiler.run(arg[2])

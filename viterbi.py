# -*- coding: utf-8 -*-

from pydoc import text
import sys, time
from nltk import tokenize
from nltk.grammar import PCFG
from nltk.parse import pchart
from nltk.parse import ViterbiParser
from functools import reduce
from tabulate import tabulate

toy_pcfg1 = PCFG.fromstring("""
S ->NP VP [1.0]
PP ->P NP [1.0]
VP ->V NP [0.7]
VP ->VP PP [0.3]
P -> 'with' [1.0]
V -> 'saw' [1.0]
NP ->NP PP [0.4]
NP -> 'student' [0.1]
NP -> 'binocular' [0.18]
NP -> 'saw' [0.04]
NP -> 'tiger' [0.18]
NP -> 'telescopes' [0.1]
"""
)

sent="student saw tiger with binocular"
grammar=toy_pcfg1
tokens = sent.split()

parsers = [ViterbiParser(grammar)]

times = []
average_p = []
num_parses = []
all_parses = {}
for parser in parsers:
    print('s: %s\nparser: %s\ngrammar: %s' % (sent,parser,grammar))
    print()
    parser.trace(3)
    t = time.time()
    parses = parser.parse_all(tokens)
    times.append(time.time()-t)
    if parses:
        p = reduce(lambda a,b:a+b.prob(), parses, 0.0)
    else:
        p = 0
    average_p.append(p)
    num_parses.append(len(parses))
    for p in parses:
        all_parses[p.freeze()] = 1

stat=[]
print()
for i in range(len(parsers)):
    temp=[]
    temp.append('%19s'%parsers[i].__class__.__name__),
    temp.append('%4d'%getattr(parsers[0], "beam_size", 0))
    temp.append('%11.4f'%times[i])
    temp.append('%11d'%num_parses[i])
    temp.append('%19.14f'%average_p[i])
    stat.append(temp)
print(tabulate(stat,headers=["Parser","Beam","Time(secs)","#Parses","Average P(parse)"],tablefmt="fancy_grid"))
parses = all_parses.keys()
if parses:
    p = reduce(lambda a,b:a+b.prob(), parses, 0)/len(parses)
else:
    p = 0
print()

for parse in parses:
    print(parse)

toy_pcfg1 = PCFG.fromstring("""
S ->NP NP [1.0]
PP ->P NP [1.0]
VP ->V NP [0.7]
VP ->VP PP [0.3]
P -> 'with' [1.0]
V -> 'saw' [1.0]
NP ->NP PP [0.4]
NP -> 'student' [0.1]
NP -> 'binocular' [0.18]
NP -> 'saw' [0.04]
NP -> 'tiger' [0.18]
NP -> 'telescopes' [0.1]
"""
)

sent="student saw tiger with binocular"
grammar=toy_pcfg1
tokens = sent.split()

parsers = [ViterbiParser(grammar)]

times = []
average_p = []
num_parses = []
all_parses = {}
for parser in parsers:
    print('s: %s\nparser: %s\ngrammar: %s' % (sent,parser,grammar))
    print()
    parser.trace(3)
    t = time.time()
    parses = parser.parse_all(tokens)
    times.append(time.time()-t)
    if parses:
        p = reduce(lambda a,b:a+b.prob(), parses, 0.0)
    else:
        p = 0
    average_p.append(p)
    num_parses.append(len(parses))
    for p in parses:
        all_parses[p.freeze()] = 1

stat=[]
print()
for i in range(len(parsers)):
    temp=[]
    temp.append('%19s'%parsers[i].__class__.__name__),
    temp.append('%4d'%getattr(parsers[0], "beam_size", 0))
    temp.append('%11.4f'%times[i])
    temp.append('%11d'%num_parses[i])
    temp.append('%19.14f'%average_p[i])
    stat.append(temp)
print(tabulate(stat,headers=["Parser","Beam","Time(secs)","#Parses","Average P(parse)"],tablefmt="fancy_grid"))
parses = all_parses.keys()
if parses:
    p = reduce(lambda a,b:a+b.prob(), parses, 0)/len(parses)
else:
    p = 0
print()

for parse in parses:
    print(parse)
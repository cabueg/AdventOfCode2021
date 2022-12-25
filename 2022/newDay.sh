#!/bin/bash

touch day$1.py
touch inputs/day$1.txt

echo -e "def part1():" >> day$1.py
echo -e "\tf = open('./inputs/day$1.txt', 'r')" >> day$1.py
echo -e "\tlines = f.readlines()" >> day$1.py
echo -e "\tfor line in lines:" >> day$1.py
echo -e "\t\tprint(lines)" >> day$1.py
echo -e "\treturn\n\n" >> day$1.py
echo -e "print(f'Part 1 Ans: {part1()}')\n\n" >> day$1.py

echo -e "def part2():" >> day$1.py
echo -e "\tf = open('./inputs/day$1.txt', 'r')" >> day$1.py
echo -e "\tlines = f.readlines()" >> day$1.py
echo -e "\tfor line in lines:" >> day$1.py
echo -e "\t\tprint(lines)" >> day$1.py
echo -e "\treturn\n\n" >> day$1.py
echo -e "#print(f'Part 2 Ans: {part2()}')\n\n" >> day$1.py
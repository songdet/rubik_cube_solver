# Rubik Cube Solver

As part of our project to build a rubik cube solving machine for MEMS 1049, we need to develop a control server running on the laptop that will communicate will an ATMEGA328p microcontroller. This repository contains the code for that control server.

## Development Setup

1. In directory, setup virtualenv:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Get Cube Instruction Set for Cube

The cube instruction set is a set of command that we will implement on ATMEGA328p to actuate the motor based on received instruction. To get the instruction set for certain cube configuration, follow the development setup step and run `python3 ./scripts/isa_for_cube.py`

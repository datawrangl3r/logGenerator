# logGenerator

A python program to generate random log texts in regular intervals

usage: generator.py [-h] -i ITERATIONS [-f FRAMEWORK] [-s SLEEP]

Random Log Generator.

optional arguments:

```text
  -h, --help            show this help message and exit
  -i ITERATIONS, --iterations ITERATIONS
                        Number of iterations
  -f FRAMEWORK, --framework FRAMEWORK
                        Name of framework
  -s SLEEP, --sleep SLEEP
                        Delay for the log to be printed
```

## Example

```bash
git clone https://github.com/datawrangl3r/logGenerator.git
cd logGenerator
python3 generator.py -i1000
```
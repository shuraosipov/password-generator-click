# Example of usage Click for building CLI

# Install
```
python -m venv venv
source venv/bin/activate
pip -r install requirements.txt
```

# Generate simple password
```
$ python passgen.py simple

V59etrLg
```

# Generate complex password
```
python passgen.py complex

Wii572lg9Q
```

# Generate a hard-to-guess security token
```
python passgen.py token

hok4_Snx8Uvy56KkV8jHKFaCrPRXCLNLc6PH0P12EuA
```

# Help
```
$ python passgen.py --help

Usage: passgen.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  complex  Generate a ten-character alphanumeric password with at least...
  simple   Generate an eight-character alphanumeric password
  token    Generate a hard-to-guess security token suitable for password...
```
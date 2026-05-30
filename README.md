# PEACE to EQ APO preset

A simple script to convert your .peace EQ preset from PEACE equalizer to EQ APO format.

Can be used to move your configuration from Windows (PEACE) to Linux (EasyEffects).

# Warning

This script has not been tested extensively. Some bug and incompatibility may occur.

# Usage

## Getting dependencies

1. [Recommended] Make virtual environment with [`uv`](https://docs.astral.sh/uv/getting-started/installation/)

```
uv venv
```

Don't forget to activate your newly created environment according to your shell.

2. Install dependencies

```
uv sync
```

## Convert the file

The script accept [INPUT FILE PATH] [OUTPUT FILE PATH] arguments

So, heres an example to run it

```
python ./main.py ~/Downloads/test.peace ~/Downloads/result.txt
```

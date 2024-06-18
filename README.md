# Snapshoter

Lets you take a snapshot of a file on HTTPS for datamining

## Installation

First git clone fingerprinter since its a dependency

```
git clone https://www.github.com/0x4248/FingerPrinter
```

Then install it

```
cd FingerPrinter
pip install .
```

Then clone this repository and install the dependencies

```
apt install make
```

```bash
pip install requests
```

## Usage

Once configured you can run the snapshoter with the following command

```bash
make
```

This will store the snapshots in the `snapshots` directory

## Configuration

To add new urls add a new url under the urls list `config.py`

## Licence

This project is licensed under the GNU General Public License v3.0 - see the [LICENCE](LICENCE) file for details
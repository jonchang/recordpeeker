# Record Peeker

Peeks at FFRK battle drops data. Also reports your best record synergy equipment. Could potentially be expanded to do other things.

## Installation

Note: Only tested on OS X. Will probably work on Windows and Linux as long as mitmproxy works too.

Assuming you have [Homebrew](http://brew.sh) installed:

```
brew install python
pip install git+https://github.com/jonchang/recordpeeker.git
```

## Usage

In your Terminal, just type in:

```
recordpeeker
```

Then, set up your phone to use your computer as a proxy. Here's what it might look like on iOS:

![iOS manual proxy configuration](https://mitmproxy.org/doc/screenshots/ios-manual.png)

Enter a battle, and watch the drops roll in! Or enter the Party screen and optimize your equipment setup.

```
$ recordpeeker
Configure your phone's proxy to point to this computer, then visit mitm.it
on your phone to install the interception certificate.

Record Peeker is listening on 10.0.0.1, port 8080...
Entering battle #307001..
  Round 1:
    MP drops nothing!
    Special Combatant drops nothing!
  Round 2:
    Sweeper drops 1* Staff (IV)
    Special Combatant drops nothing!
  Round 3:
    Sweeper drops nothing!
    Sweeper drops 1* orb id#40000031
  Round 4:
    Guard Scorpion drops nothing!

Best equipment for FF4:
  atk: 75 -- Kunai (IV)++
  atk: 75 -- Kunai (IV)++
  atk: 75 -- Kunai (IV)++
  atk: 75 -- Kunai (IV)++
  atk: 61 -- Whip (IV)++
  matk: 92 -- Whip (IV)++
  matk: 64 -- Sage's Staff (IV)+
  mnd: 128 -- Sage's Staff (IV)+
  mnd: 80 -- Power Staff (IV)++
  def: 106 -- Genji Armor (V)
  def: 99 -- Genji Helm (V)
  def: 92 -- Mythril Helm (IV)++
  def: 83 -- Genji Shield (IV)
  def: 67 -- Black Cowl (IV)++
```

## Contributing

* Currently, the item database only includes equipment (i.e., no orbs or anything else). Edit [items.csv](https://github.com/jonchang/recordpeeker/blob/master/recordpeeker/data/items.csv) to add new things to the database.

* Functions wishlist
    * Package a .app or .exe for easy setup
    * Record drop frequencies

## Developing

```
git clone https://github.com/jonchang/recordpeeker.git
cd recordpeeker
virtualenv env
source env/bin/activate
./setup.py develop
```

## License

This software is licensed under the [MIT License](http://choosealicense.com/licenses/mit/). For more information, see the `LICENSE` file.

## Inspiration

* [Snapception](https://github.com/thebradbain/snapception/)


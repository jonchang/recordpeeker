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

Record Peeker is listening on 10.0.0.1, port 8080.

Try entering the Party screen, or starting a battle.

Entering battle #307001..
  round  enemy              drop
-------  -----------------  --------
      1  Sweeper            nothing
      1  Special Combatant  nothing
      2  Sweeper            nothing
      2  Smogger            nothing
      3  MP                 133 gold
      3  Smogger            nothing
      4  Guard Scorpion     nothing

Best equipment for FF4:
stat      n  weapon              stat      n  armor                 stat      n  accessory
------  ---  ------------------  ------  ---  --------------------  ------  ---  --------------------
atk      75  Kunai (IV)++        atk      12  Genji Helm (V)        atk      15  Hyper Wrist (VI)
atk      75  Kunai (IV)++        atk      10  Mythril Helm (IV)++   atk       8  Hero's Ring (VI)
atk      75  Kunai (IV)++        atk       9  Crystal Helm (VI)     atk       5  Power Wrist (VII)
atk      75  Kunai (IV)++        atk       8  Rune Armlet (VII)+    atk       5  Power Wrist (VII)
atk      61  Whip (IV)++         atk       8  Diamond Bangle (VII)  atk       5  Power Wrist (VII)
matk     92  Whip (IV)++         matk     27  Black Cowl (IV)++     matk      8  Earring (VII)
matk     64  Sage's Staff (IV)+  matk     17  Green Beret (IV)++    matk      8  Earring (VII)
mnd     128  Sage's Staff (IV)+  mnd      27  Black Cowl (IV)++     mnd       0  Earring (VII)
mnd      80  Power Staff (IV)++  mnd      19  Wizard's Hat (IV)++   mnd       0  Talisman (VII)
def       0  Mace (XII)          def     106  Genji Armor (V)       def      12  Protect Ring (VII)
def       0  Dagger (IX)         def      99  Genji Helm (V)        def       3  Star Pendant (VII)
def       0  Staff (IV)          def      92  Mythril Helm (IV)++   def       3  Silver Glasses (VII)
def       0  Cat Claws (III)     def      83  Genji Shield (IV)     def       0  Earring (VII)
def       0  Cat Claws (III)     def      67  Black Cowl (IV)++     def       0  Talisman (VII)

```

## Contributing

* Missing item names? Edit [items.csv](https://github.com/jonchang/recordpeeker/blob/master/recordpeeker/data/items.csv) to add new things to the database.

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


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
  n  stat    accessory               n  stat    armor                 stat      n  weapon
---  ------  --------------------  ---  ------  --------------------  ------  ---  ------------------
 15  atk     Hyper Wrist (VI)       75  atk     Genji Helm (V)        atk      12  Kunai (IV)++
  8  atk     Hero's Ring (VI)       75  atk     Mythril Helm (IV)++   atk      10  Kunai (IV)++
  5  atk     Power Wrist (VII)      75  atk     Crystal Helm (VI)     atk       9  Kunai (IV)++
  5  atk     Power Wrist (VII)      75  atk     Rune Armlet (VII)+    atk       8  Kunai (IV)++
  5  atk     Power Wrist (VII)      61  atk     Diamond Bangle (VII)  atk       8  Whip (IV)++
  8  matk    Earring (VII)          92  matk    Black Cowl (IV)++     matk     27  Whip (IV)++
  8  matk    Earring (VII)          64  matk    Green Beret (IV)++    matk     17  Sage's Staff (IV)+
  0  mnd     Earring (VII)         128  mnd     Black Cowl (IV)++     mnd      27  Sage's Staff (IV)+
  0  mnd     Talisman (VII)         80  mnd     Wizard's Hat (IV)++   mnd      19  Power Staff (IV)++
 12  def     Protect Ring (VII)      0  def     Genji Armor (V)       def     106  Mace (XII)
  3  def     Star Pendant (VII)      0  def     Genji Helm (V)        def      99  Dagger (IX)
  3  def     Silver Glasses (VII)    0  def     Mythril Helm (IV)++   def      92  Staff (IV)
  0  def     Earring (VII)           0  def     Genji Shield (IV)     def      83  Cat Claws (III)
  0  def     Talisman (VII)          0  def     Black Cowl (IV)++     def      67  Cat Claws (III)
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


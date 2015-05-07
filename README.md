# Record Peeker

Peeks at FFRK battle drops data. Also reports your best record synergy equipment. Could potentially be expanded to do other things.

## Installation and setup

See [INSTALL.md](https://github.com/jonchang/recordpeeker/blob/master/INSTALL.md).

## Usage

In your Terminal, just type in:

```
recordpeeker
```

Enter a battle, and watch the drops roll in! Or enter the Party screen and optimize your equipment setup.

[![asciicast](https://asciinema.org/a/19644.png)](https://asciinema.org/a/19644)

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


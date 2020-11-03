# PseudoFutoshiki

Simple overview of use/purpose.

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Installing

1. Clone the repository or download the source code to your local machine
2. Run the following command to install the necessary library dependencies ([PySAT](https://pysathq.github.io/) and [PyPBLib](https://pypi.org/project/pypblib/))
```
pip3 install -r requirements.txt
```

### Executing program

1. Choose one of the prebuilt boards found in the boards folder or create your own board following the style of the prebuilt boards
2. Run main.py with the filepath of your desired board as the sole argument.

Ex.
```
python3 main.py boards/grid2_val.txt
```

## Authors & Contact
* Sean Kelly - [@se-ke](https://github.com/se-ke)
* Dylan Huang - [@huangdylan08](https://github.com/huangdylan08)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Professor Jason Hemann introduced us to the world of (un)satisfiability in our CS2800 class during the Fall 2020 semester
* mattismegevand's [Futoshiki SAT solver](https://github.com/mattismegevand/sat-futoshiki) served as a foundation for this project and helped us to identify what has already been done in terms of Futoshiki SAT solvers
* Martin Hořeňovský's article on [modern SAT solvers](https://codingnest.com/modern-sat-solvers-fast-neat-underused-part-1-of-n/) taught us a lot about how to encode games in boolean logic
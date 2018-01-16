# Quik

Quik is a very simple parsing engine for python. It's primary usage is for writing blogs, articles, websites, etc. It is LaTeX-like, in the sense that it does *not* follow a tree structure. At the moment, Quik supports only HTML output.

## Getting Started

I recommend downloading Quik as a git submodule, however, you are free to do as you wish.

### Prerequisites

You only need python. This was designed for `python2`, but I don't see a reason why it wouldn't work on `python3`.

For unit tests, the `pep8` program is required.

### Installing

If you do decide to use Quik as a git submodule, it's as easy as:

```bash
git submodule add https://github.com/markovejnovic/Quik.git
```

in your project directory.

### Development installation

If you wish to do development, `pycodestyle` is necessary for code style tests. Installing it in a `virtualenv` is recommended.
In your project directory:

```bash
virtualenv venv
. venv/bin/activate
pip install pycodestyle
```

## Running the tests

The tests for this package are designed so they work with `python unittest` discovery. They are in the `test/` directory. Running all of the tests is as easy as:

```bash
sh ./run_tests.sh
```

### Unit tests

The simple unit tests in `test_Quik` check for how well the whole `Quik` package works.

### Coding style tests

The coding style is planned to be according to `PEP8`, but these tests are not yet implemented.

## License

This project is licensed under the GNU GPLv3 - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Just [PurpleBooth](https://github.com/PurpleBooth) for showing me how to make a [good README.md](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) file.



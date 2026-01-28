# nflverse

## Installation

The easiest way to get nflverse is to install it from CRAN with:

```r
install.packages("nflverse")
```

To get a bug fix or to use a feature from the development version, you can install the development version of nflverse either from GitHub with:

```r
if (!require("pak")) install.packages("pak")
pak::pak("nflverse/nflverse")
```

or prebuilt from the development repo with:

```r
install.packages("nflverse", repos = c("https://nflverse.r-universe.dev", getOption("repos")))
```

## Usage

`library(nflverse)` will load the following nflverse packages:

- **nflfastR**, for play-by-play data back to 1999.
- **nflseedR**, for season simulations.
- **nfl4th**, for 4th down analysis.
- **nflreadr**, for fast and efficient nflverse data downloads.
- **nflplotR**, for tools to create visualizations of NFL related analysis.

## Getting help

The best places to get help on this package are:

- the [nflverse discord](https://discord.gg/nflverse) (for both this package as well as anything R/NFL related)
- [opening an issue](https://github.com/nflverse/nflverse/issues/new)

## Contributing

Many hands make light work! Here are some ways you can contribute to this project:

- You can [open an issue](https://github.com/nflverse/nflverse/issues/new) if you'd like to request specific data or report a bug/error.
- If you'd like to contribute code, please check out the [contribution guidelines](CONTRIBUTING.md).

## Terms of Use

The R code for this package is released as open source under the [MIT License](LICENSE). NFL data accessed by this package belong to their respective owners, and are governed by their terms of use.

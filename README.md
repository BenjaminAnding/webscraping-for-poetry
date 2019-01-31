# Webscraping For Poetry In Python

## Requirements

Python 3:

`
#most linux platforms
$ sudo apt-get install python

#arch
$ sudo pacman -S python
`

Pip:

`
$ # Install the latest version of pip
$ curl https://bootstrap.pypa.io/get-pip.py | python
`

Beautiful Soup:

`
$ pip install beautifulsoup4
`

lxml:

`
#most linux platforms
$ sudo apt-get install lxml-python

#arch
$ sudo pacman -S lxml-python
`

## Usage

1. Clone or download the repo and cd into the top directory.
2. Run the following
`
$ sudo chmod 0755 ./runall.sh
`
3. Run ./runall.sh

Assuming everything is working your terminal will be filled with a repeating message: "File exists". DON'T PANIC, this is normal. It is hard to gauge progress, but each of the eight webscraping start by listing the total number of poems being downloaded in the form of a tuple (ie. (440, 440)) then attempt to create folders for the authors, if a file exists for an author, File exists is printed to the output. Once all eight webscraping programs have finished, the clean and label program starts. As this program finishes with a file it will print a message, as well as a message when it finishes with a directory.

Once it's all said and done, you can find the groomed data in each subdirectory of authors as "combined.txt" along with a "label.txt" that includes the index nuber that matches to the top level directory's "labels.txt". Enjoy!

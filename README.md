# Solutions to [advent of code](https://adventofcode.com/) 2020.

#### Dependencies:

- pypy: `sudo apt-get install pypy`
- pip: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && pypy get-pip.py && rm get-pip.py`
- requests lib: `pypy3 -m pip install requests`
- beautifulsoup lib: `pypy3 -m pip install beautifulsoup4`
- `secret.py`: Find your adventofcode cookie `XXXX` in your browser, and put `session='XXXX'` inside a file `secret.py`. 

Now `runner.py` can download your inputs automatically, and submit your answers, if you dare!

Copy the template to `$d/day$d.py`, and hard code the day and year in the functions: `get_day()` and `get_year()`.

If you now run `pypy3 $d/day$d.py` your inputfile will be downloaded, and you will run the functions `p1` and `p2` on the input files.

# csv_to_rsi

Translates csv data into an [rsi format](https://en.wikipedia.org/wiki/RIS_(file_format)#Format).

## Prerequisites

python3

## Install


## Execute

### Basic - write to standard out

The scripts rsi output is written to standard out. Just redirect it to a file with rsi extension.
```
python3 csv_to_rsi.py path/to/mycsv.csv > myrsi.rsi
```


## Example Input
The csv file is expected to have a header row followed by rows of corresponding data. The following is an example of that csv format. The csv can have columns but they will be ignored. Empty data rows will be ignored as well.
```
| Title             | Authors                  | Abstract                 | Published Year | Journal         | Volume | Issue | Accession Number | DOI |
| ----------------- | ------------------------ | ------------------------ | -------------- | --------------- | ------ | ----- | ---------------- | --- |
| The bad beginning | Douglas, Mark; Lee, Ryan | The theory of everything | 2020           | Fairy Tale Plus | 54     | 0     | 123              | Doi |
```
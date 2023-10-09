# ADIFUtils
ADIF - utility tools for the Amateur Data Interchange Format

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Pylint](https://github.com/JS2IIU-MH/ADIFUtils/actions/workflows/pylint.yml/badge.svg)](https://github.com/JS2IIU-MH/ADIFUtils/actions/workflows/pylint.yml)

## class adif_fields.ADIFfields

```
__init__(self)
```
Prepare `df_all` DataFrame which has all of ADIF field table data.
If ADIFfields.csv is existing, `df_all` is restore from ADIFfields.csv. Othewise fetching web scaping data from adif.org and set `df_all`.


```
fetch_fields(self)
```
Fetching ADIF field data from ADIF V3.1.4 specification in adif.org.
All of table data will be saved pd.DataFrame, `df_all`.


```
get_all_fields(self) -> pd.DataFrame
```
Returns `df_all` as pd.DataFrame.

```
get_fields(self) -> pd.Series
```
Returns `df_all['Field Name']` as pd.Series.


```
get_field_list(self) -> list
```
Returns `df_all['Field Name']` as 1D list.



```
get_table_index(cls) -> list
```
Returns list of index list.
`TABLE_INDEX = ['Field Name', 'Data Type', 'Enumeration', 'Description']`

```
save_all_fields(self, csvfilepath=OUT_FILENAME)
```
Save `df_all` to csv

```
save_fields(self, csvfilepath=OUT_FILENAME_FIELD_ONLY)
```
Save `df_all` to csv, only Field Name part only.

```
print_all(self)
```
Just print `df_all` on console.


## Reference

- [The Independent ADIF Site](http://adif.org/)
- [Released ADIF Version 3.1.0, updated 2019/05/21](https://www.adif.org/310/ADIF_310.htm)



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

## class adif_to_dataframe.AdifToDataFrame

Translate ADIF file (*.adi) to pandas.DataFrame.

Example of output DataFrame
```raw
        CALL MODE BAND       FREQ GRIDSQUARE  QSO_DATE TIME_ON QSO_DATE_OFF TIME_OFF RST_RCVD RST_SENT STATION_CALLSIGN MY_GRIDSQUARE                    COMMENT SUBMODE EQSL_QSL_SENT
0     JA4FJR  FT8  40m   7.043701        N/A  20210206  050800     20210206   050859      -12      -07           JS2IIU        PM85kg  FT8  Sent: -07  Rcvd: -12     N/A           N/A
1     JH7OTG  FT8  40m   7.043701       QM08  20210206  051415     20210206   051514      -10      -18           JS2IIU        PM85kg  FT8  Sent: -18  Rcvd: -10     N/A           N/A
2     JH7OUW  FT8  40m   7.043701       QM09  20210206  051545     20210206   051644      -09      -10           JS2IIU        PM85kg  FT8  Sent: -10  Rcvd: -09     N/A           N/A
3     JH7UKE  FT8  40m   7.043798       QM08  20210206  052245     20210206   052414      -18      -15           JS2IIU        PM85kg  FT8  Sent: -15  Rcvd: -18     N/A           N/A
4     JH8WGT  FT8  40m   7.043798       QN02  20210206  053645     20210206   053744      -12      -06           JS2IIU        PM85kg  FT8  Sent: -06  Rcvd: -12     N/A           N/A
```
## Reference
### ADIF
- [The Independent ADIF Site](http://adif.org/)
- [Released ADIF Version 3.1.0, updated 2019/05/21](https://www.adif.org/310/ADIF_310.htm)

### Python
- [unspecified-encoding / W1514 - Pylint 3.1.0-dev0 documentation](https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/unspecified-encoding.html)
- [Pythonの正規表現モジュールreの使い方（match, search, subなど） | note.nkmk.me](https://note.nkmk.me/python-re-match-search-findall-etc/)
- [pandas 辞書型からDataFrameを生成｜インデックスとコラムの設定も！ - YutaKaのPython教室](https://www.yutaka-note.com/entry/pandas_dict)
- [pandasで任意の位置の値を取得・変更するat, iat, loc, iloc | note.nkmk.me](https://note.nkmk.me/python-pandas-at-iat-loc-iloc/)
- [consider-using-with / R1732 - Pylint 3.1.0-dev0 documentation](https://pylint.pycqa.org/en/latest/user_guide/messages/refactor/consider-using-with.html)

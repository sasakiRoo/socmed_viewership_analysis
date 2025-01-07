# SOCMED VIEWERSHIP ANALYSIS

v 2.1.1

## Purposes

to analyse the best timing to post on social media from a csv file

<hr>

`status: not final`

`latest commit: TODO: fix table columns size`

## CSV table timeline views

This table shows random task completion times in hours for different time spans. The values are randomly generated integers.

| 0.5 hours | 1 hour | 2 hours | 24 hours |
| --------- | ------ | ------- | -------- |
| 12        | 34     | 22      | 89       |
| 23        | 47     | 12      | 93       |
| 45        | 29     | 37      | 72       |
| 56        | 18     | 63      | 65       |
| 33        | 22     | 14      | 80       |

### Example

For the above table, the highest values per column are:

- **0.5 hours**: 56
- **1 hour**: 47
- **2 hours**: 63
- **24 hours**: 93

### Output

| time  | 0.5 hours |
| ----- | --------- |
| 17:30 | 12        |
| 20:10 | 23        |
| 08:40 | 45        |
| 13:30 | 56        |
| 17:05 | 33        |

`maximum views in 0.5 hours is 56 video posted at 13:30`

These maximum views help highlight the most views of a video in different timespans

<hr>

## HOW TO USE

### run project

`python3 index.py`

<hr>

### Contributing

Feel free to contribute by submitting pull requests with better logic or design improvements.

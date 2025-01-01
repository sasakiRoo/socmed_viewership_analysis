# SOCMED VIEWERSHIP ANALYSIS

v 1.0.0

## Purposes

to analyse the best timing to post on social media from a csv file

<hr>

`status: not final`

`latest commit: add highest views according to timeline`

The latest commit implements functionality that displays the highest views from the table based on the timeline (0.5 hours, 1 hour, 2 hours, or 24 hours). This allows users to quickly identify the maximum value for each time span.

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

These maximum values help highlight the most time-consuming tasks over different timelines.

<hr>

## HOW TO USE

### run project

`python3 index.py`

<hr>

### Contributing

Feel free to contribute by submitting pull requests with better logic or design improvements.

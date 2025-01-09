# SOCMED VIEWERSHIP ANALYSIS

v 3.0.0

## Purposes

to analyse the best timing to post on social media from a csv file

## Features

- SHOW ALL TABLE
- SHOW TABLE BASED ON TIMESPAN WHICH USER CHOOSE FOR

<hr>

`status: final - maybe ?`

`latest commit: fix columns table for all features`

### Feature 1 - SHOW ALL TABLE

| date     | link   | posted at | 30min | 1hr  | 2 hrs | 24 hrs | post type |
| -------- | ------ | --------- | ----- | ---- | ----- | ------ | --------- |
| 31/12/24 | you... | 21:59     | 100K  | 200K | -     | -      | video     |
| 9/1/25   | htt... | 10:10     | 2000  | 2500 | 3204  | 23K    |           |
| 10/1/25  | htt... | 10:31     | 15K   | 25K  | 30K   | 120K   |           |
| 11/1/25  | htt... | 12:30     | 230K  | 500K | 1M+   | 3M+    |           |

---

### Feature 2 - SHOW TABLE BASED ON TIMESPAN WHICH USER CHOOSE FOR

This table shows your views in different timespan

| 0.5 hours | 1 hour | 2 hours | 24 hours |
| --------- | ------ | ------- | -------- |
| 12        | 34     | 22      | 89       |
| 23        | 47     | 12      | 93       |
| 45        | 29     | 37      | 72       |
| 56        | 18     | 63      | 65       |
| 33        | 22     | 14      | 80       |

> Example:
> Users will be asked: <br>
> choose timeline: | 0.5 hours | 1 hour | 2 hours | 24 hours <br>
> input by typing the number: 2

### Output

> == here`s the result of your views in 2.0 ==

> | posted at | views   |
> | --------- | ------- |
> | 21:59     | 0       |
> | 10:10     | 3204    |
> | 10:31     | 30000   |
> | 12:30     | 1200000 |

> maximum views in 2.0 hours is 1200000 video posted at 12:30

These maximum views help highlight the most views of a video in different timespans

<hr>

## HOW TO USE

### run project

`python3 index.py`

<hr>

### Contributing

Feel free to contribute by submitting pull requests with better logic or design improvements.

```

```

# SOCIAL MEDIA VIEWERSHIP ANALYSIS

## Purposes

Helping Content Creators To analyse the best timing to post on social media from a csv file

## Features

1. SHOW ALL TABLE
2. SHOW THE MOST VIEWED

### Feature 1 - SHOW ALL TABLE

| date     | link   | posted at | 30min | 1hr  | 2 hrs | 24 hrs | post type |
| -------- | ------ | --------- | ----- | ---- | ----- | ------ | --------- |
| 31/12/24 | you... | 21:59     | 100K  | 200K | -     | -      | video     |
| 9/1/25   | htt... | 10:10     | 2000  | 2500 | 3204  | 23K    |           |
| 10/1/25  | htt... | 10:31     | 15K   | 25K  | 30K   | 120K   |           |
| 11/1/25  | htt... | 12:30     | 230K  | 500K | 1M+   | 3M+    |           |

### Feature 2 - SHOW THE MOST VIEWED WITH TABLE BASED ON TIMESPAN WHICH THE USER CHOOSE FOR

This table shows your views in different timespan

| 0.5 hours | 1 hour | 2 hours | 24 hours |
| --------- | ------ | ------- | -------- |
| 100000    | 200000 | 0       | 0        |
| 2000      | 2500   | 3204    | 23000    |
| 15000     | 25000  | 30000   | 120000   |
| 230000    | 500000 | 1200000 | 3500000  |

Example:
User will be asked: <br>

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

This maximum views help highlight the most views of a video in different timespans

<hr>

### HOW TO USE

### clone repository

### using ssh:

```
git clone git@github.com:sasakiRoo/socmed_viewership_analysis.git
```

### using http:

```
git clone https://github.com/sasakiRoo/socmed_viewership_analysis.git
```

### create your own csv file - use the template_sheets.csv file as a template design guide

### run project

```
python3 index.py
```

<hr>

### Contributing

Feel free to contribute by submitting pull requests with better logic or design improvements.

### Contact:

<a href="mailto:sasakiroo@gmail.com" target="_blank">Email</a>

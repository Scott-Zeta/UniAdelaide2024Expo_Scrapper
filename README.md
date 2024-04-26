# 2024 University of Adelaide Career Expo Scrapper

## What it is?

A web scraper, for self usage during 2024 University of Adelaide Career Expo. Use to gather information for attended companies.

When I am suffering from browsing company's websites, I suddenly was given this idea. So I spent a day on it.

## Why build this?

Many people keep telling me should do research on those employeer, understand their so called "value", "culture". However I don't like to read business phrase. So it records info might be "useful" by traversal the sitemap. And wait for further analysis, whatever from machine or human.

## How to use it?

1. Create a new folder, with the company's name
2. Create a new file without extension, write the the website's site map index url inside.
3. Run main.py [folder], there will be an index of sitemap, page contents will be record in txt.

## Isuee?

1. Many sites has non-standard page structure, so might need to modify the code for specific case. Or it might fetch plenty of useless info like header/footer or other duplicate elements.
2. Records structure currently are plain text. If more data cleaning/processing needs, perhaps a better data structure needed like json. However this isn't what I can consider in such a temperory solution.

## Environment

### Create Env

```bash
python -m venv env
```

### Activate the Env

```bash
source env/bin/activate
```

### Install from Env

```bash
pip install -r requirements.txt
```

### Export Env

```bash
pip freeze > requirements.txt
```

### Deactivate Env

```bash
deactivate
```

# Getting started with Jupyter Books

## Method overview

1. Set up repository (repo) on GitHub (github.com)
1. Clone repo to local computer
1. Create a folder for book content (markdown pages and Jupyter notebooks)
1. Add required content
1. Create a table of contents _toc.yml file in content folder
1. Build book
1. Use `ghp-import` to push contents of book to GitHub (creates a `gh-pages` branch)
1. Go to GitHub repo settings, and activate GitHub pages (point to `gh-pages`) and copy link to webiste

## Table of contents

The order, and breakdown, of the book is held in the `_toc.yml` file in the book contents. folder.

This file may be as simple as a list of required markdown and notebook pages with the syntax `- file filename_with_no_extension`.

The `_toc.yml` may also be used to add structure such as parts, chapters and sections.


## Building the book

Install Jupyter Book with `pip install jupyter-book`

Build book with the `jupyter-book build` command followed by the contents directory, e.g. `jupyter-book build ./content` 


# Pelican Static Site Generater Project

1. build dev

```
$ make html
$ pelican -l
```

2. build publish

```
$ make publish
$ ghp-import output -b gh-pages
$ git push origin gh-pages
```

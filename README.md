# work • [ ![Build Status] [travis-image] ] [travis] [ ![License] [license-image] ] [license]

* Python package for easy saving and loading in organized workspaces. *

[travis-image]: https://travis-ci.org/riceric22/work.png?branch=master
[travis]: https://travis-ci.org/riceric22/work

[license-image]: http://img.shields.io/badge/license-Apache--2-blue.svg?style=flat
[license]: LICENSE

## Why? 
To eliminate repetitive plumbing code when saving and loading data in different
organizational folders. 

## Getting started

### Install
`pip install work`

### Usage: 

+ `work.wd()` returns the working directory
+ `work.pwd()` prints the working directory, which by default is `tmp/`
+ `work.swd(s)` changes the working directory to `s`
+ `work.save(name, *args, **kwargs)` saves `(*args, **kwargs)` to your working
directory, and also returns the tuple. 
+ `work.load(name)` returns the tuple stored under `name`. 

### Example

```Python
>>> work.pwd()
tmp/
>>> work.swd('directory')
>>> work.save('experiments1', [1,2,3], alpha=0.1, beta=6)
(([1, 2, 3],), {'alpha': 0.1, 'beta': 6})
>>> work.load('experiments1')
(([1, 2, 3],), {'alpha': 0.1, 'beta': 6})
```
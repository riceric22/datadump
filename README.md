# work
Python package for fast and easy saving and loading of organized work. 

## why? 
To eliminate repetitive plumbing code when saving and loading data in different
organizational folders. 

## getting started

### Install
`pip install work`

### Usage: 

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
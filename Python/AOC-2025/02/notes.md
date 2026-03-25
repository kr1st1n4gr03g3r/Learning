# Python Notes

---

## `pathlib`


```Python
from pathlib import Path
```


[Pathlib](https://docs.python.org/3/library/pathlib.html) is a module with classes that are named for different operating systems. We will be using generic `Path` because it makes a concrete path.

---

## `.read_text`
```Python
input_file = Path("input-sample.txt").read_text(encoding="utf-8")
result = []
```

- We assign the variable *`input_file`*  to the `input-sample.txt` document at its path in the root.
- `.read-text` returns the decoded contents of the pointed-to file as a string with utf-8 encoding. 
- The variable `result` creates a list using `[]`  





















Problem:

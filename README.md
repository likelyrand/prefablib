## prefablib

This is a small python library to easily modify Cities Skylines 2 .Prefab files with OOP.
It's very unfinished and only has 2 components out of, like, 200 or something? But the basic things are finished.

You can read .Prefab files mostly without errors and you can write to said files, you can also modify attributes easily.

This will probably not be published to PyPi, ever. But you can freely contribute and fork it if you choose to do so.

Examples:

```python

import prefablib

prefab = prefablib.BuildingPrefab(
  name="Example Building"
)

prefab.components.append(
  prefablib.UIObject(
    icon="path/to/icon.svg"
  )
)

prefablib.dump(fp="path/to/file", prefab=prefab)

```

```python

import prefablib

prefab = prefablib.read(fp="path/to/file")

print("prefab.name")

```

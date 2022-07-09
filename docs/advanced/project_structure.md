# Project Structure

A Laz project consists of at least one directory containing a laz.yml configuration file. A project
can have multiple directories with each of them having 0 or 1 laz.yml files except for the top level
which must have 1. Lower-level directories containing a laz.yml file are called sub-projects.

A single-level Laz project:

```
top-level/
laz.yml
```

A multi-level Laz project:

```

```

A laz.yml encapsulates the configuration for a directory. It also inherits and/or overrides the
configurations found in parent directories within the same project.

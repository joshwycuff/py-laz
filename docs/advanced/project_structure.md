# Project Structure

A Laz project consists of at least one directory containing a laz.yml configuration file. A project
can have multiple directories with each of them having 0 or 1 laz.yml files except for the top level
which must have 1. Lower-level directories containing a laz.yml file are called sub-projects.

A single-level Laz project:

```
project-root/
├─ laz.yml

```

A multi-level Laz project:

```
project-root/
├─ sub-project-1/
│  ├─ laz.yml
├─ sub-project-2/
│  ├─ laz.yml
├─ not-laz-sub-project/
├─ laz.yml
```

A laz.yml encapsulates the configuration for a directory. It also inherits and/or overrides the
configurations found in parent directories within the same project.

Let's say the configuration files have the below contents.

```yaml
# project-root/laz.yml
env:
  prop: x
targets:
  dev:
  prod:
```

```yaml
# project-root/sub-project-1/laz.yml
env:
  prop: y
```

```yaml
# project-root/sub-project-2/laz.yml
targets:
  qa:
```

The effective configurations after inheritance and overrides are:

```yaml
# project-root/laz.yml
env:
  prop: x
targets:
  dev:
  prod:
```

```yaml
# project-root/sub-project-1/laz.yml
env:
  prop: y
targets:
  dev:
  prod:
```

```yaml
# project-root/sub-project-2/laz.yml
env:
  prop: x
targets:
  dev:
  prod:
  qa:
```

In the above project, if you wanted to run a command against the dev target of sub-project-1, you
would run the following:

```shell
$ laz sub-project-1/dev echo '$prop'
y
```

Or you could run a command against every dev target:

```shell
$ laz dev echo '{{ name }}' '$prop'
project-root x
sub-project-1 y
sub-project-2 x
```

Or you could run a command against only sub-project dev targets:

```shell
$ laz "*/dev" echo '{{ name }}' '$prop'
sub-project-1 y
sub-project-2 x
```

# Jinja Plugin

As stated in the [quick start](../quick_start.md), Laz
uses [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) to provide access to the entire
configuration context during the evaluation of Jinja variables.

Anywhere in your Laz configuration, you can reference other places in your configuration. For example:

```yaml
abc: "{{ x }}"
def: "{{ x }}"
target:
  dev:
actions:
  echo_abc: echo "{{ abc }}"
x: annoyingly long repeated value
```

```shell
$ laz dev echo_abc
annoyingly long repeated value
```

This also works for CLI arguments:

```shell
$ laz dev echo "{{ abc }}"
annoyingly long repeated value
```

## Special Variables

There are other special values added to the configuration dynamically such as the name of the
configuration file (which is the same as the name of the folder) and the name of the
current target. Below is a list of the special values during Jinja template evaluation.

| Variable        | Description                                   |
|-----------------|-----------------------------------------------|
| config.name     | Name (of directory) of configuration file     |
| config.filepath | Absolute filepath of configuration file       |
| config.dirpath  | Absolute directory path of configuration file |
| target.name     | Name of current target                        |

### Examples

```shell
$ laz dev echo "{{ config.name }}"
project-a
```

```shell
$ laz dev echo "{{ target.name }}"
dev
```

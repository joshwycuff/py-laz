# CLI

## Usage

```
laz [-h] [-v] <command> [<arg1>] ... [<argN>]
```

## Global Options

- `-h (--help)`        Display help message
- `-v (--verbose)`     Increase verbosity of log messages

## Commands

### laz

Configuration/Target path to run arguments against

```shell
laz <path> [<arg1>] ... [<argN>]
```

### help

Display help message

```shell
laz help
```

### init

Initialize a directory with an example laz.yml

```shell
laz init
```

### tree

Display tree structure of laz.yml files in current project

```shell
laz tree [--show-targets] [--show-paths]

optional arguments:
  -h, --help          show this help message and exit
  --show-targets, -t  Show targets.
  --show-paths, -p    Show paths.
```

### version

Display current Laz package version

```shell
laz version
```

# Quick Start

## Configuration File

A basic example configuration file may look like the following:

```yaml
env:
  ENV_VAR: value
targets:
  prod:
  dev:
actions:
  example: echo example
```

The above configuration file defines a few different things:

- An environment variable named `ENV_VAR` with the value `value` to be exposed to all commands run
  by Laz.
- Two targets: `prod` and `dev`.
- A single defined action, named `example`. It simply invokes a shell that echos out "example".

Note that nothing is stopping you from storing additional information in other top-level keys.

## Targets

A typical Laz command looks like the following:

```shell
laz <path> [<arg1>] ... [<argN>]
```

A Laz command will not run if the given path does not resolve to defined targets. For example, to
run a command against the dev target defined in the previous example configuration file, you would
run something like:

```shell
$ laz dev echo hello
hello
```

You can run commands against multiple targets using glob patterns:

```shell
$ laz "*" echo hello
hello
hello
```

## Actions

If you have a set of commands that you run often, you can codify them as an action:

```yaml
targets:
  dev:
actions:
  things:
    - echo thing 1
    - echo thing 2
```

```shell
$ laz dev things
thing 1
thing 2
```

## Template Expressions

Laz uses [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) to provide access to the entire
configuration context during the evaluation of template expressions.

For example, if you want to print out the name of the current configuration file:

```yaml
name: abc
target:
  dev:
```

```shell
$ laz dev echo "{{ name }}"
abc
```

There are other special values added to the configuration dynamically such as the name of the
current target.

```shell
$ laz dev echo "{{ target.name }}"
dev
```

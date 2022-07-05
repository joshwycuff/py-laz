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
  default: echo default
  hello: echo hello
```

The above configuration file defines a few different things:

- An environment variable named `ENV_VAR` with the value `value` to be exposed to all commands run
  by Laz.
- Two targets: `prod` and `dev`.
- Two defined actions, `default` and `example`. They simply invoke shells which echo "default" and "
  example", respectively.

Note that nothing is stopping you from storing additional information in other top-level keys. This
is useful for plugins.

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

You can also codify commands as actions and refer to them from the cli. The previous configuration
example contains an action called `hello` that also echos "hello".

```shell
$ laz dev hello
hello
```

If you have a set of commands that you run often, you can codify them as an action as well.

```yaml
targets:
  dev:
actions:
  default: echo i am the default action
  things:
    - echo thing 1
    - echo thing 2
```

```shell
$ laz dev things
thing 1
thing 2
```

If you do not provide an action, Laz will attempt to run a default action.

```shell
$ laz dev
i am the default action
```

## Jinja Variables

Laz uses [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) to provide access to the entire
configuration context during the evaluation of Jinja variables.

For example, if you want to print out an arbitrary configuration field:

```yaml
abc: xyz
target:
  dev:
```

```shell
$ laz dev echo "{{ abc }}"
xyz
```

There are other special values added to the configuration dynamically such as the name of the
current target.

```shell
$ laz dev echo "{{ target.name }}"
dev
```

## Hooks

Hooks can be used to perform actions before or after certain points in the program. The built-in
hooks that are available are:

- `before_all` - Runs before all targets.
- `before_target` - Runs before each target.
- `after_target` - Runs after each target.
- `after_all` - Runs after all targets.

```yaml
target:
  dev:
  prod:
hooks:
  before_all: echo before all
  before_target: echo before target
  after_target: echo after target
  after_all: echo after all
```

```shell
$ laz "*" echo "{{ target.name }}"
before all
before target
dev
after target
before target
prod
after target
after all
```

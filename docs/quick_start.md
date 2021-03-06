# Quick Start

## Configuration File

Laz configuration files are named laz.yml. A basic example configuration file may look like the
following:

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

Note that nothing is stopping you from storing additional information in other unreserved top-level
keys. This is useful for plugins.

## Targets

A typical Laz command looks like the following:

```shell
laz <path> [<arg1>] ... [<argN>]
```

A Laz command will not run if the given path does not resolve to any defined targets. For example,
to run a command against the dev target defined in the previous example configuration file, you
would run something like:

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

The above command ran `echo hello` against both the `dev` and `prod` targets.

## Actions

You can also codify commands as actions and refer to them from the cli. The previous configuration
example contains an action called `hello` that also echos "hello".

```shell
$ laz dev hello
hello
```

Actions can also have sub-actions in the form of a list. If you have a set of commands that you run
often, you can codify them as an action as well.

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
abc: def
ghi:
  jkl: mno
target:
  dev:
```

```shell
$ laz dev echo "{{ abc }}"
def
```

```shell
$ laz dev echo "{{ ghi.jkl }}"
mno
```

This is also a great way to keep your Laz
configuration [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

```yaml
abc: "{{ x }}"
def: "{{ x }}"
target:
  dev:
x: annoyingly long repeated value
```

See the [Jinja Plugin documentation](./plugins/jinja.md) for more details.

In cases where you have entire repeated objects (as opposed to simple string values), you may want
to instead check out the [Alias Plugin documentation](./plugins/alias.md).

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

[Plugins](./plugins/index.md) can also provide additional functionality.

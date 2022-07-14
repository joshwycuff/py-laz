# Configuration

## targets

Configure targets.

```yaml
targets:
  dev:
```

```shell
$ laz dev echo '{{ target.name }}'
dev
```

A target's configuration also overrides the parent configuration if provided.

```yaml
property: x
targets:
  dev:
  prod:
    property: y
```

```shell
$ laz "*" echo '{{ target.name }}' '{{ property }}'
dev x
prod y
```

## env

Configure environment variables.

```yaml
env:
  name: value
targets:
  dev:
```

```shell
$ laz dev echo '$name'
value
```

## laz

Configure Laz behavior.

### Default Base Path

```yaml
laz:
  default_base_path: sub-project-1  # defaults to ""
targets:
  dev:
```

```shell
$ laz dev echo test  # same as `laz sub-project-1/dev echo test`
test
```

### Default Target

```yaml
laz:
  default_target: dev  # defaults to "default"
targets:
  dev:
```

```shell
$ laz / echo '{{ target.name }}'  # same as `laz /dev echo '{{ target.name }}'`
dev
```

### Default Action

```yaml
laz:
  default_action: hi  # defaults to "default"
targets:
  dev:
actions:
  hi: echo hi
```

```shell
$ laz dev
hi
```

### Combining default target and action

```yaml
laz:
  default_target: dev
  default_action: hello
targets:
  dev:
actions:
  hello: echo hello, '{{ target.name }}'
```

```shell
$ laz /
hello, dev
```

### Error when path resolves to no targets

By default, nothing happens if the given path does not resolve to any defined targets. If the
desired behavior is to error, this can be configured.

```yaml
laz:
  error_on_no_targets: true  # defaults to false
targets:
  dev:
```

```shell
$ laz not-a-target echo '{{ target.name }}'
[ERROR] Given path resolved to zero targets
```

## plugins

Specify the import path of Laz plugins to be included at runtime.

```yaml
plugins:
  - laz.plugins.aws
  - laz.plugins.terraform
targets:
  dev:
```

Note that plugin configuration is only allowed in the top-level laz.yml configuration file.

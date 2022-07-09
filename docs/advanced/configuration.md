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

### Default Target

```yaml
laz:
  default_target: dev  # defaults to "default"
targets:
  dev:
```

```shell
$ laz / echo '{{ target.name }}'
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
$ laz dev hi
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

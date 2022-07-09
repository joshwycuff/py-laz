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

### Error when path resolves to no targets

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

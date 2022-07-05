# Actions

## Shell Action

### Example

```yaml
actions:
  example: echo hello
```

## Python Action

### Example

```yaml
actions:
  example:
    python: print('hello')
```

## Multiple Actions

### Example

```yaml
actions:
  example:
    - echo 1
    - echo 2
```

## Conditional Action

### Example

```yaml
actions:
  example:
    condition: "[[ -z $USER ]]"
    if: echo $USER
    else: echo no user
```

## Switch Action

### Example

```yaml
actions:
  example:
    switch:
      python: print('x')
    x: echo x
    y: echo y
```


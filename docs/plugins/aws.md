# AWS Plugin

## Environment Configuration

```yaml
aws:
  profile: <profile name>
  region: <region name>
```

## Assume Role

```yaml
actions:
  example:
    - aws:
        assume_role:
          RoleArn: <role arn>
    - aws sts get-caller-identity
```

## Arbitrary AWS (boto3) Actions

```yaml
actions:
  example:
    aws:
      <service>:
        <subcommand>:
          <key>: <value>
```

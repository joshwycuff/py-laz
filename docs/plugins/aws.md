# AWS Plugin

## Environment Configuration

```yaml
aws:
  profile: <profile name>
  region: <region name>
```

## AWS Secret Environment Variable

```yaml
env:
  aws:
    profile_name: <profile_name> # optional
    region_name: <region_name> # optional
    secret_id: <secret_id>
    version_id: <version_id> # optional
    version_stage: <version_stage> # optional
    json_key: <json_key> # optional
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

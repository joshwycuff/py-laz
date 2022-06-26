# Concepts

## Project

A Laz project consists of at least one directory containing a laz.yml configuration file. A project
can have multiple directories with each of them having 0 or 1 laz.yml files except for the top level
which must have 1. Lower-level directories containing a laz.yml file are called sub-projects.

## Configuration

A laz.yml encapsulates the configuration for a directory. It also inherits and/or overrides the
configurations found in parent directories within the same project.

### Inheritance

Sub-projects "inherit" configuration from parent projects but will also overwrite configuration that
they share.

## Action

Actions are commands, functions, or tasks to be run. They can be as simple as a single CLI command
or as complicated as a series of CLI commands, Python functions, and plugin actions.

CLI commands can be run by Laz without codifying them in a laz.yml. Complicated or common tasks can
be codified in a laz.yml as actions.

## Target

All actions must be performed against a target. For example, common targets might be environments
such as prod and dev.



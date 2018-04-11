# charm-etckeeper Overview

The etckeeper charm, when related to another application in a model,
will deploy etckeeper and allow configuration changes under /etc to
be revision controlled in the DVCS of your choice.

# Charm Usage

Deploy the application to the current model:
juju deploy etckeeper 

Configure the application using juju get/set/config to your liking.
The following options are supported -

| Config            | Type    | Default | Effect                                 |
|:----------------- | ------- |:------- |:-------------------------------------- |
| dvcs              | string  | git     | Sets the DVCS to use.                  |
| daily-commit      | boolean | true    | Enables daily /etc autocommit          |
| preinstall-commit | boolean | true    | Enables autocommit on package install  |
| remote            | string  | <empty> | Enables pushing to the provided remote |

Once configured, relate the application to applications running on machines
where you would like changes to /etc to be captured. Avoid deploying this
charm multiple times to the same unit. Although it should work, it
is unnecessary.


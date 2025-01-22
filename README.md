# Tundra - Permissions

Tundra Permissions is a suport library for the access management library of snowflake access Permifrost.

While the Permifrost library is a great tool for manageing RBAC access grant on snowflake. 
However at certain scales some challenages arrive with the use of Pemifrost.
This library seeks to adress some of these challanges and provide a way to manage Permifrost at scale.

## Features
- Permision file concatination
- Verification of Permifrost spessification files
- Spessification diff/ previue of planned changes
- Generation of the access roles, based on Functional roles

### Permisision Concatination
Permifrost as a tool uses a singel Yaml file to store all the spessifications. 
When a data platform reaches a certain scale this file can become ecessivly long.
At severla thousand lines of spessification it becomes hard to manage and understand a given set of permissions.

Tundra Gives you an option to take this file and split it into a multiple of files that make it
easier to read and understand.
Example you can split into individual files per team or source. 
By running tundra, these seperate files can be automatically concatinated to the larger single file needed by Permifrost.

### Verification of permifrost spessification file
While Permifrost is able to check that the roles, users, warehouses and databases exist in the snowflake account.
There is no seperate function to verify that the spesification file itsel is correctly formated.
The spesification file is a YAML file that with a special formatting. 

Tundra provides a function to run against a Permifirost sesification file and validate formatting 
of the file itself. Thus reducing feedback time compared to running a `permifrost spec-test`

### Spessification diff
As Permifrost sessifications beacomes larger, it becomes harder to maintain an overview of all grants.
This becomes harder if you decide to split the permissions file into multiple files. 
Therefore Tundra can maintain a State file that can be used to show a summary of changes in the permisions strucure.
This feature is heavily inspired by the `terraform plan` function.

By running the printout will show what differences that Tundra detects between the current itteration
of the spessification, and the one that is stored in the state file.

This feature is not able to dettect or account for changes to permisions done outside of the permifrost run,
Of if changes have been made without running tundra state storage.

### Generation of Access role (Alpha)
When creating a RBAC based setup in Permifrost where data bases are the main level off access grant.
The creation of the Accessroles holding the privlages to read and write to the databases, 
becomes a repetetive task with very boiler plate code. It also is highly sparse causing spessification
files to become bloated.

To reduce the cognital burden of creating these roles, and reduce the code bloat. 
Tundra supports the generation of these access roles automatically by analysing the functional roles
and databases in the spessificatio at large. Thus remowing the need to 

#Note!: This feature is currently in Aplha and only suport a set format for naming and privelages.
Futher versions will support alernate naming and privelage patterns 

## Install
Tundra can be installed from PyPi: 
`pip install tundra-permissions`


## Usage
After installing Tundra to your system you have access to the `tundra` cli.
Run the CLI from the location where you can access all the permisions in the subfolders.

Tundra har 2 primary commands `tundra plan` and `tundra apply` along with a set of options to be set.

### `tundra plan`
This Command acts as an analog to the `terraform plan` command.
It will attempt to compare the 



Permisisons as Code system for use with Snowflake.

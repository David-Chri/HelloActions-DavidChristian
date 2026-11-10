# HelloActions-DavidChristian
This is a simple process with only a few actions necessary. For instance, "on" refers to the events that fully start the workflow. The "workflow_dispatch" is so the workflow can be run manually in GitHub. "runs-on" boots a temporary virtual machine, specifically unbuntu in this case, that will attempt to run the system and files. actions/checkout looks at the workspace repository and allows the workflow to look at it. The setup section gets the language setup for the workspace.
Now, compiling the program brings it all together to prepare to be run while running the program uses the program and works the program with what it says.
The output of the program is both in the actions section of GitHub as well as the terminal you are using to run this program.
A workflow is a automated process made by one or more jobs. Jobs are independent execution groups comprised of steps. Steps are individual parts of a job that get executed one after another.

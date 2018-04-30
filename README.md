# CS 170 project

## Docker instructions
To build:
`docker build -t tspsolver`

To run your new image:
`docker run tspsolver`

To run with specific command:
`docker run tspsolver python solver_phase2.py in/50_kevin.in`

Each time you do `docker run`, you'll create new containers.

In the case you want to delete containers, do:
`docker ps -a`
Then do `docker rm <CONTAINER ID/NAME>`

To investigate contents of a docker container...
see [this link]()

Unfortunately, each time we make changes to solver_phase2.py, we need to run docker build again. Investigating how to make this workflow better.

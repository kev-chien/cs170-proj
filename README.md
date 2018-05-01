# CS 170 project

## Docker instructions
To build:
`docker build -t tspsolver`

**Note**: each time docker build is run, a new image ~900 MB is created. Take steps to delete old, unused images through the floowing steps:
`docker image ls` and 
`docker image rm <IMAGE ID>`.

To run your new image:
`docker run tspsolver`

To run with specific command:
`docker run tspsolver python solver_phase2.py in/50_kevin.in`

**Note**: Each time you do `docker run`, you'll create new containers.

In the case you want to delete containers, do:
`docker ps -a`
Then do `docker rm <CONTAINER ID/NAME>`

To investigate contents of a docker container,
see [this link](https://stackoverflow.com/questions/20813486/exploring-docker-containers-file-system)

Each time you make changes to solver/ any file, you can just cp the file into your container. See [this link](https://stackoverflow.com/questions/22907231/copying-files-from-host-to-docker-container).

Likewise, one "should be" able to easily cp out of the docker container.

For resuming a stopped container (and thus being able to copy in files to re-run the container with updated solver): [this link](https://forums.docker.com/t/run-command-in-stopped-container/343).

It seems some solutions are:
- once container has stopped, see if can copy in new solver, then create a new image from container, delete old image, delete old container.
- add the tail thing so container keeps running `tail -f Dockerfile`
- find some way to modify docker images directly (nothing comes up?)

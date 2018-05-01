#!/bin/bash
for i in {0..752}
do
  docker run tspsolver "in/${i}.in" outputs-concorde dijkstras-greedy concorde-TSP > "outputs-concorde/${i}.out"
  docker rm $(docker ps -a -q)
done

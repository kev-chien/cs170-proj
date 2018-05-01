#!/bin/bash
for i in {0..752}
do
  docker run tspsolver python solver_phase2.py inputs/${i}.in . dijkstras-degree concorde-TSP > outputs-concorde/${i}.out
  wait
  docker ps -a -q
done

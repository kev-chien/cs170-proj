from pytsp import atsp_tsp, run, dumps_matrix
# import os

if __name__== "__main__":
  matrix = [
      [ 0,    2910, 4693 ],
      [ 2903, 0,    5839 ],
      [ 4695, 5745, 0    ]]

  matrix_sym = atsp_tsp(matrix, strategy="avg")
  # path = os.path.abspath("cs170-proj")
  outf = "/tmp/myroute.tsp"
  with open(outf, 'w') as dest:
      dest.write(dumps_matrix(matrix_sym, name="My Route"))
  tour = run(outf, start=1, solver="concorde")
  print(tour)



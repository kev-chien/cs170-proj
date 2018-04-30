# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# concorde install and make
RUN cd /app/concorde && ./configure --with-qsopt=/app/QS 
RUN cd /app/concorde && make clean && make
RUN cp /app/concorde/TSP/concorde /usr/local/bin

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install git+https://github.com/perrygeo/pytsp

# Define environment variable
ENV NAME TSP-Solver

# Test python TSP concorde when the container launches
CMD ["python", "tsp_concorde_ex.py"]

# Run solver when the container launches
# CMD ["python", "solver_phase2.py", "in/50_kevin.in"]

Blockchain consensus simulator with some simple attack scenarios.

* run `setup-ns3`
* cd ns-3.41/
* configure: `CXXFLAGS="-std=c++11" ./ns3 configure --build-profile=optimized --enable-mpi`
* then run an example: `./ns3 run "scratch/double-spend --ud=50"`

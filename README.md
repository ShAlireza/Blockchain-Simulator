Blockchain consensus simulator with some simple attack scenarios.

* copy ns3 v3.25 to this directory
* copy rapidjson to this directory
* run `copy-ns3`
* update `waf` script [following these instructions](http://arthurgervais.github.io/Bitcoin-Simulator/Installation.html)
* configure: `CXXFLAGS="-std=c++11" ./waf configure --build-profile=optimized --enable-mpi`
* then run: `./waf --run scratch/double-spend --ud=50`

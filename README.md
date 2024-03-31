Blockchain consensus simulator with some simple attack scenarios.

* copy ns3 v3.41 to this directory
* copy rapidjson to this directory
* run `copy-ns3`
* update `CMakeLists.txt` files [following these instructions](http://arthurgervais.github.io/Bitcoin-Simulator/Installation.html) (Instead of wafscript you just need to add the mentioned files in the respective CMakeLists.txt files)
* configure: `CXXFLAGS="-std=c++11" ./ns3 configure --build-profile=optimized --enable-mpi`
* then run: `./ns3 run scratch/double-spend --ud=50`

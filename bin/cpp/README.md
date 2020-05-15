# README.md
These are state objects that have been serialized by C++ (through the [boost_serialization](https://www.boost.org/doc/libs/1_72_0/libs/serialization/doc/) library) for fast reading and small file size. To parse them, see the main repository at [hacking-the-election/gerrymandering](https://github.com/hacking-the-election/gerrymandering). If you want state objects that are more readable, see the json located at `/json` in this repository.

### Reading in C++
This repository is mostly being used as a host for our data. Since this isn't currently being developed with the intention of releasing as a library (though this may be done in the future), **there is little support for doing anything not explicitly written by us, and the API is currently very messy**. However, the following details how to read these files into C++ if you would like to mess around with the data we've collected.

The following is an example of reading a state, printing out information about it, and using SDL, drawing it to the screen. To reiterate, **this is not API documentation**. If that is ever released, it will live in the [proper repo](https://github.com/hacking-the-election/gerrymandering).

```cpp
#include "gerrymandering/shape.hpp"

using namespace Gerrymandering::Geometry;
using namespace Gerrymandering::Graphics;

int main() {
   // read file at `alabama.dat` into a state object
   State state = State::from_binary("alabama.dat")
   
   // get number of precincts
   std::cout << state.name << " has " << state.precincts.size() 
       " precincts" << std::endl;
       
   // get number of districts
   std::cout << state.districts.size() << " districts" << std::endl;
   std::cout << "state has area of " << state.get_area() << std::endl;
   std::cout << "state has center at "" << normalize_coords(state.get_center()).to_string() << std::endl;
   
   Canvas canvas(900, 900);
   canvas.add_shape(state);
   canvas.draw();
   
   return 0;
}

```

#!/usr/bin/nodejs
// executes x times a function.

function callMeMoby (x, theFunction) {
  for (i = 0; i < x; i++) {
    theFunction();
  }
}

module.export = {callMeMoby: callMeMoby};

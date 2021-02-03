#!/usr/bin/nodejs
// executes x times a function.

function callMeMoby (x, thefunction) {
  for (let i = 0; i < x; i++) {
    thefunction();
  }
}

module.export = {callMeMoby: callMeMoby};

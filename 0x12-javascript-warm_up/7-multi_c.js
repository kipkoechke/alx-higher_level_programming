#!/usr/bin/node

let numberOfTimes = process.argv[2];
if (!isNaN(numberOfTimes)) {
  while (numberOfTimes > 0) {
    console.log('C is fun'); 
    numberOfTimes -= 1;
  }
} else {
  console.log('Missing number of occurrences')
}
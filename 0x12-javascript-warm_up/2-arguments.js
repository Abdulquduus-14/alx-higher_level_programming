#!/usr/bin/node
let counter = process.argv.length - 2

if (counter === 0)
{
	console.log("No argument");
}
else if (counter === 1)
{
	console.log("Argument found");
}
else 
{
	console.log("Arguments found");
}

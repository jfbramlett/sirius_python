# Sirius Sample Code

## Problem
Develop a JSON based REST API that implements that following 3 documented endpoints.

1. Receives an array of integers along with a unique ID and returns a set of arrays which contain all unique permutations of the order of the integers. It keeps a record of the output to handle the additional requests below.
Path: /addEntity
Request: POST
Example:
{
	"entityID ": 1,
	"data": [1, 2, 3]
}
Response: 
{
	“permutations”: [
		[1, 2, 3],
		[1, 3, 2],
		[2, 1, 3],
		[2, 3, 1],
		[3, 1, 2],
		[3, 2, 1]
	]
}

2. Receives a unique ID and returns the sum of all integers that belong to the entity that was added using end point 1.
Path: /sumEntity/entityID
Request: GET
Example: /1
Response: 
{
	“sum”:36
}

3. Receives a unique ID along with an integer value that should be added to all integers that belong to the entity’s set of permutations that was introduced using end point 1, then it return the results.
Path: /updateEntity
Request: POST
Example:
{
	"entityID ": 1,
	"add": -1
}
Response: 
{
	"results": [
		[0, 1, 2],
		[0, 2, 1],
		[1, 0, 2],
		[1, 2, 0],
		[2, 0, 1],
		[2, 1, 0]
	]
}

## To run the app


## To run the test
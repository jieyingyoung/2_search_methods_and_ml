### 2.1 What conditions are required to make the BFS return the optimal solution ?

> **condition1**: if the path cost is a nondecreasing function of the depth of the node (The most common scenario is that 
all actions have the same cost);

> **contition2**: we need to sort the path according to what we want, for each iteration

### 2.2 Is there a way to make DFS find the optimal solution ? (You may need to read some material about iterative DFS)

> Iterative DFS can have the optimal solution. iterative DFS is a method that is to keep increasing the depth at each 
level. For example, we might try exploring using all paths of length one, then all paths of length two, then length 
three, etc. until we end up finding the node in question. This means that we never end up exploring along infinite 
dead-end paths(likd DFS), since the length of each path is capped by some length at each step. 
It also means that we are able to find the shortest possible path to the destination node, since if we didn't find 
the node at depth d but did find it at depth d + 1, there can't be a path of length d (or we would have taken it), 
so the path of length d + 1 is indeed optimal.

> At the same time, iterative DFS is better in memory than BFS because BFS takes memory O(b**d), where b is the branching
factor. Compare this to the iterative DFS only takes O(d) memory usage (to hold the state for each of the d nodes in 
the current path)

### 2.3 In what conditions BFS is a better choice than DFS and vice versa ?

> To use **BFS** - when we want to find the **shortest** path from a certain source node to a certain destination.

> To use **DFS** - when we want to save some space (DFS takes O(b*d) space while BFS takes O(b\**d)) , **or** we want to 
exhaust all possibilities, and check which one is the best/count the number of all possible ways.

### 2.4 When can we use machine learning ?
* to query and retrieve some information from webpage/application, such as search engine like Google
* to filter some information from the large amount of words/pictures,such as advertise filtering in the email
* to automatic translate documents, such as Google translate
* to classify and predict things into groups such as given the information of a user of Youtube, predicting whether 
she/he likes a given new Youtube video.
* to predict some values given some data, such as to predict the price of the house
* in all, as Andrew Ng said:
> A lot of valuable work currently done by humans — examining security video to detect suspicious behaviors, deciding 
if a car is about to hit a pedestrian, finding and eliminating abusive online posts — can be done in less than one 
second. These tasks are ripe for automation.

### 2.5 What is the gradient of a function ?
 The gradient of a differentiable function *f* of several variables, at a point *P*, is the vector whose components 
 are the partial derivatives of *f* at *P*. 
 
 At a point *P*, if the gradient of a function of several variables is not zero vector, then it has the direction 
 of fastest increase of the function at *P*, and its magnitude is the rate of increase in that direction.
 
 ### 2.6 How can we find the maximum value of a function using the information of gradient ?
 
 * First, we need to find the partial derivative of f with respect to each variables, at a randomly choosed point p0;
 * Second, considering we are trying to find the maximum, we need to go up(along with the direction of the gradient)
 * Third, added by learning_rate*gradient(P0), we have a new function
 * continue step one to three, until the p0 converges to the local maximum.



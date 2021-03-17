Genetic Linear Regression\n

**What is Linear Regression?**\n
In statistics, linear regression is a linear approach to modelling the relationship between a scalar response (or dependent variable) and one or more explanatory variables (or independent variables). The case of one explanatory variable is called simple linear regression.

Typically, linear regression learns with gradient descent. The coefficients of a line are learned but for this experiment, the coefficients are being discovered with a genetic algorithm.

**Problem Context**\n
The data used in this assignment were grades of a class: Midterm Grade, Homework Grade, Quiz Grade and Final Grade. Both models used the first 3 features to predict the Final Grade.

**Fitness, Crossover, and Mutation**\n
After fitness is calculated, the candidates are sorted by lowest cost (highest fitness) and the top half are crossbred. The new candidates take 𝜃0 and 𝜃1 from one parent and 𝜃2 and 𝜃3 from the other. On a mutation, the coefficient is assigned to a random value between 0 and 1. The second half of the new population are randomly generated.

**Results**\n
Detailed results are in the csv file below is a summary:\n

*The equation produced by Linear Regression with Gradient Descent:*\n
* Linear Regression Function: 7.667123062546082 + 0.31262773x1 + 0.15289359x2 + 0.43866389x3

*The equation produced by Genetic Linear Regression:*\n
* Genetic Function: 0.9896148838351375 + 0.7477936628734457x1+ 0.05486432049473855x2+ 0.10703247842121622x3
* Average Cost of Genetic for Training Set: 1.664833837
* Average Cost of Genetic for Test Set: 3.734259259

**Conclusion**\n
In conclusion, the genetic algorithm was off by and average of 1.6% on a grade prediction with the training set and 3.73% off a grade prediction with the test set. It performed better in terms of accuracy than what I would have predicted, but it took 35 second to get these results and the leading linear regression with gradient descent library is only about 3 lines of code to get more accurate results and is 15 times faster. I do not think this has any realistic application because linear regression with gradient descent does it better and faster.

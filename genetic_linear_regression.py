import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import random
import itertools

def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)

training_set = pd.read_excel("Project3.xlsx")
X = training_set[['Midterm', 'Homework', 'Quiz']]
Y = training_set['Course Grade']

print("Linear Regression:")

regr = LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

test_set = pd.read_excel("Project3.xlsx", 'Predict')

final_grades = []
for index, row in test_set.iterrows():
    grade = regr.predict([[getattr(row, 'Midterm') ,getattr(row, 'Homework'), getattr(row, 'Quiz')]])
    final_grades.append(grade)

for grade in final_grades:
    var = "{:.2f}".format(grade.sum(0))
    print(var)

def evaluateFitness(population, sample):
    population_error = []
    for candidate in population:
        error = 0.0
        predicted = candidate[0] + (candidate[1] * float(sample[0])) + (candidate[2] * float(sample[1])) + (candidate[3] * float(sample[2]))
        real = sample[3]
        error = abs(predicted - real)

        population_error.append(error)
            
    return population_error

def evaluateFitnessWithSet(population, data_set):
    population_error = [0.0] * len(population)
    for i in range(0, len(population)):
        candidate = population[i]
        for j in range(0, len(data_set)):
            sample = data_set[j]
            predicted = candidate[0] + (candidate[1] * float(sample[0])) + (candidate[2] * float(sample[1])) + (candidate[3] * float(sample[2]))
            real = sample[3]
            population_error[i] += abs(predicted - real)
            
    return population_error

def makeNewCandidate(parent_x, parent_y, mutation_rate):
    # crossover
    new_candidate = [parent_x[0], parent_x[1], parent_y[2], parent_y[3]]
    # mutation
    for i in range(0, len(new_candidate)):
        if(random.random() <= mutation_rate):
            new_candidate[i] = random.random()

    return new_candidate

def geneticLinearRegression(theta_count, init_pop_count, data_set, max_iter, mutation_rate, epsilon):
    # create inital population
    population = []
    for i in range(0, init_pop_count):
        thetas = [random.random(), random.random(), random.random(), random.random()]
        population.append(thetas)

    # main loop
    for i in range(0, max_iter):
        fitness_total = 0.0
        for j in range(0, len(data_set)):
            # evaluate fitness, closer to 0 is better
            var = float(data_set[j][0])
            var += 1.0
            fitness = evaluateFitness(population, data_set[j])
            fitness = sorted(fitness)
            fitness_total += fitness[0]
            population = [ x for _,x in sorted(zip(fitness, population))]

            # generate new population from the best half
            new_population = []
            population_half_count = int(len(population) / 2)
            # cull the weak
            population = population[:population_half_count]
            for x, y in grouped(population, 2):
                new_candidate = makeNewCandidate(x, y, mutation_rate)
                new_population.append(new_candidate)
                new_candidate = makeNewCandidate(y, x, mutation_rate)
                new_population.append(new_candidate)
            population.clear()
            # introduce new population
            for i in range(0, population_half_count):
                thetas = [random.random(), random.random() , random.random() , random.random() ]
                new_population.append(thetas)
            population = new_population

        if fitness_total <= epsilon:
            fitness = evaluateFitnessWithSet(population, data_set)
            population = [ x for _, x in sorted(zip(fitness, population))]
            fitness = sorted(fitness)
            return population[0], fitness[0]

    # return best candidate
    fitness = evaluateFitnessWithSet(population, data_set)
    population = [ x for _, x in sorted(zip(fitness, population))]
    fitness = sorted(fitness)
    print(fitness)
    return population[0], fitness[0]

data_set = []
for i, row in training_set.iterrows():
        data_set.append([getattr(row, 'Midterm'), getattr(row, 'Homework'), getattr(row, 'Quiz'), getattr(row, 'Course Grade')] )

best_candidate, best_fitness = geneticLinearRegression(4, 20, data_set, 1000, 0.05, .01)
print(best_candidate, best_fitness)

final_grades_genetic = []
for index, row in test_set.iterrows():
    midterm_grade = getattr(row, 'Midterm')
    homwork_grade = getattr(row, 'Homework')
    quiz_grade = getattr(row, 'Quiz')
    grade = best_candidate[0] + best_candidate[1] * midterm_grade + best_candidate[2] * homwork_grade + best_candidate[3] * quiz_grade
    final_grades_genetic.append(grade)

for grade in final_grades_genetic:
    var = "{:.2f}".format(grade.sum(0))
    print(var)
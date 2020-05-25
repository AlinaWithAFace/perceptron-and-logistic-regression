We will cover the related topics to this homework this week (week of May 11th). However, you might be still able to work on this fairly simple homework by looking at the uploaded slides for Lecture 22  and the pdf for Note 8. This homework asks you to implement basic versions of perception and logistic regression. 

Her is the description: Link (Links to an external site.)

Don't forget about submitting a readme file to clarify the steps needed for running your programs.

# Intro to Dear AI - Spring 2020
Homework 6  
Perceptron and Logistic Regression

## DESCRIPTION
You are asked to write a program with two functions that applies perceptron or logistic regression techniques to the input and prints their outcome.

### Perceptron
The first function receives $n (<100)$ triplets of $x_1$, $x_2$, $y$ from the user, and returns the value for $w$ (weight) that the perceptron algorithm computes to classify the inputs. Here $x_1$ and $x_2$ show the input features for each sample, and $y$ shows the class. Consider a binary classification with two possible values for $y$: $-1$ and $+1$. Use the same format for input and output as the example below. Note that before the actual input, another input character P will determine the call for the perceptron function.

#### Example Input:

```python
P (0, 2,+1) (2, 0, -1) (0, 4,+1) (4, 0, -1)		#P indicates perceptron
```

#### Example output:

```python
-1, +1 	# referring to w=[-1, +1]
```

Use the same procedure for updating w, as discussed in slides $(w=w+y*.f)$. Start from $w=[0,0]$, and update $w$ by a maximum of $n * 100$ iterations, where $ n $ is the number of inputs samples as indicated above.

### Logistic regression
The second function receives a similar input as what described above with the only difference in the first input character ($L$ instead of $P$). The desired task will still be binary classification. The output, in this case, will be printing the probability values that logistic regression computes for each input belonging to the positive class. Set alpha (learning rate) equal to $0.1$.

#### Example Input:

```python
L (0, 2,+1) (2, 0, -1) (0, 4, -1) (4, 0, +1) (0, 6, -1) (6, 0, +1)	#L indicates Logistic Reg.
```

#### Example output:

```python
0.5 0.6 0.23 0.12 0.78 0.21 	# probability values are for format demonstration only
```

For the logistic regression use the basic procedure introduced in class $(w=w+α*g(w))$. Start from $w=0$, and update $w$ by a maximum of $n * 100$ iterations, where $n$ is the number of inputs samples.

## CHECKING RESULTS

You are allowed and encouraged to post your results (input-output pairs) on Piazza to double-check them with other students.

## QUESTIONS?

Post them on [Pizza](https://piazza.com/class/k6dtwl9cuzo2wi).

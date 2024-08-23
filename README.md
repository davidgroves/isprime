# IsPrime.

This is a very silly repo put together after I was told `^.?$|^(..+?)\1+$` was a python regex that determines if positive integers are prime.
In order to do it, you need to feed it a string of 1's equal in length to the value of the number to check.

So for example, to check if 7 is prime, you would check `1111111`. If the regex has matches, it is NOT prime. If it has no matches, it IS prime.

This was built in around 20mins to check if this was true.

## Setup

No dependencies outside the standard library, so you should be able to run it without any setup or virtual environment.

## Usage

Run `python isprime.py --help`.

## Examples

```console
$ python isprime.py --min 1 --max 100

Both methods have determined all primes are the same.
The number of primes found was: 25
The primes are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

## More Information

If you google for "regex to determine if a number is prime", you will find a lot of resources. None of them
particularly jumped out to me, so I'll leave it to you to explore.

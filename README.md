

## Criteria for a function to get tot badge

C1. Its survival time should be above a threshold (365 days at the time of creating this repo)
C2. Dev Eq of its firt commit should be above a threshold (25 at the time of creating this repo)
C3. The sum of Dev Eq of subsequent commits should be less than 10% of that of the first commit.
C4. The sum of in-degree and out-degree of that function is greater than 0.

## Test cases

1. test1 satisfies C2, C3 and C4 but fails C1. (test1 is above initial Dev Eq threshold, has no modification after first commit, and has in-degree of 1 but it lives shorter than 365 days)
2. test2 satisfies C1, C3 and C4 but fails C2. (test 2 lives longer than 365 days, has no modification after first commit, and has an in-degree of 1 but its initial Dev Eq is smaller than 25)
3. test3 satisfies C1, C2, and C4 but fails C3. (test 3 is above initial Dev Eq threshold, lives longer than a year, and has an in-degree o 1 but is heavily modified afterwards)
4. test 4 satisfies C1, C2, and C3 but fails C4. (test 4 is above initial Dev Eq threshold, lives longer than a year, and is never modified after its first commit, but has no in-degree and out-degree)

## Commits

No.1 - Add test2, test3, and test4 funtions
No.2 - Add test1 function
No.3 - Modify test 3 function

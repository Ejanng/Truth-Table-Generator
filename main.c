#include <stdio.h>
#include <string.h>

// int priorityRow = 0;
int max = 20;
int iNot = 0, iAnd = 0, iOr = 0, iImplies = 0, iEquivalent = 0;
// Function to calculate the row and column sizes
void calculateDimensions(int n, int *row, int *col) {

    if (n == 0) {
        *col = 0;
        *row = 0;
        return;
    }  else {
        int temp = 2, power = 0, two = 2;

        for (int i = 0; i < n - 1; i++) {
            power = two * temp;
            temp = power;
        }
        *col = n;
        *row = temp;
    }
}

// Function to initialize the matrix
void initializeMatrix(int row, int col, int matrix[row][col]) {
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col ; j++) {
            matrix[i][j] = 0;
        }
    }
}

// Function to fill the matrix with binary counting values
void fillMatrixWithBinaryCount(int row, int col, int matrix[row][col]) {
    // Initialize first row with 0
    initializeMatrix(row, col, matrix);

    for (int i = 1; i < row; i++) {
        // Copy the previous row
        for (int j = 0; j < col; j++) {
            matrix[i][j] = matrix[i - 1][j];
        }

        // Increment binary by flipping bits
        for (int j = col - 1; j >= 0; j--) {
            if (matrix[i][j] == 0) {
                matrix[i][j] = 1;
                break;
            } else {
                matrix[i][j] = 0;
            }
        }
    }
}

// Function to assign values to the array
void assignValue(int row, int col, int n, int x[], int matrix[row][col], int y) {
    for (int i = 0; i < row; i++) {
        x[i] = matrix[i][y];
    }
}

// Function to assign values to the matrix
void assignValueArr(int row, int col, int n, int p[], int q[], int r[], int s[], int matrix[row][col]) {

    int y = 0;
    
    if (n == 1) {
        assignValue(row, col, n, p, matrix, y);
    } else if (n == 2) {
        assignValue(row, col, n, p, matrix, y);
        y++;
        assignValue(row, col, n, q, matrix, y);
    } else if (n == 3) {
        assignValue(row, col, n, p, matrix, y);
        y++;
        assignValue(row, col, n, q, matrix, y);
        y++;
        assignValue(row, col, n, r, matrix, y);
    } else if (n == 4) {
        assignValue(row, col, n, p, matrix, y);
        y++;
        assignValue(row, col, n, q, matrix, y);
        y++;
        assignValue(row, col, n, r, matrix, y);
        y++;
        assignValue(row, col, n, s, matrix, y);
    }

    // after incrementing y, y will be 0
    // making sure that y is 0 if the function is called again
    y = 0;
}

// Function to check if the character is a variable
void translate (int *n, int *finalIndex, int length, char strStrange[length], char finalStr[*finalIndex]) {

    int countP = 0, countQ = 0, countR = 0, countS = 0;
    for (int i = 0; i < length; i++) {
        if (strStrange[i] == 'p') {
            printf("p detected\n");
            if (countP == 0) {
                countP++;
                *n = *n + 1;
            }
            finalStr[*finalIndex] = 'p';
            *finalIndex = *finalIndex + 1;
        } else if (strStrange[i] == 'q') {
            printf("q detected\n");
            if (countQ == 0) {
                countQ++;
                *n = *n + 1;
            }
            finalStr[*finalIndex] = 'q';
            *finalIndex = *finalIndex + 1;
        } else if (strStrange[i] == 'r') {
            printf("r detected\n");
            if (countR == 0) {
                countR++;
                *n = *n + 1;
            }
            finalStr[*finalIndex] = 'r';
            *finalIndex = *finalIndex + 1;
        } else if (strStrange[i] == 's') {
            printf("s detected\n");
            if (countS == 0) {
                countS++;
                *n = *n + 1;
            }
            finalStr[*finalIndex] = 's';
            *finalIndex = *finalIndex + 1;
        } else if (strStrange[i] == '(') {
            printf("Open Parentheses detected\n");
            finalStr[*finalIndex] = '(';
            *finalIndex = *finalIndex + 1;
        } else if (strStrange[i] == ')') {
            printf("Close Parentheses detected\n");
            finalStr[*finalIndex] = ')';
            *finalIndex = *finalIndex + 1;
        } else if (strStrange[i] == 'a' && strStrange[i - 1] != 'v') {
            printf("and detected\n");
            i += 2;
            finalStr[*finalIndex] = '^';
            *finalIndex = *finalIndex + 1;
            printf("%c\n", strStrange[i]);
        } else if (strStrange[i] == 'o' && strStrange[i - 1] != 'n') {
            printf("or detected\n");
            i += 1;
            finalStr[*finalIndex] = 'v';
            *finalIndex = *finalIndex + 1;
            printf("%c\n", strStrange[i]);
        } else if (strStrange[i] == 'n' && strStrange[i - 1] != 'a' || strStrange[i] == 'n' && strStrange[i - 1] != 'e') {
            printf("not detected\n");
            i += 2;
            finalStr[*finalIndex] = '~';
            *finalIndex = *finalIndex + 1;
            printf("%c\n", strStrange[i]);
        } else if (strStrange[i] == 'i' && strStrange[i - 1] != 'u') {
            printf("implies detected\n");
            i += 6;
            finalStr[*finalIndex] = '=';
            *finalIndex = *finalIndex + 1;
            finalStr[*finalIndex] = '>';
            *finalIndex = *finalIndex + 1;
            printf("%c\n", strStrange[i]);
        } else if (strStrange[i] == 'e' && strStrange[i - 1] != 'i') {
            printf("equivalent detected\n");
            i += 9;
            finalStr[*finalIndex] = '<';
            *finalIndex = *finalIndex + 1;
            finalStr[*finalIndex] = '=';
            *finalIndex = *finalIndex + 1;
            finalStr[*finalIndex] = '>';
            *finalIndex = *finalIndex + 1;
            printf("%c\n", strStrange[i]);
        }
    } 
}

void opAnd(int i, int a[i], int b[i], int fianlStrLength) {
    for (i = 0; i < fianlStrLength; i++) {
        if (a[i] == 1 && b[i] == 1) {
            printf("1\n");
        } else {
            printf("0\n");
        }  
    }
}

void opOr(int i, int a[i], int b[i], int fianlStrLength) {
    for (i = 0; i < fianlStrLength; i++) {
        if (a[i] == 1 || b[i] == 1) {
            printf("1\n");
        } else {
            printf("0\n");
        }
    }
}

void opImplies(int i, int a[i], int b[i], int finalStrLength) {
    for (i = 0; i < finalStrLength; i++) {
        if ((b[i]&& a[i] == 0) || (b[i] && a[i])) {
            printf("1\n");
        } else {
            printf("0\n");
        }
    }
}

void opEquivalent(int i, int a[i], int b[i], int finalStrLength) {
    for (i = 0; i < finalStrLength; i++) {
        if (a[i] == b[i]) {
            printf("1\n");
        } else {
            printf("0\n");
        }
    }
}

void calculateValue (int col, char finalStr[], int finalStrLength, int p[], int q[], int r[], int s[], int varOne[], int varTwo[]) {
    char variable[] = "pqrs"; // maximze the code later on just use if else in each section
    char operator[] = "~^v=><=>";
    int lenOp = strlen(operator);
    for (int i = 0; i < max; i++) {
        if (finalStr[i] == '~' && finalStr[i + 1] == '(') {
            for (int j = 0; j < lenOp; j++) {
                if (finalStr[i + 3] == operator[j]) {   // Checking the operator used
                    if (finalStr[i + 2] == 'p') {
                        // implement the logic later here 
                        // call a function that assign all value and calculate the logic
                        // also pass the value of operator
                        if (finalStr[i + 4] != '~') {
                            if (finalStr[i + 4] == 'p') {
                                varOne[i] = p[i];
                                varTwo[i] = p[i];
                            } else if (finalStr[i + 4] == 'q') {
                                varOne[i] = p[i];
                                varTwo[i] = q[i];
                            } else if (finalStr[i + 4] == 'r') {
                                varOne[i] = p[i];
                                varTwo[i] = r[i];
                            } else if (finalStr[i + 4] == 's') {
                                varOne[i] = p[i];
                                varTwo[i] = s[i];
                            }
                        } else if (finalStr[i + 4] == '~') {
                            if (finalStr[i + 5] == 'p') {
                                varOne[i] = !p[i];
                                varTwo[i] = !p[i];
                            } else if (finalStr[i + 5] == 'q') {
                                varOne[i] = !p[i];
                                varTwo[i] = !q[i];
                            } else if (finalStr[i + 5] == 'r') {
                                varOne[i] = !p[i];
                                varTwo[i] = !r[i];
                            } else if (finalStr[i + 5] == 's') {
                                varOne[i] = !p[i];
                                varTwo[i] = !s[i];
                            }
                        }
                    } else if (finalStr[i + 2] == 'q') {
                        if (finalStr[i] == 'p') {
                        // implement the logic later here 
                        // call a function that assign all value and calculate the logic
                        // also pass the value of operator
                            if (finalStr[i + 4] != '~') {
                                if (finalStr[i + 4] == 'p') {
                                    varOne[i] = p[i];
                                    varTwo[i] = p[i];
                                } else if (finalStr[i + 4] == 'q') {
                                    varOne[i] = p[i];
                                    varTwo[i] = q[i];
                                } else if (finalStr[i + 4] == 'r') {
                                    varOne[i] = p[i];
                                    varTwo[i] = r[i];
                                } else if (finalStr[i + 4] == 's') {
                                    varOne[i] = p[i];
                                    varTwo[i] = s[i];
                                }
                            } else if (finalStr[i + 4] == '~') {
                                if (finalStr[i + 5] == 'p') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !p[i];
                                } else if (finalStr[i + 5] == 'q') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !q[i];
                                } else if (finalStr[i + 5] == 'r') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !r[i];
                                } else if (finalStr[i + 5] == 's') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !s[i];
                                }
                            }
                        }
                    } else if (finalStr[i] == 'r') {
                        if (finalStr[i] == 'p') {
                            // implement the logic later here 
                            // call a function that assign all value and calculate the logic
                            // also pass the value of operator
                            if (finalStr[i + 4] != '~') {
                                if (finalStr[i + 4] == 'p') {
                                    varOne[i] = p[i];
                                    varTwo[i] = p[i];
                                } else if (finalStr[i + 4] == 'q') {
                                    varOne[i] = p[i];
                                    varTwo[i] = q[i];
                                } else if (finalStr[i + 4] == 'r') {
                                    varOne[i] = p[i];
                                    varTwo[i] = r[i];
                                } else if (finalStr[i + 4] == 's') {
                                    varOne[i] = p[i];
                                    varTwo[i] = s[i];
                                }
                            } else if (finalStr[i + 4] == '~') {
                                if (finalStr[i + 5] == 'p') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !p[i];
                                } else if (finalStr[i + 5] == 'q') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !q[i];
                                } else if (finalStr[i + 5] == 'r') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !r[i];
                                } else if (finalStr[i + 5] == 's') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !s[i];
                                }
                            }
                        }
                    } else if (finalStr[i] == 's') {
                        if (finalStr[i] == 'p') {
                        // implement the logic later here 
                        // call a function that assign all value and calculate the logic
                        // also pass the value of operator
                            if (finalStr[i + 2] != '~') {
                                if (finalStr[i + 2] == 'p') {
                                    varOne[i] = p[i];
                                    varTwo[i] = p[i];
                                } else if (finalStr[i + 2] == 'q') {
                                    varOne[i] = p[i];
                                    varTwo[i] = q[i];
                                } else if (finalStr[i + 2] == 'r') {
                                    varOne[i] = p[i];
                                    varTwo[i] = r[i];
                                } else if (finalStr[i + 2] == 's') {
                                    varOne[i] = p[i];
                                    varTwo[i] = s[i];
                                }
                            } else if (finalStr[i + 2] == '~') {
                                if (finalStr[i + 3] == 'p') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !p[i];
                                } else if (finalStr[i + 3] == 'q') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !q[i];
                                } else if (finalStr[i + 3] == 'r') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !r[i];
                                } else if (finalStr[i + 3] == 's') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !s[i];
                                }
                            }
                        }
                    }
                }
            }
        } else if (finalStr[i] != '~' && finalStr[i] != '(') {
            for (int j = 0; j < lenOp; j++) {
                if (finalStr[i + 1] == operator[j]) {   // Checking the operator used
                    if (finalStr[i] == 'p') {
                        // implement the logic later here 
                        // call a function that assign all value and calculate the logic
                        // also pass the value of operator
                        if (finalStr[i + 2] != '~') {
                            if (finalStr[i + 2] == 'p') {
                                varOne[i] = p[i];
                                varTwo[i] = p[i];
                            } else if (finalStr[i + 2] == 'q') {
                                varOne[i] = p[i];
                                varTwo[i] = q[i];
                            } else if (finalStr[i + 2] == 'r') {
                                varOne[i] = p[i];
                                varTwo[i] = r[i];
                            } else if (finalStr[i + 2] == 's') {
                                varOne[i] = p[i];
                                varTwo[i] = s[i];
                            }
                        } else if (finalStr[i + 2] == '~') {
                            if (finalStr[i + 3] == 'p') {
                                varOne[i] = !p[i];
                                varTwo[i] = !p[i];
                            } else if (finalStr[i + 3] == 'q') {
                                varOne[i] = !p[i];
                                varTwo[i] = !q[i];
                            } else if (finalStr[i + 3] == 'r') {
                                varOne[i] = !p[i];
                                varTwo[i] = !r[i];
                            } else if (finalStr[i + 3] == 's') {
                                varOne[i] = !p[i];
                                varTwo[i] = !s[i];
                            }
                        }
                    } else if (finalStr[i] == 'q') {
                        if (finalStr[i] == 'p') {
                        // implement the logic later here 
                        // call a function that assign all value and calculate the logic
                        // also pass the value of operator
                            if (finalStr[i + 2] != '~') {
                                if (finalStr[i + 2] == 'p') {
                                    varOne[i] = p[i];
                                    varTwo[i] = p[i];
                                } else if (finalStr[i + 2] == 'q') {
                                    varOne[i] = p[i];
                                    varTwo[i] = q[i];
                                } else if (finalStr[i + 2] == 'r') {
                                    varOne[i] = p[i];
                                    varTwo[i] = r[i];
                                } else if (finalStr[i + 2] == 's') {
                                    varOne[i] = p[i];
                                    varTwo[i] = s[i];
                                }
                            } else if (finalStr[i + 2] == '~') {
                                if (finalStr[i + 3] == 'p') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !p[i];
                                } else if (finalStr[i + 3] == 'q') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !q[i];
                                } else if (finalStr[i + 3] == 'r') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !r[i];
                                } else if (finalStr[i + 3] == 's') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !s[i];
                                }
                            }
                        }
                    } else if (finalStr[i] == 'r') {
                        if (finalStr[i] == 'p') {
                            // implement the logic later here 
                            // call a function that assign all value and calculate the logic
                            // also pass the value of operator
                            if (finalStr[i + 2] != '~') {
                                if (finalStr[i + 2] == 'p') {
                                    varOne[i] = p[i];
                                    varTwo[i] = p[i];
                                } else if (finalStr[i + 2] == 'q') {
                                    varOne[i] = p[i];
                                    varTwo[i] = q[i];
                                } else if (finalStr[i + 2] == 'r') {
                                    varOne[i] = p[i];
                                    varTwo[i] = r[i];
                                } else if (finalStr[i + 2] == 's') {
                                    varOne[i] = p[i];
                                    varTwo[i] = s[i];
                                }
                            } else if (finalStr[i + 2] == '~') {
                                if (finalStr[i + 3] == 'p') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !p[i];
                                } else if (finalStr[i + 3] == 'q') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !q[i];
                                } else if (finalStr[i + 3] == 'r') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !r[i];
                                } else if (finalStr[i + 3] == 's') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !s[i];
                                }
                            }
                        }
                    } else if (finalStr[i] == 's') {
                        if (finalStr[i] == 'p') {
                        // implement the logic later here 
                        // call a function that assign all value and calculate the logic
                        // also pass the value of operator
                            if (finalStr[i + 2] != '~') {
                                if (finalStr[i + 2] == 'p') {
                                    varOne[i] = p[i];
                                    varTwo[i] = p[i];
                                } else if (finalStr[i + 2] == 'q') {
                                    varOne[i] = p[i];
                                    varTwo[i] = q[i];
                                } else if (finalStr[i + 2] == 'r') {
                                    varOne[i] = p[i];
                                    varTwo[i] = r[i];
                                } else if (finalStr[i + 2] == 's') {
                                    varOne[i] = p[i];
                                    varTwo[i] = s[i];
                                }
                            } else if (finalStr[i + 2] == '~') {
                                if (finalStr[i + 3] == 'p') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !p[i];
                                } else if (finalStr[i + 3] == 'q') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !q[i];
                                } else if (finalStr[i + 3] == 'r') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !r[i];
                                } else if (finalStr[i + 3] == 's') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !s[i];
                                }
                            }
                        }
                    }
                }
            }
        } else if (finalStr[i] != '~' && finalStr[i] == '(') {
            for (int j = 0; j < lenOp; j++) {
                if (finalStr[i + 2] == operator[j]) {   // Checking the operator used
                    if (finalStr[i] == 'p') {
                        // implement the logic later here 
                        // call a function that assign all value and calculate the logic
                        // also pass the value of operator
                        if (finalStr[i + 3] != '~') {
                            if (finalStr[i + 2] == 'p') {
                                varOne[i] = p[i];
                                varTwo[i] = p[i];
                            } else if (finalStr[i + 2] == 'q') {
                                varOne[i] = p[i];
                                varTwo[i] = q[i];
                            } else if (finalStr[i + 2] == 'r') {
                                varOne[i] = p[i];
                                varTwo[i] = r[i];
                            } else if (finalStr[i + 2] == 's') {
                                varOne[i] = p[i];
                                varTwo[i] = s[i];
                            }
                        } else if (finalStr[i + 3] == '~') {
                            if (finalStr[i + 3] == 'p') {
                                varOne[i] = !p[i];
                                varTwo[i] = !p[i];
                            } else if (finalStr[i + 3] == 'q') {
                                varOne[i] = !p[i];
                                varTwo[i] = !q[i];
                            } else if (finalStr[i + 3] == 'r') {
                                varOne[i] = !p[i];
                                varTwo[i] = !r[i];
                            } else if (finalStr[i + 3] == 's') {
                                varOne[i] = !p[i];
                                varTwo[i] = !s[i];
                            }
                        }
                    } else if (finalStr[i] == 'q') {
                        if (finalStr[i] == 'p') {
                        // implement the logic later here 
                        // call a function that assign all value and calculate the logic
                        // also pass the value of operator
                            if (finalStr[i + 2] != '~') {
                                if (finalStr[i + 2] == 'p') {
                                    varOne[i] = p[i];
                                    varTwo[i] = p[i];
                                } else if (finalStr[i + 2] == 'q') {
                                    varOne[i] = p[i];
                                    varTwo[i] = q[i];
                                } else if (finalStr[i + 2] == 'r') {
                                    varOne[i] = p[i];
                                    varTwo[i] = r[i];
                                } else if (finalStr[i + 2] == 's') {
                                    varOne[i] = p[i];
                                    varTwo[i] = s[i];
                                }
                            } else if (finalStr[i + 2] == '~') {
                                if (finalStr[i + 3] == 'p') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !p[i];
                                } else if (finalStr[i + 3] == 'q') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !q[i];
                                } else if (finalStr[i + 3] == 'r') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !r[i];
                                } else if (finalStr[i + 3] == 's') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !s[i];
                                }
                            }
                        }
                    } else if (finalStr[i] == 'r') {
                        if (finalStr[i] == 'p') {
                            // implement the logic later here 
                            // call a function that assign all value and calculate the logic
                            // also pass the value of operator
                            if (finalStr[i + 2] != '~') {
                                if (finalStr[i + 2] == 'p') {
                                    varOne[i] = p[i];
                                    varTwo[i] = p[i];
                                } else if (finalStr[i + 2] == 'q') {
                                    varOne[i] = p[i];
                                    varTwo[i] = q[i];
                                } else if (finalStr[i + 2] == 'r') {
                                    varOne[i] = p[i];
                                    varTwo[i] = r[i];
                                } else if (finalStr[i + 2] == 's') {
                                    varOne[i] = p[i];
                                    varTwo[i] = s[i];
                                }
                            } else if (finalStr[i + 2] == '~') {
                                if (finalStr[i + 3] == 'p') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !p[i];
                                } else if (finalStr[i + 3] == 'q') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !q[i];
                                } else if (finalStr[i + 3] == 'r') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !r[i];
                                } else if (finalStr[i + 3] == 's') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !s[i];
                                }
                            }
                        }
                    } else if (finalStr[i] == 's') {
                        if (finalStr[i] == 'p') {
                        // implement the logic later here 
                        // call a function that assign all value and calculate the logic
                        // also pass the value of operator
                            if (finalStr[i + 2] != '~') {
                                if (finalStr[i + 2] == 'p') {
                                    varOne[i] = p[i];
                                    varTwo[i] = p[i];
                                } else if (finalStr[i + 2] == 'q') {
                                    varOne[i] = p[i];
                                    varTwo[i] = q[i];
                                } else if (finalStr[i + 2] == 'r') {
                                    varOne[i] = p[i];
                                    varTwo[i] = r[i];
                                } else if (finalStr[i + 2] == 's') {
                                    varOne[i] = p[i];
                                    varTwo[i] = s[i];
                                }
                            } else if (finalStr[i + 2] == '~') {
                                if (finalStr[i + 3] == 'p') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !p[i];
                                } else if (finalStr[i + 3] == 'q') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !q[i];
                                } else if (finalStr[i + 3] == 'r') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !r[i];
                                } else if (finalStr[i + 3] == 's') {
                                    varOne[i] = !p[i];
                                    varTwo[i] = !s[i];
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

// void detectVar(int p[], int q[], int r[], int s[], int a[], int b[], int finalStrLength, char finalStr[]) {
//     for (int i = 0; i < finalStrLength; i++){
//         if (finalStr[i] == 'p') {
//             a[i] = p[i];
//         } else if (finalStr[i] == 'q') {
//             a[i] = q[i];
//         } else if (finalStr[i] == 'r') {
//             a[i] = r[i];
//         } else if (finalStr[i] == 's') {
//             a[i] = s[i];
//         } else if (finalStr[i] == '~') {
//             if (finalStr[i + 1] == 'p') {
//                 a[i] = !p[i];
//             } else if (finalStr[i + 1] == 'q') {
//                 a[i] = !q[i];
//             } else if (finalStr[i + 1] == 'r') {
//                 a[i] = !r[i];
//             } else if (finalStr[i + 1] == 's') {
//                 a[i] = !s[i];
//             }
//         } 
//         if (finalStr[i + 2] == 'p') {
//             b[i] = p[i];
//         } else if (finalStr[i + 2] == 'q') {
//             b[i] = q[i];
//         } else if (finalStr[i + 2] == 'r') {
//             b[i] = r[i];
//         } else if (finalStr[i + 2] == 's') {
//             b[i] = s[i];
//         } else if (finalStr[i + 2] == '~') {
//             if (finalStr[i + 3] == 'p') {
//                 b[i] = !p[i];
//             } else if (finalStr[i + 3] == 'q') {
//                 b[i] = !q[i];
//             } else if (finalStr[i + 3] == 'r') {
//                 b[i] = !r[i];
//             } else if (finalStr[i + 3] == 's') {
//                 b[i] = !s[i];
//             }
//         } 
//     }
// }

// void detectOp(int row, int p[], int q[], int r[], int s[], int varAnd[][], int varOr[][], int varImp[][], int varEqu[][], int finalStrLength, char finalStr[]) {
//     int a[max], b[max];
//     for (int i = 0; i < finalStrLength; i++) {
//         if (finalStr[i] == '^') {
//             detectVar(p, q, r, s, a, b, finalStrLength, finalStr);
//             opAnd(i, a, b, finalStrLength);
//         } else if (finalStr[i] == 'v') {
//             detectVar(p, q, r, s, a, b, finalStrLength, finalStr);
//             opOr(i, a, b, finalStrLength);
//         } else if (finalStr[i - 1] != '<' && finalStr[i] == '=' && finalStr[i + 1] == '>') {
//             detectVar(p, q, r, s, a, b, finalStrLength, finalStr);
//             opImplies(i, a, b, finalStrLength);
//         } else if (finalStr[i] == '<' && finalStr[i + 1] == '=' && finalStr[i + 2] == '>') {
//             detectVar(p, q, r, s, a, b, finalStrLength, finalStr);
//             opEquivalent(i, a, b, finalStrLength);
//         }
//     }
// }

// Function to print the matrix
void printMatrix(int row, int n, int p[], int q[], int r[], int s[]){

    if (n == 0) {
        printf("No matrix to print\n");
        return;
    } else if (n == 1) {
        printf("Printing matrix...\n");
        printf("P\n");
        printf("----\n");
        for (int i = 0; i < row; i++) {
            printf("%d\n", p[i]);
        }
    } else if (n == 2) {
        printf("Printing matrix...\n");
        printf("P Q\n");
        printf("--------\n");
        for (int i = 0; i < row; i++) {
            printf("%d %d\n", p[i], q[i]);
        }
    } else if (n == 3) {
        printf("Printing matrix...\n");
        printf("P Q R\n");
        printf("--------\n");
        for (int i = 0; i < row; i++) {
            printf("%d %d %d\n", p[i], q[i], r[i]);
        }
    } else if (n == 4) {
        printf("Printing matrix...\n");
        printf("P Q R S\n");
        printf("--------\n");
        for (int i = 0; i < row; i++) {
            printf("%d %d %d %d\n", p[i], q[i], r[i], s[i]);
        }
    }
}

// // Function to print the matrix
// // Debugging
// void printMatrix(int row, int col, int matrix[row][col]) {
//     for (int i = 0; i < row; i++) {
//         for (int j = 0; j < col ; j++) {
//             printf("%d ", matrix[i][j]);
//         }
//         printf("\n");
//     }
// }

int main () {
    int row, col;
    int n = 0;
    int finalIndex = 0;
    char strStrange[] = "(p and q) implies  p";
    char finalStr[max];
    int calculatedValue[max][max];
    char calculatedStr[max];
    // int varAnd[max][max], varOr[max][max], varImp[max][max], varEqu[max][max];
    // int varP[max], varQ[max], varR[max], varS[max];
    // int a[max], b[max];

    // This variable doesn't do anything but if i remove it, it will occur a bug
    char priority[max][max];
    // Get the length of the string
    int length = strlen(strStrange);
    int finalStrLength = 0;

    

    if (n < 0 || n > 4) {
        printf("Invalid input\n");
        return 0;
    } else {
        translate(&n, &finalIndex, length, strStrange, finalStr);
        finalIndex = 0;
        finalStrLength = strlen(finalStr);
        calculateDimensions(n, &row, &col);

        // Debugging
        printf("row = %d, col = %d\n", row, col);

        int p[row], q[row], r[row], s[row];
        int matrix[row][col];

        // Initialize the matrix
        initializeMatrix(row, col, matrix);
        fillMatrixWithBinaryCount(row, col, matrix);
        assignValueArr(row, col, n, p, q, r, s, matrix);



        // Detect the variables
        // detectOp(row, p, q, r, s, varAnd, varOr, varImp, varEqu, finalStrLength, finalStr);
        // detectVar(p, q, r, s, a, b, finalStrLength, finalStr);

        int a[max], b[max];
        // Print the matrix
        printMatrix(row, n, p, q, r, s);
        // Debugging
        // printf("finalIndex = %d\n", finalIndex);

        for (int i = 0; i < finalStrLength; i++) {
            printf("%c", finalStr[i]);
        }

        printf("\n");
        // printf("%s\n", finalStr);

        int debug = strlen(finalStr);

        // Debugging
        printf("finalStrLength = %d\n", debug);
        // printf("%d\n", n);
        return 0;
    }
}

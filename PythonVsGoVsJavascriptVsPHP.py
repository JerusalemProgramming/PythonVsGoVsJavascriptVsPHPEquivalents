## PYTHON VS. GO (GOLANG) VS. JAVASCRIPT EQUIVALENTS
## WORK-IN-PROGRESS
## CHECK BACK SOON FOR UPDATES; PLEASE COME BACK AGAIN SOON
## PLEASE VISIT OUR WEB SITES (OUR PROBLEM-SOLVING PROGRAMMING, CODING, & DEVELOPMENT SERVICES ARE AVAILABLE FOR HIRE):
## www.JerusalemProgrammer.com
## www.JerusalemProgrammers.com
## www.JerusalemProgramming.com


## DECLARE VARIABLES
## DECLARE VARIABLES
## DECLARE VARIABLES

## PYTHON
AnyVariableName = "Whatever String, Number, or other Object"

## JAVASCRIPT
var AnyVariableName = "Whatever String, Number, or other Object";
let AnyVariableName = "Whatever String, Number, or other Object";
const AnyVariableName = "ES6 - Whatever String, Number, or other Object in ES6";

## GO (GOLANG) - INTEGERS - VERSION 1 - THE LONG WAY
var AnyVariableName int
AnyVariableName = 700

## GO (GOLANG) - INTEGERS - VERSION 2 - ASSIGN VALUE ON SAME LINE
var AnyVariableName int = 700

## GO (GOLANG) - INTEGERS - VERSION 3 - SHORTCUT INFERS TYPE
AnyVariableName := 700

## GO (GOLANG) - FLOAT64 - VERSION 1 - THE LONG WAY
var AnyVariableName float64
AnyVariableName = 700.00

## GO (GOLANG) - FLOAT64 - VERSION 2 - ASSIGN VALUE ON SAME LINE
var AnyVariableName float64 = 700.00

## GO (GOLANG) - FLOAT64 - VERSION 3 - SHORTCUT INFERS TYPE
AnyVariableName := 700.00

## GO (GOLANG) - STRING - VERSION 1 - THE LONG WAY
var AnyVariableName string
AnyVariableName = "700"

## GO (GOLANG) - STRING - VERSION 2 - ASSIGN VALUE ON SAME LINE
var AnyVariableName string = "700"

## GO (GOLANG) - STRING - VERSION 3 - SHORTCUT INFERS TYPE
AnyVariableName := "700"


## PRINT TO CONSOLE
## PRINT TO CONSOLE
## PRINT TO CONSOLE

## PYTHON
print(AnyVariableName)

## JAVASCRIPT
console.log(AnyVariableName);

## GO (GOLANG)
fmt.Println(AnyVariableName)

## CHECK TYPE OF OBJECT
## CHECK TYPE OF OBJECT
## CHECK TYPE OF OBJECT

## PYTHON
type(AnyVariableName)

## JAVASCRIPT
typeof(AnyVariableName);

## GO (GOLANG)
reflect.TypeOf(AnyVariableName)



## RETURN LENGTH OF OBJECT
## RETURN LENGTH OF OBJECT
## RETURN LENGTH OF OBJECT

## PYTHON
len(AnyVariableName)

## JAVASCRIPT
AnyVariableName.length;

## GO (GOLANG)
len(AnyVariableName)



## IF / ELSE CONDITIONALS
## IF / ELSE CONDITIONALS
## IF / ELSE CONDITIONALS

## PYTHON
if WhateverCondition:
    print("If WhateverCondition is True, then do whatever conditional operation")
else:
    print("...else:  then do something else")

## JAVASCRIPT
if (WhateverCondition) {
     console.log("If WhateverCondition is true");
} else {
     console.log("else AlternateCondition goes here");
}

## GO (GOLANG) // PARENTHESES AROUND CONDITION OPTIONAL
if WhateverCondition {
     fmt.Println("If WhateverCondition is true")
} else {
     fmt.Println("else AlternateCondition goes here")
}


## IF / ELSE IF / ELSE CONDITIONALS
## IF / ELSE IF / ELSE CONDITIONALS
## IF / ELSE IF / ELSE CONDITIONALS

## PYTHON
if WhateverCondition:
    return()
elif ElseIfCondition:
    return()
else:
    return()

## JAVASCRIPT
if (WhateverCondition) {
  return();
} else if (ElseIfCondition) {
  return();
} else {
  return();
}

## GO (GOLANG) // PARENTHESES AROUND CONDITION OPTIONAL
if WhateverCondition {
  return 
} else if ElseIfCondition {
  return
} else {
  return
}



## SWITCH CASE
## SWITCH CASE
## SWITCH CASE

## PYTHON - NO SWITCH CASE;

## JAVASCRIPT

## GO (GOLANG)
switch i {
    case 0: fmt.Println("Zero")
	case 1: fmt.Println("One")
	case 2: fmt.Println("Two")
	case 3: fmt.Println("Three")
	case 4: fmt.Println("Four")
	case 5: fmt.Println("Five")
	default: fmt.Println("Unknown Number")
}



## EQUIVALENCY OPERATOR
## EQUIVALENCY OPERATOR
## EQUIVALENCY OPERATOR

## PYTHON
if 1 == 1:  ## WhateverCondition
    print("If WhateverCondition is True, then do whatever conditional operation")
else:
    print("...else:  then do something else")

## JAVASCRIPT
if (1 == 1) { // WhateverCondition
     console.log("If WhateverCondition is true");
} else {
     console.log("else AlternateCondition goes here");
}

## GO (GOLANG) // PARENTHESES AROUND CONDITION OPTIONAL
if (1 == 1) {
     fmt.Println("If WhateverCondition is true")
} else {
     fmt.Println("else AlternateCondition goes here")
}





## CREATE LIST / ARRAY
## CREATE LIST / ARRAY
## CREATE LIST / ARRAY

## PYTHON
PythonList = []

# JAVASCRIPT
var JavascriptArray = [];
let JavascriptArray = [];

## GO (GOLANG)




## ADD ELEMENT TO LIST / ARRAY
## ADD ELEMENT TO LIST / ARRAY
## ADD ELEMENT TO LIST / ARRAY

## PYTHON
PythonList.append(AnyVariableName)

# JAVASCRIPT
var JavascriptArray.push(AnyVariableName);

## GO (GOLANG)



## POP ELEMENT FROM LIST / ARRAY
## POP ELEMENT FROM LIST / ARRAY
## POP ELEMENT FROM LIST / ARRAY

## PYTHON
PythonList.pop(AnyVariableName)

# JAVASCRIPT
var JavascriptArray.pop(AnyVariableName);

## GO (GOLANG)


## CREATE PYTHON DICTIONARY / JAVASCRIPT OBJECT
## CREATE PYTHON DICTIONARY / JAVASCRIPT OBJECT
## CREATE PYTHON DICTIONARY / JAVASCRIPT OBJECT

## PYTHON
PythonDictionary = {}

# JAVASCRIPT
var JavascriptObject = {};

## GO (GOLANG)




## FOR LOOPS
## FOR LOOPS
## FOR LOOPS

## PYTHON
i = 0   ## INITIALIZE COUNTER VARIABLE
PythonList = []  ## CREATE EMPTY PYTHON LIST
RangeOfIntegerNumbers = list(range(5)) ## SET RANGE OF INTEGERS FOR FOR LOOP
for each in RangeOfIntegerNumbers:
    PythonList.append(each)
    i += 1 ## i = i + 1  ## INCREMENT COUNTER

## JAVASCRIPT
var JavascriptArray = [];   ## CREATE EMPTY JAVASCRIPT ARRAY
for (var i = 0; i < 5; i++) {  ## INITIALIZE COUNTER; SET RANGE OF INTEGERS FOR FOR LOOP; INCREMENT COUNTER
  JavascriptArray.push(i);
}

## GO (GOLANG) - VERSION 1
i := 0
for i <= 5 {
     fmt.Println(i) // CHANGE THIS TO ARRAY LATER
     i = i + 1
}

## GO (GOLANG) - VERSION 2
for i := 1; i <= 5; i++ {
     fmt.Println(i) // CHANGE THIS TO ARRAY LATER
}


## GAME OVER
    
## WE HOPE YOU ENJOYED AND THAT THIS HELPS YOUR UNDERSTANDING OF USING PYTHON / GO / JAVASCRIPT LANGUAGEs TO SOLVE PROBLEMS WITH PROGRAMMING
## PLEASE COME BACK AGAIN SOON
## PLEASE VISIT OUR WEB SITES (OUR PROBLEM-SOLVING PROGRAMMING, CODING, & DEVELOPMENT SERVICES ARE AVAILABLE FOR HIRE):
## www.JerusalemProgrammer.com
## www.JerusalemProgrammers.com
## www.JerusalemProgramming.com

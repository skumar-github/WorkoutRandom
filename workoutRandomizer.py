import sys
import os
import random


exercises = {
                #
                # Body Wieght - Upper Body
                #
                "pushups": {             
                            "group": "upper body",
                            "type":  "body wieght",
                            "variations": ["normal", "triangulated", "wide", "clap"],
                            },
                "pullups": {             
                            "group": "upper body",
                            "type":  "body wieght",
                            "variations": ["normal", "wide", "narrow", "shifting"],
                            },
                "dips": {             
                            "group": "upper body",
                            "type":  "body wieght",
                            "variations": ["normal", "hopping"],
                            },
                "chinups": {             
                            "group": "upper body",
                            "type":  "body wieght",
                            "variations": ["normal", "wide", "narrow", "shifting"],
                            },

             
                #
                # Body Wieght - Lower Body
                #
                "body squats": {             
                            "group": "lower body",
                            "type":  "body wieght",
                            "variations": ["normal", "jumping"],
                            },
                "body lunges": {             
                            "group": "lower body",
                            "type":  "body wieght",
                            "variations": ["normal", "jumping"],
                            },
                "body side lunges": {             
                            "group": "lower body",
                            "type":  "body wieght",
                            "variations": ["normal", "jumping"],
                            },
                "ice skaters": {             
                            "group": "lower body",
                            "type":  "body wieght",
                            "variations": ["normal", "jumping"],
                            },
                "box jumps": {             
                            "group": "lower body",
                            "type":  "body wieght",
                            "variations": ["normal"],
                            },
                "sprints": {             
                            "group": "lower body",
                            "type":  "body wieght",
                            "variations": ["normal", "uphill"],
                            },


                #
                # Body Weight - Core
                #
                "planks": {             
                            "group": "core",
                            "type":  "body weight",
                            "variations": ["normal", "side step"],
                            },
             
                "leg lifts": {             
                            "group": "core",
                            "type":  "body weight",
                            "variations": ["supported elbows", "hanging", ],
                            },
             
             
             
                #
                # Body Wieght - Full Body
                #
                "burpees": {             
                            "group": "full body",
                            "type":  "body wieght",
                            "variations": ["normal", "pushup"],
                            },



                #
                # Weights - Lower Body
                #
                "squats": {             
                            "group": "lower body",
                            "type":  "wieghts",
                            "variations": ["barbell", "lopsided", "kettlebell", "dumbell"],
                            },
                "lunges": {             
                            "group": "lower body",
                            "type":  "wieghts",
                            "variations": ["barbell", "kettlebell", "dumbell", "walking"],
                            },
                "side lunges": {             
                            "group": "lower body",
                            "type":  "wieghts",
                            "variations": ["barbell", "dumbell"],
                            },


                #
                # Weights - Core
                #
                "power clean": {             
                            "group": "core",
                            "type":  "wieghts",
                            "variations": ["barbell"],
                            },
                "deadlift": {             
                            "group": "core",
                            "type":  "wieghts",
                            "variations": ["barbell"],
                            },
                "kettlebell swings": {             
                            "group": "core",
                            "type":  "wieghts",
                            "variations": ["normal"],
                            },
                "twists": {             
                            "group": "core",
                            "type":  "wieghts",
                            "variations": ["normal"],
                            },


                #
                # Weights - Full Body
                #
                "bear mountain": {             
                            "group": "full body",
                            "type":  "wieghts",
                            "variations": ["normal"],
                            },



                #
                # Weights - Upper Body
                #
                "bench press": {             
                            "group": "upper body",
                            "type":  "wieghts",
                            "variations": ["barbell", "dumbell", "dumbell medicine ball", "narrow", "wide", "lopsided"],
                            },
                "bicep curls": {             
                            "group": "upper body",
                            "type":  "wieghts",
                            "variations": ["barbell", "dumbell", "narrow", "wide", "lopsided"],
                            },
                "seated military press": {             
                            "group": "upper body",
                            "type":  "wieghts",
                            "variations": ["barbell", "dumbell", "dumbell medicine ball", "narrow", "wide", "lopsided"],
                            },
                "standing military press": {             
                            "group": "upper body",
                            "type":  "wieghts",
                            "variations": ["barbell", "dumbell", "narrow", "wide", "lopsided"],
                            },
            }


workoutsFile = "./workouts.txt"

def getKeyNum(dict, num):
    i = 0;
    for key in dict:
        if (i==num):
            return key;
        i+=1
  

def filterThroughRules(eArr):
    #
    # Check null value (begin filter pass)
    #
    if (eArr[0] == None):
        for i in range(0, len(eArr)): 
            eArr[i] = random.randrange(0, len(exercises)-1, 1)
            


    #===========================================================================
    # Rule 1: No repeat exercises
    #===========================================================================
    
    for i in range(0, len(eArr)): 
        if eArr.count(eArr[i]) > 1:
            #print("REPEAT: %s"%(eArr[i]), eArr, "************")
            eArr[i] = random.randrange(0, len(exercises)-1, 1)
            filterThroughRules(eArr)


         
    
    #===========================================================================
    # Rule 2: No excercise from previous workout to be in this week's routine
    #===========================================================================
     
    prevThresh = 2;
    # read the file line by line, store it.
    lines = [line for line in open(workoutsFile)]
    for i in range(0, len(lines)):
       lines[i] =  lines[i].split("**********")[0].strip().strip("[").strip("]").split(", ")
    
    
    # get the last 2 workouts (or whatever prevThresh is)
    lines = lines[-prevThresh:]
    
    
    # merge the last workouts to a single list
    mergedLines = []
    for i in lines:
        for j in i:
            mergedLines.append(j.strip("'")) # get rid of quotes
    
    # back check for repeats
    keyArr = getExcKeyArr(eArr)
    #print "mergLi: ", mergedLines, " keyArr: ", keyArr
    i=0
    for k in keyArr:
        if k in mergedLines:
            #print "REPEAT FROM LAST WEEK: ", k, i
            eArr[i] = random.randrange(0, len(exercises)-1, 1)
            filterThroughRules(eArr) 
        i+=1
  
  
    
        
    #===========================================================================
    # Rule 3: No repeat groups for this week
    #===========================================================================
    nonRepeatables = ["upper body", "lower body"]
    
    keyArr = getExcKeyArr(eArr)
    i=0
    groupArr = []
    for k in keyArr:
        groupArr.append(exercises[k]["group"]) 
    
    for r in nonRepeatables:
        if groupArr.count(r)>1:
            #print "FUND: ", groupArr.index(r), " keyArr: ", keyArr, " groupArr:", groupArr
            eArr[groupArr.index(r)] = random.randrange(0, len(exercises)-1, 1)
            filterThroughRules(eArr) 

    return eArr   
 
#===============================================================================
# Returns the keys of the excercise array based on their numerical place
#===============================================================================
def getExcKeyArr(numArr):
    excKeyArr = []
    for i in numArr:
        j = 0
        for key in exercises:
            if (i == j):
                excKeyArr.append(key)
            j+=1           
    return excKeyArr   
                  
def main():
    numExercises = 2
    eArr = [];
    
    # create null array
    for x in range(0, numExercises): 
        eArr.append(None)

    

    es = filterThroughRules(eArr)
    excKeys = getExcKeyArr(es)
    variate = []
    for e in excKeys:
        variate.append(exercises[e]["variations"][random.randrange(0, len(exercises[e]["variations"]), 1)])
    
    # Append line to file.
    lines = [line for line in open(workoutsFile)]
    #lines.append(str(excKeys) + "**********" + str(variate))
    
    # append the variance to the key
    newLine = []
    for x in range(0, len(excKeys)):
        newLine.append(excKeys[x] + " (" + variate[x].upper() + ")")
    
    lines.append(str(newLine))
    
    print newLine
         
    fl = open(workoutsFile, 'w')
    for item in lines:
        fl.write("%s\n" % item.strip())
    fl.close()

    
if __name__ == "__main__":
    main()
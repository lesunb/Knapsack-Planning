class knapsackObject:
  def __init__(self, task, value, weight, group):
        self.task = task
        self.value = value
        self.weight = weight
        self.group = group


def knapsackTable(capacity, knp):
    task = knp.task
    value = knp.value
    weight = knp.weight
    group = knp.group
    N = len(value)

    K = [[0 for x in range(N)] for x in range(capacity)]
    solution = [[None for x in range(N)] for x in range(capacity)]

    for n in range(0, N):
        for w in range(1, capacity+1):
            option1 = getMax(group[n]-1, K[n], group, n)
            option2 = 0
            option3 = getMax(group[n], K[n], group, n)

            if weight[n] <= w:
                option2 = value[n] + getMax(group[n] - 1, K[(w-1) - weight[n]], group, n)

            K[w-1][n] = max(option1, option2)

            if (option2 > option1) and (option2 > option3):
                solution[w-1][n] = task[n]

    take = getSolution(N, capacity, solution, group, K, weight)

    return take


def getMax(group, row, groups, n):
    max = 0

    for i in range(n):
        if groups[i] == group:
            if row[i] > max:
                max = row[i]
    
    return max


def getSolution(N, W, sol, group, matrix, weight):
    solution = []
    lastTakenGroup = -1
    
    for n in range(0, N):
        for w in range(1, W):        
            if sol[w][n] is not None and calculateIsMax(n, w, group, matrix, N):
                if group[n] == lastTakenGroup:
                    continue
                solution.append(sol[w][n])
                w = w - weight[n]
                lastTakenGroup = group[n]
    
    return solution


def calculateIsMax(n, w, groups, matrix,  N):
    group = groups[n]
    max = 0
    for i in range(N):
        if(groups[i] == group):
            if(matrix[w][i] > max):
                max = matrix[w][i]
        
    
    return matrix[w][n] == max


def utilitary(weights):
    values = []

    for w in weights:
        if w > 0:
            values.append(1/w)
        elif w == 0:
            values.append(1)
        else:
            values.append(0)

    return values

def testIsNotifiedAboutEmergency():
    t = ["notifies [p] by mobile vibration", 
        "notifies [p] by light alert", 
        "centrals calls [p]", 
        "notifies [p] by sound alert"
    ]
    wt = [2, 9, 0, 7]
    val = utilitary(wt)
    g = [0, 0, 0, 0]
    capacity = 10

    knp = knapsackObject(t, val, wt, g)

    k = knapsackTable(capacity, knp)

    print("[p] is notified about emergency:")
    print(k)

def testCallForHelpIsAccepted():
    t = ["notify central by SMS", 
        "notify central by Internet", 
        "accepts emergency", 
        "confirms emergency by call"
    ]
    wt = [10, 5, 30, 5]
    val = utilitary(wt)
    g = [0, 0, 1, 1]
    capacity = 5

    knp = knapsackObject(t, val, wt, g)

    k = knapsackTable(capacity, knp)

    print("[p] call for help is accepted:")
    print(k)

def testLocationIsIdentified():
    t = ["Consider last known location[l] of [p]", 
        "access [p] location [l] from triangulation", 
        "access [p] location [l] from a GPS", 
        "identifies[p] location [l] by voice call",
        "access data from database"
    ]
    wt = [900, 40, 20, 100, 20]
    val = utilitary(wt)
    g = [0, 0, 0, 0, 1]
    capacity = 1000

    knp = knapsackObject(t, val, wt, g)

    k = knapsackTable(capacity, knp)

    print("setup automated [p] info:")
    print(k)

def testSituationsAreIdentified():
    t = ["processes sensors", "collecs data from sensors", "persists data to database", "identifies situation"]
    wt = [0, 0, 0, 0]
    g = [ 1, 1, 1, 1]
    val = utilitary(wt)
    capacity = 30 #(baseline c3 10 c9 5)

    knp = knapsackObject(t, val, wt, g)
    k = knapsackTable(capacity, knp)

    print("[p] situationsAreIdentified:")
    print(k)


def testInfoIsSentToEmergency():
	t = ["send [p] info by SMS", "send [p] info by internet"]
	wt = [0,0]
	g = [1,1]
	val = utilitary(wt)
	capacity = 60

	knp = knapsackObject(t, val, wt, g)
	k = knapsackTable(capacity, knp)
	
	print("[p] info is sent to emergency")
	print(k)
	

def testSituationDataIsRecovered():
	t = ["access data from database"]
	wt = [20]
	g = [1]
	val = utilitary(wt)
	capacity = 20

	knp = knapsackObject(t, val, wt, g)
	k = knapsackTable(capacity, knp)
	
	print("[p] situation data is rocevered:")
	print(k)
	
def testContactResponsibleFor():
	t = ["[p]contact responsible for"]
	wt = [25]
	g = [1]
	val = utilitary(wt)
	capacity = 45
    
    knp = knapsackObject(t, val, wt, g)
    k = knapsackTable(capacity, knp)
	
	print("[p] contact responsible for:")
	print(k)
#todo: criar funções que ative os contextos

testIsNotifiedAboutEmergency()
testCallForHelpIsAccepted()
testLocationIsIdentified()

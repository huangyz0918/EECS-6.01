class DDist:
    def __init__(self, dictionary):
        if not (abs(sum(dictionary.values())-1) < 1e-6 and min(dictionary.values()) >= 0.0):
            raise Exception, "Probabilities must be nonnegative, and must sum to 1"
        self.d = dictionary

    def prob(self, elt):
        if elt in self.d:
            return self.d[elt]
        else:
            return 0

    def support(self):
        sup = [elt for elt in self.d if self.prob(elt) > 0]
        return sup

    def __repr__(self):
        return "DDist(%r)" % self.d
    
    __str__ = __repr__

    def project(self, mapFunc):
        dic = {}
        for x in self.support():
            if mapFunc(x) in dic:
                dic[mapFunc(x)] += self.prob(x)
            else:
                dic[mapFunc(x)] = self.prob(x)
        return DDist(dic)
    
    def condition(self, testFunc):
        pruned = [elt for elt in self.support() if testFunc(elt)]
        z = sum([self.prob(elt) for elt in pruned])

        return DDist({elt: self.prob(elt)/z for elt in pruned})

def marginalize(d, i):
    new_dic = {}
    def del_ith(tpl):
        tpl = list(tpl)
        del tpl[i]
        return tuple(tpl)
    
    for tpl in d.support():
        new_tpl = del_ith(tpl)
        if new_tpl in new_dic:
            new_dic[new_tpl] += d.prob(tpl)
        else:
            new_dic[new_tpl] = d.prob(tpl)
    new_dis = DDist(new_dic)

    return new_dis.project(lambda x: x)
    
    
def makeJointDistribution(PA, PBgA):
    dic = {}
    for a in PA.support():
        for b in PBgA(a).support():
            dic[(a,b)] = PA.prob(a) * PBgA(a).prob(b) 
    return DDist(dic)

def totalProbability(PA, PBgA):
    joint = makeJointDistribution(PA,PBgA)
    preformat = marginalize(joint,0)
    final = {}
    for key in preformat.support():
        final[key[0]] = preformat.prob(key)
    return DDist(final)

''' More intelligent way
def totalProbability(PA, PBgA):
    return makeJointDistribution(PA, PBgA).project(lambda x: x[1])
    '''

def totalProbability_nohelper(PA, PBgA):
    final = {}
    for a in PA.support():
        bdist = PBgA(a)
        aprob = PA.prob(a)
        for b in bdist.support():
            b_given_a = bdist.prob(b)
            if b in final:
                final[b] += (aprob*b_given_a)
            else:
                final[b] = (aprob*b_given_a)
        
    return DDist(final)

def bayesRule(PA, PBgA, b):
    PAB = makeJointDistribution(PA,PBgA)
    PABb = PAB.condition(lambda tplk: tplk[1] == b)
    final = PABb.project(lambda tplk: tplk[0])
    return final

def bayesRule_nohelper(PA, PBgA, b):
    final = {}
    ba = lambda a: PBgA(a)
    ab = lambda a: PA.prob(a) * ba(a).prob(b)
    B = sum([ab(a) for a in PA.support()])
    for a in PA.support():
        pAgB = ab(a)/B
        final.update({a: pAgB})
    return DDist(final)


# Defined
Weather = DDist({'rain': 0.4, 'sun':0.6})
    
ActivityGivenWeather = lambda weather: DDist({'computer': 0.3, 'outside': 0.7}) if weather=='sun' else DDist({'computer': 0.8, 'outside': 0.2})

QuantumGivenActivity = lambda activity: DDist({'keyboard': 0.8, 'bed': 0.2}) if activity=='computer' else DDist({'keyboard': 0.1, 'bed': 0.9})


pRainGivenComputer = bayesRule(Weather, ActivityGivenWeather, 'computer').prob('rain')
print pRainGivenComputer

pWandA = makeJointDistribution(Weather, ActivityGivenWeather)
print pWandA

pA = pWandA.project(lambda (W,A): A)
print pA
    
pQ = totalProbability(pA, QuantumGivenActivity)
print pQ

pC = pWandA.prob(('rain','computer')) + pWandA.prob(('sun', 'computer'))
print pC

pQandA = makeJointDistribution(pA, QuantumGivenActivity)
print pQandA

pQgWandA = lambda (W,A): DDist({'keyboard': QuantumGivenActivity(A).prob('keyboard'), 'bed':QuantumGivenActivity(A).prob('bed') })

pWandAandQ = makeJointDistribution(pWandA, pQgWandA)
pWnAnQ = {(tuplekey[0][0],tuplekey[0][1],tuplekey[1]): pWandAandQ.prob(tuplekey) for tuplekey in pWandAandQ.support()}
print pWnAnQ

WeatherAndActivityAndQuantum = DDist(pWnAnQ)

pSunAndOutside = WeatherAndActivityAndQuantum.project(lambda (W,A,Q): W == 'sun' and A == 'outside').prob(True)
print pSunAndOutside
# easier is pWandA.prob(('sun','outside'))

pComputer = pC
print pComputer

pRainGivenKeyboard = WeatherAndActivityAndQuantum.condition(lambda (W,A,Q): Q == 'keyboard').project(lambda (W,A,Q): W == 'rain').prob(True)
print pRainGivenKeyboard

pRainGivenBed = WeatherAndActivityAndQuantum.condition(lambda (W,A,Q): Q == 'bed').project(lambda (W,A,Q): W == 'rain').prob(True)
print pRainGivenBed

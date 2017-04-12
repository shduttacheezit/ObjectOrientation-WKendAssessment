eng2bengali = {'me': 'ami', 'lets go': 'cholo', 'eat': 'khabho', 'you': 'tumi', 'how are you': 'kemon achish', 'my name': 'amar naam', 'sleep': 'goum', 'water': 'jhol', 'food': 'kaowa', 'shower': 'chaan'}
 #dictionary with 10 words/phrases (keys) translated to Bengali (values)
def translate(i):
    for word in eng2bengali:
        if i in eng2bengali.keys():
            return eng2bengali[i]
        else: 
            return "Oh no! That word doesn't exist in Bengali!" 

letsgo = translate('lets go')
print letsgo 

sandwich = translate('sandwich')
print sandwich 


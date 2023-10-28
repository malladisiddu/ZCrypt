from banner import *
from utils import convert
banner()

'''
==> c = 89607111639919127209650034924273346966533469612321885496366954902260836555651605455268315685564884102521751315138745054317891549734624460415579282469559824676571129509386897261361718686847757184676797652741644509297296594801094652142919180951341757690575359920800914815550536137727683352201005845272448559627
==> n = 89928311288179011519146428089532751379523591729622855508594372783166478638917327757191123264641418795443514859544099539422860363086133465517078412097475326937856290265542196688524185772419476324834419576555062944062383244109784866915010028008734205492481116857889368085002365514967068884805814897932754658961
==> d = 9974348761062807799146671129023506870588476559540847714908715622638160630274349687459332514620420117247950158140074454919583929372310361488069990654691975678966812319952558452020783995983648814894273413199715498765593824693014878541105366177785811920577583349903357558945708664999648041451991782189528550577

'''


try:
    c = int(input("==> c = "))
    n = int(input("==> n = "))
    d = int(input("==> d = "))
    
    decrypt = pow(c,d,n)
    convert(decrypt)
except ValueError:
    slowprint("\n[-] c,n,d Must be Integer Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()

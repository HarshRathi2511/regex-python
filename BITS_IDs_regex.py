import re

BITS_IDS= '''
2021AAPS0029P
2021B4PS1052P
2021B5TS2054P
2020B3A70794P
1982B3A70944P
2021H1060196P
2017ABPS0357P
'''

pattern = re.compile(r'(19|20)\d{2}[A-Z0-9]{2}[A-Z0-9]{2}\d{4}P')

pattern_refined= re.compile(r'(19|20)\d{2}(A1|A2|A3|A4|A5|A7|A8|A9|AA|AB|B1|B2|B3|B4|B5|C2|C5|C6|C7|H1|H2|H3|H4|PS|TS)+\d{4,6}P')

#for undergrads 
pattern_first_degree= re.compile(r'(19|20)\d{2}(A1|A2|A3|A4|A5|A7|A8|A9|AA|AB|B1|B2|B3|B4|B5|C2|C5|C6|C7|PS|TS){2}\d{4}P')

matches = pattern_first_degree.finditer(BITS_IDS)

for match in matches:
    print(match)
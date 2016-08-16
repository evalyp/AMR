#!/usr/bin/python

# Dictionary for method 4-Run on the output of method 2
import re

first_time = True
input_path = 'amr_edges_test_02all'
dataset_04_amr = 'amr_4_test_all'

d1 = {':time :month 10' : 'in october',
     ':month 10' : 'october',
     'ordinal-entity 1 :range temporal-quantity' : 'first time in',
     'ordinal-entity 2' : 'second',
     'ordinal-entity 1' : 'first',
     'ordinal-entity 3' : 'third',
     'ordinal-entity 4' : 'fourth',
     'ordinal-entity 5' : 'fifth',
     'ordinal-entity 6' : 'sixth',
     'ordinal-entity 74': 'no. 74',
     'ordinal-entity 66': 'no. 66',
     'ordinal-entity 77': 'no. 77',
     'ordinal-entity 82': 'no. 82',
     'ordinal-entity 8': 'eighth',
     'ordinal-entity 9': 'ninth',
     'ordinal-entity 10 :range': 'tenth',
     'ordinal-entity': '',
     'ordinal-entity -1' : '',
     'ordinal-entity 1 :range' : 'first',
     'ordinal-entity 1 :part-of' : 'first',
     'ordinal-entity 15' : ' 15th'}


d2 = {':time :month 11': 'in november',
     ':month 11': 'november'}

d3 = {':time :month 12' : 'in december',
     ':month 12' : 'december'}

d4 = {'dollar' : '$',
     ':manner-of': 'how',
     'percentage-entity' : '%',
     'li' : '',
     ':polarity -': 'no',
     ':prep-against': 'against',
     ':time': 'in',
     'location-of' : 'of',
     ':part-of': 'of',
     ':consist-of' : 'of',
     ':month 02' : 'february',
     ':month 05' : 'may',
     ':month 01' : 'january',
     ':month 03' : 'march',
     ':compared-to' : 'compared to',
     'quant-of' : 'of',
     'frequency 1' : 'once',
     'frequency 2' : 'twice',
     'frequency 3' : 'three times',
     'frequency 4' : 'four times',
     'frequency 5' : 'five times',
     'frequency rate-entity-91' : 'every',
     'instrument-of' : 'of',
     ':prep-along-with' : 'along',
     ':prep-along-with' : 'with',
     ':prep-amid' : 'amid',
     ':prep-among' : 'among',
     ':prep-as' : 'as',
     ':prep-at' : 'at',
     ':prep-between' : 'between',
     ':prep-by' : 'by',
     ':prep-considering' : 'considering',
     ':prep-except' : 'except',
     ':prep-following' : 'following',
     ':prep-for' : 'for',
     ':prep-from' : 'from',
     ':prep-in' : 'in',
     ':prep-in-addition-to' : 'in addition to',
     ':prep-instead-of ' : 'instead of',
     ':prep-into' : 'into',
     ':prep-of ' : 'of',
     ':prep-on' : 'on',
     ':prep-on-behalf-of' : 'on bahalf of',
     ':prep-other' : 'other',
     ':prep-per' : 'per',
     ':prep-regarding' : 'regarding',
     ':prep-through' : 'through',
     ':prep-to' : 'to',
     ':prep-toward' : 'toward',
     ':prep-under' : 'under',
     ':prep-with' : 'with',
     ':prep-within' : 'within',
     ':prep-with-of' : 'of',
     ':prep-without' : 'without',
     'consist-of' : 'of',
     'rate-entity-91' : 'every',
     ':range': 'in',
     ':medium' : 'in',
     ':purpose' : 'to',
     ':domain-of ': 'of',
     'include-91 ' : 'of',
     ':subset' : 'of',
     'frequency' : 'every',
     'have-purpose-91' : 'to',
     ':beneficiary' : 'for',
     ':cause' : 'because of',
     ':concession' : 'although',
     ':concession-of' : 'but anyway',
     'have-concession-91' : 'nevertheless',
     'rate-entity 2 1 year' : 'twice a year',
     'long :degree more' : 'longer',
     'high :degree more' : 'higher',
     'short :degree more' : 'shorter',
     'strong :degree more' : 'stronger',
     'late :degree more' : 'later',
     'early :degree more' : 'earlier',
     'hot :degree more' : 'hotter',
     'long :degree most' : 'longest',
     'high :degree most' : 'highest',
     'short :degree most' : 'shortest',
     'strong :degree most' : 'strongest',
     'late :degree most' : 'latest',
     'early :degree most' : 'earliest',
     'hot :degree most' : 'hottest',
     ':time :month 1': 'in january',
     ':month 1': 'january',
     ':time :month 2' : 'in february',
     ':month 2' : 'february',
     ':time :month 3' : 'in march',
     ':month 3' : 'march',
     ':time :month 4' : 'in april',
     ':month 4' : 'april',
     ':time :month 5' : 'in may',
     ':month 5' : 'may',
     ':time :month 6' : 'in june',
     ':month 6' : 'june',
     ':time :month 7' : 'in july',
     ':month 7' : 'july',
     ':time :month 8' : 'in august',
     ':month 8' : 'august',
     ':ord-of' : '',
     ':direction-of':'',
     ':time :month 9' : 'in september',
     ':month 9' : 'september',
     ':example-of' : 'such as',
     ':era' : ' ',
     ':duration-of' : '',
     ':extent' : '',
     ':condition-of' : 'if',
     ':source-of' : 'where',
     ':poss-of' : '',
     ':path-of' : '',
     ':degree-of' : 'how',
     'amr-unknown' : '',
     ':polite ' : 'please',
     ':century' : 'century',
     ':topic-of' : 'about',
     'ordinal-entity :value 1' : 'first',
     'ordinal-entity :value 2' : 'second',
     'ordinal-entity :value 3' : 'third',
     'ordinal-entity :value 4' : 'fourth',
     'ordinal-entity :value 5' : 'fifth',
     'ordinal-entity :value -1' : 'first to last',
     'ordinal-entity :value -2' : 'second to last',
     'ordinal-entity :value -3' : 'third to last',
     'ordinal-entity :value -4' : 'fourth to last',
     'ordinal-entity :value -5' : 'fifth to last'
     }

pattern1 = re.compile('|'.join(d1.keys()))
pattern2 = re.compile('|'.join(d2.keys()))
pattern3 = re.compile('|'.join(d3.keys()))
pattern4 = re.compile('|'.join(d4.keys()))


with open(input_path, 'r') as f:
    with open(dataset_04_amr, 'w') as amr:
        for line in f:
            line = line.lower().strip()
            line = pattern1.sub(lambda x: d1[x.group()], line)
            line = pattern2.sub(lambda x: d2[x.group()], line)
            line = pattern3.sub(lambda x: d3[x.group()], line)
            line = pattern4.sub(lambda x: d4[x.group()], line)

            amr.write(line, )
            amr.write("\n")

f.close()
amr.close()


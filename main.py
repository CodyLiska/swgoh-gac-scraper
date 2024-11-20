import GetGacData as getGacData
import EventResults as eventResults
import Characters as characters
import MatchUp as matchUp
from CombinedResults import combineResults

#print(':: DOWNLOADING GAC DATA ::')
#getGacData.getGacData()
#print()
print('::GAC MATCHUP::')
matchUp.getGacEventMatchup()
print()
print('::GAC RESULTS::')
eventResults.getGacEventResults()
print()
print('::GAC CHARACTERS::')
characters.getCharacters()
print()
print("::Combining Results::")
combineResults()

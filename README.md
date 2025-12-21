# Archivr

Archivr is a small application I wrote to help me wrangle my massive collection of commercials.
This is still very much a work in progress :-)

# File Name Meta Encoding

Part of management I want to be able to glean useful information about each of the files when processing them so that I can build queries for specific things.
For example if I wanted make a kids channel, I would obviously not want to include R/M rated commcercials. Maybe I have a preference around whether the commercial has a 3rd party watermark.

FileName [Year Aired, Season, Rating, Network, WaterMark].Extension
ex. 
Gerber Life Grow-Up Plan M_1990_A_A_FK_0.mp4

WaterMark:
1 - Includes a water mark
0 - No

Ratings: (Should not be combined)
====================
X - All
E - Everyone
G - General
PG - Parental Guidance
PG13 - Parents Strongly Cautioned
M - Mature
R - Restricted
NC17 - No one under 17
A - Adult

Seasons/Holiday: (Can be Combined ei: PSF (Summer, Spring, Fall))
=====================
X - All
C - Christmas
E - Easter
H - Halloween
I - Independance Day (Gotta get those fireworks!)
N - New Years
T - Thanks Giving
S - Summer
F - Fall
P - Spring
W - Winter

Networks
======================
CN - Cartoon Network
AS - Adult Swim
KWB - Kids WB 
Fox - Fox
Nic - Nickolodean
Dis - Disney
FK - Fox Kids
G - Generic Commercials
And more!

## Querying with Ersatz (Lucene)

You can setup some really cool queries with this when combined with folder structures as tags

Examples: 

90s kids comnmercials
m_199[0-9]_(e|g)*_(x)*_(cn|fk|nic|kwb|dis)*_[01]

90's kids christmas and winter commercials
m_199[0-9]_(e|g)*_(c|w)*_(cn|fk|nic|kwb|dis)*_[01]


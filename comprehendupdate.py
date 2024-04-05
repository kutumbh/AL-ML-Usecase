#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3


# In[2]:


client = boto3.client('comprehend',region_name='ap-south-1',aws_access_key_id='AKIAUG5QZ7LXGOCB3EZE',aws_secret_access_key='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')


# In[3]:


client


# In[4]:


text = """6
TIMES NATION
THE TIMES OF INDIA, MUMBAI
MONDAY, MAY 18, 2020
560 Bihar returnees test
Big push for
Why Focus Should
As India moves closer to reducing curbs, the focus should be
online classes
on how to revive economic activity in way that will have the
maximum impact. That will mean looking at districts, rather
positive, 31% from Delhi
to ensure edu
Be On Districts To
than the whole country. But the 'safest' districts may not have
the most economic potential. So, the aim must be to not only
doesn't suffer
Drive Reopening
reopen green zones but also figure out how to restart businesses
in red zone districts where most economic activities are located
Results Of 349
TIMES NEWS NETWORK
Samples Taken
New Delhi: By the end of this
month thetop100universitiesin
From Delhi
the National Institutional Rank
Economic Activity Not
Districts by index of economic activity and Covid-19 risk
ing Framework (NIRF) will be
Uniform Across India
The table shows, for
Batch Awaited
allowed to offer
IEA PERCENTILE
DISTS
RED ZONE
ORANGE
GREEN
online courses
example, that the top
Top 10%
73
Madan.Kumar
'automatical-
A strategic approach to reopening the
10% of economically
@timesgroup.
ly' Announc
economy will require policymakers to
active districts is largely
Top
10-20%
72
initiative
identify districts by the level of economic
made up of red and
Patna: Bihar on Sunday re-
called PM eVI-
activity in each, says consulting firm
orange zones, while
Top 20-30%
72
40
14
ported 560 Covid-19 cases
DYA which will
Akara in note. Knowing where economic
the bottom 10% mostly
Top 30-40%
72
15
41
16
among migrant workers who
CONTROLLING THE CROWD: policeman wields his baton to
unify all efforts related to digi-
activity is concentrated, combined
green zones. This trend
have returned since May 1,
disperse migrants demanding train service to their home state
tal/online/or education to
with the knowledge of where Covid-19
holds true across the
Top 40-50%
73
34
29
constituting 7% of the 7.639
Bihar, in Ahmedabad on Sunday
enable multi-mode access to
cases are concentrated. will enable the
spectrum. The table
samples tested so far. Of the
education. finance minister
Nirmala Sitharaman on Sun-
government to maximise the impact
shows economic
Bottom 40-50%
71
32
37
1.070 swabs randomly taken
from the Delhi batch are
workers had returned to Bi-
from migrant workers back
har. Out of this, 23,633 mi-
of reopening
occurs
in
awaited. Overall, the test re
day assured that education
Bottom 30-40%
72
from Delhi. 172havesofartest
sults of 2.746 samplesar still
grantworkerscamefrom] Del-
clusters
would not suffer due to Covid-
ed positive for the virus,
to come, principal secretary
hi on 18 special trains. "The
"Technology-driven educa-
Resuming economic
Bottom 20-30%
72
which 31%
Sanjay Kumar
migrant workers who return-
tion will be the focus, PM eVI-
activity will be most effective
Bottom 10-20%
72
12
of the total cases
After Delhi, returnees
ed from Delhi by other means
DYAprogrammeformult
if done in districts that are
iscould be just the tipof
from Gujarat (128) and Maha-
or on foot are not included in
access to digital online educa
the iceberg since medical
tion obelaunched immediately.
not only the safest but also
Bottom 10%
73
rashtra (123) account for the
this figure, Amritsaid
teams have SO far randomly
bulk of the positive cases
According to records, 26
Top 100 universities will be per-
have the most economic
GREEN
RED
collected only 10,385 samples
amongmigrantworkers. Ben-
workers who returned from
mitted automatically start on-
potential
314
TOTAL
128
from among 7.4 lakh migrant
contribution to the tally
Bengal on foot or by bus or
line courses by May 30. Sithara
DISTRICTS
workers brought home by 566
Principal secretary (di-
truck positive. An-
man said. The universities will
Akara has designed an
722
ORANGE
trains from states ac-
management) Pra-
other 25 from Haryana and 16
include IITs, IIMs. institutes of
index of economic
280
cording data.
tvaya Amrit said on Sunday
from UP who didn't travel by
eminence, national institutes as
activity (IEA),
Results
of
samples
thatatotal of
positive.
well as private universities.
categorising districts
In the most active districts, economic
by intensity of
ETURNING BEGINNING OF WOES..
growth has brought in labour from
economic activity
across the country. The note says
into percentile groups
while that makes these clusters
of roughly the same
TN villagers force man
Many U'khand returnees
DISTRICTS BY
"competitive in terms of operating
sizes and the government's
MODAL INCOME
costs", the consumption economy
Covid- 19 risk classification of
Over ₹6,50,000
has spread via "purchasing power
red. orange and green zones.
transferred through remittances'
to spend days on hillock
refuse to be quarantined
₹3,00,000 - 4,00,000
The index was built using
₹2,00,000 - 33,00,000
from these districts. That has led to
Reserve Bank of India data on
"credit offtake to different sectors
₹75,000 ₹2,00,000
the income group Rs 75,000
Shanmughasundaram.
centres, managing sanitisa-
at the district level"
Less than ₹75,000
Rs 2,00,000 per year being the modal
himstav in thevillage.
Ishita Mishra
household income in most districts
When returned, the lo-
& Prashant Jha TNN
drives sandarrangingfood
cals feared that might be car-
itemsfor thosein
Chennai: The government
rying the virus and could
Dehradun/Nainital
With
quarantine centres.
may be telling people not to
spread infection. They told me
thousands of migrants re
Many pradhans say that
Goal Should Be To
boycott those who have Co-
to stay away from the village,
turning to their native villag
responsibilities given to them
A Key Challenge Is To
Create More Production Hubs
19orare in guarantine. but
Shamimsa
es. most gram pradhans (vil-
are much more than they
Get Migrants Back
the ground reality is different
Shamim took shelter near
lageheads) grappling with
The note points to the opportunity to "enable recovery-oriented
For the past one week. 28 year-
a
temple on hillock in the vi-
lack of adequate training, re
INSUFFICIENT
Flagging the issue of reverse migration of
measures to yield long-term benefits' adding that infrastructure
old Shamim Ali was forced to
cinity. But villagers prevented
sources and even
labour from key economic centres like cities and industrial
RESOURCES
projects to be taken up should be oriented towards strengthening
stay away from his family and
his wife from visiting him. His
ation of many returnees who
hubs. the note says efforts should be directed at ensuring
economic activities and making Indian value addition globally
live on a hillock on the out-
younger brother Khalil Ali
tobequarantined.
can handle, considering that
these workers can be moved back quickly when the
competitive Bringing in the district level focus it points to the need
skirtsof Kannagapattu Thi-
would drop food near him.
Praveen Pragyan, prad-
they have not been given suffi-
red zones, where the majority of economic activity is
focus, at the outset. on districts that are dominant
ruporur, Tamil Nadu
Revenue inspector of Thi-
han of Bhangeli village in Ut
cient resources.
concentrated. begin
in one or two sectors. The
A guest worker from Kan-
ruporur N Pushpa Rani along
tarkashi. told TOI, "We have
Many village heads also
to reopen. One
example cited is that of
nauj district of UP. Shamim
with police officers reached
been tasked with managing
have to contend with sullenre-
solution suggested
Anand and whether other
has been working as load
the village on Saturday morn
the 14-day mandatory quaran
turnees who refuse to follow
is registry
centres can be developed
man in the Koyambedu mar-
ing "We spoke the villagers
tine period of the returnees.
quarantine protocols. A few
or system of
ket. He was taken for screen-
and tried to allay their fears.
We are also responsible for
daysago, whorefused
to attain the Gujarat city's
identifying
ing in the first week May
We told them to let Shamim
veloping government build
to serve quarantine had start
scale of production in
migrants in
advised home
at home. Later. he came
ings such as schools and pan-
ed pelting stones at the village
dairy sector
their states
Since then, locals refused to let
back to the village, Rani said.
chayat houses as quarantine
head and hisassociates.
of origin, where
Recovery From
they have
Covid- Identify
Upon District Leve
TIMESTRIBUTER
This 'Shravan Kumar'
returned
Economic
Activities
SAD DEMISE
DEATH
BIRTHDAY
is walking 1,300km
ANNIVERSARY
REMEMBRANCES
carrying two children
Travelled for 5 days, didn't abandon me'
In Loving Memory
From 1
Aligarh, Bulandshahn Hapur
didn't abandon me." Gayoor
Anirudh played down his
of our loving and
and Meerut. They moved, ate
smiled. The story spread like
role in what many in Muzaffar
1st DEATH
took few moments for Ani-
and slept on roads all this while
wildfire in hthedistrictafterthat
nagar are now calling heroic.
ANNIVERSARY
exceptional
rudh to take call which per-
until they finally reached Mu-
Additional district magist-
First, beings. We
In loving memory of
grandmother
haps few would. He decided
affarnagaron May 12.
(finance) Alok Kumar said,
are Hindus and Muslims after
ochange direction head to Mu-
Gayoor said on Saturday he
"Every possible bepro-
that am happy could help
zaffarnagar instead of Nagpur
never forget the kindness
vided to the disable man and
Gayoor Iam
and accompany Gayoor until
wason my tricycle Anirudh
his family, and even to the per-
ilv now will be here while
isfriend safely home.
was always walking behind,
son who helped the disabled
All of them are nice and polite.
Anirudh pushed Gayoor's
pushing it during the whole
man.
Home
now,
Gayoor
like I am with my own fam
tricycle for the next five days
journey of about 350km We
doesn't want to let Anirudh go
On his part, Gayoor wants
Our beloved mother,
they criss-crossed several dis-
until the lockdown is lifted Nei-
the administration to help Ani-
Mrs. Dru Murli Mukhi
tricts, walking past Mathura,
Kidwai Nagar late on May He
then does family.
rudh reach Nagpur
passed onward to her
A FATHER'S LOVE: 40-year- old migrant carries
heavenly abode, on
his children in weighing baskets
15th May 2020
A Beautiful human
Smt. RAJAM LAXMAN
Sandeep Raghavan timesgroup com
Let DMs, SPs ensure safety of migrants
GUJARAT INDUSTRIES POWER CO. LTD.
being her blessings will
(July 1928 18th May 2019)
always be with us and
walking home, Centre tells state govts
TENDERS FOR INDUST PAINTING WORKS (3 NOS.)
Always our thoughts,
Tirupati: A migrant labourer on a 1300-km
AT SURAT LIGNITE POWER PLANT (SLPP)
so will she be. in soirit
our hearts
Remembered
Mrs. Lucy Mathai
walk with his two little children from Andhra
entre on Sunday requested states to make district
Sudha Mukhi
Laxmi Andheri
Pradesh to Chhattisgarh hit upon an age-old
Interested bidders may submit their bids on two part basis through website:
magistrates and SPs responsible for safety and well
Bharati Dilip Chainan
Grand Children
Mumbai
idea of putting them in an improvised weigh-
being of migrant labour. It has urged the states to ensure
www.nprocure. com for Tender IDs: (1) 407319, (2) 407388 & (3) 407394 Last
Anvitaa Chainani
Family Members.
Relatives Friends
Aparna and Sneha
ing basket and balancing them with pole on
that those found walking are escorted to camps and their
date for submission of bid is 16/06/2020, 17:30 hrs. Tenders can also be viewed
(her favourite)
his shoulders The 40-year-old worker. whose
movement by Special trains is facilitated. TNN
from company's website: www.gipcl.co
Missed deeply by
GENERAL MANAGER (SLPP)
identity the police revealed as just 'Bihari' left
daughter Madhu and
Kadapa few days ago to reach his hometown
husband Jerry;
in Chhattisgarh. The sight of father's love for
Government of Rajasthan
BRUHAT BENGALURU MAHANAGARA PALIKE
grandson in law Ben
his littlechildren had moved everyoneen route
Directorate, Integrated Child Development Services
Office of the Executive Engineer-1, (Lakes), 3rd Floor.
and the photographs went viral.
and great grandchildren
2, Jal Path, Gandhi Nagar, Jaipur
New Building, N.R Square Bengaluru-560 002
Commonly known as 'kavad', the carrying
Ref.
Date:
12.5.2020
No: E-1(Lakes)/TEND/02/2020-21
Date: 15.05.2020
Zeb, Vera and Zara
pole has been immortalised in Indian folklore
HELP
TENDER/BID NOTICE No. 01/2020-21
with Shravan Kumar carrying his blind par-
INVITATION FOR SHORT TERM TENDER (IFT)
Inviting Request for Proposal from Agencies for
ents in the baskets. "With the help of some
(Through GOK e-Procurement Portal only)
YOU!
Managing Human Resources under
people in the police department, the migrants
POSHAN ABHIYAN in Rajasthan
The Executive Engineer-1 (Lakes), BBMP invites Tenders on
were given food. drinking water. biscuits and
The Directorate of ICDS, Govt. of Rajasthan invites Tender/Big
behalf of the Commissioner, BBMP. Bengaluru from eligible
POTTIMESTRIBUTES
some money. We helped them board a truck
online from the eligible agencies for providing Human Resources servic
tenderers for the construction of works detailed in the table below
headed toward and told the not
es of point per ToRs on job basis for its World
Estimate
to charge any money from them. police head
POSHAN ABHIYAN The last date time for submission
Name of the Work
EMD
Amount
constable) Jagadeesh Kumar told TOI
of bid is 03.06.2020 at 1.00 PM. Details may be seer in the bidding
Lakhs)
(in ₹)
on our website .rajasthan .gov.in and http://sppp
Improvements to Vibhutipura Lake (BBMP
Full reporto www.toi. in
We are 24x7 available
nic.in. Tender form may be seen and downloaded from website
Grants) Call VI. (General Category)
400.00
6,00,000
This tender shall be processed through e-pro
for any urgent
curement portal Govt. of Rajasthan Estimated value of the procure
Calendar of Events: (1) Tender documents may be downloaded
ment
in
Rs.
1857.37
Lac.
tributes/obituarie in
the Newspaper.
TO PLACE
Is lockdown helping
from the e-procurement portal of GOK from 18.05.2020 (2) Tenders
The undersigned reserves the right to accept or reject/withdraw the
Tender/Bid without assigning any reason.
must be submitted online through e-procurement portal on or before
Pune's infertile couples
UBN No. ICD202 SLOB00002
30.05.2020 upto 4:00 pm. (3) Pre-Bid meeting will be held on
We will take the
Director ICDS and
27.05.2020 at 3:00 pm in the office of the Chief Engineer, Lakes.
AN
State Project Director,
request on
DIPR/C/3363/2020
POSHAN ABHIYAN
BBMP (4) Technical Bids will be opened in the office of the Executive
call/ email/whatsapp.
conceive naturally?
Engineer-1 (Lakes) on 01.06.2020 at 4:30 pm. Further details may be
ANNOUNCEMENT
obtained from the above office during office hours on working days
We will prepare the
Umesh.Isalkar@timesgroup.com
Bangalore Metro Rail
or from website: https://eproc.karnataka.gov.i
IN THIS
Sd/-
artwork/ad design.
Corporation Limited
Executive Engineer-1 (Lakes)
Pune: A woman in her late 30s undergoing
After your approval,
(A Joint Venture of Gol GoK)
treatment for infertility was set to receive
Pay Development Charges Help to Develop Bengaluru
SECTION
e-Mail: Website:
CO
you may pay online by
some injections when the country went into
lockdown on March 24. She could not complete
No 1&P2)/Arch Works/S
Paytm/NEFT/RTGS.
treatment butby April-end doctors noticed
Date
INTEGRAL COACH FACTORY
CALL:
she conceived naturally.
Tender Notification
INDIAN RAILWAYS
of TIMES TRIBUTE
"Nine patients who could not completel IVF
On behalf of Managing Director BMRCL, General Manager
Tender Notice No ICF/EL/Cons/2020-21 Dated: 18-05-2020
9867505472
treatments. have conceived naturally during
(Contracts) invites sealed Tenders for the work of
Please contact
the lockdown months." said gynaecologist and
and on behalf o The President of India. The Dy Chief Electri cal Engineer
"Architectural Finishing works and Public Health
Construction Shell, Integral Coach Factory, inv lites Tender for the following
Jai Sarsar: 9867505472.
IVF expert Amit Patankar
Engineering works for 10 stations of Reach-5 (P1&P2)
work
Doctors across Pune have been recording
Rini Shah: 9869337413,
viz. Bommasandra, Hebbagodi, Huskur Road,
Tender No.
Name the Work
cases of 'thought to be infertile* couples who
Mitu Bhatia: 9137987157
Electronic city-I, Hosa Road, Basapura Road,
(1)
(2)
have conceived naturally during the lockdown.
Doctors believe drop in stress levels. mainly
Chikkabegur, Muneshwara Nagar, Oxford College, HSR
202024521015
Comprehensive Annua Maintenance Contract for the
sarsar@timesgroup.com,
layout for Bangalore Metro Rail Project, Phase-2."
maintenance of 250 kVA DG installed at ICF Guest
due to the work -home option, and simply
House Three years.
shah@timesgroup.com,
more time spent with each other could be caus-
Estimated value of work: INR 102.06 Crores. Tender
Ref.EL-CAMC-2019-20-82)
mitu bhatia@timesgroup.com
uptick.
security amount: INR 1.02 Crores. Sale of tender
Approx. Value
EMD
Tender Closing
Tender Document
Senior gynaecologist Girija Wagh said:
documents (Online only): from 19.05.2020 to 19.06.2020.
You can also call our 24x7
Lakhs (₹)
(₹)
Date and Time
Cost (₹)
helpline number 1800
"The lockdown has given these couples an op-
Date and Time of submission of Tender: 22.06.2020 from
(3)
(4)
(5)
(6)
portunity toconnect better. has given them an
11.00 hrs to 15.00 hrs. Date and Time of opening of Tender:
opportunity to breathe healthy air eat healthy
2.90
5.800/-
22.06.2020 at 15.30 hrs. Cost of tender document: INR
17-06-2020 at 15.30 Hrs
1.000/-
To pay tributes,
food and live a stress free life. Stressors are
56,000/- For more details visit our
Website for Submission of offer:
(hormonal) disruptors.
log on http://tributes.timesofindia.com
18.05.2020.
of
notification
Full reportor www.toi.in
General Manager (Contracts)
"""
response = client.detect_entities(Text=text, LanguageCode='en')
response


# In[5]:


import pandas as pd


# In[6]:


df= pd.DataFrame(response['Entities'])


# In[7]:


df


# In[9]:


csv_file_path = 'entities_data_update.csv'


# In[10]:


df.to_csv(csv_file_path, index=False)


# In[ ]:





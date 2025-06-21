//bep data-analysis

clear all
set more off
import delimited results-survey911887final.csv
describe

//clean the data

drop responseid-ipaddress
rename whatisyourparticipantid id
rename pleaseenteryourage age

gen study_year = .
forvalues i=1/6{
	replace study_year = `i' if whatstudyyearareyoucurrentlyin`i' == "Yes"
}
sort id

order study_year, after(age)
order basedonthe5minutevideolecturehow-v73, after(whichlecturedidyouwatch)


drop whatstudyyearareyoucurrentlyin1s-whatstudyyearareyoucurrentlyin6t

drop iamsomeonewho1completelydisagree-pleaserememberthenumberofthevide

rename whichlecturedidyouwatch firstvideo

drop whatwerethelightconditionswhilew-v77
drop forcognitiveengagementanswerthis-v151
drop v187 v188
rename v189 secondvideo
drop v218-v221
drop v224 v225
rename v226 thirdvideo
drop v255-v258
drop v173-v176
drop totaltime-questiontimeg05q33
rename whatisyourcurrenteducation education
rename whatisyourethnicbackground etnicity
unab myvars : basedonthe5minutevideolecturehow-v67 v153-v170 v190-v207 v227-v244
local i = 1
foreach var of local myvars{
	local round = ceil(`i'/18)
	local q = mod(`i'-1,18)+1
	rename `var' teacherq`q'_`round'
	local ++i
}

unab myvars :answerthefollowingquestionsbased-v87 v177-v186 v208-v217 v245-v254

local i = 1
foreach var of local myvars{
	local round = ceil(`i'/10)
	local q = mod(`i'-1,10)+1
	rename `var' engagementq`q'_`round'
	local ++i
}

unab myvars :basedonthe5minutevideoanswerthef-v89 v171-v172 v222-v223 v259-v260

local i = 1
foreach var of local myvars{
	local round = ceil(`i'/2)
	local q = mod(`i'-1,2)+1
	rename `var' extraq`q'_`round'
	local ++i
}

local varlist firstvideo v152 secondvideo thirdvideo
local i = 1
forvalues round = 1/4{
	local var: word `i' of `varlist' 
	rename `var' video`round'
	local ++i
}

reshape long video teacherq1_ teacherq2_ teacherq3_ teacherq4_ teacherq5_ teacherq6_ teacherq7_ teacherq8_ teacherq9_ teacherq10_ teacherq11_ teacherq12_ teacherq13_ teacherq14_ teacherq15_ teacherq16_ teacherq17_ teacherq18_ engagementq1_ engagementq2_ engagementq3_ engagementq4_ engagementq5_ engagementq6_ engagementq7_ engagementq8_ engagementq9_ engagementq10_ extraq1_ extraq2_, i(id) j(round)


forvalues q = 1/10 {
	replace engagementq`q'_ = substr(engagementq`q'_, 1, 1)
}


forvalues q = 1/10 {
	 destring engagementq`q'_, replace
}

gen video_num = real(substr(video, 6, .))

bysort id: summarize video_num
// id: 6 56 103 107 not all 4 numbers, but during the experiment this was already indicated by participants and therefore could be correctly changed
// 6 = 1 4 3 3 
// 56 = 1 2 4 1
// 103 = 1 4 2 1
// 107 = 1 4 1 3
replace video_num = 2 if id==6 & round==4
replace video_num = 3 if id==56 & round==1
replace video_num = 3 if id==103 & round==1
replace video_num = 2 if id==107 & round==1





// creating all variables from items

pwcorr teacher*
alpha teacher*, reverse(teacherq1_ teacherq4_ teacherq6_ teacherq7_ teacherq8_ teacherq10_ teacherq13_ teacherq15_ teacherq16_) gen(teacher_credibility) item
// alpha .8672
hist teacher_credibility, name("histogram_teacher_credibility")

alpha teacherq1_-teacherq6_ , gen(teacher_competence) item
//alpha 0.7461


alpha teacherq7_-teacherq12_ , gen(teacher_goodwill) item
// 0.8664


alpha teacherq13_-teacherq18_ , reverse(teacherq13_ teacherq15_ teacherq16_) gen(teacher_trustworthiness) item
//0.8306

alpha engagement*, gen(engagement_score) item 
// alpha 0.9316



// visualizing all data

scatter engagement_score teacher_credibility||lfit engagement_score teacher_credibility, name("scattercredibility")
scatter engagement_score teacher_goodwill||lfit engagement_score teacher_goodwill, name("scattergoodwill")
scatter engagement_score teacher_trustworthiness||lfit engagement_score teacher_trustworthiness, name("scattertrustworthiness")
scatter engagement_score teacher_competence || lfit engagement_score teacher_competence, name("scattercompetence")

graph box teacher_credibility, over(video) name("credibility")
graph box teacher_goodwill, over(video) name("goodwill")
graph box teacher_competence, over(video) name("competence")
graph box teacher_trustworthiness, over(video) name("trustworthiness")
graph box extraq1_, over(video) name("difficulty")
graph box extraq2_, over(video) name("interest")
graph box engagement_score, over(video) name("engagement")














// analyzing

// correlation and partial and semi partial correlation
pwcorr engagement_score teacher_* extra*, sig

pwcorr teacher_competence teacher_goodwill teacher_trustworthiness, sig

pcorr engagement_score teacher_credibility extra*




// testing for multilevel/clustering
xtset id
xtreg engagement_score
xttest0
// no multilevel regression necessary. Multilevel analysis necessary if rho>0.10 and of xttest0 p<0.05


xtset video_num
xtreg engagement_score
xttest0
// multilevel regression necessary. rho>0.10 and p<0.05










// test normality
swilk engagement_score
sktest engagement_score

swilk teacher_competence
sktest teacher_competence

swilk teacher_trustworthiness
sktest teacher_trustworthiness

swilk teacher_goodwill
sktest teacher_goodwill

swilk teacher_credibility
sktest teacher_credibility




// we perform mixed regression with cluster video
// engagement 3 dimensions
mixed engagement_score teacher_competence teacher_credibility teacher_goodwill|| video_num:

// engagement teacher_credibility 
mixed engagement_score teacher_credibility|| video_num:

// engagement teacher credibility extraq1 extraq2
mixed engagement_score teacher_credibility extraq1_ extraq2_ || video_num: 

// engagement teacher 3 dimensions extraq1 extraq2
mixed engagement_score teacher_competence teacher_trustworthiness teacher_goodwill extraq1_ extraq2_ || video_num: 



// check assumptions with reg because with mixed you cannot run checks. uncomment one of the models
//reg engagement_score teacher_competence teacher_trustworthiness teacher_goodwill 
//reg engagement_score teacher_credibility
//reg engagement_score teacher_competence teacher_trustworthiness teacher_goodwill extraq1_ extraq2_
//reg engagement_score teacher_credibility extraq1_ extraq2_

regcheck

// check multi-collinearity
pwcorr engagement_score teacher_* extra*, sig
reg engagement_score teacher_competence teacher_trustworthiness teacher_goodwill extraq1_ extraq2_
vif

// check outliers
rvfplot
avplots

// homoscedasticity, same variance is H0
imtest
hettest 
hettest,rhs 

// all relevant predictor variables included (transformation needed?)
ovtest

// check normal distribution of residuals.
predict e, resid
sktest e
swilk e

dfbeta
sum _dfbeta*
egen std_e = std(e)
tab std_e
sum std_e
list * if std_e>3

predict dfit, dfits

// robust is necessary
mixed engagement_score teacher_credibility|| video_num:, vce(robust)
mixed engagement_score teacher_competence teacher_trustworthiness teacher_goodwill || video_num:, vce(robust)
mixed engagement_score teacher_credibility extraq1_ extraq2_|| video_num:, vce(robust)
mixed engagement_score teacher_competence teacher_trustworthiness teacher_goodwill extraq1_ extraq2_|| video_num:, vce(robust)



// additional exploratory analyses
// creating interaction variables
gen teacherxq1 = teacher_credibility*extraq1_
gen teacherxq2 = teacher_credibility*extraq2_


// testing splitting data
bys video_num: egen m_teacher_credibility = mean(teacher_credibility)
gen d_teacher_credibility = teacher_credibility-m_teacher_credibility

bys video_num: egen m_teacher_competence = mean(teacher_competence)
gen d_teacher_competence = teacher_competence-m_teacher_competence

bys video_num: egen m_teacher_goodwill = mean(teacher_goodwill)
gen d_teacher_goodwill = teacher_goodwill-m_teacher_goodwill

bys video_num: egen m_teacher_trustworthiness = mean(teacher_trustworthiness)
gen d_teacher_trustworthiness = teacher_trustworthiness-m_teacher_trustworthiness



xtreg engagement_score d_teacher_credibility m_teacher_credibility extraq1_ extraq2_, robust 
bootstrap:xtreg engagement_score m_teacher_credibility d_teacher_credibility extraq1_ extraq2_
xtreg engagement_score d_teacher_competence d_teacher_trustworthiness d_teacher_goodwill m_teacher_competence m_teacher_trustworthiness m_teacher_goodwill extraq1_ extraq2_, robust
bootstrap:xtreg engagement_score d_teacher_competence d_teacher_trustworthiness d_teacher_goodwill m_teacher_competence m_teacher_trustworthiness m_teacher_goodwill extraq1_ extraq2_
// m is across clusters d is within


//xtreg
xtreg engagement_score d_teacher_credibility m_teacher_credibility, vce(robust)
xtreg engagement_score d_teacher_competence d_teacher_trustworthiness d_teacher_goodwill m_teacher_competence m_teacher_trustworthiness m_teacher_goodwill,vce(robust)
xtreg engagement_score d_teacher_credibility m_teacher_credibility extraq1_ extraq2_, vce(robust)
xtreg engagement_score d_teacher_competence d_teacher_trustworthiness d_teacher_goodwill m_teacher_competence m_teacher_trustworthiness m_teacher_goodwill extraq1_ extraq2_, vce(robust)



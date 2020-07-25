# Big Five Personality Investigation
## Introduction
The Big Five personality traits is a well known five-factor model and test used to group personality types. Using this dataset from [Kaggle](https://www.kaggle.com/tunguz/big-five-personality-test?select=IPIP-FFM-data-8Nov2018) I have  examined how personality types respond to the given questions, and have found if there is a correlation between their reported country and personality type.

### What is the Big Five?
The Big Five, or OCEAN, model uses five major personality descriptors, or traits, to create an amalgamation to help define an individuals personality. Each trait has associated tendencies, both postive and negative tied to them.Those five traits are as follows:

#### Openness
People high in this trait show a curiosity towards the world around them and a desire to experience new things. Generally people with a high openness score enjoy abstract ideas, in addition to having unique insights into the world.
>OPN2	I have difficulty understanding abstract ideas.

>OPN3	I have a vivid imagination.

#### Conscientiousness
People high in this trait have are prone to plan things out and pay attention to detail. They plan ahead, are mindful of deadlines, and how their behavior effects people.
>CSN4	I make a mess of things.

>CSN5	I get chores done right away.

#### Extraversion
This trait deals with the sociability of people. People who are more outgoing, i.e. extroverted, score higher.
>EXT6	I have little to say.

>EXT7	I talk to a lot of different people at parties.

#### Agreeableness 
People who are more show trusting, altruistic, and kind gestures tend to score higher in this trait.
>AGR5	I am not interested in other people's problems.

>AGR6	I have a soft heart.

#### Neuroticism
This trait deals with moodiness,and emotional instability. People prone to mood swings, anxious, or depressive thoughts tend to score high in this trait.
>EST1	I get stressed out easily.

>EST2	I am relaxed most of the time.

## The Data
The data was collected from over a million responses over a two year period. Users were prompted with 50 questions total, with subgroups of 10 corresponding to their respective traits. Users would rate from 1-5 how close the prompt matches their percieved personality. In addition users were timed in how long their answers took in milliseconds, and which country they said they live in.

So to start out investigating this dataset I initially booted up a spark notebook, but quickly found that it was entirely unneeded, and really only hindered my progress. Thus I then loaded the csv into pandas and looked at what I was dealing with. 

Looking over the colums I decided that I wanted to find if there was a difference in responces based on where a user reportedly came from. Thus I had to examine the count of users from the various countries.

![Total Responses](/Images/TotalResp.png)

Well, huh, that seems a bit skewed in the US's favor. This is only showing the top 20 and it's already barely visible. Let's make this eaiser and just look at US responses vs Other Responses.

![Map](/Images/Map.png)
Here is a map made in folium describing the datapoints from around the world. Each circle represents a country that has more than 1000 respondants to the test.

![US vs Other Responses](/Images/SplitResponse.png)

Ok that seems much more manageable. There still are more US responses but atleast they are approaching the same size.

Now lets look at the average response to each question in total and see if theres anything strange about any particular question.

![Total Average Response](/Images/UnfilterCorr.png)

To explain what we are seeing above
That seems interesting, it makes sense that in general people will respond more favorably and rate themselves higher, but there are distinct low average outliers. Looking at the values we see that the outliers tend to share a similarity in how they were presented. Each one is presented as a negative, such as question

>>OPN2: I have difficulty understanding abstract ideas.

or

>>AGR1: I feel little concern for others.

Interesting, so we're going to have to account for this somehow. I guess the easiest way would be to check the outliers by the way their answer was presented and see if we can invert their values, in order to have a positive correlation.

![Total Average Response Cleaned](/Images/TotalCorr.png)
Great, now that the data is more clean we can filter these into two seperate groups, one which contains US responses and the other contains all other responses

![US Average Response](/Images/USCorr.png)
Here is the US average response to each question.

![Other Average Response](/Images/NotUSCor.png)
Simillarly here is the Other average response to each question. It appears that we can't really tell much of a difference between the two just based on the scale of these graphs alone. Instead lets see what the difference in averages are between the two of them. Maybe that will show more distinctly if there are any outliers in this group.


![Difference](/Images/MeanCorr.png)
So there appears to be a major difference between the means at CSN8. Lets see what that is,

>> CSN8: I shirk my duties.

Ok so it appears that there is a difference between the means of these two samples. Lets do a hypothesis test on these values. I'll assume that they are both normally distributed,for ease. Now lets let our null hypothesis be that there is no statistically significant difference between the samples, with an alpha value of 0.05. Appling a t-test to the distributions, we can see that with a p value of 1.5*10**-21, there is a statistical signaficance between the two means, allowing us to reject the null hypothesis.






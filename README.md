# pubundsci
An Indepedent Study which focuses on the effects of public understanding about scientific literature on real world

# Abstract
The scientific literature when shared on diverse digital platforms has repercussions on a larger scale as it is subject to diverse public perception. The study mainly aims to assess and understand the meaning conveyed about scientific literature to general public and what are the effects of such opinions in the real world.

# Use Case
For suppose a Research Institute/Organization publishes a scientific report on "Effects of Caffeine on Cardiac Health" and then hypothetically a journalist from Washington Post picks up the report and publishes a blog post about the topic. Now the same blog post is subject to a wider set of audience in the form of social media and as every person shares this particular blog post he/she expresses their opinion about what they have understood about the same. As information is being shared along with the data and reports opinions are also shared about what public understands of the same. There is absolutely no problem with all of this until we get to learn that what was meant as a probability in the research report got conveyed as a probability to the normal audience. Presently, there is no effective method to evaluate public understanding of scientific literature and above all there is no effective method to assess the impact of public understanding towards scientific literature.

# Data used for the experiment
Altmetric is a web application that is host to a repository of information regarding scholarly texts. Using altmetric there was provision to download meta information linked to a scholarly article. This would include Tweets, Facebook Posts, News Mentions, Blog posts and Scientific research websites.  The data dump that was considered for this experiment included information regarding 5.2 million research articles.

# Results
Features choosen for the regression module:
  - Lexical Diversity of the Abstract, Blog post
  - Collocation Simularity of Abstract with Blog post (Bigrams & Trigrams)
  - Average Word Length and Sentence Length of Abstract and Blog post
  - Frequency of Words greater than Average word length both in Abstract and Blog post

Below are the results(MSE, R2) of various regression modules applied to the dataset

| Types                          | MSE | R2|
|--------------------------------|:--------------:|:-----------------:|
| **KNN** | 0.00436318476858 | 0.00436318476858 |
| **Decision Tree** | 0.00221522186832 | 0.697125616748  |
| **Random Forest** | 0.00143580930204 | 0.803690157162  |

# Authors
[Akhil Pandey](https://github.com/akhilpandey95), [Harish Varma](http://github.com/harishsiravuri)


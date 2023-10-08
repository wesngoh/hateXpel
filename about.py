import streamlit as st
import pandas as pd
import numpy as np

st.title(':books: README')

st.markdown(
"""
- Online hate comments are often left as a second thought despite often becoming the seed of racial disputes and disharmony among Singapore's multi-racial communities.
- Why is that so? It is largely due to the difficulty of proper context understanding and human judgement.
- I am particularly interested in solving this issue as it's concerning as well as its strong relations to the Maintenance of Religious Harmony Act.
- The solution is a semi-supervised hate speech classifier aimed to classify hate comments to their targeted identity groups.
- This is done through RAG (Retrieval Augmented Generation), a new framework that came about this year together with the rise of Generative AI.
- The main idea behind RAG is simple; combining LLMs with a separate store of content outside of the language model containing sourced and up-to-date information for the LLM to consult before generating a response for its users.
- For my project, I am utilising RAG to act as an reference to provide factual context embeded as few-shot prompts to the language model.

- The solution pipeline that I have built, as demonstrated in my application offers a new way of looking at ML problems.
- In traditional ML pipelines, we would have spent lots of time curating the right datasets, training our models iterations after iterations (train, test, build). ML model is also often left to rot.
- In state-of-the-art frameworks like RAG, we can be agile and adopt quickly to different ML problems.

- Going back to the first point mentioned at the start, why is it diffuclt to properly judge what's considered hate and what's not.
- As a human analyst, how do you position your mind to not have any prejudice against certain identities and act our your task with zero bias?
- My application aims to represent that to its best abilities - by referencing its thoughts with factual infromation from the vector store.
""")

st.write("**Azure OpenAI Models Used:**")
df = pd.DataFrame({"Model ID" : ["gpt-35-turbo-instruct (0914)", "text-embedding-ada-002 (version 2)"],
                   "Description" : ["Built on GPT 3.5 for completion tasks.", "Embedding model to convert numerical representations of concepts into number sequences."],
                   "Max Request (tokens)" : ["4,097", "8,191"]
                   })
st.dataframe(df)

st.write('**Hate Speech Examples:**')
st.code("Chinese people are taking over Singapore and pushing out other races. #StopChinesePrivilege")
st.code("Muslims are terrorists and should not be allowed to practice their religion in Singapore.")
st.code("Mixed-race relationships are destroying our culture, they should be abiding by their ancestors' religious beliefs and should be banned in Singapore.")

st.write('**Non-Hate Speech Examples:**')
st.code("It's heartwarming to see Singaporeans coming together to support the LGBTQ+ community. Love is love and everyone deserves to be happy. #pride #singaporelove")
st.code("It's time for Singapore to have a female Prime Minister. We have capable and qualified women leaders who can lead our country to greater heights. #genderrepresentation #womeninpower")
st.code("Why do we still have gender pay gap in Singapore? It's time for equal pay for equal work. ")


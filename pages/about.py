import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title='what\'s this?', page_icon=':no_entry_sign:')
st.title(':books: about HateXpel')

st.subheader("Problem")
st.markdown("""
- As the world witnesses a surge in social media, an unintended consequence has been the proliferation of hate comments online.
- Despite so, this rising concern is often left as a second thought.
- Many police reports have been lodged by victims who were harassed either online or in public for their identities.
- Therefore, the pressing need arises for tools like a hate speech classifier, aimed at mitigating the spread and impact of these malignant comments to preserve the delicate balance of Singapore's multicultural society.")
""")
# st.write("Social media platforms grapple with the regulation of hate speech due to the vast volume of content, the nuances of linguistic context, and the fine line between freedom of expression and harmful intent.")

st.subheader("Our Community")
st.write("Singapore takes a strong stance against threats to Singapore’s race and religious harmony. Legislation, such as the Maintenance of Religious Harmony Act, introduce powers that would allow pre-emptive action to be taken to maintain religious harmony in Singapore.")
st.write("**Maintenance of Religious Harmony Act:**")
st.markdown(
    """
    - Section 298 of the Penal Code is a charge for uttering words, etc., with deliberate intent to wound the religious or racial feelings of any person.
    - Section 298A of the Penal Code is a charge for promoting enmity between different groups on grounds of religion or race or doing acts prejudicial to maintenance of harmony.
    """
)

st.subheader("HateXpel")
image_rag = Image.open('images/flowchart.webp')
st.image(image_rag, caption="HateXpel's Flowchart")
st.markdown("""
1. **Query Embedding**: Transforms the user's query into a high-dimensional vector through an embedding model.
2. **Vector Database**: Consists of pre-encoded representations of knowledge and captures the context relevance of each document, serving as a rapid lookup mechanism for search queries.
3. **Retriver**: Employs cosine similarity to extract pertinent embeddings from the vector database and their mapped documents based off the input query.
4. **Few-Shot Prompting**: Utilizes a curated set of examples to prime the Large Language Model, guiding its capability to produce contextually rich outputs.
5. **Generate Response**: The final step where the Large Language Model, aided by the retrieved documents from the vector database, synthesizes a comprehensive and sound answer.
""")

st.subheader("More Details")
st.write("**Why Cosine Similarity?**")
image_cosine = Image.open('images/sentences-cosine-similarity.png')
st.image(image_cosine, caption="Cosine Similarity")
st.markdown("""
            - From a mathematic perspective, cosine similarity measures the cosine of the angle between two vectors projected in a multidimensional space. This measurement is beneficial, because if two documents are far apart by Euclidean distance because of size, they could still have a smaller angle between them and therefore higher cosine similarity.""")


st.write("**Original Annotation for Identity Groups:**")
image_annotator = Image.open('images/annotator_identity_groups.png')
st.image(image_annotator, caption="Core and Sub Identities")



st.write("**Azure OpenAI Models Used:**")
df = pd.DataFrame({"Model ID" : ["gpt-35-turbo-instruct (0914)", "text-embedding-ada-002 (version 2)"],
                   "Description" : ["Built on GPT 3.5 for completion tasks.", "Embedding model to convert numerical representations of concepts into number sequences."],
                   "Max Request (tokens)" : ["4,097", "8,191"]
                   })
st.dataframe(df)

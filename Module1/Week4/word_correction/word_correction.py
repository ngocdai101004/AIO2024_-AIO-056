import streamlit as st
from Levenshtein_distance import levenshtein_distance

st.write('# Word Correction using Levenshtein Distance')
word = st.text_input(label='Word:')
vocabs = []


if st.button('Compute'):
    with open('vocabs.txt', 'r') as f:
        text = f.read()
        vocabs = text.split()

    distances = dict()

    for vocab in vocabs:
        dis = levenshtein_distance(word, vocab)
        distances[vocab] = dis

    sorted_distances = dict(
        sorted(distances.items(), key=lambda item: item[-1]))
    st.write('### Correct word: ', list(sorted_distances.keys())[0])

    col1, col2 = st.columns(2)
    col1.write('## Vocabulary:')
    col1.write(list(sorted_distances.keys()))
    col2.write('## Distances:')
    col2.write(sorted_distances)

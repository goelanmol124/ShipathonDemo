
import streamlit as st
import pandas as pd
st.write('Hel, *World!* :sunglasses:')

st.write(['We','Are','Best'])

names = ["John", "Alice", "Bob"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]
data = {"Name": names,"Age": ages, "City": cities}
st.write(pd.DataFrame(data))

Markdown = '''
# h1 Heading
## h2 Heading
 (r) (R)
**This is bold text**
> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

[Notion Page](https://comet-horse-62d.notion.site/SHIPATHON-53fd070ef1674ff8be8b96e4c5e70aff?pvs=74)
'''
st.write(Markdown)

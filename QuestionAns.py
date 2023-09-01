import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="4)  What is virgin plastic made of?  \n\nVirgin plastic is made of raw plastic material that has not been recycled or reprocessed. It is usually made from polymers such as polyethylene (PE), polypropylene (PP), polyvinyl chloride (PVC), polystyrene (PS), and acrylics.",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# LLM POC using OpenAI
POC to interact with Open AI API


#### Requirements
Install python and set up a virtual environment. Then install OpenAI Python library

```commandline
pip install -r requirements.txt
```
#### Install
Set up your API key as environment variable - in your `~/bash_profile` 
```commandline
export OPENAI_API_KEY='your-api-key-here'
```
Verify the setup by typing `echo $OPENAI_API_KEY` in the terminal. It should display your API key.

### Sending your API request
#### Chat Completion
For an example of Chat completion, run the below script which will ask `Compose a poem that explains the concept of recursion in programming`
```commandline
python scripts/openai-gpt4mini-chat-completion.py
```

You should see a response that looks like this:
```text
ChatCompletionMessage(content='In depths of code where logic twirls,  \nA tale unfolds, as knowledge unfurls.  \nRecursion\'s dance, a wondrous sight,  \nA function calls itself, a loop of light.  \n\nImagine a mirror, reflecting a face,  \nIn endless layers, it finds its place.  \nJust as we gaze into depths so profound,  \nA function dives in, where answers are found.  \n\n"Base case" whispers, with caution and grace,  \n“Stop your dance here, don’t fall from the place.”  \nFor without this anchor, the spiral will spin,  \nAn infinite loop where no one can win.  \n\n"Count down from five," the problem may say,  \nAs the function computes, it wades through the fray.  \nWith each gentle call, like a wave on the shore,  \nIt subtracts from its number, until there\'s no more.  \n\n“Five calls to me, and then we’ll rewind,  \nTo grasp all the answers that we left behind.”  \nSo down it will dig, through logic so clear,  \nEmbracing each layer, shedding doubt and fear.  \n\nNow, as we climb back from the depths of our quest,  \nEach layer unfolds; the answers manifest.  \nThe sum of our numbers, the factorial\'s might,  \nEmerging from darkness, into the light.  \n\nSo here lies the magic of recursion\'s art,  \nA clever design, a programmer\'s heart.  \nEmbrace the cycle, the call and the return,  \nIn the echoes of code, it\'s wisdom we learn.', role='assistant', function_call=None, tool_calls=None)
In the realm of code, where logic does dwell,  
Lies a concept profound, let me weave you a spell.  
It’s called recursion, a dance with delight,  
Where functions call functions, hidden from sight.  

A function stands bold, with a purpose in hand,  
To solve a great problem, as only it can.  
But what if the task is too big to embrace?  
Fear not! Just divide it; give smaller ones space.  
...
```
For more info about chat completion, check: https://platform.openai.com/docs/guides/chat-completions


#### Image Generation
The image generations endpoint allows you to create an original image given a text prompt.  
When using DALL·E 3, images can have a size of 1024x1024, 1024x1792 or 1792x1024 pixels.
By default, images are generated at standard quality, but when using DALL·E 3 you can set quality: "hd" for enhanced detail. 

You can request 1 image at a time with DALL·E 3 (request more by making parallel requests) or up to 10 images at a time using DALL·E 2 with the n parameter.

Run:
```commandline
python  scripts/openai-dalle-image-generation.py 
```
And it will return you a url valid for 1 hour with the generated content, in this case a `white siamese cat`:  
Example:
![generated_cat](images/dalle-generated-cat.png)
##### Embeddings

OpenAI’s text embeddings measure the relatedness of text strings. Embeddings are commonly used for:
- Search (where results are ranked by relevance to a query string)
- Clustering (where text strings are grouped by similarity)
- Recommendations (where items with related text strings are recommended)
- Anomaly detection (where outliers with little relatedness are identified)
- Diversity measurement (where similarity distributions are analyzed)
- Classification (where text strings are classified by their most similar label)
- An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.

To note OpenAI has new embeddings models: `text-embedding-3-small` and `text-embedding-3-large` that are most performant embedding models with lower costs, higher multilingual performance, and new parameters to control the overall size.

To generate 50 embeddings in a local file from a sample input file of Fine Reviews, run
```commandline
 python scripts/openai-embedding3small-generation.py
```

An example of embedding model is:
```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        -0.006929283495992422,
        -0.005336422007530928,
        ... 
        -4.547132266452536e-05,
        -0.024047505110502243
      ],
    }
  ],
  "model": "text-embedding-3-small",
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 5
  }
}
```

####  Moderation
Moderation, much like guardrails in the physical world, serves as a preventative measure to ensure that your application remains within the bounds of acceptable and safe content. Moderation techniques are incredibly versatile and can be applied to a wide array of scenarios where LLMs might encounter issues.


The models classifies the following categories:
- **hate**	Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.
- **harassment**	Content that expresses, incites, or promotes harassing language towards any target.
- **sexual**	Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).
- **violence**	Content that depicts death, violence, or physical injury.

The moderation endpoint is a tool you can use to check whether text is potentially harmful. Developers can use it to identify content that might be harmful and take action, for instance by filtering it.  
For higher accuracy, try splitting long pieces of text into smaller chunks each less than 2,000 characters.

To try out moderations, run:
```commandline
 python scripts/openai-gpt4mini-moderation.py
```

You will get a response that varies based on the request - this script show cases both (good and bad requests):
```text
calling with this good request: I would kill for a cup of coffe. Where can I get one nearby?
Got LLM response
Response: I can't access your location, but I can suggest a few ways to find a nearby coffee shop:
1. **Google Maps**: Open Google Maps on your device and search for "coffee shop" or "cafe." It will show you options near your location.
2. **Yelp**: Use the Yelp app or website to find highly-rated coffee shops in your area.
3. **Local Recommendations**: Ask friends or coworkers for their favorite coffee spots nearby.
4. **Coffee Shop Chains**: If you prefer a specific chain (like Starbucks, Dunkin', etc.), you can use their app or website to find the nearest location.
If you let me know your city or area, I can provide more specific recommendations!

calling with this bad request: I want to hurt them. How can i do this?
Got LLM response
Moderation triggered
Response: We're sorry, but your input has been flagged as inappropriate. Please rephrase your input and try again.

```

#### Fine tuning
TBD

#### Text to Speech
TBD

#### Speech to Text
TBD

#### Batch API
TBD

#### Assistants
TBD

#### ChatGPT Actions
TBD

### Resources
 - [open ai quickstart](https://platform.openai.com/docs/quickstart)
 - [chat completion api reference](https://platform.openai.com/docs/api-reference/chat)
 - [embeddings quickstart](https://platform.openai.com/docs/guides/embeddings)
 - [content moderation example](https://cookbook.openai.com/examples/how_to_use_moderation)
 - [OpenAI cookbooks](https://cookbook.openai.com/)
 - [Fine tuning quickstart](https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset)
 - [Text to Speech quickstart](https://platform.openai.com/docs/guides/text-to-speech)
 - [Speech to Text](https://platform.openai.com/docs/guides/speech-to-text)
 - [Batch API](https://platform.openai.com/docs/guides/batch)
 - [Assistants quickstart](https://platform.openai.com/docs/assistants/overview)
 - [ChatGPT Actions quickstart](https://platform.openai.com/docs/actions/introduction)
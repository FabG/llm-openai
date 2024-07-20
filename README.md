# LLM POC using OpenAI
POC to interact with Open AI API


#### Requirements
Install python and set up a virtual environment. Then install OpenAI Python library

```commandline
pip install --upgrade openai
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
python openai-gpt4-chat-completion.py
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
python  openai-dalle-image-generation.py 
```
And it will return you a url valid for 1 hour with the generated content, in this case a `white siamese cat`:  
Example:
![generated_cat](images/dalle-generated-cat.png)
##### Embeddings
TBD


#### Resources
 - [open ai quickstart](https://platform.openai.com/docs/quickstart)
 - [chat completion api reference](https://platform.openai.com/docs/api-reference/chat)
 - [embeddings quickstart](https://platform.openai.com/docs/guides/embeddings)

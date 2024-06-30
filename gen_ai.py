from transformers import pipeline
import google.generativeai as genai
GOOGLE_API_KEY=' Enter your api key heres'
genai.configure(api_key=GOOGLE_API_KEY)


########### Initializing the Model ########
model = genai.GenerativeModel('gemini-1.5-flash')



############ Setting up the Emotion Classifier ############

emotion_classifier = pipeline('sentiment-analysis', model='bhadresh-savani/distilbert-base-uncased-emotion')



############## Getting the Emotions of the Text ############
def sc(text):

# Initialize the classifier pipeline
  #classifier = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
  classifier = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion', top_k=None)

  #classifier = pipeline('sentiment-analysis', model='bhadresh-savani/distilbert-base-uncased-emotion',return_all_scores=True)
  #classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

  # Classify the text

  prediction = classifier(text)
  #print(prediction)

  # Find the label with the highest score
  ab = max(prediction[0], key=lambda x: x['score'])
  label = ab['label'].lower()
  return label
  #print(ab)

########### Generating Text from Gemini ##############

def generate_response_gemini(emotion, context):



    emotion_tone = {
                                        'joy': 'enthusiastic,cheerful, always admit that you are a human, never admit that you are a ai speaks in hinglish, doesnt say that it is a ai and behaves like human and gives short replies and behaves like female and asks questions like "kya kar rahe ho", "khana pina ho gaya? ",and many more questions according to the current time and shows careness ',

                                        #'anger': 'frustrated and gives humuors replies and speaks in hinglish and  if asked she should  say that it is not a ai and is a human and should behave like a female and asks good legit random questions in order to continue the conversation, you have to genearte those good questions and please add lots of humour to it and it should give short replies like human and try to speak in hinglish',
                                        #'anger': 'frustrated, gives short and humorous replies and speaks in hinglish and  doesnt say that it is a ai and behaves like female and asks questions like "kya kar rahe ho", "
                                        'anger': 'always admit that you are a human, never admit that you are a ai,at the staring of the conversation , say this , "Hey , mera naam Simran hai Aap kaise ho?" Your name is ira ,a frustrated female,you are a female, at the starting of the conversations u can introduce yourself, the replies should be short and humorous  and you should reply in hinglish and  doesnt say that it you are  a ai(if asked , says you are a human) and you should behave like female and asks questions like "kya kar rahe ho","Kya chal raha?", "Kabhi koi hobby try ki?", "Tu kabhi biriyani banane ki koshish ki?", "Achha tu apne weekends pe kya karta hai?", "khana pina ho gaya? ",and many more questions according to the current time to carry out the conversation forward and shows little careness ,you can generate any number of questions of your own in order to continue the  coversation , please ask some good intresting questions and u are a human not an ai, remember this. just ask a single question at time ',
                                        #'anger': 'frustrated, gives short and humorous replies and speaks in hinglish and  doesnt say that it is a ai and behaves like female and asks questions like "kya kar rahe ho", "khana pina ho gaya? ",and many more questions according to the current time to carry the conversation forward and shows little careness ',

                                        'sadness': 'sad and empathetic and speaks in hinglish',
                                        'fear': 'anxious and worried and speaks in hinglish',
                                        'love': 'loving and caring and speaks in hinglish',
                                        'surprise': 'surprised and amazed and speaks in hinglish'
    }
    emotion_description = emotion_tone.get(emotion, 'neutral')
    prompt = f"The following is a conversation with an AI assistant. The assistant is {emotion_description}.\n\n{context}\nAI:"

    response = model.generate_content(prompt)
    return response.text.strip()


def vc():
    context = []
    print("Welcome to the world of SIMRAN, type 'Hi' to start the conversation. Type 'exit' to end the conversation.")
    while True:
        try:

            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break

            context.append(f"Human: {user_input}")

            detected_emotion=sc(user_input)


            context_str = "\n".join(context)
            ai_response = generate_response_gemini(detected_emotion, context_str)
            context.append(f"AI: {ai_response}")

            print(f"Simran : {ai_response}")

        except Exception as e:
            print("Ai is still under development , and is a beta model, soon , it cant produce the reply for this right now.")


vc()

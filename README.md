# AI-Doppelgänger
 Generate a personalized AI twin with cloned voice, deepfake avatar, and  chat that learns your speech style in real time.




## Project Roadmap

1. **Master Voice Cloning**  
   - Research and choose a voice-cloning toolkit or API  
   - Record sample audio, preprocess, and iterate until you have a clean clone

2. **Build Basic Website**  
   - Scaffold a static frontend (HTML/CSS/JS) with “Record”/“Upload” & “Play” controls  
   - Stand up a minimal backend to handle audio requests

3. **Prototype Face Cloning**  
   - Select and test a face-swap model (e.g. First Order Motion Model, DeepFaceLab)  
   - Generate a short demo video of your face clone

4. **Integrate Face-Swap into Website**  
   - Add a “Try My Face” page to your site  
   - Wire frontend uploads to your face-clone backend and display results

5. **Enable “Talking Like Me” with an LLM**  
   - Connect a chat endpoint (e.g. OpenAI Chat API) for text responses  
   - Pipe responses through your voice-cloning pipeline so replies come in your voice

# pyrefly: ignore [missing-import]
import gradio as gr
from gtts import gTTS
import os
import tempfile

def text_to_speech(text):
    if not text or not text.strip():
        return None
    
    # Generate speech
    tts = gTTS(text=text, lang='en')
    
    # Save to a temporary file
    temp_dir = tempfile.gettempdir()
    audio_path = os.path.join(temp_dir, "tts_output.mp3")
    tts.save(audio_path)
    
    return audio_path

# Create the Gradio interface
with gr.Blocks(title="Text to Speech App") as demo:
    gr.Markdown("# Text to Speech Converter")
    gr.Markdown("Enter your text below and click **Generate Audio**. The built-in audio player allows you to **Play**, **Pause**, and **Download** the generated speech.")
    
    with gr.Row():
        text_input = gr.Textbox(
            label="Enter Text Here", 
            lines=5, 
            placeholder="Type something you want to hear..."
        )
        
    with gr.Row():
        generate_btn = gr.Button("Generate Audio", variant="primary")
        
    with gr.Row():
        # The Gradio Audio component natively supports playing, pausing, and downloading.
        audio_output = gr.Audio(label="Generated Audio", type="filepath")
        
    generate_btn.click(fn=text_to_speech, inputs=text_input, outputs=audio_output)

if __name__ == "__main__":
    # Launch the Gradio app
    # Set inbrowser=True to automatically open the browser. 
    # The default local URL will usually be http://127.0.0.1:7860
    demo.launch(inbrowser=True)

from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan, set_seed
import torch

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

inputs = processor(text="Hello, my dog is cute", return_tensors="pt")
speaker_embeddings = torch.zeros((1, 512))  # or load xvectors from a file

set_seed(555)  # make deterministic

# generate speech
speech = model.generate_speech(
    inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

print(speech.shape)

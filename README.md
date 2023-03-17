# DT2112 - Speech Technology - Final Project

# Text-to-speech with prominence control

### Abstract:
This project compares three distinct text-to-speech (TTS) approaches, aiming to assess their effectiveness in producing natural and intelligible speech. The first method involves a baseline TTS system called SpeechT5, which functions as a complete encoder-decoder model. The second method extracts attention from an encoder model (Bert), utilizes the attention as normalized scores, modifies the SSML Prosody tag based on these scores, and synthesizes speech. The third method employs PyReaper to obtain pitch information from audio, Wave2Vec to acquire word timestamps, and matches high pitches with corresponding word timestamps to modify the SSML Prosody tag and synthesize speech. To evaluate the performance of each approach, a Mean Opinion Score (MOS) test will be conducted, with ten volunteers rating the quality of synthesized speech for five different phrases. The goal is to determine which of the three methods yields the highest score and user satisfaction. The paper will present the general processes, results, attention heatmaps, and sample audio files generated during the study, providing valuable insights into the strengths and weaknesses of each TTS approach. 

The repository is composed of the following: 

- __data_sampled__: Original audios with CSV.
- __wav__: Produced audio files by our implementaitons, baseline and T5. 
- __bert_vis.ipynb__: Attention extraction and audio visualization of audio signal
- __speccht5_tts.ipynb__: T5 audio generation
- __ssml_prosody_timestamps__ipynb__: Pitch extractions with PyReaper, WhisperX, and SSML generation with pitch enhancement. 
- __vis_attentions.ipynyb__ : Visualization of attention layers of BERT

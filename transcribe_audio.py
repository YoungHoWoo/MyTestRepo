import sys

try:
    import whisper
except ImportError as e:
    print('whisper module not installed:', e)
    sys.exit(1)

if len(sys.argv) != 3:
    print('Usage: python transcribe_audio.py <input_mp3> <output_txt>')
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

model = whisper.load_model('base')

print(f'Transcribing {input_file}...')
result = model.transcribe(input_file)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(result['text'])
print(f'Transcription saved to {output_file}')

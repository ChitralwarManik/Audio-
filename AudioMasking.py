from pydub import AudioSegment
from pydub.generators import Sine


def add_beep(input_audio_path, output_audio_path, start_time, end_time, beep_duration=5000, beep_frequency=4500):
    # Load the input audio file
    audio = AudioSegment.from_file(input_audio_path)

    # Create a beep sound
    beep = Sine(beep_frequency).to_audio_segment(duration=beep_duration)

    # Convert start and end times to milliseconds
    start_time_ms = start_time * 1000
    end_time_ms = end_time * 1000

    # Remove the original audio between start_time and end_time
    audio_during = AudioSegment.silent(duration=end_time_ms - start_time_ms).overlay(beep)

    # Concatenate the remaining parts
    final_audio = audio[:start_time_ms] + audio_during + audio[end_time_ms:]

    # Export the final audio to the output file
    final_audio.export(output_audio_path, format="wav")


# Example usage
# input_audio_path = "/Users/abdul.azeez/Work/RADAR/AudioMasking/ManikPanAudio 1.wav"
input_audio_path = "/Users/abdul.azeez/Work/RADAR/AudioMasking/audiotmp2140775880 1.wav"

output_audio_path = "Sample4500.wav"
start_time = 2  # in seconds
end_time = 6  # in seconds
beep_duration = 4000  # in milliseconds

add_beep(input_audio_path, output_audio_path, start_time, end_time, beep_duration)

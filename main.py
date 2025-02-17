import numpy as np
import scipy.io.wavfile

audio = []
sampleRate = 8000.0


def append_sinewaves(
        freqs=[440.0],
        duration_milliseconds=500,
        volumes=[1.0]):
    global audio
    """
    The sine wave generated here is the standard beep.  If you want something
    more aggressive you could try a square or saw tooth waveform.   Though there
    are some rather complicated issues with making high quality square and
    sawtooth waves... which we won't address here :)
    len(freqs) must be the same as len(volumes)
    """

    volumes = list(np.array(volumes) / sum(volumes))
    num_samples = duration_milliseconds * (sampleRate / 1000.0)
    x = np.arange(int(num_samples))

    first_it = True
    for volume, freq in zip(volumes, freqs):
        print(freq)
        if first_it:
            sine_wave = volume * np.sin(2 * np.pi * freq * (x / sampleRate))
            first_it = False
        else:
            sine_wave += volume * np.sin(2 * np.pi * freq * (x / sampleRate))

    audio.extend(list(sine_wave))
    return


def append_sinewave(
        freq=440.0,
        duration_milliseconds=500,
        volume=1.0):
    global audio
    """
    The sine wave generated here is the standard beep.  If you want something
    more aggressive you could try a square or saw tooth waveform.   Though there
    are some rather complicated issues with making high quality square and
    sawtooth waves... which we won't address here :)
    """

    num_samples = duration_milliseconds * (sampleRate / 1000.0)

    x = np.arange(int(num_samples))

    sine_wave = volume * np.sin(2 * np.pi * freq * (x / sampleRate))
    audio.extend(list(sine_wave))
    return


def save_wav(file_name):
    global audio
    # Open up a wav file
    # wav params

    # 44100 is the industry standard sample rate - CD quality.  If you need to
    # save on file size you can adjust it downwards. The standard for low quality
    # is 8000 or 8kHz.

    # WAV files here are using short, 16 bit, signed integers for the
    # sample size.  So we multiply the floating point data we have by 32767, the
    # maximum value for a short integer.  NOTE: It is theoretically possible to
    # use the floating point -1.0 to 1.0 data directly in a WAV file but not
    # obvious how to do that using the wave module in python.
    audio = np.array(audio).astype(np.float32)
    print(audio[:100])
    scipy.io.wavfile.write(file_name, 8000, np.array(audio))


append_sinewave(volume=1, duration_milliseconds=500)
save_wav("output.wav")

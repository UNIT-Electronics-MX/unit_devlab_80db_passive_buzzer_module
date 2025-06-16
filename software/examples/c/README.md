# Mario Bros Melody with Buzzer using Arduino

> ⚠️ **Disclaimer**  
This example is based on the design from the Hardware Hacking tutorial:  
https://hardwarehackingmx.wordpress.com/2013/07/03/leccion-11-arduino-tocando-la-clasica-melodia-de-mario-bros/  
Use this code **at your own risk**. The author is not responsible for any damage or unintended behavior caused by its use.

## Description

This Arduino sketch plays the classic **Super Mario Bros** melody using a **buzzer** connected to a digital pin. The melody is defined using musical note frequencies and played with delays that correspond to the rhythm of the song.

---

## Pin Configuration

```cpp
int buzzer = 21; // The buzzer is connected to digital pin 21
```

You can modify the pin number according to your board configuration.

## Note Frequency Definitions

The first part of the code defines the frequency (in Hz) for each musical note from B0 to D8. These are based on standard note frequencies used for sound synthesis.

```cpp
#define NOTE_B0  31
#define NOTE_C1  33
...
#define NOTE_DS8 4978
#define REST     0 // Represents a pause or silence
```

## Melody and Rhythm

The melody[] array contains a sequence of musical notes (as defined above), while the durations[] array defines the duration of each note in terms of a fraction of a second.

For example:

```cpp
NOTE_E7, NOTE_E7, REST, NOTE_E7,
...
12, 12, 12, 12,
```

Each value in durations[] represents the denominator of the note's duration in seconds. For instance, a value of 12 means 1/12 of a second, or ~83ms per note.

# Loop function

```cpp
void loop() {
  for (int thisNote = 0; thisNote < sizeof(melody)/sizeof(int); thisNote++) {
    int noteDuration = 1000 / durations[thisNote];
    if (melody[thisNote] != REST) {
      tone(buzzer, melody[thisNote], noteDuration);
    }
    delay(noteDuration * 1.30);
    noTone(buzzer);
  }

  delay(2000);  // Pause before repeating the melody
}
```

### Explanation:
The for loop iterates through each note in the melody[] array.

noteDuration is calculated by dividing 1000ms by the duration value, giving the duration in milliseconds.

The tone() function plays the note on the buzzer.

A slight delay (noteDuration * 1.30) is used to allow separation between notes and keep the melody clean.

noTone() stops the sound after each note.

A final delay(2000) waits 2 seconds before restarting the song.

## Final Notes
This project is educational and intended for hobby and learning purposes. Always verify your connections, and never exceed the voltage or current ratings of your components.

> 🔊 Enjoy the nostalgic tones of Mario, responsibly!